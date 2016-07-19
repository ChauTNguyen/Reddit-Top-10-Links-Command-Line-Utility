#!env/bin/python

import argparse, smtplib, praw
from config import * # password, my_email_address, target_email_address

r = praw.Reddit(user_agent="Customized Reddit Feed for Myself")

list_of_subreddits = [
    "learnprogramming", "cscareerquestions", "leagueoflegends",
    "todayilearned", "worldnews", "graphic_design"
]


def send_email(message):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(my_email_address, password)
    send_mail_status = smtpObj.sendmail(my_email_address, target_email_address, message.encode('utf-8'))

    if send_mail_status != {}:
        print('There was a problem sending the email to', target_email_address)
    else:
        print('Email successfully sent to', target_email_address)

    smtpObj.quit()
    print()


def send_top():
    print("*********************TOP******************************")
    message = "Subject: Your customized reddit newsfeed: Hot\n"

    for subreddit in list_of_subreddits:
        submissions = r.get_subreddit(subreddit).get_top(limit=10)

        print("---r/" + subreddit + "--- ::: ", end='')
        print("LOADING => ::: ", end='')

        message += "---r/" + subreddit + "---" + "\n"

        for submission in submissions:
            message += str(submission) + " => " + submission.short_link + "\n"

        message += "\n"

        print("=> LOADED")

    print("\nDone.")

    send_email(message)


def send_rising():
    print("*******************RISING****************************")
    message = "Subject: Your customized reddit newsfeed: Rising\n"

    for subreddit in list_of_subreddits:
        submissions = r.get_subreddit(subreddit).get_rising(limit=10)

        print("---r/" + subreddit + "--- ::: ", end='')
        print("LOADING => ::: ", end='')

        message += "---r/" + subreddit + "---" + "\n"

        for submission in submissions:
            message += str(submission) + " => " + submission.short_link + "\n"

        message += "\n"

        print("=> LOADED")

    print("\nDone.")

    send_email(message)


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--all",
                        action="store_true",
                        help="Sends the 10 top links and 10 currently rising links.")
    parser.add_argument("-t", "--top",
                        action="store_true",
                        help="Sends the 10 top links.")
    parser.add_argument("-r", "--rising",
                        action="store_true",
                        help="Sends the 10 currently rising links.")

    args = parser.parse_args()

    if args.all:
        send_top()
        send_rising()
    elif args.top:
        send_top()
    elif args.rising:
        send_rising()
    else:
        pass

    return args


def main():
    args = parse_args()

if __name__ == "__main__":
    main()