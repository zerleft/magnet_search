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

    def in_range(self, node_id):
        #判断是否在桶的范围内
        return node_id >= self.beg and node_id > self.end

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count >= self.K

    def shift_nodes(self, lbucket, rbucket):
        if is_empty():
            return

        for node_id in self.nodes:
            if lbucket.in_range(node_id) and not lbucket.is_full():
                lbucket.add(node_id, nodes[node_id])
                delete(node_id)

            elif rbucket.in_range(node_id) and not rbucket.is_full():
                rbucket.add(node_id, nodes[node_id])
                delete(node_id)

    def add(self, node_id, addr):
        if not in_range(node_id):
            return

        if not is_full():
            self.nodes[node_id] = addr
            self.count += 1
        else:

    def delete(self, node_id):
        if is_empty():
            return

        if self.nodes.has_key(node_id):
            del nodes[node_id]
            self.count -= 1

    def split(self):
        if self.end - self.beg <= 8:
            return

        lbucket = kbucket(beg, (beg + end) / 2)
        rbucket = kbucket((beg + end) / 2, end)
        shift_nodes(lbucket, rbucket)
