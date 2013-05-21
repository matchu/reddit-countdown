Reddit Countdown
================

This is a pretty basic attempt to implement a countdown in a subreddit's
sidebar to help Reddit communities count down to important events.


Quick Start
-----------

First, set up [Python 2.7][py] and [the `pip` package manager][pip] if you
haven't already, then install our lone dependency: `praw`, the Python Reddit
API Wrapper.

    pip install praw

Next, create a `countdown.cfg` file based on the provided
`countdown.cfg.sample`. I'd recommend making a new bot account and granting it
mod access to the subreddit you'd like to count down in.

Finally, now that the script is ready to run, update your subreddit's sidebar
to contain countdown placeholders:

    There are [some](#days) days, [some](#hours) hours, [some](#minutes)
    minutes, and [some](#seconds) seconds remaining.

Run the script and, assuming all goes well, it will automatically fill in the
blanks and save its changes.

    python countdown.py

Since the countdown placeholders are implemented as links, you might want to
restyle them in your subreddit's CSS:

    a[href="#days"], a[href="#hours"], a[href="#minutes"], a[href="#seconds"] {
        color: inherit;
        cursor: text;
    }

Ta da! You can style all that however you like and set up your computer to run
at regular intervals or whatever you like.


[py]: http://python.org/
[pip]: http://dubroy.com/blog/so-you-want-to-install-a-python-package/#installing
