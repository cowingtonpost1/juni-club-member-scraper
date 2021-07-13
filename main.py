from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
scratch_2 = 0
scratch_1 = 0
python_1 = 0
python_2 = 0
python_3 = 0
java_1 = 0
java_2 = 0
java_3 = 0
cpp = 0
pygame = 0
usaco_bronze = 0
usaco_silver = 0
usaco_gold = 0
web_1 = 0
web_2 = 0
ai = 0
ap_cs = 0
js_1 = 0
js_2 = 0
math_early_elementary_a = 0
math_early_elementary_b = 0
math_pre_algebra_a = 0
math_pre_algebra_b = 0
lines = []
with open("juni_profiles.txt") as f:
    lines = f.readlines()

browser = webdriver.Firefox()
for line in lines:
    browser.get(line.strip())
    time.sleep(10)

    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Scratch Level 2')]"):
            scratch_2+=1
    except:
        pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Scratch Level 1')]"):
            scratch_1+=1
    except:
        pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Python Level 1')]"):
            python_1+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Python Level 2')]"):
            python_2+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Python Level 3')]"):
            python_3+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'PyGame')]"):
            pygame+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'USACO Bronze')]"):
            usaco_bronze+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'USACO Silver')]"):
            usaco_silver+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'USACO Gold')]"):
            usaco_gold+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'C++')]"):
            cpp+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Java Level 1')]"):
            java_1+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Java Level 2')]"):
            java_2+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Java Level 3')]"):
            java_3+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Web Level 1')]"):
            web_1+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'JavaScript Level 1')]"):
            js_1+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Web Level 2')]"):
            web_2+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'JavaScript Level 2')]"):
            js_2+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'AI Level 1')]"):
            ai+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'AP Computer Science A')]"):
            ap_cs+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Early Elementary A')]"):
            math_early_elementary_a+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Early Elementary B')]"):
            math_early_elementary_b+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Pre-Algebra A')]"):
            math_pre_algebra_a+=1
    except: pass
    try:
        if browser.find_element_by_xpath("//*[contains(text(),'Pre-Algebra B')]"):
            math_pre_algebra_b+=1
    except: pass

print("Scratch 2: " + str(scratch_2))
print("Scratch 1: " + str(scratch_1))
print("Python 1: " + str(python_1))
print("Python 2: " + str(python_2))
print("Python 3: " + str(python_3))
print("Java 1: " + str(java_1))
print("Java 2: " + str(java_2))
print("Java 3: " + str(java_3))
print("C++ 1: " + str(cpp))
print("USACO Bronze: " + str(usaco_bronze))
print("USACO Silver: " + str(usaco_silver))
print("USACO Gold: " + str(usaco_gold))
print("PyGame: " + str(pygame))
print("Web 1: " + str(web_1))
print("Web 2: " + str(web_2))
print("JavaScript 1: " + str(js_1))
print("JavaScript 2: " + str(js_2))
print("AI: " + str(ai))
print("AP CS A: " + str(ap_cs))
print("Early Elementary A Math: " + str(math_early_elementary_a))
print("Early Elementary B Math: " + str(math_early_elementary_b))
print("Pre-Algebra A Math: " + str(math_pre_algebra_a))
print("Pre-Algebra B Math: " + str(math_pre_algebra_b))
