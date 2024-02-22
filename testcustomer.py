from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestCustomerForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        self.base_url = "http://localhost/customerphp/customer.php"

    def common_setup(self):
        print("Running setup...")
        self.driver.get(self.base_url)

    def fill_and_submit_form(self, title_index, first_name, last_name, age):
        self.common_setup()
        
        name = self.driver.find_element(By.ID, "firstName")
        last = self.driver.find_element(By.ID, "lastName")
        age_field = self.driver.find_element(By.ID, "age")
        drp_title = Select(self.driver.find_element(By.ID, "title"))
        drp_title.select_by_index(title_index)

        name.send_keys(first_name)
        last.send_keys(last_name)
        age_field.send_keys(age)

        submit = self.driver.find_element(By.ID, "submit")
        submit.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstName"))
        )

        return self.driver.find_element(By.ID, "firstName").text

    def test_input1(self):
        print("Running test_input1...")
        result = self.fill_and_submit_form(0, "johnjohn", "canonc", "2")
        self.assertEqual("First Name: johnjohn", result)
        print("Test case test_input1 completed successfully.")

    def test_input2(self):
        print("Running test_input2...")
        result = self.fill_and_submit_form(1, "Johnj", "canoncanoncano", "149")
        self.assertEqual("First Name: Johnj", result)
        print("Test case test_input2 completed successfully.")

    def test_input3(self):
        print("Running test_input3...")
        result = self.fill_and_submit_form(1, "johnjo", "canoncanoncanon", "150")
        self.assertEqual("First Name: johnjo", result)
        print("Test case test_input3 completed successfully.")

    def test_input4(self):
        print("Running test_input4...")
        result = self.fill_and_submit_form(1, "johnjohnjohnjo", "canoncan", "75")
        self.assertEqual("First Name: johnjohnjohnjo", result)
        print("Test case test_input4 completed successfully.")

    def test_input5(self):
        print("Running test_input5...")
        result = self.fill_and_submit_form(1, "johnjohnjohnjoh", "canoncan", "75")
        self.assertEqual("First Name: johnjohnjohnjoh", result)
        print("Test case test_input5 completed successfully.")

    def test_input6(self):
        print("Running test_input6...")
        result = self.fill_and_submit_form(1, "John", "cannoncan", "75")
        self.assertEqual("First Name: John", result)
        print("Test case test_input6 completed successfully.")

    # Uncomment and fix the following test cases if needed
    # def test_input7(self):
    #     print("Running test_input7...")
    #     result = self.fill_and_submit_form(1, "johnjohnjohnjohn", "cannoncan", "75")
    #     self.assertEqual("First Name: johnjohnjohnjohn", result)
    #     print("Test case test_input7 completed successfully.")

    # def test_input9(self):
    #     print("Running test_input9...")
    #     result = self.fill_and_submit_form(1, "johnjohn", "canoncanoncanonc", "75")
    #     self.assertEqual("First Name: johnjohn", result)
    #     print("Test case test_input9 completed successfully.")

    def test_input8(self):
        print("Running test_input8...")
        result = self.fill_and_submit_form(1, "johnjohn", "canon", "75")
        self.assertEqual("First Name: johnjohn", result)
        print("Test case test_input8 completed successfully.")

    def test_input10(self):
        print("Running test_input10...")
        result = self.fill_and_submit_form(1, "johnjohn", "canoncan", "10")
        # Update the assertion based on the expected result after submitting the form
        self.assertEqual("First Name: mary", result)
        print("Test case test_input10 completed successfully.")

    def test_input11(self):
        print("Running test_input11...")
        result = self.fill_and_submit_form(1, "johnjohn", "canoncan", "150")
        self.assertEqual("First Name: johnjohn", result)
        print("Test case test_input11 completed successfully.")    

    def tearDown(self):
        print("Capturing screenshot...")
        self.driver.save_screenshot(self._testMethodName + '.png')
        print("Screenshot captured.")
        print("Tearing down...")
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
