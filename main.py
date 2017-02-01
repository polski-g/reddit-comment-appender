import praw
import pprint
from config import *
import time

r = praw.Reddit(
    user_agent="signature-appender",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD)

while True:
    for x in r.redditor(USERNAME).comments.new(limit=20):
        body = x.body
        if body.endswith("^."):
            continue
        body = body + "\n\n~~-----~~\n\n%s^." % SIGNATURE
        x.edit(body)
        x.save()
    time.sleep(int(MINUTES_BETWEEN_RUNS) * 60)
