from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from dotenv import load_dotenv
import os

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


class Test_authorization(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://passport.yandex.ru/auth/")

    def test_page_title(self):
        self.assertEqual(self.browser.title, "Авторизация")


    def test_login_password(self):
        search_string_password = self.browser.find_element(By.XPATH,
                                                           "//*[@id='passp"
                                                           "-field-login']")
        time.sleep(2)
        search_string_password.send_keys(LOGIN)
        self.browser.find_element(By.XPATH,
                                  "//*[@id='passp:sign-in']").click()
        time.sleep(2)

        search_string_password = self.browser.find_element(By.XPATH,
                                                           "//*[@id='passp"
                                                           "-field-passwd']")
        time.sleep(2)
        search_string_password.send_keys(PASSWORD)
        time.sleep(5)

        self.browser.find_element(By.XPATH,
                                  "//*[@id='passp:sign-in']").click()
        time.sleep(2)

        user_login = self.browser.find_element(By.XPATH,
                                               '//*[@id="__next"]/div/main/div'
                                               '/section[1]/div/div/ul/li['
                                               '2]/span').text
        time.sleep(2)
        self.assertEqual(user_login, LOGIN)


if __name__ == "__main__":
    unittest.main()
