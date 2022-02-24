from web_scrapper import WebScrapper
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--startpage', required=True, help='Start page number to scrape')
parser.add_argument('--endpage', required=True, help='End page number to scrape')

args = parser.parse_args()
print("The webscrapping service for page {} to {} is starting...".format(args.startpage, args.endpage))
start_page = int(args.startpage)
end_page = int(args.endpage)

BASE_URL = "https://www.logic-immo.com/vente-immobilier-paris-75,100_1/options/groupprptypesids=1"
web_scrapper = WebScrapper(BASE_URL, start_page, end_page)

# Set all links
web_scrapper.set_all_pages_links()

# Export all links
web_scrapper.export_to_gcs()


