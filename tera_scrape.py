from secret import username, password #This is where the username and password info are stored.
from selenium import webdriver
import os, glob
import datetime
import time
from shutil import move
import pandas as pd
import openpyxl
from openpyxl import load_workbook

# Need to download the browser driver online @ https://sites.google.com/a/chromium.org/chromedriver/downloads
exe_path = "C:\Program Files (x86)\chromedriver.exe"

# This changes the default directory that the file is saved to
prefs = {
   "download.default_directory": r"C:\Users\Hank\Documents\Testom"
}
options = (
    webdriver.ChromeOptions()
)  # Changed chrome_options to options because chrome_options is depreciated.

# chrome_options.add_argument("--headless")#makes it so that the browser doesn't actually open
options.headless = True  # this also makes it work without opening the browser

options.add_argument("--log-level=3")  # This should get rid of a depreciation error.

options.add_experimental_option("prefs", prefs)
# applies the above changes to the webdriver
driver = webdriver.Chrome(exe_path, options=options)

url = "gdchiller.teraportal.com"
driver.get(url)
uid = username
pwd = password
user = browser.find_element_by_id("login_mail")
password = browser.find_element_by_id("login_pass")
user.clear()
password.clear()
user.send_keys(uid)
password.send_keys(pwd)
time.sleep(3)
browser.find_element_by_name("submit").click()#This may or may not work because it seems like the id isn't shown for sign in but it does show the type, name and value and two of those are "submit" and the other is "Login"
time.sleep(15)
#After signing in go to this page: https://gdchillers.teraportal.com/tadmin/minister/prepaids/advanced-search
csv_url = "https://gdchillers.teraportal.com/tadmin/minister/prepaids/advanced-search"
browser.get(csv_url)
time.sleep(15)
browser.find_element_by_id("btn-download").click()
time.sleep(20)
