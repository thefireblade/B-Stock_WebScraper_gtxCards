from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from Source import ScraperFunctions


url900 = "https://www.evga.com/products/productlist.aspx?type=8&family=GeForce+900+Series+Family"
url1000 = "https://www.evga.com/products/productlist.aspx?type=8&family=GeForce+10+Series+Family"
url700 = "https://www.evga.com/products/productlist.aspx?type=8&family=GeForce+700+Series+Family"
soup900 = soup(urlopen(url900).read(), "html.parser")
soup1000 = soup(urlopen(url1000).read(), "html.parser")
soup700 = soup(urlopen(url700).read(), "html.parser")
#Grabs each container containing the graphics card information
data900 = soup900.findAll("div", {"class": "list-item"})
data1000 = soup1000.findAll("div", {"class": "list-item"})

print("GTX 700 Series\n")
print("--------------------------------------------------------------------------\n")
ScraperFunctions.printData(soup700)
print("\nGTX 900 Series\n")
print("--------------------------------------------------------------------------\n")
ScraperFunctions.printData(soup900)
print("\nGTX 10 Series\n")
print("--------------------------------------------------------------------------\n")
ScraperFunctions.printData(soup1000)
