from google.auth.transport import requests


class WebScraper:
    def scrape_the_web(self):
        tide_page = requests.get('https://tides.willyweather.com.au/nsw/sydney/bondi-beach.html')
        tide_page = bs(tide_page.text, "lxml")
        print(tide_page)
        table = tide_page.find_all('li', {'class': 'day'})
        print(f'Found {len(table)} table/tables.')
        # table = table[0]
        print(table)
        # table_rows = table.find_all('tr')
        # print(f'Found {len(table_rows)} row/rows.')
        # print(table_rows)