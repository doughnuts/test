from wxauto import WeChat
import time
import random

wx=WeChat()

while True:
    list01=['张三','李四','王五','赵六']
    wx.SendMsg(list01[random.randint(0,3)],'姐姐')
    time.sleep(random.randint(1, 10))