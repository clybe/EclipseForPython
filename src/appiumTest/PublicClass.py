# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: willie
'''

from appium import webdriver
import time


# 连接设备

def connDevice():
    # 指定平台、启动的设备、包名和启动的activity
    desired_caps = {'platformName': 'Android', 'platformVersion': '6.0', 'deviceName': '217706d3','appPackage': 'net.easyconn.carman', 'appActivity': '.MainActivity'}
    # 关联Appium
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


driver = connDevice()

def getMyTime():
    mytime=time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
    
    return mytime


# 点击resourceid
def clickResourceID(resourceid):
    try:
        if driver.find_element_by_id(resourceid):   
            getScreenShot("点击id前的界面")
            driver.find_element_by_id(resourceid).click()
            getScreenShot("点击id后的界面")
            return True
                
        else:
            print("未找到该控件："+resourceid)
            getScreenShot("未找到该控件")
            return False
    except :
        print("未找到该控件："+resourceid)
        return False    
# 点击文本
def clickText(text):
    try:
        if driver.find_element_by_name(text):
            getScreenShot("点击"+text+"前的界面")
            driver.find_element_by_name(text).click()
            getScreenShot("点击"+text+"后的界面")
            return True
        else:
            print("未找到名字："+text)
            getScreenShot("未找到文本："+text)
            return False
    except:
        print("未能点击到文本"+text)  
        return False      

# 查找文本
def findText(text):
    try:   
        if driver.find_element_by_name(text):
            getScreenShot(text)
            return True
        else:
            getScreenShot("未找到文本："+text)
            return False
    except:
        getScreenShot("未找到文本："+text)
        return False 
       

# 截屏
def getScreenShot(filename):
    mytime=getMyTime()
    myscreenshot="C:/Users/willie/Documents/"+mytime+filename+".png"
    driver.get_screenshot_as_file(myscreenshot)

