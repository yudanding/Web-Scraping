import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Wcssm1229,",
  database="statestreet"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE MKT (Date VARCHAR(255), Price VARCHAR(255))")

while True: 
	date = datetime.today().strftime('%Y-%m-%d')

	url = 'https://finance.yahoo.com/quote/MKC?p=MKC&.tsrc=fin-srch'
	response = requests.get(url)

	soup = BeautifulSoup(response.text, 'xml')

	Ticker = soup.find()

	price = soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
	price = float(price)


	mycursor = mydb.cursor()

	sql = "INSERT INTO MKT (Date, Price) VALUES (%s, %s)"
	val = (date, price)
	mycursor.execute(sql, val)

	mydb.commit()

	time.sleep(86400)


