#!/usr/bin/env python


###
#
#   "Why can't we use twitter to visual share how we're feeling?"
#
#   (c) Samuel Steele, cryptoc1
#
###

import os, sys, ConfigParser
import tweepy
import webbrowser

_usage = "avi.py usage:\n\
    -h|--help  :  Print this message\n\
    --init  :  Initialize your config\n\
    -l|--list  :  Print possible feelings\n\
    -s|--set <feeling-title>  :  Set your avi to the \"feeling\" specified in `avi --list`"

def init_config():
    pass

def config_exists():
    return os.path.exists(os.path.expanduser('~/.config/avi/default.cfg'))

def config_initialized():
    conf = ConfigParser.ConfigParser()
    if config_exists():
        conf.read(os.path.expanduser('~/.config/avi/default.cfg'))
        if conf.get('twitter', 'consumer_key') != 'None' and conf.get('twitter', 'consumer_secret') != 'None' and conf.get('twitter', 'access_key') != 'None' and conf.get('twitter', 'access_secret') != 'None':
            return True
        else:
            return False
    else:
        return False

def get_tokens():
    conf = ConfigParser.ConfigParser()
    if config_exists():
        conf.read(os.path.expanduser('~/.config/avi/default.cfg'))
        return {
            "consumer_key": conf.get('twitter', 'consumer_key'),
            "consumer_secret": conf.get('twitter', 'consumer_secret'),
            "access_key": conf.get('twitter', 'access_key'),
            "access_secret": conf.get('twitter', 'access_secret')
        }
    else:
        return None

def get_name():
    conf = ConfigParser.ConfigParser()
    if  config_exists():
        conf.read(os.path.expanduser('~/.config/avi/default.cfg'))
        return conf.get('user', 'name')
    else:
        return None

def set_avi(mood):
    if mood + '.png' in os.listdir(os.path.expanduser('~/.config/avi/images/')):
        try:
            tokens = get_tokens()
            auth = tweepy.OAuthHandler(tokens['consumer_key'], tokens['consumer_secret'])
            auth.set_access_token(tokens['access_key'], tokens['access_secret'])
            api = tweepy.API(auth)
            api.update_profile_image(os.path.expanduser('~/.config/avi/images/') + mood + '.png')
            api.update_profile(name=mood + " " + get_name())
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
        if sys.argv[1] == '--init':
            init_config()
        elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print _usage
        elif sys.argv[1] == '-l' or sys.argv[1] == '--list':
            list_moods()
        else:
            print _usage
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-s' or sys.argv[1] == '--set':
            if config_exists() and config_initialized():
                set_avi(sys.argv[2])
            else:
                print 'Config does not exist, or was not properly setup.'
        else:
            print _usage
    else:
        print _usage
