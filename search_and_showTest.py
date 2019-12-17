# -*- coding: utf-8 -*-
'''
 * Name        : kgview.py - 知识图谱api请求
 * Author      : Yener(Zheng Wenyu) <yener@ownthink.com>
 * Version     : 1.0
 * Description : 从OwnThink知识图谱中获取数据，利用D3.js实现知识图谱的可视化。
 	数据获取https://api.ownthink.com/kg/knowledge?entity=刘德华
'''
import os
import subprocess
import sys
import requests


def kg_view(entity="图灵"):
    url = 'https://api.ownthink.com/kg/knowledge?entity=%s' % entity  # 知识图谱API

    sess = requests.get(url)  # 请求
    text = sess.text  # 获取返回的数据

    response = eval(text)  # 转为字典类型
    knowledge = response['data']

    nodes = []
    for avp in knowledge['avp']:
        if avp[1] == knowledge['entity']:
            continue
        node = {'source': knowledge['entity'], 'target': avp[1], 'type': "resolved", 'rela': avp[0]}
        nodes.append(node)

    for node in nodes:
        node = str(node)
        node = node.replace("'type'", 'type').replace("'source'", 'source').replace("'target'", 'target')
        print(node + ',')

    # print(nodes)
    return nodes


def writehtml(entity, nodes):
    file = open("index.html", "r")
    file_add = open("index.html", "r")
    content = file.read()
    content_add = str(nodes) + ";"
    pos = content.find("links =")
    if pos != -1:
        content = content[:pos + 7] + content_add + content[pos + 7:]
        # file = open(entity + ".html", "wb")
        file = open("showtest.html", "wb")
        content = content.encode("utf-8")
        file.write(content)
        file.close()
        file_add.close()


if __name__ == '__main__':
    # entity = "图灵"
    entity = input("输入要查询的实体(输入0退出)：")
    while (1):

        if (entity == "0"):
            break
        nodes = []
        nodes = kg_view(entity)
        writehtml(entity, nodes)

        # subprocess.call('showtest.html')
        os.system(r'start .\showtest.html')
        entity = input("输入要查询的实体(输入0退出)：")
