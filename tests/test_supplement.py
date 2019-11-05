# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_QCaseInsensitiveDict
   Description :
   Author :        patrick
   date：          2019/11/1
-------------------------------------------------
   Change Activity:
                   2019/11/1:
-------------------------------------------------
"""
from unittest import TestCase

from util.supplement import normalize_class_name, QCaseInsensitiveDict, normalize_func_name

__author__ = 'patrick'


class TestQCaseInsensitiveDict(TestCase):

    def test_caseInsensitiveDict(self):
        qdict = QCaseInsensitiveDict()
        qdict['test'] = 'test_str'
        self.assertEqual(qdict['Test'], 'test_str')
        qdict['Test'] = 'Test_str'
        self.assertEqual(qdict['Test'], 'Test_str')

        for key, value in qdict.items():
            print(key, value)

    def test_normalize_class_name(self):
        result = normalize_class_name("hello world")
        self.assertEqual(result, "HelloWorld")

    def test_normalize_func_name(self):
        result = normalize_func_name("hello world")
        self.assertEqual(result, "hello_world")
