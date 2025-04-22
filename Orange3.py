import time
from tkinter.font import names

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from faker import Faker


class Add_Employee_Test(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver,10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def login(self):

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


        username = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        username.send_keys("Admin")

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("admin123")

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()



    def test_add_employee_is_added(self):
        fake = Faker()
        self.login()

        pim_menu = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//a[@class='oxd-main-menu-item'])[2]")))
        pim_menu.click()

        add_employee_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Add Employee']")))
        add_employee_button.click()

        image = self.wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='file']")))
        image.send_keys(r"C:\Users\LENOVO\OneDrive\Pictures\Screenshots\Screenshot 2025-03-03 143017.png")
        First_name = self.driver.find_element(By.NAME,"firstName")
        First_name.send_keys(fake.name())
        middle_name = self.driver.find_element(By.NAME,"middleName")
        middle_name.send_keys(fake.name())
        Last_name = self.driver.find_element(By.NAME,"lastName")
        Last_name.send_keys(fake.name())
        employeeId = self.driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
        employeeId.send_keys(fake.building_number())

        time.sleep(2)
        save = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")))

        save.click()
        time.sleep(5)

        employee_details_header = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Personal Details']")))
        self.assertTrue(employee_details_header.is_displayed(), "Next page did not open after adding employee")

        self.driver.close()













