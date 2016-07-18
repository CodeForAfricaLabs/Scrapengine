import os

SCRAPERS = dict(
        rss={
            "allafrica.com.africa": "http://allafrica.com/tools/headlines/rdf/africa/headlines.rdf",
            "allafrica.com.asiaaustraliaafrica": "http://allafrica.com/tools/headlines/rdf/asiaaustraliaandafrica/headlines.rdf"
            },

        article={
            "100r": "https://100r.org/section/all-categories/page/2/",
            "": "",
            
            }
        )


ARCHIVE = os.getenv("SCRAPENGINE_ARCHIVE_PATH", ".")
