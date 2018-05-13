##-------------- Number of Items ----------------------
def items(soup1):
    page_info = soup1.find(class_='page_info')
    info = page_info.get_text()
    no_of_items = info[(info.find('of')+3):len(info)]
    print("No of items = "+no_of_items)

##-------------- Number of Pages ----------------------
def no_of_pages(soup1):
    page_num = soup1.find(class_='page_num')
    data_point_id = page_num.find_all('a')
    print("Last Page = "+data_point_id[-2].get_text())

##-------------- All products ----------------------
def all_products(soup1):
    products = soup.find(class_='goodlist_1')
    products_name = products.find_all('li')
##    print(len(products_name))
    for product_name in products_name:
        name = product_name.find(class_='title')
        product_title = name.find('a')
        print("Title : "+product_title.get_text())
        print("Title Link: "+product_title.get('href'))
        new_price = product_name.find(class_='price wh_cn')
        print("Price : "+new_price.get_text())
        old_price = product_name.find(class_='price_old wh_cn')
        if old_price != None:
            print ("Old Price : "+old_price.get_text())



import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.banggood.com/Wholesale-Toys-Hobbies-and-Robot-c-133.html')
soup = BeautifulSoup(page.text, 'html.parser')

all_products(soup)
items(soup)
no_of_pages(soup)
