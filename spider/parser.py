# -*- coding: utf-8
"""
    parser
    ~~~~~~~
    
    Description
    
    :author: Jason Wang
    :copyright: (c) 2019
    :date created: 2019-11-05
    :python version: 3.6
"""
from pyquery import PyQuery as pq


def parse_year_link(content):
    """
    从联赛页面中解析不同年份的页面地址

    :param content:
    :return:
    """
    ret_dict = dict()
    doc = pq(content)
    try:
        for a in doc('div.select-border').eq(0).find('li a'):
            year = a.text
            link = 'https://data.leisu.com' + a.attrib['href'][2:]
            ret_dict[year] = link
    except:
        return False, None
    return True, ret_dict
