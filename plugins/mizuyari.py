# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import default_reply
from threading import Thread
from datetime import datetime
import time

class MizuyariThread(Thread):
    _count = 0
    _runningId = 0
    def __init__(self,message):
        self._id = 0
        self._message = message
        self._isMizuyari = True
        if MizuyariThread._count < 3:
            MizuyariThread._count += 1
            self._id = MizuyariThread._count
        else:
            self._message.reply("水のやり過ぎです。もう少し待ってから試してみてください")
            self._isMizuyari = False

        Thread.__init__(self)

    def run(self):
        name = self._message.user["name"]
        while self._id != MizuyariThread._count:
            time.sleep(1)

        self._message.send("`{name}` さんが水やりを開始しました。".format(name=name))
        date = str(datetime.now())
        print("[slackbot][{date}][INFO][bot]: Start the mizuyari".format(date=date))
        time.sleep(10)
        self._message.send("水やり終了")
        date = str(datetime.now())
        print("[slackbot][{date}][INFO][bot]: Finish the mizuyari".format(date=date))
        MizuyariThread._count -= 1


@respond_to('mizuyari')
def mizuyari(message):
    date = str(datetime.now())
    name = message.user["name"]
    body = message.body["text"]
    print("[slackbot][{date}][INFO][{name}]: {body}".format(date=date, name=name, body=body))
    mizuyariThread = MizuyariThread(message)
    mizuyariThread.start()
