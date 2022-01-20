import praw
import pandas as pd
import datetime
import arxiv


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

import arxivscraper
scraper = arxivscraper.Scraper(category='physics:cond-mat', date_from='2017-05-27',date_until='2017-06-07')
output = scraper.scrape()
import pandas as pd
cols = ('id', 'title', 'categories', 'abstract', 'doi', 'created', 'updated', 'authors')
df = pd.DataFrame(output,columns=cols)


search = arxiv.Search(
    query="healthcare AND \"machine learning\"",
    max_results=3,
    sort_by=arxiv.SortCriterion.SubmittedDate,
    sort_order=arxiv.SortOrder.Descending
)

for result in search.results():
    print('Title: ', result.title, '\nDate: ', result.published, '\nId: ', result.entry_id, '\nSummary: ',
          result.summary, '\nURL: ', result.pdf_url, '\n\n')

