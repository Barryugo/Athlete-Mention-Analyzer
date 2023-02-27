from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random
from textblob import TextBlob

try:
    # initialize the Chrome driver with headless option
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # navigate to the LinkedIn website and log in
    driver.get('https://www.linkedin.com/')
    # wait for the page to load with random interval
    time.sleep(random.randint(3, 5))
    driver.find_element(By.ID, 'session_key').send_keys(
        'equivalent121@gmail.com')
    time.sleep(random.randint(1, 3))  # wait with random interval
    driver.find_element(By.ID, 'session_password').send_keys('nweke1000')
    time.sleep(random.randint(1, 3))  # wait with random interval
    # click the sign-in button
    driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-button').click()
    # wait for the page to load with random interval
    time.sleep(random.randint(3, 5))

    # keywords to search for
    keywords = ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Lebron James"]

    # navigate to the LinkedIn search page and search for the keywords
    driver.get('https://www.linkedin.com/search/results/content/?keywords=' +
               ' OR '.join(keywords))
    # wait for the page to load with random interval
    time.sleep(random.randint(3, 5))

    # scroll down to the bottom of the page to load more content
    for i in range(1000):  # scroll down 3 times
        driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);')
        # wait with random interval for the content to load
        time.sleep(random.randint(2, 4))

    # scrape the post content and count the number of times the keywords are mentioned
    count = {keyword: 0 for keyword in keywords}
    sentiment_score = {keyword: 0 for keyword in keywords}
    post_elements = driver.find_elements(
        By.CLASS_NAME, 'feed-shared-update-v2__description-wrapper')  # find all post elements
    for post in post_elements:
        post_text = post.text
        for keyword in keywords:
            count[keyword] += post_text.count(keyword)
            if keyword.lower() in post_text.lower():
                post_sentiment = TextBlob(post_text).sentiment.polarity
                sentiment_score[keyword] += post_sentiment
        # wait with random interval before proceeding to the next post
        time.sleep(random.randint(1, 3))

    for keyword, keyword_count in count.items():
        if keyword_count > 0:
            # calculate the sentiment score for each keyword
            sentiment_score[keyword] /= keyword_count
            # print the count and sentiment score for each keyword
            print(
                f"{keyword} was mentioned {keyword_count} times with a sentiment score of {sentiment_score[keyword]:.2f}.")
        else:
            print(f"{keyword} was not mentioned in any of the posts.")
except Exception as e:
    print("An error occurred: ", e)
finally:
    driver.quit()  # close the browser
