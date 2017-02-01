Reddit Comment Signature Appender

1) The only python dependency is Praw: https://pypi.python.org/pypi/praw/4.3.0
2) You need to go to https://www.reddit.com/prefs/apps/ and create a new "script" app.
3) You need to create a config.py with the following template, using the client secret
   and client ID you got from Step 2.

CLIENT_ID = "abc"
CLIENT_SECRET = "abcdef"
USERNAME = "myuser"
PASSWORD = "mypass"
SIGNATURE = "Signature Text!"
MINUTES_BETWEEN_RUNS = 20

4) Now you can run main.py and it will loop through, every MINUTES_BETWEEN_RUNS, appending
   your signature to each comment you make. By default, it will only fetch the 20 most
   recent comments to edit.