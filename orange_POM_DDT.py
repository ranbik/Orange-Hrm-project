import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import XLUtils

class  Add_employee_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

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

        self.login()

        path = r"C:\Users\LENOVO\PycharmProjects\pythonProject\Orange-Hrm-project\MOCK_DATA (4).xlsx"
        rows = XLUtils.getrowcount(path, "data1")

        for r in range(3, rows + 1):

            try:
                firstname = XLUtils.readdata(path, "data1", r, 1)
                middlename = XLUtils.readdata(path, "data1", r, 2)
                lastname = XLUtils.readdata(path, "data1", r, 3)
                employeeid = XLUtils.readdata(path, "data1", r, 4)
                username = XLUtils.readdata(path, "data1", r, 5)
                password = XLUtils.readdata(path, "data1", r, 6)
                confirm = XLUtils.readdata(path, "data1", r, 7)

                pim_menu =self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='oxd-icon oxd-main-menu-item--icon'])[2]")))
                pim_menu.click()
                time.sleep(1)

                add_employee_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Add Employee']")))
                add_employee_button.click()

                First_name = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='First Name']")))
                First_name.send_keys(firstname)

                Middle_name = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder= 'Middle Name']")))
                Middle_name.send_keys(middlename)

                Last_name = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder= 'Last Name']")))
                Last_name.send_keys(lastname)

                Employee_id = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")))
                Employee_id.clear()
                Employee_id.send_keys(employeeid)

                image = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class = 'oxd-file-input']")))
                image.send_keys(r"C:\Users\LENOVO\OneDrive\Pictures\Screenshots\Screenshot 2025-02-08 183244.png")

                login_details =self.wait.until((EC.element_to_be_clickable((By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]"))))
                self.driver.execute_script("arguments[0].click();", login_details)
                time.sleep(2)

                Username = self.wait.until((EC.element_to_be_clickable((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]"))))
                Username.send_keys(username)
                time.sleep(2)

                Password = self.wait.until((EC.element_to_be_clickable((By.XPATH, "(//input[@type='password'])[1]"))))
                Password.send_keys(password)

                Confirmpass =self.wait.until((EC.element_to_be_clickable((By.XPATH, "(//input[@type='password'])[2]"))))
                Confirmpass.send_keys(confirm)

                save = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
                save.click()
                time.sleep(2)

                try:
                    self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Personal Details']")))
                    print("Test Passed")
                    XLUtils.writedata(path, "data1", r, 8, "passed")



                except Exception as e:
                    error_msg = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                             "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"))).text
                    print(f"Signup failed for {username}: {error_msg}")
                    XLUtils.writedata(path, "data1", r, 8, "failed")



            except Exception as e:
                print(f"An error occurred during signup for row {r}: {e}")
                XLUtils.writedata(path, "data1", r, 8, "failed")

            continue









