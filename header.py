#!/usr/bin/python
#coding=utf8
#  by luwei
#  begin:2013-9-11
#  developing...

import sys,os

reload(sys)
sys.setdefaultencoding('utf-8')

#node_id
my_node_id_16 = 0x92acb11e9df2fe73132dd59c550b5a13dfad5ab2
my_node_id_10 = 837363810007459258937404368625908675606987233970L
my_node_id_str = '\x92\xac\xb1\x1e\x9d\xf2\xfes\x13-\xd5\x9cU\x0bZ\x13\xdf\xadZ\xb2'

#transaction_id
my_transaction_id = 'zerleft'
#my_transaction_id_str = 

#路由表长度
length = 160
max_ = 2 ** 160

#桶大小
K = 8

#node_id长度
id_len = 20

#info_hash长度
info_hash_len = 20
