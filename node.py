#!/usr/bin/python
#coding=utf8
#  by luwei
#  begin:2013-9-11
#  developing...

import sys,os
import socket
reload(sys)
sys.setdefaultencoding('utf-8')

class node:
    def __init__(self, node_id, addr):
        #节点id
        self.node_id = node_id
        #(ip, port)
        self.address = addr
        #上一次与我们通信的时间
        self.last_talk = 0
        #self.find_node_send = 0
        #self.get_peer_recv = 0
        #self.announce_peer_recv = 0

    def distance(self, other_id):
        '''
        通过异或来计算两个节点之间的距离
        结果越小距离越近
        '''
        return self.node_id ^ other_id

    def find_node(self):
        
