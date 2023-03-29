import streamlit as st
import snscrape 
import snscrape.modules.twitter as sntwitter

st.title("Twitter User Scraper")

account_name = st.text_input("Enter a Twitter account name")

if st.button("Scrape"):

  user = next(sntwitter.TwitterUserScraper(account_name).get_items())

st.write(f"{account_name} has {user.user.followersCount} followers and {user.user.favouritesCount} likes and {user.user.friendsCount} people.")
