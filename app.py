# browser automation on github.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(chrome_options)
browser.get("https://github.com/")

sleep(3)
# go to github.com/login
signin_link = browser.find_element(By.LINK_TEXT, "Sign in")
signin_link.click()

sleep(4)
# select login field for username
username_box = browser.find_element(By.ID, "login_field")

# simulation of the user types in the username filed
username_box.send_keys("your github username or email")

# select login field for password
password_box = browser.find_element(By.ID, "password")

# simulation of the user types in the password filed
password_box.send_keys("your github password")

password_box.submit()


# assurance for login
sleep(5)
assert "fateme-jaberi" in browser.page_source

# a better way for assurance to login
sleep(30)
profile_link = browser.find_element(By.CLASS_NAME, "dashboard")
link_label = profile_link.get_attribute("innerHTML")
print(link_label)
assert "fateme-jaberi" in link_label
