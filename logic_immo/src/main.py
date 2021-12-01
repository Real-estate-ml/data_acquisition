base_url = 'https://www.logic-immo.com/vente-immobilier-ile-de-france,1_0/options/groupprptypesids=1'
web_scrapper = WebScrapper(base_url)
home_page = web_scrapper.get_html_page(None)
print(web_scrapper.get_page_number(home_page))