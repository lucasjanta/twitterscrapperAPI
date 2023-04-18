from fastapi import FastAPI
import snscrape.modules.twitter as sntwitter

app = FastAPI()

query = "drive.google.com"
limit = 10
tweets = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
   if len(tweets) == limit:
       break
   else:
        links = []
        for link in tweet.links:
            links.append(link.url)
        tweets.append({'content': tweet.content, 'linkDrive': links, 'linkTweet': tweet.url})


@app.get("/")
def home():
    return {"Tweets": len(tweets)}


@app.get("/tweets/{id_tweet}")
def pegar_tweet(id_tweet: int):
    return tweets[id_tweet]
