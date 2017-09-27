#-*- coding:utf-8 -*-
import unittest
import os
import HTMLTestRunner

from unit import logins

suit = unittest.TestSuite()

# 加入到测试套件里面
suit.addTest(unittest.makeSuite(logins.Login))


# 指定路径
filename = os.getcwd()+"/jd.html"

fils = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fils,title=u'京东',description=u'描述')

runner.run(suit)

