# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import default_reply
from threading import Thread
from datetime import datetime
from plugins import device
import time

class MizuyariThread(Thread):
    __count = 0
    def __init__(self,message):
        self._message = message
        Thread.__init__(self)

    def run(self):
        name = self._message.user["name"]
        if MizuyariThread.__count != 0:
            self._message.reply("現在水やり中です。")
            return

        MizuyariThread.__count = 1
        self._message.send("`{name}` さんが水やりを開始しました。".format(name=name))
        date = str(datetime.now())
        print("[slackbot][{date}][INFO][bot]: Start the mizuyari".format(date=date))
        motor = device.Motor()
        motor.on()
        time.sleep(10)
        motor.off()
        self._message.send("水やり終了")
        date = str(datetime.now())
        print("[slackbot][{date}][INFO][bot]: Finish the mizuyari".format(date=date))
        MizuyariThread.__count = 0



@respond_to('mizuyari')
def mizuyari(message):
    date = str(datetime.now())
    name = message.user["name"]
    body = message.body["text"]
    print("[slackbot][{date}][INFO][{name}]: {body}".format(date=date, name=name, body=body))
    mizuyariThread = MizuyariThread(message)
    mizuyariThread.start()
