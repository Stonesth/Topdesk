#!/usr/bin/python
# -*- coding:utf-8 -*-
from Tools import tools_v000 as tools
import os
from os.path import dirname
import sys

# -7 for the name of this project Topdesk
#save_path = dirname(__file__)[ : -7]
save_path = os.path.dirname(os.path.abspath("__file__"))[ : -7]
propertiesFolder_path = save_path + "\\"+ "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'Topdesk', 'user_text=')

incidentNumber = ""
incidentTitle = ""
description_text = ""

def connectViaLink() :
    tools.driver.get("https://nnbe.topdesk.net/tas/secure/incident?action=lookup&lookup=naam&lookupValue="+incidentNumber)
    tools.waitLoadingPageByID("idp-9755e903-8758-4a25-8067-acb2d6341ab6")
    submit_button = tools.driver.find_element_by_id("idp-9755e903-8758-4a25-8067-acb2d6341ab6")
    submit_button.click()

def incidentTitle() :
    global incidentTitle
    tools.waitLoadingPageByXPATH("/html/body/div[1]/div/h1/div[1]")
    incidentTitle = tools.driver.find_element_by_xpath("/html/body/div[1]/div/h1/div[2]").text
    print("incidentTitle : " + incidentTitle.encode(sys.stdout.encoding, errors='replace'))
    
    global description_text     # /html/body/div[1]/div/div[3]/div[3]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]
    tools.waitLoadingPageByXPATH("/html/body/div[1]/div/div[3]/div[3]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]")
    description_text = tools.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]").text.encode('utf-8').strip()
    print("description_text : " + description_text.encode(sys.stdout.encoding, errors='replace'))
