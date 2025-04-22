
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        email = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
        email.send_keys("Admin")

        password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password.send_keys("admin123")

        login_bttn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_bttn.click()

        Johntest = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")))
        Johntest.click()

        logout = self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
        logout.click()

        login_panel = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h5[text()='Login']"))
        )
        self.assertTrue(login_panel.is_displayed(), "Login page did not load after logout")

        time.sleep(5)















if __name__ == "__main__":
    unittest.main()


