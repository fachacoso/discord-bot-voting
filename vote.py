#!/usr/bin/env python3

"""
In order to run this script you must install selenium first.
Instructions to install can be found here.

https://selenium-python.readthedocs.io/installation.html

This script uses a json file and selenium to automate logging in and voting
on the Discord bot website.

You must edit the "browser", "email", and "password" element in the settings.json file
with your login information in order for the script to log in.
"""

#Imports
import time
import datetime
import sys
import json

#Selenium set up
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

"""
Votes for Discord bot if vote is available.
Else, print out wait time.
"""
def main():
    # Load settings.json
    with open("settings.json", "r") as jsonFile:
        settings = json.load(jsonFile)

    # Text to input saved in settings.json
    email = settings["email"]
    password = settings["password"]

    # Checks settings.json was correctly edited
    if email == "insert email here" || password == "insert password here":
        print("""You must change the "email", and "password" element in the settings.json file
        with your login information.""")
        sys.exit(0)

    # Format for datetime object in json
    format = '%m/%d/%y %H:%M:%S'

    # Checks if json has been initialized
    if settings["last_vote"] == "0":
        settings["last_vote"] = datetime.datetime.min.strftime(format)
        with open("settings.json", "w") as jsonFile:
            json.dump(settings, jsonFile)

    # Checks if 12 hours has passed sinced last voting
    last_vote = settings["last_vote"]
    cooldown = datetime.timedelta(hours = 12)
    next_vote = datetime.datetime.strptime(last_vote, format) + cooldown
    now = datetime.datetime.now()
    time_left = str(next_vote - now)

    # If 12 hours hasn't passed, quit the program
    if next_vote > now:
        format = '%I:%M %p'
        print("Must wait %s hours and %s minutes" % (time_left[:2], time_left[3:5]))
        if (next_vote.day - now.day == 1):
            print("Next vote available tomorrow at " + next_vote.strftime(format))
        else:
            print("Next vote available at " + next_vote.strftime(format))
        sys.exit(0)



    # Selenium
    browser = settings["browser"]
    if browser = "safari":
        driver = webdriver.Safari()
    elif browser = "firefox":
        driver = webdriver.Firefox()
    elif browser = "chrome":
        driver = webdriver.Chrome()
    else:
        print("Invalid/unsupported browser inputted.  Please check settings.json")
        sys.exit(0)

    # Go to login page
    driver.get('https://top.gg/login?redir=%2Fbot%2F432610292342587392%2Fvote')

    # Elements
    em = WebDriverWait(driver, 10).until(
            lambda x: x.find_element_by_name('email'))
    pw = WebDriverWait(driver, 10).until(
            lambda x: x.find_element_by_name('password'))
    login = WebDriverWait(driver, 10).until(
            lambda x: x.find_element_by_css_selector("button[type='submit']"))

    # Interact
    em.send_keys(email)
    pw.send_keys(password)
    login.click()

    time.sleep(5)

    # Authorize bot access
    footer = WebDriverWait(driver, 10).until(
            lambda x: x.find_elements_by_xpath("//*[contains(text(), 'Authorize')]"))[1]
    authorize =  footer.find_element_by_xpath('..')
    authorize.click()

    time.sleep(5)

    # Vote
    vote = WebDriverWait(driver, 10).until(
            lambda x: x.find_element_by_id("votingvoted"))
    vote.click()

    time.sleep(5)

    # Display result
    if vote.text == "You already voted for this bot. Try again in 12 hours.":
        print("Must wait at most 12 hours.  Initializing timer.")
    else:
        print("Vote successful! New roll added.")

    # Saves last vote time for future script use
    settings["last_vote"] = now.strftime(format)
    with open("settings.json", "w") as jsonFile:
        json.dump(settings, jsonFile)

# Calls function
main()
