#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:
 @author: yansh
"""
from public.basepage import BasePage


class HomePage(BasePage):
    kw = ['id', 'kw']
    # driver.type(kw, 'selenium+python')
    # driver.my_sleep(3)/
    # driver.type(kw, 'selenium')
    su = ['id', 'su']

    # driver.click(su)
    # type(kw, "s")

    def type_search(self, text):
        self.type(self.kw, text)

    def send_submit_btn(self):
        self.click(self.su)
