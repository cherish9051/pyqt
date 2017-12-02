# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QDialog
from ui_Login import Ui_Login

class Login(QDialog):
    """登录窗口"""
    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
#        self.ui.labelTips.hide()
        # 连接槽函数登录按钮
        self.ui.OK.clicked.connect(self.slotLogin)
        # 连接槽函数退出按钮
        self.ui.Cancel.clicked.connect(self.slotCancle)

    def slotLogin(self):
        print(self.ui.User.text(),self.ui.Passwd.text())
        # if self.ui.lineEditUser.text() != "admin" or self.ui.lineEditPasswd.text() != "123456":
        #     self.ui.labelTips.show()
        #     self.ui.labelTips.setText("用户名或密码错误！")
        # else:
        #     self.accept()

    def slotCancle(self):
        self.reject()