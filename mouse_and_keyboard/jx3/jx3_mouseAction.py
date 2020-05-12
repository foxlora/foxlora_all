import win32com.client
from win32gui import FindWindow

import random
import time
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


class JX3(object):
    def __init__(self):
        self.dm = win32com.client.Dispatch('dm.dmsoft')
        print("大漠插件版本:", self.dm.ver())

        regRst = self.dm.Reg("foxlora17d659c0ffe6793f5fba9ef6668a1b77", "")
        if regRst == 1:
            print("大漠插件已成功注册")
        elif regRst == -2:
            print("请已管理员身份运行程序")
        else:
            print("大漠插件注册出现问题")

        self.hwnd = FindWindow("KGWin32App", None)
        print("剑三程序句柄为:", self.hwnd)
        self.bindWindowEx()

    def bindWindowEx(self):
        '''
        绑定窗口并进行初始化设置，参数来源于大漠绑定测试工具
        :param hwnd:窗口句柄
        :return:None
        '''
        self.dm.BindWindowEx(self.hwnd, "normal", "dx.mouse.position.lock.api|dx.mouse.position.lock.message|"
                                                  "dx.mouse.clip.lock.api|dx.mouse.input.lock.api|"
                                                  "dx.mouse.state.api|dx.mouse.api|dx.mouse.cursor", "normal", "", 101)
        # 设置前台键鼠的模拟方式.
        self.dm.SetSimMode(1)
        # 开启鼠标/键盘真实模拟
        self.dm.EnableRealMouse(1, 2, 30)
        self.dm.EnableRealKeypad(1)

    def UnBindWindow(self):
        '''
        取消绑定窗口
        :return:
        '''
        self.dm.UnBindWindow()

    def mouseMoveTo(self, x, y):
        '''
        设置鼠标移动到的位置
        :return:
        '''
        # 操作前激活窗口
        self.dm.SetWindowState(self.hwnd, 12)
        self.dm.MoveTo(x, y)

    def mouseLeftClick(self):
        '''
        设置鼠标执行的动作
        :return:
        '''
        self.dm.LeftClick()

    def keyPress(self, key):
        '''
        设置按键
        :param key:
        :return:f
        '''
        # 操作前激活窗口
        self.dm.SetWindowState(self.hwnd, 12)
        self.dm.KeyPress(ord(key))

    def t1Action(self):
        print("键盘点击时间:", datetime.now())
        self.keyPress('F')
        self.mouseMoveTo(132, 326)
        time.sleep(0.1)

    def t2Action(self):
        print("鼠标点击时间:", datetime.now())
        self.mouseMoveTo(132, 326)
        self.mouseLeftClick()
        time.sleep(0.02)

    def action(self):
        old_time = time.time()

        for i in range(1):
            self.mouseMoveTo(804,492)
            self.dm.RightClick()
            time.sleep(0.6)
            #除滞散
            #self.mouseMoveTo(201,254)
            #战狂牌
            self.mouseMoveTo(215,303)
            #旋返书
            #self.mouseMoveTo(154,351)
            self.mouseLeftClick()
            time.sleep(0.6)

        # self.t1Action()
        # self.t2Action()

    def time(self):
        print(datetime.now())


if __name__ == '__main__':
    jx3 = JX3()
    jx3.action()
    jx3.UnBindWindow()
    #设置定时任务
    scheduler = BlockingScheduler()
    scheduler.add_job(jx3.time,'cron',hour=11,minute=59,second=50)
    scheduler.add_job(jx3.time,'cron',hour=17,minute=59,second=50)
    scheduler.add_job(jx3.action,'cron',hour=2,minute=10,second=28)

    # try:
    #     scheduler.start()
    # except Exception as e:
    #     print(e)




