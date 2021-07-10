import datetime
from time import sleep
import tweepy
import selenium
import requests
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import emoji


#		      ______ ______
#		    _/      Y      \_
#		   // ~~ ~~ | ~~ ~  \\       Easter Egg 1/2 found
#		  // ~ ~ ~~ | ~~~ ~~ \\      by Matt Welter
#		 //________.|.________\\ 
#		`----------`-'----------'


auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET") #  Insert your consumer key & consumer secret given to you by the Twitter Dev API
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET") #  Insert your access token & access token secret given to you by the Twitter Dev API
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

CoinMarketCap_URL = "https://coinmarketcap.com/currencies/dogecoin/" #	Copy and paste the Coin Market Cap URL into this field
TickerSymbol = "$DOGE" #  Write down the Ticker Symbol of the Cryptocurrency you'd like to use





price = None
percent = None
minute1 = 0     #  You can leave these alone, they
minute2 = 15    #  post the price every 15 minutes.
minute3 = 30    
minute4 = 45

def check_doge():
	session = HTMLSession()  # Starts session
	response = session.get(CoinMarketCap_URL)  # Requests page
	soup = bs(response.html.html, "html.parser")  # Reads page
	open("info.html", "w", encoding='utf8').write(response.html.html)  # Stores page content in HTML file (same directory)

	with open('info.html', 'r') as f:  #  Opens the HTML file stated above
		contents = f.read()  #  Reads the content of the HTML file
		soup = bs(contents, 'lxml')  #  Pretty prints the HTML file (makes it more readable)

		try:  #  Tries to find the price & percent of the cryptocurrency 
			price = soup.select("#__next > div > div.main-content > div.sc-57oli2-0.dEqHl.cmc-body-wrapper > div > div.sc-16r8icm-0.epyToK.container > div.sc-16r8icm-0.dOJIkS.container___lbFzk > div.sc-16r8icm-0.dOJIkS.priceSection___3kA4m > div.sc-16r8icm-0.dOJIkS.priceTitle___1cXUG > div")
			percent = soup.select("#__next > div > div.main-content > div.sc-57oli2-0.dEqHl.cmc-body-wrapper > div > div.sc-16r8icm-0.epyToK.container > div.sc-16r8icm-0.dOJIkS.container___lbFzk > div.sc-16r8icm-0.dOJIkS.priceSection___3kA4m > div.sc-16r8icm-0.dOJIkS.priceTitle___1cXUG > span")
			print("-"*70)  #  This is a divider for the console

			for pr in price:    #  Allows for the program to read the actual text of the <div> or <span>
				print(pr.text)

			for pe in percent:  #  Allows for the program to read the actual text of the <div> or <span>
				print(pe.text)

			api.update_status(TickerSymbol + "\n" + emoji.emojize(":label:") + price.text + "\n" +  emoji.emojize(":chart_increasing:") + percent.text)  # This is the code that actually tweets the result
			
			#  The tweet should look like this:
			#  $DOGE
			#  $0.3401
			#  5.6%

			print("Tweeted " + TickerSymbol + "'s Price & Percent")
			print("-"*70)  #  This is a divider for the console
		except:
			pass

while True: 
	if (datetime.datetime.now().minute == minute1):  #  If the current minute is equal to 0
		print(datetime.datetime.now().minute)
		check_doge()
	elif (datetime.datetime.now().minute == minute2):  #  If the current minute is equal to 15
		print(datetime.datetime.now().minute)
		check_doge()
	elif (datetime.datetime.now().minute == minute3):  #  If the current minute is equal to 30
		print(datetime.datetime.now().minute)
		check_doge()
	elif (datetime.datetime.now().minute == minute4):  #  If the current minute is equal to 45
		print(datetime.datetime.now().minute)
		check_doge()
	else:
		print(datetime.datetime.now().minute)
	sleep(60)
