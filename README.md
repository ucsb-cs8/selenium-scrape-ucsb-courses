# selenium-scrape-ucsb-courses

Using Selenium with Python to Scrape the UCSB Courses Search page


# Using the code in this repo

## To just use the JSON

You'll only need the contents of the json subdirectory, where data
has been scraped as of the date shown.

## To do your own scraping...

You'll need either the Chrome or Firefox Selenium Driver program for your platform:

* Firefox: You need the Geckodriver binary, which you may be able to find here: <https://github.com/mozilla/geckodriver/releases>

* Chrome: You'll need the Chromedriver binary, which you may be able to find here: <http://chromedriver.chromium.org/downloads>


# Big Picture

Sometimes the data we want is on a web page, but not in a form that
makes it easy to work with.

For example, data about UCSB courses is available at the web page
<https://my.sa.ucsb.edu/public/curriculum/coursesearch.aspx>.

We might prefer to have that data in CSV format so that we can load it
into a spreadsheet, or in JSON format so that we can work with it in a
Python program.

The code in this repo shows how to use Python programming along
with a piece of software called
Selenium to "scrape" the data we want from the UCSB Courses Search page,
and then store it either in CSV or JSON format.

# Background

The following tutorial will help in understanding the code in this repo:

<http://selenium-python.readthedocs.io/>

# More

* <https://blog.miguelgrinberg.com/post/using-headless-chrome-with-selenium>
