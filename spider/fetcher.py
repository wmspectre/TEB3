# -*- coding: utf-8
"""
    fetch
    ~~~~~~~
    
    抓取网页内容

    :author: Jason Wang
    :copyright: (c) 2019
    :date created: 2019-11-05
    :python version: 3.6
"""
from time import sleep

import requests


def fetch(url, headers, cookies):
    """
    获取网页内容，会做一些重试之类的逻辑

    :param url:
    :param headers:
    :param cookies:
    :return:
    """
    max_retry = 5
    while max_retry > 0:
        rsp = requests.get(url, headers=headers, cookies=cookies)
        if rsp.status_code == 200:
            return True, rsp.content
        sleep(10)
        max_retry -= 1
    return False, None
