from unittest import TestCase
from nose.tools import ok_, eq_
from selenium import webdriver
from elements.enums import *
from util.element_act import *


class HogeTestCase(TestCase):
    def setUp(self):
        print('before test')

    def tearDown(self):
        print('after test')

    def gmail_scenario(self):
        browser = webdriver.Firefox()
        browser.get('https://www.google.com/')
        e = element_act(browser)

        e.get(Gt.gmail).click()

        ok_(e.is_displayed(Gm.login_btn))
        eq_(e.get(Gm.login_btn).text, "ログイン")

        browser.close()

    def search_scenario(self):
        browser = webdriver.Firefox()
        browser.get('https://www.google.com/')
        e = element_act(browser)

        e.get(Gt.search_word).send_keys("hoge")
        e.get(Gt.search_btn).click()

        ok_(True)

        browser.close()