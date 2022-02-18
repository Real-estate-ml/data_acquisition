import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--page', required=True, help='Page number to scrape')

args = parser.parse_args()
page = args.page
print(page)