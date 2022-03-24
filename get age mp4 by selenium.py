from selenium.webdriver.common.by import By
from time import sleep
import re
import os
from selenium import webdriver

EDGE = {
            "browserName": "MicrosoftEdge",
            "version": "99.0.1150.46",
            "platform": "LINUX",
            "ms:edgeOptions": {
                'extensions': [],
                'args': [
                    '--headless',
                    '--disable-gpu',
                    '--remote-debugging-port=9222',
                ]}
        }
driver = webdriver.Edge(executable_path="/home/uwillno/Desktop/Python/driver/msedgedriver",capabilities=EDGE)
#无头模式
 



def getmp4(url):
    driver.get(url=url)
    sleep(1)
    iframe = driver.find_element(By.ID, "age_playfram")
    driver.switch_to.frame(iframe)
    sleep(1)
    html = driver.page_source
    d = re.findall(r'src="(https.*?mp4)"', html)
    return d
        

def main():
    # f=open("urls.txt","w+")
    # i=6
    unset_proxy="unset http_proxy;unset https_proxy;" #关代理
    name="摇曳百合S2" #番剧名称
    start=1 #开始集数
    end=12 #结束集数
    url = "https://www.agemys.com/play/20120083?playid=2_" #链接去除集数
    os.system("mkdir "+name)
    for i in range(start,end+1):
        temp = url+str(i)
        mp4 =getmp4(temp)
        for item in mp4:
            print("正在下载第"+str(i)+"集")
            os.system(unset_proxy+"cd "+name+";wget "+item+" -O "+name+"_"+str(i)+".mp4")
    # print("hello")
    # f.close
    print("下载完成")
    driver.close()

if __name__=="__main__":
    main()
