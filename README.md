# selenium-scrape-ucsb-courses

Using Selenium with Python to Scrape the UCSB Courses Search page


# Using the code in this repo

## installs

You'll need:

```
pip install selenium
```

or

```
pip3 install selenium
```

## To just use the JSON

You'll only need the contents of the json subdirectory, where data
has been scraped as of the date shown.

## To do your own scraping...

You'll need either the Chrome or Firefox Selenium Driver program for your platform:

* Firefox: You need the `geckodriver` binary, which you may be able to find here: <https://github.com/mozilla/geckodriver/releases>

* Chrome: You'll need the `chromedriver` binary, which you may be able to find here: <http://chromedriver.chromium.org/downloads>

You then need to put those in your path.  If you know how to do that, great, go ahead.  If not, read on.

Here's how you can check whether they are in your path. The command `which` followed by a executable file name will tell you, if that executable file name is in your path, where it found it:

```
169-231-155-129:AHI pconrad$ which geckodriver
/usr/local/bin/geckodriver
169-231-155-129:AHI pconrad$ which chromedriver
./chromedriver
169-231-155-129:AHI pconrad$
```

If it's not in your path, you'll be given an empty response:

```
169-231-155-129:AHI pconrad$ which chromedriver
169-231-155-129:AHI pconrad$
```

If that's what you get, then you need to follow the steps to add the
driver (`chromedriver` or `geckodriver`) into your path (see below.)

# The error you get when you don't have the driver in your path

You need to both:
* download the file `chromedriver` (for Chrome) or the file `geckodriver` (for Firefox) and
* put it in your path (explained below)

If you haven't done BOTH steps, you'll get this error message:

```
169-231-155-129:AHI pconrad$ python3 getAHI.py
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/selenium/webdriver/common/service.py", line 76, in start
    stdin=PIPE)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/subprocess.py", line 709, in __init__
    restore_signals, start_new_session)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/subprocess.py", line 1344, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'chromedriver': 'chromedriver'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "getAHI.py", line 26, in <module>
    driver = webdriver.Chrome()
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/selenium/webdriver/chrome/webdriver.py", line 68, in __init__
    self.service.start()
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/selenium/webdriver/common/service.py", line 83, in start
    os.path.basename(self.path), self.start_error_message)
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home

```

# How do I get it in my path?

First, put the file `geckodriver` or `chromedriver` in your current directory,
like this:

```
169-231-155-129:AHI pconrad$ ls
chromedriver	geckodriver.log	getAHI.py	getAHI.py~
```

Then, you need this command, which adds the current directory, i.e. `.`, to your `PATH`:

```
169-231-155-129:AHI pconrad$ export PATH=${PATH}:.
169-231-155-129:AHI pconrad$ 
```

Let's understand what we just did.  If we type `echo PATH`, it just gives us
the letters `PATH`:

```
169-231-155-129:AHI pconrad$ echo PATH
PATH
169-231-155-129:AHI pconrad$
```

But if we put a `$` in front of PATH, or with `{}` like this: `${PATH}`, it
*dereferences* the shell environment variable called `PATH`, and we get the
value of that variable:

```
169-231-155-129:AHI pconrad$ echo $PATH
/Library/Frameworks/Python.framework/Versions/3.6/bin:/Library/Frameworks/Python.framework/Versions/3.6/bin:/Users/pconrad/.nvm/versions/node/v6.0.0/bin:/Users/pconrad/bin:/Users/pconrad/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/usr/local/bin:/usr/local/heroku/bin:/Library/Frameworks/Python.framework/Versions/3.4/bin:/Users/pconrad/.rvm/gems/ruby-2.1.7/bin:/Users/pconrad/.rvm/gems/ruby-2.1.7@global/bin:/Users/pconrad/.rvm/rubies/ruby-2.1.7/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/Library/TeX/texbin:/opt/X11/bin:/Users/pconrad/.rvm/bin:/Applications/Postgres.app/Contents/Versions/9.4/bin:/Users/pconrad/.rvm/bin:/Users/pconrad/apache-ant-1.9.7/bin:.
169-231-155-129:AHI pconrad$ 
```

What is this value?  It is a list of directories where the shell looks for programs.   They are each separated by a colon, `:`.

By adding `.` at the end, we tell the operating system (Windows, Mac or Linux) that we want it to look in the current directory for programs after it has looked everywhere else:

```
169-231-155-129:AHI pconrad$ export PATH=${PATH}:.
169-231-155-129:AHI pconrad$ 
```

That should make it look in the current directory for your your `geckodriver` or your `chromedriver` binary, which allows your Python script to communicate with the browser of your choice.

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
