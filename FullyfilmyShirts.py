
import bs4
from bs4 import BeautifulSoup as soup # HTML data structure# HTML data structure
from urllib.request import urlopen as ureq  # Web client


# URl to web scrap from.
# In this example we web scrap T-shirts from Fullyfilmy.com
my_url = "https://fullyfilmy.in/collections/t-shirts"

# opens the connection and downloads html page from url
uClient = ureq(my_url)

# To read the html content on the URL
page_html = uClient.read()
uClient.close()

# Parses html into a soup data structure to traverse html
# As if it were a json data type.
page_soup = soup(page_html, "html.parser")

#Reads the header h1
page_soup.h1

# Finds each product from the store page
containers = page_soup.findAll("div",{"tt-description"})

# Name the output file to write to local disk
out.filename = "fullyfilmy_tshirts.csv"

# Header of csv file to be written
headers = "T-shirt Name, New price ,Old Price\n"

# Opens file, and writes headers
f = open(filename, "w")
f.write(headers)

# To find the lenght of the Container or how many products are there in the Container
len(containers)
containers[0]

# Loops over each product and grabs attributes about
# Each product
for container in containers:

    
    shirt_container = container.findAll("h2",{"class":"tt-title prod-thumb-title-color"})
    shirt_name = shirt_container[0].text
    
    
    Newprice_container = container.findAll("span",{"class":"new-price"})
    shirt_newprice = Newprice_container[0].text
    
    Oldprice_container = container.findAll("span",{"class":"old-price"})
    shirt_oldprice = Oldprice_container[0].text

    # Prints the dataset to console
    print ("shirt_name: " +shirt_name)
    print("shirt_newprice: " +shirt_newprice)
    print("shirt_oldprice: " +shirt_oldprice)
    
    # Writes the dataset to file
    f.write(shirt_name + "," + shirt_newprice + "," + shirt_oldprice + "\n")
    
# Close the file
f.close()  


