import requests					# for getting get, post request
from bs4 import BeautifulSoup			# for HTML parser (Web scraping)
import smtplib					# for connecting SMTP server

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)					# smtp for google
		
    server.ehlo()								# tells the server (gmail) that we want to use the ESMTP (Extended SMTP)
    server.starttls()								# to improve security we use this (Transport Layer Security)
    server.login('Your email address','your password')
    
    
    subject = 'Price Fell Down'							# Subject of Message
    
    body = 'Check this link : https://www.amazon.in/Apple-iPhone-XR-64GB-Black/dp/B07JWV47JW/ref=sr_1_1_sspa?keywords=iphone+xr&qid=1566062871&s=gateway&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTjZQWFlGUFdQSU0xJmVuY3J5cHRlZElkPUEwNTQ1NDM5MUZZVEdBMkdLTEQxRCZlbmNyeXB0ZWRBZElkPUEwNDI2NjM0MVZSOERFSFdOR0hTUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

    msg = "Subject : "+subject+"\n\n"+body					# 'Subject : ' is used to include subject of message
    
    server.sendmail(
        'Sender email address (Your email)','Reciever email address',msg
    )
    server.quit()								# Quits connection


def mainFunction():
    url = 'https://www.amazon.in/Apple-iPhone-XR-64GB-Black/dp/B07JWV47JW/ref=sr_1_1_sspa?keywords=iphone+xr&qid=1566062871&s=gateway&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTjZQWFlGUFdQSU0xJmVuY3J5cHRlZElkPUEwNTQ1NDM5MUZZVEdBMkdLTEQxRCZlbmNyeXB0ZWRBZElkPUEwNDI2NjM0MVZSOERFSFdOR0hTUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

	# for user-agent you can type my user agent on google and copy it and paste here
	
    header = {"USER-AGENT":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'} 
    
    page = requests.get(url,headers=header)					# getting data from the above URL

    soup = BeautifulSoup(page.content,'html.parser')				# parsing into HTML

    title = soup.find(id="productTitle").get_text().strip()			# getting text of tag whose id="product Title"
    price = soup.find(id="priceblock_ourprice").get_text().strip()

    priceInFloat=""
    
    for x in price:															# Removing all the symbols and extra characters from price
        if x >='0' and x<= '9' or x=='.':
            priceInFloat += x

    priceInFloat = float(priceInFloat)

    if priceInFloat < 60000:							# comparing price
        send_mail()															
        print('Mail Sent')

if __name__ == '__main__':
    mainFunction() 
