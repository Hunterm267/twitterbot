# Twitterbot
Twitterbot is a simple Python application for reading and parsing a RSS feed and posting its title and links to a Twitter account.

The bot is limited to handle one feed and one Twitter account.

## How do I install Twitterbot?

1. Download or git clone this repository.
2. Install the dependencies:
  - <code>pip install <a href="https://pythonhosted.org/feedparser/">feedparser</a></code>
  - <code>pip install <a href="https://twython.readthedocs.org/en/latest/">twython</a></code>
3. Create a <a href="https://apps.twitter.com/">Twitter application</a>, and access tokens and keys.
4. Modifiy the settings in the source code.
   - Modify <code>FeedUrl</code> to the RSS feed you want to read.
   - Modify the variables in the <code>TwitterAuth</code> class and add the access tokens and keys for connecting to Twitter.

## How do I use Twitterbot?

Read the RSS feed and post to Twitter account:

<code>$ python rss2twitter.py rss</code>

Preferably, you should use crontab to set it up to run once every hour or so.
