from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
URL = "https://www.instagram.com/accounts/login/?source=auth_switcher"


class InstaFollower:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url=URL)
        self.target_id = ""
        time.sleep(3)

    def login(self):
        username = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main'
                                                      '/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
        username.send_keys(self.username)
        password = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main'
                                                      '/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)

    def find_following(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/"
                                           "div/div/div[2]/div[2]/span/div/a/div/div[1]/div").click()
        search = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/'
                                                    'div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
        search.send_keys(self.target_id)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/"
                                           "div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div"
                                           "/div/span").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]"
                                           "/section/main/div/header/section/ul/li[3]/a").click()

    def find_followers(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/"
                                           "div/div/div[2]/div[2]/span/div/a/div/div[1]/div").click()
        search = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/'
                                                    'div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
        search.send_keys(self.target_id)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/"
                                           "div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div"
                                           "/div/span").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/"
                                           "section/main/div/header/section/ul/li[2]/a").click()

    def follow(self):
        time.sleep(5)
        n = 1
        try:
            while True:
                try:
                    following = self.driver.find_element(By.XPATH, f"/html/body/div[5]/div[1]/div/div[2]/div/div/div/"
                                                                   f"div/div[2]/div/div/div[4]/div[1]/div/div[{n}]/"
                                                                   f"div/div/div/div[3]/div/button")
                    following.click()
                    n += 1
                    time.sleep(2)
                except ElementClickInterceptedException:
                    cancel_requested = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div"
                                                                          "/div/div/div/div/button[2]")
                    cancel_requested.click()
                    time.sleep(2)
        except NoSuchElementException:
            print("Following done")

    def unfollow(self):
        time.sleep(5)
        n = 1
        try:
            while True:
                try:
                    following = self.driver.find_element(By.XPATH, f"/html/body/div[5]/div[1]/div/div[2]/div/div/div/"
                                                                   f"div/div[2]/div/div/div[3]/div[1]/div/div[{n}]/"
                                                                   f"div/div/div/div[3]/div/button")
                    following.click()
                    n += 1
                    time.sleep(2)
                except ElementClickInterceptedException:
                    cancel_requested = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/"
                                                                          "div/div/div/div/button[1]")
                    cancel_requested.click()
                    time.sleep(2)
        except NoSuchElementException:
            print("Unfollowing done")
