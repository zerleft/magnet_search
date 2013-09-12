#!/usr/bin/python
#coding=utf8
#  by luwei
#  begin:2013-9-11
#  developing...

import sys,os
import types

reload(sys)
sys.setdefaultencoding('utf-8')

'''
b编码
'''
def req_ping_encode(dic):
    try:
        #发送ping编码
        if dic.has_key('q') and dic['q'] == 'ping':
            return 'd1:ad2:id20:' + dic['a']['id'] + \
                    'e1:q4:ping1:t' + str(len(dic['t'])) + \
                    ':' + dic['t'] + '1:y1:qe'
    except ValueError:
        return ''

def req_find_node_encode(dic):
    try:
        #发送find_node编码
        if dic.has_key('q') and dic['q'] == 'find_node':
            return 'd1:ad2:id20:' + dic['a']['id'] + \
                   '6' + ':target20:' + dic['a']['target'] + \
                   'e1:q9:find_node1:t' + str(len(dic['t'])) + \
                   ':' + dic['t'] + '1:y1:qe'
    except ValueError:
        return ''

def req_get_peer_encode(dic):
    try:
        #发送get_peer编码
        if dic.has_key('q') and dic['q'] == 'get_peer':
            return 
    except ValueError:
        return ''

'''
解码
'''
def bdecode(string):
    res = {}
    try:
         
