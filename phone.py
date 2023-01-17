import mechanize
from bs4 import BeautifulSoup

url= "https://www.findandtrace.com/trace-mobile-number-location"

brow = mechanize.Browser()  #here you can even use selenium
brow.set_handle_robots(False)
# we have make it as false because some websites doesn't allow us to make to scrap data 
#so if our script found that (robots.txt) file it will just ignore taht and we'll continue using our scrapping
brow.open(url)
brow.select_form(name="trace")
brow['mobilenumber']= str(input("Enter the mobile number: "))  #give your mobile number

#it'll search for almost all the mobile except few which haven't registered anywhere or that data is explored

result = brow.submit()  # we'll record our response in result

soup = BeautifulSoup(result.read(),'html.parser')
table_extr = soup.find_all('table', class_='shop_table')
print(len(table_extr))  #it'll give how many tables are there