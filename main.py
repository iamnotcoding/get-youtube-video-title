# -*- coding: utf-8 -*-

from typing import Text
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

url = "https://hcs.eduro.go.kr/#/loginHome"

userInfoInput = open("output.txt", "w")

# class definitions


class userInfo:
    def __init__(self):
        self.myName = "심현우"
        self.myPassWord = "7949"
        self.myCity = "경기도"
        self.mySchoolLevel = "중학교"
        self.mySchool = "영덕"
        print("class is constructed")

# ----------------------------------------------------- end

# function definitions


def ErrorExit(str, driver):
    """
        prints str and close driver and exit the program
    """

    print(str)
    driver.close()
    exit()


def GetUserInfo():
    """
        gets user info from userinfo.txt
    """

    print("getting user info form userinfo.txt...")
    pass


def SelectSchool(driver):
    #driver = WebDriver(driver)

    driver.find_element_by_id("schul_name_input").click()

    cityButton = driver.find_element_by_id("sidolabel")
    cityButton.click()

    print("getting cities list...")

    isFound = False

    for city in cityButton.find_elements_by_tag_name("option"):
        if city.text == info.myCity:
            city.click()
            isFound = True

    if isFound:
        print("clicked " + info.myCity)
    else:
        ErrorExit("error : cannot find " + info.myCity, driver)

    schoolLevelButton = driver.find_element_by_id("crseScCode")
    schoolLevels = schoolLevelButton.find_elements_by_tag_name("option")
    isFound = False

    for schoolLevel in schoolLevels:
        if schoolLevel.text == info.mySchoolLevel:
            schoolLevel.click()
            isFound = True

    if isFound:
        print("clicked " + info.mySchoolLevel)
    else:
        ErrorExit("error : cannot find " + info.mySchoolLevel, driver)

    driver.find_element_by_id("orgname").send_keys(info.mySchool)
    print("enetered " + info.mySchool)

    driver.find_element_by_class_name("searchBtn").click()
    print("clicked school search button")

    # not fully implemented yet
    time.sleep(1)
    driver.find_element_by_tag_name("a")
    # ----------------------------------------------------- end
#  ----------------------------------------------------- end


print("starting program...")

info = userInfo()
# time.sleep(2)

print("note : userinfo.txt file encoidng has to be UTF-8")
print("note : please check whether your userinfo.txt encoding is UTF-8 or not")

GetUserInfo()

driver = webdriver.Chrome()
driver.get(url)  # opens url

driver.find_element_by_id("btnConfirm2").click()
print("clicked go button")

SelectSchool(driver)

time.sleep(3)
driver.close()
