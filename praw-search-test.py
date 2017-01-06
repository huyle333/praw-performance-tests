import praw
import argparse
import time

parser = argparse.ArgumentParser(description="Choose debug mode or not.")
parser.add_argument("-i", "--id", help="Print stdout and stderr messages.",
                    required=True)
parser.add_argument("-s", "--secret", help="Print stdout and stderr messages.",
                    required=True)
args = parser.parse_args()

reddit = praw.Reddit(client_id=args.id,
                     client_secret=args.secret,
                     user_agent="/u/microwavesam")

startTime = time.time()

subreddit = reddit.subreddit("nba")
search_query = "[Post Game Thread] Golden State Warriors Cleveland Cavaliers"

for submission in subreddit.search(search_query, limit=1):
    if (submission):
    	print(submission.url, submission.title)

elapsedTime = time.time() - startTime
elapsedTime = elapsedTime * 1000
print(elapsedTime)