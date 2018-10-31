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

def p_to_tuple(p_element):
    '''
    turn a p element into a tuple (course_num,title) for a given GE

    given the selenium object that represents one p element
    from the target web page, return a dictionary of the form,
    for example: {"ANTH 131":"North American Indians"}

    The p element has this format:

    <p style="text-indent: -10px; margin-top: 0px; margin-bottom: 0px; padding: 0px; margin-left: 23px;">
        ANTH    131   - <i> North American Indians 
    </i>
    </p>
    '''

    # Course Number, e.g. ANTH 131, is the text of the p element,
    # stripped of white space
    p_text = p_element.text.strip()
    course_num = p_text.split("-",1)[0].strip()
    
    # course_title, e.g. "North American Indians"
    # is the text of the child i element

    child_i_element =  p_element.find_elements_by_xpath("i")
    course_title = child_i_element[0].text.strip()

    return (course_num,course_title)
   


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

    list_of_p_elements =  driver.find_elements_by_xpath("//div[@id='content']/div[@class='contentpadding']/p")

    # dictionary <- list of tuples <- map <- (list of elem mapped to tuples)
    
    AHI_dict = dict(list(map(p_to_tuple,list_of_p_elements)))

    pprint.pprint(AHI_dict)
    driver.close()
