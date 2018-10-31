#!/usr/bin/env python3

# Get a dictionary of the courses that meet the
# American History and Institutions GE requirement at UCSB
# from this page:
# https://my.sa.ucsb.edu/catalog/Current/UndergraduateEducation/AHICourseList.aspx

import json
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pprint
from copy import deepcopy
from time import sleep

ahi_url="https://my.sa.ucsb.edu/catalog/Current/UndergraduateEducation/AHICourseList.aspx"

def p_to_dict(p_element):
    '''
    turn a p element into a dictionary for a given GE

    given the selenium object that represents one p element
    from the target web page, return a dictionary of the form,
    for example: {"ANTH 131":"North American Indians"}
    '''

    return {"fake key":"fake value"}
   


if __name__=="__main__":
    
    # Bring up the firefox driver (this line would be different for Chrome)
    # See README.md of this repo for instructions on downloading that
    
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()

    driver.get(ahi_url)
    expected_title = "UC Santa Barbara General Catalog - American History and Institutions Course List"
    stripped_title=driver.title.strip()
    if expected_title == stripped_title:
        print("found ",expected_title)
    else:
        print("I was expecting title:",expected_title)
        print("But what I got instead was: ",stripped_title)

    # Look for div with id=content
    # Under that we want div with class contentpadding
    # Under that we want ALL of the p elements

    div_id_content =  driver.find_elements_by_xpath("//div[@id='content']")

    div_class_contentpadding =  driver.find_elements_by_xpath("//div[@id='content']/div[@class='contentpadding']")

    list_of_p_elements =  driver.find_elements_by_xpath("//div[@id='content']/div[@class='contentpadding']/p")

    print(div_id_content)
    print(div_class_contentpadding)
    print(list_of_p_elements)

    #subject_area_options =  driver.find_elements_by_xpath("//select[@name='ctl00$pageContent$courseList']/option")

    #subject_area_options =  driver.find_elements_by_xpath("//select[@name='ctl00$pageContent$courseList']/option")

    list_of_dictionaries = list(map(p_to_dict,list_of_p_elements))

    pprint.pprint(list_of_dictionaries)
        
    sleep(10) 
    driver.close()
