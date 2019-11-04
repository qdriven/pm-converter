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

from core.supplement import QCaseInsensitiveDict

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
