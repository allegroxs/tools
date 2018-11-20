#!/usr/bin/python
# -*- coding: utf-8 -*-
#预处理：数据块to数组

from __future__ import print_function
import re
import os
import struct
import numpy as np
def get_array(block_path):#文件名
  
  block_name = os.path.basename(block_path)

  #是否执行
  #flag = input('Process '+ block_name +'? (Y/N)')
  #if flag != 'Y' and flag != 'y':
  #  return 0
  #print(type(flag))
  print('Now we process:',block_name)

  #文件名中可能有当前所处理的区块的数据长度，要拆分出来：
  block_name_apart = re.split('[_.]',block_name)   #相比*.split，re.split可以在[]中引入多个分隔符
  file_size = os.path.getsize(block_path)

  #获得int类型的width:
  st = block_name_apart[2]
  width = int(re.sub("\D", "", st))

  #计算文件所含条目：
  items_per_block = int(file_size/width)

  #打开文件：
  f = open(block_path,'rb')#,'r',encoding='ISO-8859-1')
  lines = []

  #读数据存入列表。需要考虑是否现在就将Bytes转化成int。
  r = f.read(width)
  while r:
    line = r#int.from_bytes(r, byteorder='big', signed=True)
    lines.append(line)
    r = f.read(width)
  f.close()
  print('Including items:',len(lines))

  #将ITEMS数值化的一些统计
  #转化成整数
  values = []
  for i in range(0,items_per_block):
    sum = 0
    for j in range(0,width):
      sum = int(lines[i][j]) * (256 ** j) + sum
      #sum = ord(lines[i][j]) * (256 ** j) + sum
    values.append(sum)
  return(values)


support_blocks = np.array([get_array('./dataset/O_SHIPPRIORITY_4Bytes_0.txt'),  #1
                                           get_array('./dataset/O_ORDERDATE_10Bytes_0.txt'),  #2
                                           get_array('./dataset/P_SIZE_4Bytes_0.txt'),  #5
                                           get_array('./dataset/PS_SUPPLYCOST_8Bytes_0.txt'),  #6
                                           get_array('./dataset/L_PARTKEY_4Bytes_0.txt'),  #7
                                           get_array('./dataset/L_ORDERKEY_4Bytes_0.txt'),  #8
                                           get_array('./dataset/P_COMMENT_23Bytes_0.txt'),  #9
                                           get_array('./dataset/P_PARTKEY_4Bytes_0.txt'),
                                           get_array('./dataset/C_ACCTBAL_8Bytes_0.txt') ] ,  
                                           dtype = np.float64)
support_labels =np.array([[1,0,0,0,0,0,0,0],
                                         [0,1,0,0,0,0,0,0], 
                                         [0,0,1,0,0,0,0,0], 
                                         [0,0,0,1,0,0,0,0], 
                                         [0,0,0,0,1,0,0,0], 
                                         [0,0,0,0,0,1,0,0], 
                                         [0,0,0,0,0,0,1,0],
                                         [0,0,0,0,0,0,0,1],
                                         [0,0,0,1,0,0,0,0]])

np.save('support_blocks.npy', support_blocks)
np.save('support_labels.npy', support_labels)


