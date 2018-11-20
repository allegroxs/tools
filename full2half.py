# -*- coding: cp936 -*-

"""
���ɣ������ո񣩣�
  ȫ���ַ�unicode�����65281~65374 ��ʮ������ 0xFF01 ~ 0xFF5E��
  ����ַ�unicode�����33~126 ��ʮ������ 0x21~ 0x7E��

������
  �ո�Ƚ����⣬ȫ��Ϊ 12288��0x3000�������Ϊ 32��0x20��
  ���ո��⣬ȫ��/��ǰ�unicode����������˳�����Ƕ�Ӧ�ģ���� + 0x7e= ȫ�ǣ�,���Կ���ֱ��ͨ����+-��������ǿո����ݣ��Կո񵥶�����

ע��
  ����������Զ��ȫ��
  ��������Ӣ�ġ�ȫ���������ǲ�ͬ��

"""


def full2half(string):
    ustring = string.decode('cp936')
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:                              #ȫ�ǿո�ֱ��ת��            
            inside_code = 32 
        elif (inside_code >= 65281 and inside_code <= 65374): #ȫ���ַ������ո񣩸��ݹ�ϵת��
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring
    
	
def half2full(string):
    ustring = string.decode('cp936')
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 32:                                 #��ǿո�ֱ��ת��                  
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:        #����ַ������ո񣩸��ݹ�ϵת��
            inside_code += 65248

        rstring += chr(inside_code)
    return rstring
	
"""
b = full2half("�ϣ������������������������󡡣��� ������������졡������������󣮣ɣ�����������ӣ��������".encode('cp936'))                           
print (b)
c = half2full("���123abc����԰".encode('cp936'))                           
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
