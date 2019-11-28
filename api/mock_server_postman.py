# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     mock_server_postman
   Description :
   Author :        patrick
   date：          2019/11/28
-------------------------------------------------
   Change Activity:
                   2019/11/28:
-------------------------------------------------
"""
import os

from flask import Flask

__author__ = 'patrick'

app = Flask(__name__)

@app.route('/mock')
def httpmock():
    # file_name='mock.json'
    return ""

if __name__ == '__main__':
    app.run(host=os.environ['HOST'],port=os.environ['PORT'],debug=True)