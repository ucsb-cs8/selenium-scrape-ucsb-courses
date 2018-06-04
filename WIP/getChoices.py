#!/usr/bin/env python3

import json
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pprint import pprint as pp
from copy import deepcopy

courses_search_url="https://my.sa.ucsb.edu/public/curriculum/coursesearch.aspx"

def option2dict(option):
    return { "text": option.text,
             "value": option.get_attribute("value") }
   
if __name__=="__main__":
    driver = webdriver.Firefox()

    driver.get(courses_search_url)
    expected_title = "Curriculum Search"
    if expected_title in driver.title:
        print("found ",expected_title)

    subject_area_options =  driver.find_elements_by_xpath("//select[@name='ctl00$pageContent$courseList']/option")

    subject_areas = list(map(option2dict,subject_area_options))

    quarter_options =  driver.find_elements_by_xpath("//select[@name='ctl00$pageContent$quarterList']/option")

    quarters = list(map(option2dict,quarter_options))

    course_levels_options = driver.find_elements_by_xpath("//select[@name='ctl00$pageContent$dropDownCourseLevels']/option")

    course_levels = list(map(option2dict,course_levels_options))

    choices = { "subject_areas" : subject_areas,
               "quarters": quarters,
                "course_levels": course_levels,
               "date": datetime.datetime.now().isoformat() }

    with open('choices.json', 'w') as outfile:
        json.dump(choices, outfile,indent=2,sort_keys="True")

    driver.close()
