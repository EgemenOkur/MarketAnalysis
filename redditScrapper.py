import praw
import pandas as pd
import datetime
# Define user agent
user_agent = "praw_scraper_1.0"

# Create an instance of reddit class
reddit = praw.Reddit(username="GarantBM",
                     password="Egemen35.",
                     client_id="XCs0DPVOWx6-ylVmfV_TbA",
                     client_secret="SOR87C835--8tTB9TFTx8I-O2WkPhg",
                     user_agent=user_agent
                     )

# Create sub-reddit instance
subreddit_name = "algotrading"
subreddit = reddit.subreddit(subreddit_name)

df = pd.DataFrame()  # creating dataframe for displaying scraped data

# creating lists for storing scraped data
titles = []
scores = []
ids = []
numComments = []
ids = []
url = []
date = []

# looping over posts and scraping it
for submission in subreddit.hot(limit=100):
    titles.append(submission.title)
    numComments.append(submission.num_comments)
    scores.append(submission.score)  # upvotes
    url.append(submission.url)
    ids.append(submission.id)
    date.append(datetime.datetime.fromtimestamp(submission.created))

df['Title'] = titles
df['Id'] = ids
df['Upvotes'] = scores  # upvotes
df['numComments'] = numComments  # upvotes
df['post'] = url
df['date'] = date


print(df.head(100))
