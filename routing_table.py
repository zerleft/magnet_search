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
        self.bucket = kbucket.kbucket(0, 2 ** header.length)
        #新建一个字典来存放node
        self.nodes = {}  #{node_id:(ip, port)}

    def add_node(self, node_id, addr):
        #加入节点
        if node_id < 0 or node_id >= 2 ** header.length:
            return

        if self.nodes.has_key(node_id):
            return

        self.nodes[node_id] = addr

    def del_node(self, node_id):
        #删除节点
        if node_id <0 or node_id >= 2 ** header.length:
            return

        if self.nodes.has_key(node_id):
            del self.nodes[node_id]

    def get_node(self, node_id):
        if node_id < 0 or node_id >= 2 ** header.length:
            return

        if self.nodes.has_key(node_id):
            return nodes.node_id
        else:
            return ()
