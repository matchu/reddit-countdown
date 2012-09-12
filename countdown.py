from bs4 import BeautifulSoup
from ConfigParser import SafeConfigParser
from datetime import datetime
from HTMLParser import HTMLParser
import praw

def update_countdown(username, password, subreddit_name, target):
    user_agent = '/r/{0} countdown bot'.format(subreddit_name)
    reddit = praw.Reddit(user_agent)
    reddit.login(username, password)
    
    subreddit = reddit.get_subreddit(subreddit_name)
    settings = subreddit.get_settings()
    
    h = HTMLParser()
    description_html = h.unescape(settings['description'])
    description_doc = BeautifulSoup(description_html)
    
    countdown_delta = target - datetime.now()
    countdown_attrs = {
        'days': str(countdown_delta.days),
        'hours': str(countdown_delta.seconds / 3600),
        'minutes': str(countdown_delta.seconds / 60),
        'seconds': str(countdown_delta.seconds)
    }
    countdown_els = description_doc.find_all(**{'data-countdown': True})
    for el in countdown_els:
        el.string = countdown_attrs[el['data-countdown']]
    
    subreddit.update_settings(description=description_doc.prettify())

if __name__ == '__main__':
    config_parser = SafeConfigParser()
    config_parser.read('countdown.cfg')

    target = config_parser.get('reddit', 'target')
    target_datetime = datetime.strptime(target, '%B %d %Y %H:%M:%S')

    update_countdown(username=config_parser.get('reddit', 'username'),
                     password=config_parser.get('reddit', 'password'),
                     subreddit_name=config_parser.get('reddit', 'subreddit'),
                     target=target_datetime)
    
    print "Countdown updated."
