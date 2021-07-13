from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
import time
URLS = []

with open("credentials.txt") as f:
    lines = f.readlines()
    email = lines[0].strip()
    passwd = lines[1].strip()


URL="https://app.junilearning.com/learner/5b314aed2503ef0d99fbe87d/club_page/60762055b2632d7a63f28e45/general"
browser = webdriver.Firefox()

browser.get(URL)
time.sleep(5)

log_in = browser.find_elements_by_xpath("/html/body/div/div/section/div/div[2]/div/div/div/a[1]/div/button/div/small")[0]
log_in.click()
time.sleep(5)


email_field = browser.find_elements_by_xpath("/html/body/div/div/section/div/div[2]/div/div/form/div[1]/input")[0]
email_field.send_keys(email)

time.sleep(1)
password_field = browser.find_elements_by_xpath("/html/body/div/div/section/div/div[2]/div/div/form/div[2]/input")[0]
password_field.send_keys(passwd)
time.sleep(1)
log_in = browser.find_elements_by_xpath("/html/body/div/div/section/div/div[2]/div/div/form/div[3]/button")[0]
log_in.click()

time.sleep(5)
members = browser.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div")[0]
members.click()

time.sleep(1)


out = open("members.out","w+")

# /html/body/div[3]/div/div/div/div[5]/div[2]/div
members_div = browser.find_elements_by_xpath("/html/body/div[3]/div/div/div/div[5]/div[2]/div")[0]
soup = BeautifulSoup(members_div.get_attribute("innerHTML"), 'html.parser')
f = open("juni_profiles.txt", "w+")
for link in soup.find_all('a'):
    f.write("https://app.junilearning.com"+link.get('href')+"\n")
f.close()
