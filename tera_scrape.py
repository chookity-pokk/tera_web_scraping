import datetime
import time

from selenium import webdriver

from secret import (  # This is where the username and password info are stored.
    password,
    username,
)

# Need to download the browser driver online @ https://sites.google.com/a/chromium.org/chromedriver/downloads
exe_path = "C:\Program Files (x86)\chromedriver.exe"

# This changes the default directory that the file is saved to
prefs = {"download.default_directory": r"C:\Users\Hank\Documents\Testom"}
options = (
    webdriver.ChromeOptions()
)  # Changed chrome_options to options because chrome_options is depreciated.

# chrome_options.add_argument("--headless")#makes it so that the browser doesn't actually open
options.headless = True  # this also makes it work without opening the browser

options.add_argument("--log-level=3")  # This should get rid of a depreciation error.

options.add_experimental_option("prefs", prefs)
# applies the above changes to the webdriver
driver = webdriver.Chrome(exe_path, options=options)

url = "https://gdchillers.teraportal.com/tadmin/minister/prepaids/advanced-search"
print(url)
driver.get(url)
uid = username
pwd = password
user = driver.find_element_by_id("login_mail")
password = driver.find_element_by_id("login_pass")
user.clear()
password.clear()
user.send_keys(uid)
password.send_keys(pwd)
time.sleep(3)
driver.find_element_by_name("submit").click()
time.sleep(15)
print("... We're in.")
time.sleep(15)
driver.find_element_by_id("btn-download").click()
time.sleep(20)
print("Download Complete!")
