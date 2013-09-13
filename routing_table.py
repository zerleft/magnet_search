#!/usr/bin/python
#coding=utf8
#  by luwei
#  begin:2013-9-11
#  developing...

import sys,os
import header
import kbucket

reload(sys)
sys.setdefaultencoding('utf-8')

'''
关于路由表的实现
即使用位图所占空间也大得吓人
所以不可能把整个路由表放在内存中
只能来一个node加一个
'''
class routing_table:
    def __init__(self):
        #初始桶的数量为1
        self.bucket_num = 1
        #新建一个桶
        self.bucket = set(kbucket.kbucket(0, header.max_))

    def add_node(self, node_id, addr):
        #加入节点
        if node_id < 0 or node_id >= header.max_:
            return

        for b in self.bucket:
            if node_id >= b.beg and node_id < b.end:
                b.add_node(node_id, addr)

    def del_node(self, node_id):
        #删除节点
        if node_id < 0 or node_id >= header.max_:
            return

        for b in self.bucket
        if self.nodes.has_key(node_id):
            del self.nodes[node_id]

    def get_node(self, node_id):
        if node_id < 0 or node_id >= header.max_:
            return

        if self.nodes.has_key(node_id):
            return nodes.node_id
        else:
            return ()

    def get_bucket_by_node(self, node_id):
        if node_id < 0 or node_id >= header.max_:
            return

        for b in self.bucket:
            if node_id >= b.beg and node_id < b.end:
                return b
