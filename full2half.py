# -*- coding: cp936 -*-

"""
规律（不含空格）：
  全角字符unicode编码从65281~65374 （十六进制 0xFF01 ~ 0xFF5E）
  半角字符unicode编码从33~126 （十六进制 0x21~ 0x7E）

特例：
  空格比较特殊，全角为 12288（0x3000），半角为 32（0x20）
  除空格外，全角/半角按unicode编码排序在顺序上是对应的（半角 + 0x7e= 全角）,所以可以直接通过用+-法来处理非空格数据，对空格单独处理。

注：
  中文文字永远是全角
  引号在中英文、全半角情况下是不同的

"""


def full2half(string):
    ustring = string.decode('cp936')
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:                              #全角空格直接转换            
            inside_code = 32 
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring
    
	
def half2full(string):
    ustring = string.decode('cp936')
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 32:                                 #半角空格直接转化                  
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:        #半角字符（除空格）根据关系转化
            inside_code += 65248

        rstring += chr(inside_code)
    return rstring
	
"""
b = full2half("Ｏｎ　ａｐｐｒｏｘｉｍａｔｉｏｎ　ｍｅａｓｕｒｅｓ　ｆｏｒ ｆｕｎｃｔｉｏｎａｌ　ｄｅｐｅｎｄｅｎｃｉｅｓ．Ｉｎｆｏｒｍａｔｉｏｎ　Ｓｙｓｔｅｍｓ".encode('cp936'))                           
print (b)
c = half2full("ｍｎ123abc博客园".encode('cp936'))                           
print (c)
"""

inputfile = input("Please input the filename (to be process full2half):\n")
f = open(inputfile)
lines = f.readlines()
f.close()

write_lines = []
for line in lines:
    write_lines.append(full2half(line.encode('cp936')))

output = open('half_%s' % inputfile, 'w')
output.writelines(write_lines)
output.close()
