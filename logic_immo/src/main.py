from web_scrapper import WebScrapper

# Test
BASE_URL = "https://www.logic-immo.com/vente-immobilier-ile-de-france,1_0/options/groupprptypesids=1"
web_scrapper = WebScrapper(BASE_URL)

# Set total number of pages
home_page = web_scrapper.get_html_page(None)
web_scrapper.set_last_page_number(home_page)
print("There are {} pages".format(web_scrapper.nb_pages))

# Set all links
web_scrapper.nb_pages = 2
web_scrapper.set_all_pages_links()

# Export all links
web_scrapper.export_to_gcs()

