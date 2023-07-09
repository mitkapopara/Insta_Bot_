from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = "C:/Users/meet/Desktop/Development/chromedriver.exe"
SIMILAR_ACCOUNT = "pryaofficial"
USERNAME = ""
PASSWORD = ""

class InstaFollower:
    def __init__(self, path):
        self.driver_service = Service(executable_path=path)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)


    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        cookies = self.driver.find_element(by="css selector", value="._a9_0")
        cookies.click()
        time.sleep(1)
        username = self.driver.find_element(by="name", value="username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(by="name", value="password")
        password.send_keys(PASSWORD)
        log_in = self.driver.find_element(by="xpath", value='//*[@id="loginForm"]/div/div[3]/button/div')
        log_in.click()
        time.sleep(5)


    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(3)
        followers = self.driver.find_element(by="css selector", value='.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._alvs._a6hd')
        followers.click()


    def follow(self):
        time.sleep(2)
        all_followers = self.driver.find_elements(by="css selector", value="._acan._acap._acas._aj1-")
        for follower in all_followers:
            try:
                follower.click()
                time.sleep(3)

            except ElementClickInterceptedException:
                pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

