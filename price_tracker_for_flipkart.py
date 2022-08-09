import requests
from bs4 import BeautifulSoup


url = 'https://www.flipkart.com/hp-15s-ryzen-3-dual-core-3250u-8-gb-1-tb-hdd-windows-10-home-15s-gr0011au-thin-light-laptop/p/itma23a328a1f458?pid=COMFZHFWETTEFHVZ&lid=LSTCOMFZHFWETTEFHVZ2OSEK3&marketplace=FLIPKART&q=laptops&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=71770eb3-a8de-40ec-b0b5-1f6454dff158.COMFZHFWETTEFHVZ.SEARCH&ppt=hp&ppn=homepage&ssid=y4l2xc4s3k0000001620756290837&qH=c06ea84a1e3dc3c6'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

product_name = soup.find('span', {'class':'B_NuCI'}).text
print(product_name)

# Product Price
price_tag = soup.find('div', {'class':'_30jeq3 _16Jk6d'})
product_price = '0'
if price_tag:
 product_price = price_tag.text.replace('₹','').replace(',', '')
product_price = float(product_price)
print(product_price)

budget = int(input("Enter budget:"))
print(budget)
Email = "sherepunjab3060@outlook.com"

# Ratings and Reviews Count
rat_rev_main_span = soup.find('span', {'class':'_2_R_DZ'})

ratings = '0 ratings'
reviews = '0 reviews'
if rat_rev_main_span:
    rat_rev = rat_rev_main_span.text.replace(u'\xa0', ' ')
    rat_rev_list = rat_rev.split('&')
    ratings = rat_rev_list[0].strip()
    reviews = rat_rev_list[1].strip()
print(ratings, reviews)

print('Product name:', product_name)
print('Product price:', product_price)
print('Ratings:', ratings)
print('Reviews:', reviews)

if product_price >= budget:
        #diff = product_price-budget
        print("please wait for some time to get your product at best deal price")

else:
        print("HUURY UP! Your Favourite Product is Available under your budget")
        