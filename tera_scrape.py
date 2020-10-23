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

