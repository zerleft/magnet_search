#!/usr/bin/python
#coding=utf8
#  by luwei
#  begin:2013-9-11
#  developing...

import sys,os
import header

reload(sys)
sys.setdefaultencoding('utf-8')

'''
桶
嗯...
'''
class kbucket:
    def __init__(self, beg, end):
        #设定桶的范围
        self.beg = beg
        self.end = end
        self.K = header.K
        #初始节点数
        self.count = 0
        self.nodes = {}  #{node_id:(ip,port)}

    def  
