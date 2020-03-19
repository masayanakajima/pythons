#!/usr/bin/python
#-*- coding: utf-8 -*-
import tweepy

consumer_key = "nakajima1812@gmail.com"
consumer_secret = "M0rn1ng-1812"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
print "Access:", auth.get_authorization_url()
verifier = raw_input('Verifier:')
auth.get_access_token(verifier)
print "Access Token:", auth.access_token
print "Access Token Secret:", auth.access_token_secret