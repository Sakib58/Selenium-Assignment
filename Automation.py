from selenium import webdriver
from getpass import getpass
username="170042058"
password="Abc.1234"

driver=webdriver.Chrome("F:\\Software\\chromedriver.exe")
driver.get("https://elp.duetbd.org/")
login_link = driver.find_element_by_link_text('Log in')
login_link.click()
username_textbox=driver.find_element_by_id("username")
password_textbox=driver.find_element_by_id("password")

username_textbox.send_keys(username)
password_textbox.send_keys(password)

login_btn=driver.find_element_by_id("loginbtn")
login_btn.submit()