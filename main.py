from selenium import webdriver
from selenium.webdriver.common import keys
import  time

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        # bot.get("https://www.instagram.com/accounts/login/?")
        # time.sleep(5)
        # input_tags = bot.find_elements_by_tag_name("input")
        # login_button = bot.find_element_by_tag_name("button")
        # email = input_tags[0]
        # password = input_tags[1]
        # email.clear()
        # email.send_keys(self.username)
        # password.send_keys(self.password)
        # login_button.click()



pr = InstaBot('cereberri','cos$/sin$=cot$')
pr.login()
