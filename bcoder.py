#!/usr/bin/python
#coding=utf8
#  by luwei
#  begin:2013-9-11
#  developing...

import sys,os
import types

reload(sys)
sys.setdefaultencoding('utf-8')

#应该先转换成网络字节序
'''
b编码
'''
def req_ping_encode(dic):
    try:
        #请求ping编码
        if dic.has_key('q') and dic['q'] == 'ping':
            return 'd1:ad2:id20:' + dic['a']['id'] + \
                    'e1:q4:ping1:t' + str(len(dic['t'])) + \
                    ':' + dic['t'] + '1:y1:qe'
    except ValueError:
        return ''

def req_find_node_encode(dic):
    try:
        #请求find_node编码
        if dic.has_key('q') and dic['q'] == 'find_node':
            return 'd1:ad2:id20:' + dic['a']['id'] + \
                   '6:target20:' + dic['a']['target'] + \
                   'e1:q9:find_node1:t' + str(len(dic['t'])) + \
                   ':' + dic['t'] + '1:y1:qe'
    except ValueError:
        return ''

def req_get_peers_encode(dic):
    try:
        #请求get_peers编码
        if dic.has_key('q') and dic['q'] == 'get_peers':
            return 'd1:ad2:id20:' + dic['id'] + \
                   '9:info_hash20:' + dic['info_hash'] + \
                   'e1:q9:get_peers1:t' + str(len(dic['t'])) + \
                   ':' + dic['t'] + '1:y1:qe'
    except ValueError:
        return ''

def req_announce_peer_encode(dic):
    try:
        #请求announce_peer编码
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

#解码后要转换成主机字节序
'''
解码
'''
def find_value(temp, key, index):
    try:
        return temp[temp.index(key) + 1][:index]
    except ValueError, AttributeError:
        return ''

def req_ping_decode(string):
    #请求ping解码
    res = {}
    try:
        temp = string.split(':')
        res['t'] = find_value(temp, 't2', -1)
        res['y'] = find_value(temp, 'y1', -1)
        res['q'] = find_value(temp, 'q4', -1)
        res['a'] = {'id':find_value(temp, 'id20', -2)}

        return res
    except ValueError, KeyError:
        return {}

def req_find_node_decode(string):
    #请求find_node解码
    res = {}
    try:
        temp = string.split(':')
        res['t'] = find_value(temp, 't2', -1)
        res['y'] = find_value(temp, 'y1', -1)
        res['q'] = find_value(temp, 'q9', -1)
        res['a'] = {'id':find_value(temp, 'id20', -1), \
                    'target':find_value(temp, 'target20', -2)}

        return res
    except ValueError, KeyError:
        return {}

def req_get_peers_decode(string):
    #请求get_peers解码
    res = {}
    try:
        temp = string.split(':')
        res['t'] = find_value(temp, 't2', -1)
        res['y'] = find_value(tmep, 'y1', -1)
        res['q'] = find_value(temp, 'q9', -1)
        res['a'] = {'id':find_value(temp, 'id20', -1), \
                    'info_hash':find_value(temp, 'info_hash20', -2)}

        return res
    except ValueError, KeyError:
        return {}

def req_announce_peer_decode(string):
    #请求announce_peer解码
    res = {}
    try:
        temp = string.split(':')
        res['t'] = find_value(temp, 't2', -1)
        res['y'] = find_value(temp, 'y1', -1)
        res['q'] = find_value(temp, 'q13', -1)
        res['a'] = {'id':find_value(temp, 'id20', -1), \
                    'info_hash':find_value(temp, 'info_hash20', -1), \
                    'port':string[string.index('porti') + 5:string.index('e5')], \
                    'token':temp[temp.index('q13') - 1][:-2]}

        return res
    except ValueError, KeyError:
        return {}

def res_ping_decode(string):
    #回应ping解码
    res = {}
    try:
        temp = string.split(':')
        res['t'] = find_value(temp, 't2', -1)
        res['y'] = find_value(temp, 'y1', -1)
        res['r'] = {'id':find_value(temp, 'id20', -2)}

        return res
    except ValueError, KeyError:
        return {}

def res_find_node_decode(string):
    #回应find_node解码
    res = {}
    try:
        temp = string.split(':')
        res['t'] = find_value(temp, 't2', -1)
        res['y'] = find_value(temp, 'y1', -1)
        res['r'] = {'id':find_value(temp, 'id20', -1), \
                    'nodes':find_value(temp, 'nodes9', -2)}

        return res
    except ValueError, KeyError:
        return {}

'''
爬虫永远不会发送get_peers和announce_peer
所以不会收到get_peers和announce_peer的回应
不必为get_peers和announce_peer的回应解码
'''
