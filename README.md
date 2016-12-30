# Twitterbot
[![Passing](https://img.shields.io/travis/rust-lang/rust/master.svg)]()
[![UpToDate](https://img.shields.io/versioneye/d/ruby/rails.svg)]()
[![Release](https://img.shields.io/badge/release-v1.0-blue.svg)]()

Twitterbot is a simple Python application for reading and parsing a RSS feed and posting its title and links to a Twitter account.

The bot is limited to handle one feed and one Twitter account.

## How do I install Twitterbot?

1. Download or git clone this repository.
2. Install the dependencies:
  - <code>$ sudo apt-get install python-pip</code>
  - <code>$ pip install <a href="https://pythonhosted.org/feedparser/">feedparser</a></code>
  - <code>$ pip install <a href="https://twython.readthedocs.org/en/latest/">twython</a></code>
3. Create a <a href="https://apps.twitter.com/">Twitter application</a>, and access tokens and keys.
4. Modifiy the settings in the source code.
   - Modify <code>FeedUrl</code> to the RSS feed you want to read.
   - Modify the variables in the <code>TwitterAuth</code> class and add the access tokens and keys for connecting to Twitter.

## How do I use Twitterbot?

Read the RSS feed and post to Twitter account (this runs the script manually):

<code>$ python rss2twitter.py rss</code>

Preferably, you should use crontab to set it up to run once every 5 minutes or so. An example of this on Ubuntu 16.04 using Crontab would be

<code>*/5 * * * * /usr/bin/python /path/to/script/rss2twitter.py rss</code>.
