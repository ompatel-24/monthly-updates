import tweepy
import datetime
import calendar
import pytz
import os
import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "tweets.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Authenticate with the Twitter API
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

# Create a new Tweepy API object
api = tweepy.API(auth, wait_on_rate_limit=True, retry_count=3)

# Get the bot's screen name
bot_screen_name = api.verify_credentials().screen_name

# Set the time zone to EST
est_tz = pytz.timezone('US/Eastern')

# Convert current time to EST
est_time = datetime.datetime.now(est_tz)
est_date = est_time.date()

# Calculate the tweet number based on the number of days since April 22, 2023
start_date = datetime.date(2023, 4, 23)
tweet_number = (est_date - start_date).days + 1

# Calculate the progress bar and percentage of the month left
last_day = calendar.monthrange(est_date.year, est_date.month)[1]
percent = round((est_date.day / last_day) * 100, 1)
progress_bar = "▓" * int(percent / 10) + "░" * (10 - int(percent / 10))

# Compose the tweet text
month_name = calendar.month_name[est_date.month + 1]
tweet_text = f"Day {tweet_number}:\n\nToday is {est_date.strftime('%B %d, %Y')}\n\n{percent}% {month_name} Loading...\n{progress_bar}"

if __name__ == "__main__":
    logger.info(f"Tweet {tweet_number}")

# Post the tweet
api.update_status(tweet_text)
