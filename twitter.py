from snscrape.modules import twitter
import datetime
import pytz
import sqlite3

# Set the athlete name and the number of tweets to scrape
athlete_name = 'Lionel Messi'
num_tweets = 1000

# Set up a connection to the database
conn = sqlite3.connect('athlete_mentions.db')
c = conn.cursor()

# Get the ID of the latest tweet in the database
c.execute('SELECT MAX(id) FROM tweets')
last_tweet_id = c.fetchone()[0]

# Scrape the tweets mentioning the athlete since the latest tweet in the database
tweets = []
for tweet in twitter.search(f'{athlete_name} since_id:{last_tweet_id}'):
    tweets.append({
        'id': tweet.id,
        'date': tweet.date.strftime('%Y-%m-%d %H:%M:%S'),
        'content': tweet.content,
        'username': tweet.username,
        'retweets': tweet.retweetCount,
        'favorites': tweet.likeCount,
        'replies': tweet.replyCount
    })

# Insert the scraped tweets into the database
for tweet in tweets:
    c.execute('INSERT INTO tweets (id, date, content, username, retweets, favorites, replies) VALUES (?, ?, ?, ?, ?, ?, ?)', (tweet['id'], tweet['date'], tweet['content'], tweet['username'], tweet['retweets'], tweet['favorites'], tweet['replies']))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
