import time
from threading import Thread
import keyboard
from wxauto import WeChat
import sys
import cv2
import numpy
import urllib.request


file = "nmsf.png"


wx = WeChat()
wx.GetSessionList()

                                         #在这里写自动回复的昵称
listen_list = [
    'Henry',
    '牛马俊阳',
    '咸亨酒店（永远缅怀孔乙己）',
    '急止唐犟'
]

for i in listen_list:
    wx.AddListenChat(who=i)


def stop():
    keyboard.wait('c')
    sys.exit

thd = Thread(target = stop)
thd.start()


def main():
    while True:
        msgs = wx.GetListenMessage()
        for chat in msgs:
            who = chat.who
            amsg = msgs.get(chat)
            for msg in amsg:
                msgtype = msg.type
                if msgtype == 'friend':
                    send(who)
            

def send(who):
    wx.SendFiles(filepath=file, who=who)
    main()


main()