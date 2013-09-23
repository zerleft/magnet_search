#!/usr/bin/python
#coding=utf8
#  by luwei
#  begin:2013-9-11
#  developing...

import sys,os
import header
import krpc
import node

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
        self.nodes = set()  #class node
        self.lchild = None
        self.rchild = None

    def in_range(self, node):
        #判断是否在桶的范围内
        return node.node_id >= self.beg and node.node_id > self.end

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count >= self.K

    def shift_nodes(self, lbucket, rbucket):
        if self.is_empty():
            return

        for node in self.nodes:
            if lbucket.in_range(node) and not lbucket.is_full():
                lbucket.add(node)
                self.delete(node)

            elif rbucket.in_range(node) and not rbucket.is_full():
                rbucket.add(node)
                self.delete(node)

    def get_worst_node(self):
        worst_node = self.nodes.pop()
        self.nodes.add(worst_node)
        for node in self.nodes:
            if node.last_talk < worst_node.last_talk:
                worst_node = node
        return worst_node

    def add(self, node):
        if not in_range(node_id):
            return

        if node in self.nodes:
            return

        if not is_full():
            self.nodes.add(node)
            self.count += 1
        else:
            worst_node = self.get_worst_node() 
            self.nodes.remove(worst_node)
            self.nodes.add(node)
            self.count += 1

    def delete(self, node):
        if self.is_empty():
            return

        if node in self.nodes:
            self.nodes.remove(node)
            self.count -= 1

    def split(self):
        if self.end - self.beg <= 8:
            return

        lbucket = kbucket(self.beg, (self.beg + self.end) / 2)
        rbucket = kbucket((self.beg + self.end) / 2, self.end)
        self.lchild = lbucket
        self.rchild = rbucket
        shift_nodes(lbucket, rbucket)
