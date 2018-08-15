#! /usr/bin/python3

with open("env", "w") as f:
    print("type env for slackbot")
    s = input()
    str = "PAPAYA_API_KEY=\"{0}\"".format(s)
    f.write(str)
