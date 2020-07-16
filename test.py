from twitterscraper import *

if __name__ == '__main__':
    query = 'https://twitter.com/hashtag/iiitdfeehike?src=hashtag_click&f=live'
    lang = 'en'
    user= 'sahil_yadav96'

    file = open("output.txt","w")
    for tweet in query_single_page(query, lang, pos, retry=50, from_user=False, timeout=60):
        file.write(str(tweet.text.encode('utf-8')))
    file.close()