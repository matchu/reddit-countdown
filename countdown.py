from __future__ import division, print_function
from ConfigParser import SafeConfigParser
from datetime import datetime
from HTMLParser import HTMLParser
from praw import Reddit
import re

def compute_time_ago_params(target):
    countdown_delta = target - datetime.now()
    return {
        'days': countdown_delta.days,
        'hours': countdown_delta.seconds // 3600,
        'minutes': countdown_delta.seconds // 60,
        'seconds': countdown_delta.seconds
    }

def update_countdown(username, password, subreddit_name, target):
    user_agent = '/r/{0} countdown bot'.format(subreddit_name)
    reddit = Reddit(user_agent)
    reddit.login(username, password)
    
    subreddit = reddit.get_subreddit(subreddit_name)
    settings = subreddit.get_settings()
    description = HTMLParser().unescape(settings['description'])
    
    for key, value in compute_time_ago_params(target).iteritems():
        pattern = "\\[[^\\]]*\\]\\(#{0}\\)".format(key) # replace [<anything>](#<key>)
        repl = "[{0}](#{1})".format(value, key) # with [<value>](#<key>)
        description = re.sub(pattern, repl, description)
    
    print(description)
    subreddit.update_settings(description=description)

if __name__ == '__main__':
    config_parser = SafeConfigParser()
    config_parser.read('countdown.cfg')

    target = config_parser.get('reddit', 'target')
    target_datetime = datetime.strptime(target, '%B %d %Y %H:%M:%S')

    update_countdown(username=config_parser.get('reddit', 'username'),
                     password=config_parser.get('reddit', 'password'),
                     subreddit_name=config_parser.get('reddit', 'subreddit'),
                     target=target_datetime)
    
    print("Countdown updated.")
