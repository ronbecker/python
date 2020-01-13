#! user/bin/env python
import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='CLIENT_ID', \
                     client_secret='CLIENT_SECRET', \
                     user_agent='USER_ID', \
                     username='USERNAME', \
                     password='PASSWORD')

subreddit = reddit.subreddit('learnpython')

top_subreddit = subreddit.top()

for submission in subreddit.top(limit=1):
    print(submission.title, submission.id)

topics_dict = { "title": [], \
                "score":[], \
                "id":[], \
                "comms_num":[], \
                "created":[], \
                "body":[]}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)

topics_data = topics_data.assign(timestamp = _timestamp)

topics_data.to_csv('learnpython-data.csv', index=False)
