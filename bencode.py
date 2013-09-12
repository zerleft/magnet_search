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
                   '6:target20:' + dic['a']['target'] + \
                   'e1:q9:find_node1:t' + str(len(dic['t'])) + \
                   ':' + dic['t'] + '1:y1:qe'
    except ValueError:
        return ''

def req_get_peers_encode(dic):
    try:
        #发送get_peers编码
        if dic.has_key('q') and dic['q'] == 'get_peers':
            return 'd1:ad2:id20:' + dic['id'] + \
                   '9:info_hash20:' + dic['info_hash'] + \
                   'e1:q9:get_peers1:t' + str(len(dic['t'])) + \
                   ':' + dic['t'] + '1:y1:qe'
    except ValueError:
        return ''

def req_announce_peer_encode(dic):
    try:
        #发送announce_peer编码
        if dic.has_key('q') and dic['q'] == 'announce_peer':
            return 'd1:ad2:id20:' + dic['id'] + \
                   '9:info_hash20:' + dic['info_hash'] + \
                   '4:porti:' + dic['port'] + 'e5token' +\
                   str(len(dic['token'])) + ':' + dic['token'] + \
                   'e1:q13:announce_peer1:t' + str(len(dic['t'])) + \
                   ':' + dic['t'] + '1:y1:qe'
    except ValueError:
        return ''

def res_encode(dic):
    '''
    对于get_peers来说
    爬虫永远不会回应资源
    因为根本就“没有”
    只可能回应最近的8个节点
    '''
    try:
        #回应get_peers编码
        if dic.has_key('r') and dic['r'].has_key('token'):
            return 'd1:rd2:id20:' + dic['r']['id'] + \
                   '5nodes' + str(len(dic['r']['nodes'])) + \
                   ':' + dic['r']['nodes'] + '5:token' + \
                   str(len(dic['r']['token'])) + dic['r']['token'] + \
                   'e1:t' + str(len(dic['t'])) + ':' + dic['t'] + \
                   '1:y1:re'

        #回应find_node编码
        elif dic.haskey('r') and dic['r'].has_key('nodes'):
            return 'd1:rd2:id20:' + dic['r']['id'] + \
                   '5nodes' + str(len(dic['r']['nodes'])) + \
                   ':' + dic['r']['nodes'] + 'e1:t' + str(len(dic['t'])) + \
                   ':' + dic['t'] + '1:y1:re'

        #回应其他
        elif dic.haskey('r'):
            return 'd1:rd2:id20:' + dic['r']['id'] + \
                   'e1:t' + str(len(dic['t'])) + ':' + \
                   dic['t'] + '1:y1:re'
    except ValueError:
        return ''

'''
解码
'''
def bdecode(string):
    res = {}
    try:
         
