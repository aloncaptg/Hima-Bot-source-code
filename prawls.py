import praw

reddit = praw.Reddit(client_id = "9C7PU9SXE1t58g",
                    client_secret = "fbFzuItqTWTtQY68_6goNWqWrfDRAQ",
                    username = "NotCapt01",
                    password = "improlol123",
                    user_agent = "praw 123 lol")

subreddit = reddit.subreddit("memes")


top = subreddit.top(limit = 5)

for submission in top:
    print(submission.title)