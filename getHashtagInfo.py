from twitter_scraper import get_tweets

for tweet in get_tweets('#iiitdfeehike',pages=2):
    print(tweet['username'])