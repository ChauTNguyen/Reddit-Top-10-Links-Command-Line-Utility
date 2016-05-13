# Reddit-Top-10-Links-Command-Line-Utility
I came upon some program on Github that uses the argparse library, so I decided to make a small program that uses argparse as well.

This program, depending on the command, simply grabs the top 10 hot and/or rising links and sends it to my email. Since I frequent many subreddits, this program helps a lot because I don't have to open a bunch of tabs to get a quick idea of the top links of each subreddit and if something piques my interest I can click on the short link.

> python3 run.py -t (or --top)

gets the first 10 hottest links of each subreddit (and sends the titles/links as an email).

> python3 run.py -r (or --rising)

gets the first 10 rising links of each subreddit (and sends the titles/links as an email).

> python3 run.py -a (or --all)

does both.
