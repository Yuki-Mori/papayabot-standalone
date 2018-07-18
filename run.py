# coding: utf-8
import sys
from slackbot.bot import Bot
from plugins.device import Motor

def main():
    Motor.setup()
    bot = Bot()
    try:
        bot.run()
    except KeyboardInterrupt:
        Motor.finish()
        sys.exit()



if __name__ == "__main__":
    print("start slackbot")
    main()
