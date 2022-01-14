#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-05-16 21:28 
# @Author : huff 
# @File : 二叉树.py 
# @Software: PyCharm

#定义二叉树节点
class Node:
    def __init__(self,elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None

class Tree:
    def __init__(self):
        self.root = None

    #添加节点
    def add(self,elem):
        #创建节点
        node = Node(elem)
        if self.root == None:
            self.root=node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                curNode = queue.pop(0)
                if curNode.lchild == None:
                    curNode.lchild = node
                    return
                else:
                    queue.append(curNode.lchild)
                if curNode.rchild == None:
                    curNode.rchild = node
                    return
                else:
                    queue.append(curNode.rchild)

    #广度优先遍历
    def travel(self):
        queue = []
        #判断根节点是否存在
        if self.root is None:
            return
        else:
            queue.append(self.root)
        while queue:
            curNode = queue.pop(0)
            print(curNode.elem,end= '\t')
            if curNode.lchild is not None:
                queue.append(curNode.lchild)
            if curNode.rchild is not None:
                queue.append(curNode.rchild)
        print()
    #先序遍历 根 左 右
    def preOrder(self,root):
        if root is None:
            return
        else:
            print(root.elem,end='\t')
            self.preOrder(root.lchild)
            self.preOrder(root.rchild)
    #中序遍历 左 根 右
    def inOrder(self,root):
        if root is None:
            return
        else:
            self.inOrder(root.lchild)
            print(root.elem,end='\t')
            self.inOrder(root.rchild)
    #后序遍历 左 右 根
    def lastOrder(self,root):
        if root is None:
            return
        else:
            self.lastOrder(root.lchild)
            self.lastOrder(root.rchild)
            print(root.elem,end='\t')

if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    print('广度优先遍历')
    tree.travel()
    print('先序遍历')
    tree.preOrder(tree.root)
    print()
    print('中序遍历')
    tree.inOrder(tree.root)
    print()
    print('后序遍历')
    tree.lastOrder(tree.root)
