#!/usr/bin/env python3

import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pprint import pprint as pp
from copy import deepcopy

courses_search_url="https://my.sa.ucsb.edu/public/curriculum/coursesearch.aspx"

def rowToDict(row):
    retVal = {}
    tds = row.find_elements_by_xpath('td')
    retVal['course_id']=tds[1].text
    retVal['course_title']=tds[2].text.strip()
    retVal['status']=tds[3].text.strip()
    retVal['enroll_code']=tds[4].text.strip()
    retVal['instructor']=tds[5].text.strip()
    retVal['days']=tds[6].text.strip()
    retVal['times']=tds[7].text.strip()
    retVal['location']=tds[8].text.strip()
    try:
       retVal['enrollment']=int(tds[9].text.strip().split("/")[0])
    except:
       retVal['enrollment']=""
    try:
       retVal['capacity']=int(tds[9].text.strip().split("/")[1])
    except:
       retVal['capacity']=""
    return retVal

def getData(driver, dept, quarter, level):
    driver.get(courses_search_url)
    expected_title = "Curriculum Search"
    if expected_title in driver.title:
        print("found ",expected_title)
        
    driver.find_element_by_xpath("//select[@name='ctl00$pageContent$courseList']/option[@value='" + dept + "']").click()

    driver.find_element_by_xpath("//select[@name='ctl00$pageContent$quarterList']/option[@value='" + quarter +  "']").click()

    driver.find_element_by_xpath("//select[@name='ctl00$pageContent$dropDownCourseLevels']/option[@value='" + level + "']").click()

    driver.find_element_by_xpath("//input[@name='ctl00$pageContent$searchButton']").click()

    table_rows = driver.find_elements_by_xpath("//tr[@class='CourseInfoRow']")

    return list(map(lambda x:rowToDict(x),table_rows))
        

def structureLines(lines):
    retval = []
    sections = []
    thisCourse = {}
    for line in lines:
      if line['enroll_code']=='':
        if thisCourse != {}:
          thisCourse['sections']=sections
          retval.append(thisCourse)
          sections = []
        thisCourse = deepcopy(line)
        thisCourse.pop('enroll_code', None)
      else:
        sections.append(line)
        
    if thisCourse != {}:
      thisCourse['sections']=sections
      retval.append(thisCourse)
      
    return retval   
          
if __name__=="__main__":
    driver = webdriver.Firefox()
    lines  = getData(driver,"CMPSC","20182","Undergraduate")

    structured = structureLines(lines)
    pp(structured)

    with open('CMPSC_20182_U.json', 'w') as outfile:
       json.dump(structured, outfile)
    
    driver.close() 
