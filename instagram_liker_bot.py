from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from getpass import getpass

chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get("https://instagram.com")

username = chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
username.send_keys("rishabhk_kunwar04")
password = chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
pswd = getpass()
password.send_keys(pswd)
login_btn = chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
login_btn.click()

search_bar = chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_bar.send_keys("rishabh")
time.sleep(3)
search_bar.send_keys(Keys.ENTER)
search_bar.send_keys(Keys.ENTER)
post = chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
post.click()
like_btn = chrome.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
like_btn.click()
next_btn = chrome.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
next_btn.click()
while True:
    try:
        like_btn = chrome.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
        like_btn.click()
        next_btn = chrome.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
        next_btn.click()
        time.sleep(2)
    except:
        close_btn = chrome.find_element_by_xpath('/html/body/div[4]/div[3]/button')
        close_btn.click()
        break