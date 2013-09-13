#!/usr/bin/python
#coding=utf8
#  by luwei
#  begin:2013-9-11
#  developing...

import sys,os
import socket
import header

reload(sys)
sys.setdefaultencoding('utf-8')

def btol(net_str):
    #转换id和port的基础
    return long(str(net_str).encode('hex'), 16)

def ltob(long_num):
    #btol的逆操作
    num_str = hex(long_num)[2:].rstrip('L')
    if len(num_str) % 2 == 1:
        num_str = '0%s' %num_str
    return num_str.decode('hex')

def encode_id(node_id):
    #node_id编码
    if node_id < 0 or node_id >= 2 ** header.length:
        return ''
    encode_str = ltob(node_id)
    if len(encode_str) < header.id_len:
        return ('\x00' * header.id_len - len(encode_str)) + encode_str
    else:
        return encode_str

def decode_id(net_str):
    #node_id解码
    if len(net_str) != 20:
        return
    node_id = btol(net_str)
    return node_id

def encode_port(port):
    #port编码
    if port < 0 or port >= 2 ** 16:
        return ''
    encode_port = ltob(port)
    if len(encode_str) < 2:
        return ('\x00' * 2 - len(encode_port)) + encode_port
    else:
        return encode_port

def decode_port(port_str):
    #port解码
    if len(port_str) != 2:
        return
    return btol(port_str)

def encode_addr(addr):
    #地址编码
    ip, port = addr
    ip_str = socket.inet_aton(ip)
    port_str = encode_port(port)
    return ip_str+port_str

def decode_addr(addr_str):
    #地址解码
    if len(addr_str) != 6:
        return
    ip = socket.inet_ntoa(addr_str[:4])
    port = decode_port(addr_str[4:])
    return (ip, port)
