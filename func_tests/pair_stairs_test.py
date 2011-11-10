from unittest.case import TestCase
from selenium import webdriver
from django.test import Client
from selenium.webdriver.common.by import By


class TestCreatePairStairs(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_should_go_add_programmer_url(self):
        # go to page
        self.driver.get('http://localhost:8000/addprogrammer')
        title = self.driver.title
        self.assertEqual('Add Programmer', title)

    def test_add_programmer(self):
        # go to page
        self.driver.get('http://localhost:8000/pairstairs')
        # add a name, and click add button
        # check name has been added to database
        element = self.driver.find_element(By.ID, "programmer name")
        print elements
        element.send_keys()
        # Submit
        self.driver.find_element(By.CSS_SELECTOR, '#add_programmers').click()
        # redirect to the pairstairs page

        # pairstairs page should display all the programmers and pairs

        # after click the count, the count increase one


  