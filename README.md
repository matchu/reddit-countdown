Reddit Countdown
================

This is a pretty basic attempt to implement a countdown in a subreddit's
sidebar to help Reddit communities count down to important events.


Quick Start
-----------

1. Set up [Python][py] and [the `pip` package manager][pip] if you haven't
   already.
2. Install our two dependencies: `BeautifulSoup`, an HTML parser, and
   `praw`, the Python Reddit API Wrapper.
   
       pip install beautifulsoup4
       pip install praw

3. Create a `countdown.cfg` file based on the provided `countdown.cfg.sample`.
   I'd recommend making a new bot account and granting it mod access to the
   subreddit you'd like to count down in.
4. Now that the script is ready to run, update your subreddit's sidebar to
   contain countdown placeholders:
   
       There are
       <span data-countdown="days">?</span>
       days and
       <span data-countdown="hours">?</span>
       hours until release!

5. Run the script and, assuming all goes well, it will automatically fill in
   the blanks and save its changes.
   
       python countdown.py

Ta da! You can style all that however you like and set up your computer to run
at regular intervals or whatever you like.


[py]: http://python.org/
[pip]: http://dubroy.com/blog/so-you-want-to-install-a-python-package/#installing
