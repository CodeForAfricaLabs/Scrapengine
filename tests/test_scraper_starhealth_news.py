"""
scrapengine/scrapers/starhealth_news tests
"""
import os
import json
import random
import unittest
from Scrapengine.scrapers import starhealth_news
from Scrapengine.configs import ARCHIVE

class StarhealthnewsScraperTestCase(unittest.TestCase):
    
    def setUp(self,):
        self.foo = True

    def test_get_articles(self, ):
        count = random.randint(1,50)
        resp = starhealth_news.get_articles(count)
        self.assertIsInstance(resp, list)
        self.assertEqual(len(resp), count)

    def test_output(self, ):
        test_output_file = "starhealth_news-tests"
        for _file in os.listdir(ARCHIVE):
            if _file.endswith('json') and _file.startswith(test_output_file):
                # delete output files generated by the unit tests
                os.remove("%s/%s" % (ARCHIVE, _file))
        
        sample = ["foo", "bar"]
        filename = test_output_file
        starhealth_news.output(sample, outputfile=filename)

        generated = False
        for _file in os.listdir(ARCHIVE):
            if _file.endswith('json') and _file.startswith(test_output_file):
                generated = True
                os.remove("%s/%s" % (ARCHIVE, _file))
                break
        self.assertTrue(generated, msg="Output not generated")


    def test_publish_output(self, ):
        file_name = "test-file-%s.txt" % random.randint(1, 100000000000)
        testfile = "%s/%s" % (ARCHIVE, file_name)
        f = open(testfile, "w")
        f.write("test content")
        f.close()
        starhealth_news.publish_output(testfile)

        # delete file from S3
        conn = starhealth_news.boto.connect_s3(starhealth_news.AWS_API_KEY,
                starhealth_news.AWS_API_SECRET)
        bucket = conn.get_bucket(starhealth_news.S3_BUCKET_NAME)
        s3key = starhealth_news.Key(bucket)
        s3key.key = "/" + file_name
        deleteresp = bucket.delete_key(s3key)
        #self.assertIsInstance(deleteresp, int)

if __name__ == '__main__':
    unittest.main()
