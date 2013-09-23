#!/usr/bin/python
#coding=utf8
#  by luwei
#  begin:2013-9-11
#  developing...

import sys,os
import header
import kbucket
import node

reload(sys)
sys.setdefaultencoding('utf-8')

'''
路由表
'''
class routing_table:
    def __init__(self):
        #初始桶的数量为1
        self.bucket_num = 1
        #具体保存节点的桶
        self.buckets = set(kbucket.kbucket(0, header.max_))
        #树的根结点
        self.root = kbucket.kbucket(0, header.max_)

    def get_bucket_by_node(self, root, node):
        #根据节点找到对应的桶
        bucket = root
        while bucket:
            if bucket.in_range(node) and not bucket.lchild and not bucket.rchild:
                return bucket
            elif bucket.lbucket.in_range(node):
                bucket = lbucket
            elif bucket.rbucket.in_range(node):
                bucket = rbucket
            else:
                return None

    def add_node(self, root, node):
        #加入节点
        if node.node_id < 0 or node.node_id >= header.max_:
            return
        bucket = self.get_bucket_by_node(root, node)
        if bucket:
            if bucket.is_full():
                bucket.split()
                self.add_node(bucket, node)
            else:
                bucket.add(node)

    def del_node(self, node):
        #删除节点
        if node.node_id < 0 or node.node_id >= header.max_:
            return
        bucket = self.get_bucket_by_node(node)
        if bucket:
            bucket.delete(node)

    def get_closest_nodes(self, root, node, result, K):
        #获得距node最近的8个节点
        if len(result) >= K:
            return

        if not root.lchild and not root.rchild:
            result.extend(root.nodes)
            return
        if root.lchild.in_range(node):
            self.get_closest_nodes(root.lchild, node, result, K)
            self.get_closest_nodes(root.rchild, node, result, K)
        elif root.rchild.in_range(node):
            self.get_closest_nodes(root.rchild, node, result, K)
            self.get_closest_nodes(root.lchild, node, result, K)
        return
        
    def get_node(self, node_id):
        if node_id < 0 or node_id >= header.max_:
            return

        if self.nodes.has_key(node_id):
            return nodes.node_id
        else:
            return ()
