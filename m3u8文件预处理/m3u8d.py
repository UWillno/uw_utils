import re
import os
import subprocess

from tempfile import tempdir
from time import time
from unittest import result

def wget(name,url):
    wget="unset https_proxy;wget -O {0} {1}".format(name,url)
    os.system(wget)

def getm3u8():
    data="_BT.PC.player({url:'https://v2.szjal.cn/20190508/PojU2QoU/index.m3u8',urllist:{'2':['https://v2.szjal.cn/20190508/WG5xm8bj/index.m3u8','第2集'],'3':['https://v2.szjal.cn/20190508/zM09i2e1/index.m3u8','第3集'],'4':['https://v2.szjal.cn/20190508/oTqvLbkW/index.m3u8','第4集'],'5':['https://v2.szjal.cn/20190509/jCP6e9KS/index.m3u8','第5集'],'6':['https://v2.szjal.cn/20190509/N5oV71kb/index.m3u8','第6集'],'7':['https://v2.szjal.cn/20190510/kpZ0pfvO/index.m3u8','第7集'],'8':['https://v2.szjal.cn/20190510/HE7uUzRs/index.m3u8','第8集'],'9':['https://v2.szjal.cn/20190511/mDGx54uE/index.m3u8','第9集'],'10':['https://v2.szjal.cn/20190511/fcklNKab/index.m3u8','第10集'],'11':['https://v2.szjal.cn/20190512/UVjzi1Ms/index.m3u8','第11集'],'12':['https://v2.szjal.cn/20190512/oMuq2E4f/index.m3u8','第12集'],'13':['https://v2.szjal.cn/20190513/IrBIZf3a/index.m3u8','第13集'],'14':['https://v2.szjal.cn/20190513/TYCaFcYR/index.m3u8','第14集'],'15':['https://v2.szjal.cn/20190515/ombd39E4/index.m3u8','第15集'],'16':['https://v2.szjal.cn/20190515/PhSvSP2n/index.m3u8','第16集'],'17':['https://v2.szjal.cn/20190515/CwzSGP8X/index.m3u8','第17集'],'18':['https://v2.szjal.cn/20190515/E5gkOH7d/index.m3u8','第18集'],'19':['https://v2.szjal.cn/20190517/i31QIgLk/index.m3u8','第19集'],'20':['https://v2.szjal.cn/20190517/8cyq4y2r/index.m3u8','第20集'],'21':['https://v2.szjal.cn/20190518/BMHGV5Tt/index.m3u8','第21集'],'22':['https://v2.szjal.cn/20190518/nrvvnAQP/index.m3u8','第22集'],'23':['https://v2.szjal.cn/20190519/509NMf4B/index.m3u8','第23集'],'24':['https://v2.szjal.cn/20190519/ZixP3Zwy/index.m3u8','第24集'],'25':['https://v2.szjal.cn/20190520/k8skMzNg/index.m3u8','第25集'],'26':['https://v2.szjal.cn/20190520/gS3JkcRc/index.m3u8','第26集'],'27':['https://v2.szjal.cn/20190521/t5AQD62A/index.m3u8','第27集'],'28':['https://v2.szjal.cn/20190521/OjZ6WiNh/index.m3u8','第28集'],'29':['https://v2.szjal.cn/20190522/9LhsHnYL/index.m3u8','第29集'],'30':['https://v2.szjal.cn/20190522/Ty1ff66C/index.m3u8','第30集'],'31':['https://v2.szjal.cn/20190523/5rkntfKB/index.m3u8','第31集'],'32':['https://v2.szjal.cn/20190523/gIx1pvjB/index.m3u8','第32集'],'33':['https://v2.szjal.cn/20190524/myKuKxm7/index.m3u8','第33集'],'34':['https://v2.szjal.cn/20190524/1qMUQfnG/index.m3u8','第34集'],'35':['https://v2.szjal.cn/20190525/Ihr5KK6z/index.m3u8','第35集'],'36':['https://v2.szjal.cn/20190525/7CI1Agja/index.m3u8','第36集'],'37':['https://v2.szjal.cn/20190526/IACsdo8r/index.m3u8','第37集'],'38':['https://v2.szjal.cn/20190526/vEn2UtlI/index.m3u8','第38集'],'39':['https://v2.szjal.cn/20190527/MKeJ53yI/index.m3u8','第39集'],'40':['https://v2.szjal.cn/20190527/XGkrOgX0/index.m3u8','第40集'],'41':['https://v2.szjal.cn/20190528/8LDlcmM6/index.m3u8','第41集'],'42':['https://v2.szjal.cn/20190528/g2QOO7fm/index.m3u8','第42集'],'43':['https://v2.szjal.cn/20190529/CMOj8NQ6/index.m3u8','第43集'],'44':['https://v2.szjal.cn/20190529/ybwS5joM/index.m3u8','第44集'],'45':['https://v2.szjal.cn/20190530/QHtY9wuh/index.m3u8','第45集'],'46':['https://v2.szjal.cn/20190530/FlFD130P/index.m3u8','第46集'],'47':['https://v2.szjal.cn/20190531/rnTnmhKq/index.m3u8','第47集'],'48':['https://v2.szjal.cn/20190531/Ip7rWN8A/index.m3u8','第48集'],},title:'破冰行动',id:'3rqAq',vt:'163079',page:'1'});"
    urls=re.findall(r"(https://.*?.m3u8)",data)
    # print(urls[14])
    num=1
    for i in urls:
        print(num)
        print(i)
        wget("temp.m3u8",i)
        times=subprocess.getoutput("awk '/tz|ts/{print}' temp.m3u8 | wc -l")
        if int(times) > 44:
            os.system("mv -f temp.m3u8 {0}".format(str(num)+".m3u8"))
            os.system("sed -i '/^#/d' {0}".format(str(num)+".m3u8"))
            num+=1
            continue
        end=subprocess.getoutput("awk '/.m3u8/{print}' temp.m3u8")
        print(end)
        i=re.findall(r"(https://.*?)/",i)[0]
        real_url=i+end
        print(real_url)
        wget(str(num)+".m3u8",real_url)
        os.system("rm temp.m3u8")
        os.system("sed -i '/^#/d' {0}".format(str(num)+".m3u8"))
        subprocess.getoutput("chmod +x sedm.sh;bash sedm.sh {0} {1}".format(str(num)+".m3u8",i))
        num+=1



if __name__="__main__":
    getm3u8()
    

    
