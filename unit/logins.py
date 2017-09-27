#-*- coding:utf-8 -*-
import unittest

from util import firefoxutil,urlutil

from login.control import logincontrol


class Login(unittest.TestCase):


    @classmethod
    def setUpClass(self):

        # 实例化类
        self.firefox = firefoxutil.startFirfox2()
        # 实例化url类
        self.URL = urlutil.URL()

        # 实例化对象
        self.control = logincontrol.loginCon(self.firefox)

        pass

    def setUp(self):

        # 打开京东
        self.firefox.startFirFox1(self.URL.JD_LOGIN)

        pass


    def tearDown(self):

        # 关闭浏览器
        self.firefox.closeFirFox()

        pass


    def test_us_pw(self):

        # 输入内容
        self.control.Sendkeys("","","login-tab-r")

        # 断言
        self.control.LoginAssert(self,u"请输入账户名和密码",'msg-error')


        pass

    # 用户名正确,密码正确
    def test_us_corret_pw_corret(self):

        # 输入内容
        self.control.Sendkeys("15210033534", "ww970614","login-tab-r")

        # 断言
        self.control.LoginTtitle(self,u"京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！")

        pass

    # 断言切换是不是正常
    def test_us_click(self):

        # 点击用户登陆
        self.control.ClickAccout("login-tab-r")

        # 断言元素是不是存在
        self.control.LoginIsexist(self,"login-box")

        pass

    # 扫码登陆
    def test_code_click(self):

        # 点击用户登陆
        self.control.ClickAccout("login-tab-l")

        # 断言元素是不是存在
        self.control.LoginIsexist(self, "qrcode-login")

        pass