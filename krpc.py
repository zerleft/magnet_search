#!/usr/bin/python
#coding=utf8
#  by luwei
#  begin:2013-9-11
#  developing...

import sys,os
import socket
import header
import bcoder
import header.my_node_id_str as my_node
import header.my_transaction_id as my_trans

reload(sys)
sys.setdefaultencoding('utf-8')

'''
各种rpc命令的实现
'''
def send_ping_req(sock, node):
    #发送ping请求
    dic = {'t':my_trans, 'y':'q', 'q':'ping', \
           'a':{'id':my_node}}

    encode_ping_req = bcoder.req_ping_encode(dic)
    sock.sendto(encode_ping_req, node.addr)

def send_ping_res(sock, trans_id, node):
    #发送ping回应
    dic = {'t':trans_id, 'y':'r', \
           'r':{'id':my_node}}

    encode_ping_res = bcoder.res_encode(dic)
    sock.sendto(encode_ping_res, node.addr)

def send_find_node_req(sock, target, node):
    #发送find_node请求
    dic = {'t':my_trans, 'y':'q', 'q':'find_node', \
           'a':{'id':my_node, 'target':target}}

    encode_find_node_req = bcoder.req_find_node_encode(dic)
    sock.sendto(encode_find_node_req, node.addr)

def send_find_node_res
