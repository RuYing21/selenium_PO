#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:
 @author: yansh
"""
import os
import time
import unittest
from public import HTMLTestRunner
from public.log import Log

from public.mail import SendMail as mail

log = Log()
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class AllTest:  # 定义一个类AllTest
    def __init__(self):  # 初始化一些参数和数据
        global report_name
        report_path = os.path.join(root_path, 'report', 'testreport')
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        report_name = os.path.join(report_path, 'TestResult{}.html'.format(now))
        self.caseListFile = os.path.join('.\\', "caselist.txt")  # 配置执行哪些测试文件的配置文件路径
        self.caseFile = os.path.join('.\\', "testcase")  # 真正的测试断言文件路径
        self.caseList = []
        log.info('report_name' + report_name)  # 将resultPath的值输入到日志，方便定位查看问题
        log.info('caseListFile' + self.caseListFile)  # 同理
        log.info('caseList' + str(self.caseList))  # 同理

    def set_case_list(self):
        """
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):  # 如果data非空且不以#开头
                self.caseList.append(data.replace("\n", ""))  # 读取每行数据会将换行转换为\n，去掉每行数据中的\n
        fb.close()

    def set_case_suite(self):
        """

        :return:
        """
        self.set_case_list()  # 通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:  # 从caselist元素组中循环取出case
            case_name = case.split("/")[-1]  # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)  # 将discover存入suite_module元素组
        if len(suite_module) > 0:  # 判断suite_module元素组是否存在元素
            for suite in suite_module:  # 如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:  # 从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            log.error('suite_module中没有测试集')
            return None
        return test_suite  # 返回测试集

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()  # 调用set_case_suite获取test_suite
            if suit is not None:  # 判断test_suite是否为空
                # bf(suite).report(description='用例名称xx', filename=now, log_path=report_path)
                with open(report_name, 'wb') as f:  # encoding='UTF-8'
                    # 调用HTMLTestRunner
                    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='Test Report',
                                                           description='Test Description')
                    runner.run(suit)
            else:
                log.error('没有case')
        except Exception as e:
            log.error('{}'.format(e))
        finally:
            time.sleep(3)
            # 发送邮件
            # mail.send()


if __name__ == '__main__':
    AllTest().run()
    # pass
    # AllTest().set_case_list
