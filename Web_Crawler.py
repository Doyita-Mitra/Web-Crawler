import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def page_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://us.shein.com/US-Clothing-vc-34769.html?icn=clothing&ici=us_navbar05&page=' + str(page)
        #browser = webdriver.Chrome()
        #browser.get(url)
        source_code = requests.get(url)  # Collect and parse first page
        plain_text = source_code.text
        my_soup = BeautifulSoup(plain_text, 'html.parser')
        for link in my_soup.findAll('a', {'class': 'goods-name'}):    # Pull all text from the class 'goods-name' with the <a> tag
            if link.get('href') == None:
                continue
            else:
                href = 'https://us.shein.com' + link.get('href')
                title = link.string
                print(title)
                print(href)
            #get_item_desc(href)
        page += 1

"""def get_item_desc(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    my_soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in my_soup.findAll('div', {'class': 'container-header-fluid header-wrap j-header-wrap'}):
        print(item_name.string)"""

page_spider(1)
