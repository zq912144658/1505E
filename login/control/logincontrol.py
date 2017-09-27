#-*- coding:utf-8 -*-

class loginCon(object):


    def __init__(self,firefox):

        self.firefox = firefox

        pass


    # 点击账号登陆
    def ClickAccout(self,cls):

        self.firefox.ClickClass(cls)

        pass

    # 低耦合

    def Sendkeys(self,username,password,cls):

        self.ClickAccout(cls)

        # 查找控件输入用户名和密码
        self.firefox.FindId('loginname').send_keys(username)
        self.firefox.FindId('nloginpwd').send_keys(password)

        # 点击一下
        self.firefox.ClickId('loginsubmit')

        pass


    # 断言
    def LoginAssert(self,self1,expects,cls):

        # 查找控件进行断言
        message = self.firefox.FindClass(cls).text

        self1.assertEqual(message, expects)

        pass

    # 断言title的方法
    def LoginTtitle(self,self1,expects):

        title = self.firefox.getTitle()

        self1.assertEqual(title, expects)

        pass


    # 断言元素是不是存在
    def LoginIsexist(self,self1,cls):


        self1.assertTrue(self.firefox.FindClass(cls).is_displayed())

        pass