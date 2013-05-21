from __future__ import division, print_function
from ConfigParser import SafeConfigParser
from datetime import datetime
import praw

UPDATE_START_LINE = '/* COUNTDOWN LIVE UPDATE: START */'
UPDATE_END_LINE = '/* COUNTDOWN LIVE UPDATE: END */'
UPDATE_STATIC_LINES = ['a[href="#days"], a[href="#hours"], a[href="#minutes"], a[href="#seconds"] {',
                       '    color: inherit;',
                       '    cursor: text;',
                       '}']

def compute_time_ago_params(target):
    countdown_delta = target - datetime.now()
    return {
        'days': countdown_delta.days,
        'hours': countdown_delta.seconds // 3600,
        'minutes': countdown_delta.seconds // 60,
        'seconds': countdown_delta.seconds
    }

def build_live_style_content_rules(time_ago_params):
    return ['a[href="#%s"]:after { content: "%d"; }' % (k, v)
            for k, v in time_ago_params.iteritems()]

def build_live_style_lines(time_ago_params):
    return ([UPDATE_START_LINE] + UPDATE_STATIC_LINES +
            build_live_style_content_rules(time_ago_params) +
            [UPDATE_END_LINE])

def build_new_stylesheet(prev_style, time_ago_params):
    new_style_lines = []
    current_lines_are_live = False
    for line in prev_style.split('\n'):
        if line == UPDATE_START_LINE:
            current_lines_are_live = True
            new_style_lines += build_live_style_lines(time_ago_params)
        elif line == UPDATE_END_LINE:
            current_lines_are_live = False
        elif not current_lines_are_live:
            new_style_lines.append(line)
    return '\n'.join(new_style_lines)

def update_countdown(username, password, subreddit_name, target):
    user_agent = '/r/{0} countdown bot'.format(subreddit_name)
    reddit = praw.Reddit(user_agent)
    reddit.login(username, password)
    
    subreddit = reddit.get_subreddit(subreddit_name)
    stylesheet_data = subreddit.get_stylesheet()
    new_style = build_new_stylesheet(stylesheet_data['stylesheet'],
                                     compute_time_ago_params(target))
    
    print(new_style)
    subreddit.set_stylesheet(new_style, stylesheet_data['prevstyle'])

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
