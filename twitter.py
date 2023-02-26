import snscrape.modules.twitter as sntwitter
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# Download the VADER lexicon and wordnet
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('wordnet')

# Initialize the SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Define the search terms
athletes = ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Lebron James"]
synonyms = {"Lionel Messi": ["Messi", "Leo Messi"],
            "Cristiano Ronaldo": ["Ronaldo", "CR7"],
            "Neymar": ["Neymar Jr.", "NJR"],
            "Lebron James": ["LeBron"]}

# Define the search query
search_terms = []
for athlete in athletes:
    search_terms.extend([f'"{athlete}"'] +
                        [f'"{synonym}"' for synonym in synonyms[athlete]])
search_query = " OR ".join(search_terms)

# Create a list to store the tweets
tweets_list = []

# Use TwitterSearchScraper to scrape tweets
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search_query + " since:2022-01-01 until:2023-02-15").get_items()):
    if i > 1000:
        break
    tweets_list.append([tweet.date, tweet.content])

# Convert the tweets list to a pandas dataframe
tweets_df = pd.DataFrame(tweets_list, columns=["Date Created", "Tweets"])

# Count the number of times each athlete was mentioned in each tweet
for athlete in athletes:
    mentions = tweets_df["Tweets"].apply(lambda tweet: any(
        synonym in tweet for synonym in synonyms[athlete]))
    tweets_df[f"{athlete} Mentions"] = mentions.astype(int)

# Calculate the sentiment scores for each tweet
tweets_df['Sentiment'] = tweets_df['Tweets'].apply(
    lambda tweet: analyzer.polarity_scores(tweet)['compound'])

# Print the total number of mentions and sentiment scores for each athlete
for athlete in athletes:
    mentions = tweets_df[f"{athlete} Mentions"].sum()
    sentiment_score = tweets_df[tweets_df[f"{athlete} Mentions"] > 0]['Sentiment'].mean(
    )
    print(f"{athlete} was mentioned {mentions} times with a sentiment score of {sentiment_score:.2f}.")
