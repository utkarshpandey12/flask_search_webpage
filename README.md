# flask_search_webpage
Contains two parts 
1. scraping data 
2. Displaying it on a webpage
This uses a technique where the website is scraped once on invoking scrapy runspider "path to shopclues.py script" and then web scaped 
data is saved in tmp folder as a csv file named shopclues.csv where each row defined the four column data result from scraping of fields 
namely Product desc, Price,Discount,and image urls.This csv file is loaded as a dataframe in webapp.py and rendered into a web page with 
product search capability. Users can have the price change feature capability by running the scraping script and loading the product scraped details and check for price of their product by using the product search query facility on home page which is the reason I have not implemeted the price updation feature by sendng mail to admin about price change. The time it takes to run and scripts and check price for your fav product is easy and can be done by just invoking two commands hence this project does not implement sending mail to admin but provides solution to rest of problem statement.

The scripts to execute scraping are stored inside the folder named sh
web app is instantiated using web_app.py script which uses flask

# Path to script for scraping shopclues website of 4G smartphones 
path to shopclues.py can be found under folder/sh/sh/spiders/shopclues.py
settings are defined in folder/sh/sh/settings.py which defines the pipelines 

#Steps to execute the scraping from shopclues.com and view the producrt search web page 

on command line
1 . clone the repo into folder named whatever you like
2 . cd folder
3 . Type the command scrapy runspider "exact path to shopclues.py script"

# The web_app.py uses the csv file for to implement product search capability hence a file named shopclues (1).csv is stored in the working directory folder otherwise everytime you run scrapy runspier shopclues.py creates a csv file under tmp folder.
# For the sake of convenience it is stored as shopclues (1).csv inside the folder. You can always scrape the data and move these files into root folder to run webapp.py only if yoyr working directory is folder as mentioned above inside which you clone the project.
4. py web_app.py and visit the link http://127.0.0.1:5000/ in your browser to see app runnig

Alternatively if your working directory is not folder then you will have to edit web_app.py manuaaly to provide the path to shopclues.csv file in pd.read_csv function.

Visit the page and try to serach some products name in the seearch bar and submit to see matching product and its details.

#Requirements 
1. Flask
2 Scrapy
3 Pandas 






