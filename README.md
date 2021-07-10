# Twitter Crypto Price Bot – Template
![Python 2.7, 3.5](https://img.shields.io/badge/Python-2.7%2C%203.5%2B-3776ab.svg)

This is a Twitter bot template. The bot is able to post your desired Cryptocurrency's price & 24hr percent every 15 minutes.

### Dependencies
- [datetime](https://docs.python.org/3/library/datetime.html)
- [tweepy](https://www.tweepy.org/)
- [requests](https://docs.python-requests.org/en/master/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [requests_html](https://pypi.org/project/requests-html/)
- [Python 3.5 >=](https://www.python.org/downloads/)
- [pip + setuptools](https://pip.pypa.io/en/stable/installing/)

## Usage
1. [Download this repo](https://github.com/mattwelter/crypto-price-bot/archive/refs/heads/main.zip)
2. Open Terminal or Command Prompt
3. Set location to directory ``cd /path/to/dir``
4. Start the program ``python twitter_bot.py``

## FAQ

### "How do I get acess to the Twitter dev API?"

https://developer.twitter.com/en/apply-for-access

**Steps:**
1. Apply for dev account
2. Hobbyist > Making a bot > Get started
3. Fill out email, phone, name, country. Click next
4. "How will you use the Twitter API or Twitter Data?"

**Here is exactly what I said:**
```
Core use case: I’m creating a Twitter account that post the
cryptocurrency $ETH price & 24hr percentage every 15 minutes.
No other automation is being used, no messaging, no liking,
no retweeting, no following, I am only automating tweeting.
I am web scraping coinmarketcap.com and posting the price and
% data using the Twitter API. This helps the crypto Twitter
community know what the price is without having to leave
Twitter.

I’m creating a few Twitter automation accounts that post the
cryptocurrency price of a few coins every 15 minutes. No other
automation is being used. I am web scraping coinmarketcap.com
and posting the price and % data using the Twitter API.
```

5. "Are you planning to Analyze Twitter data? -> NO
6. "Will your app use Tweet, Retweet, Like, Follow, or Direct Message functionality?" -> NO
7. "Do you plan to display Tweets or aggregate data about Twitter content outside Twitter?" -> NO
8. "Will your product, service, or analysis make Twitter content or derived information available to a government entity?" -> NO
9. Review information > Submit application
