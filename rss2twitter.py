#!/usr/bin/python
# -*- coding: utf-8 -*-

# Get RSS feed items from http://medieforskarna.se/feed/ and post tweets to account @medieforskarna.
# Originally designed by Peter M. Dahlgren, edited by Hunter McNenny
# Updated on 12-29-2016

from twython import Twython, TwythonError
import csv
import sys
import os
import re
import time
import datetime
import feedparser
from datetime import date


# Settings for the application.
class Settings:
	FeedUrl = "https://status.recklessnetwork.com/rss"							# RSS feed to read and post tweets from.
	PostedUrlsOutputFile = "rss-tweets.log"				# Log file to save all tweeted RSS links (one URL per line).


# Twitter authentication settings.
class TwitterAuth:
	# Create a Twitter app at https://apps.twitter.com/
	ConsumerKey = "XXX"
	ConsumerSecret = "XXX"
	AccessToken = "XXX"
	AccessTokenSecret = "XXX"


# Post tweet to account.
def PostTweet(message):
	try:
		twitter = Twython(TwitterAuth.ConsumerKey, TwitterAuth.ConsumerSecret, TwitterAuth.AccessToken, TwitterAuth.AccessTokenSecret) # Connect to Twitter.
		twitter.update_status(status = message) # Tweet message.
	except TwythonError as e:
		print e


# Read RSS and post.
def ReadRssAndTweet(url):
	feed = feedparser.parse(url)
	for item in feed["items"]:
		title = item["title"]
		link = item["link"]
		if not (IsUrlAlreadyPosted(link)): # Make sure we don't post any dubplicates.
			message = title + " " + link
			PostTweet(message)
			MarkUrlAsPosted(link)
			print "Posted: " + link
		else:
			print "Already posted: " + link

		# Debug:
		#print(message.encode("utf-8"))
		#time.sleep(1)


# Has the URL already been posted?
def IsUrlAlreadyPosted(url):
	if os.path.isfile(Settings.PostedUrlsOutputFile):
		# Read log file and check whether URL is in the log file.
		f = open(Settings.PostedUrlsOutputFile)
		posted_urls = f.readlines()
		f.close()
		if (url + "\n" or url) in posted_urls:
			return(True)
		else:
			return(False)
	else:
		return(False)


# Mark the specific URL as already posted.
def MarkUrlAsPosted(url):
	try:
		# Write URL to log file.
		f = open(Settings.PostedUrlsOutputFile, "a")
		f.write(url + "\n")
		f.close()
	except:
		print "Write error:", sys.exc_info()[0]


# Show available commands.
def DisplayHelp():
	print "Syntax: python medieforskarna-post.py [cmd]"
	print
	print " Available commands:"
	print "    rss    Read Reckless Status and post new items to @recklessgamers"
	print "    help   Show this help screen"
	print


# Main.
if (__name__ == "__main__"):
	if len(sys.argv) > 1:
		cmd = sys.argv[1]
		if (cmd == "rss"):
			ReadRssAndTweet(Settings.FeedUrl)
		else:
			DisplayHelp()
	else:
		DisplayHelp()
		sys.exit()
