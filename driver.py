from time import sleep
from selenium import webdriver

# Replace the path to the chromedriver in your System
# Download your own chromedriver from https://sites.google.com/a/chromium.org/chromedriver/getting-started
browser = webdriver.Chrome("/Users/vincent/Desktop/Personal/LuckyBuy/chromedriver")



def login():
    browser.get("https://www.newegg.com/p/pl?d=gtx+1080")
    if browser.find_element_by_link_text("Sign in / Register"):
        browser.find_element_by_link_text("Sign in / Register").click()
        print("20s remaining to login")
        sleep(20)
        browser.get("https://www.newegg.com/p/pl?d=gtx+1080")
    sleep(2)

    print("Login success")

login()







