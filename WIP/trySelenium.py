#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

courses_search_url="https://my.sa.ucsb.edu/public/curriculum/coursesearch.aspx"


def rowToDict(row):
    retVal = {}
    tds = row.find_elements_by_xpath('td')
    retVal['course_id']=tds[1].text
    return retVal

def sel(url):
    driver = webdriver.Firefox()
    driver.get(url)
    expected_title = "Curriculum Search"
    if expected_title in driver.title:
        print("found ",expected_title)
        
    driver.find_element_by_xpath("//select[@name='ctl00$pageContent$courseList']/option[@value='CMPSC']").click()

    driver.find_element_by_xpath("//select[@name='ctl00$pageContent$quarterList']/option[@value='20182']").click()

    driver.find_element_by_xpath("//select[@name='ctl00$pageContent$dropDownCourseLevels']/option[@value='Undergraduate']").click()

    driver.find_element_by_xpath("//input[@name='ctl00$pageContent$searchButton']").click()

    table_rows = driver.find_elements_by_xpath("//tr[@class='CourseInfoRow']")

    dicts = list(map(lambda x:rowToDict(x),table_rows))
        
    #driver.close()

    return dicts

if __name__=="__main__":
    x = sel(courses_search_url)
