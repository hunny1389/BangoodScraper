import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.banggood.com/Wholesale-Toys-Hobbies-and-Robot-c-133.html')

soup = BeautifulSoup(page.text, 'html.parser')

##-------------- Number of Items ----------------------
page_info = soup.find(class_='page_info')
info = page_info.get_text()
no_of_items = info[(info.find('of')+3):len(info)]
print(no_of_items)




####-------------- Number of Pages ----------------------
##page_num = soup.find(class_='page_num')
##data_point_id = page_num.find_all('a')
##print("Last Page = "+data_point_id[-2].get_text())
####print(data_point_id[-2])
####------------------------------------------------------


## -------------- find all the products ---------------- 
##products = soup.find(class_='goodlist_1')
##
##products_name = products.find_all('li')
##print(len(products_name))
##for product_name in products_name:
####    print(product_name.prettify())
##    name = product_name.find(class_='title')
##    product_title = name.find_all('a')
####    print(len(product_title))
##    print(product_title[0].get_text())
##    new_price = product_name.find(class_='price wh_cn')
##    print(new_price.get_text())
##    old_price = product_name.find(class_='price_old wh_cn')
##    if old_price != None:
##        print (old_price.get_text())
##-------------------------------------------------------
