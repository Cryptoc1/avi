#!/usr/bin/env python


###
#
#   "Why can't we use twitter to visual share how we're feeling?"
#
#   (c) Samuel Steele, cryptoc1
#
###

import os, sys
import tweepy

_usage = "avi.py usage: \n\
    -h|--help  :  Print this message \n\
    -l|--list  :  Print possible feelings\n\
    -s|--set <feeling-title>  :  Set your avi to the \"feeling\" specified in `avi --list`"


def set_avi(mood):
    if mood + '.png' in os.listdir(os.path.expanduser('~/.config/avi/images/')):
        try:
            consumer_key = '<CHANGE-ME>'
            consumer_secret = '<CHANGE-ME>'
            access_key = '<CHANGE-ME>'
            access_secret = '<CHANGE-ME>'
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_key, access_secret)
            api = tweepy.API(auth)
            api.update_profile_image(os.path.expanduser('~/.config/avi/images/') + mood + '.png')
            print 'Avi has been changed, go to http://twitter.com to check it.'
        except Exception as e:
            print e
    else:
        print 'Unrecognized mood.'


def list_moods():
    for mood in os.listdir(os.path.expanduser('~/.config/avi/images/')):
        if mood == '.DS_Store':
            pass
        else:
            print mood.replace('.png', '')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print _usage
        elif sys.argv[1] == '-l' or sys.argv[1] == '--list':
            list_moods()
        else:
            print _usage
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-s' or sys.argv[1] == '--set':
            set_avi(sys.argv[2])
        else:
            print _usage
    else:
        print _usage
