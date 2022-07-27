import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
url="https://myappventure.herokuapp.com/login"
email="mihzay00@gmail.com"
password="testihza"
wrong_email="testxyz@gmail.com"
wrong_password="testsalah"



class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"email").send_keys(email) # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(15)

        response_data = driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.flex.items-center.justify-center.text-xs.font-semibold.text-\[\#FF8181\].pb-4 > p").text

        self.assertIn(driver.current_url, 'https://myappventure.herokuapp.com/home')

    def test_failed_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"email").send_keys(wrong_email) # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(wrong_password) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(15)

        response_data = driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.flex.items-center.justify-center.text-xs.font-semibold.text-\[\#FF8181\].pb-4 > p").text

        self.assertIn(response_data, 'Alamat Email atau Kata Sandi Tidak Valid')

    def test_wrong_email(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"email").send_keys(wrong_email) # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(15)

        response_data = driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.flex.items-center.justify-center.text-xs.font-semibold.text-\[\#FF8181\].pb-4 > p").text

        self.assertIn(response_data, 'Alamat Email atau Kata Sandi Tidak Valid')
    
    def test_wrong_password(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"email").send_keys(email) # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(wrong_password) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(15)

        response_data = driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.flex.items-center.justify-center.text-xs.font-semibold.text-\[\#FF8181\].pb-4 > p").text

        self.assertIn(response_data, 'Kata Sandi Salah')
    
    def test_blank_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"email").send_keys() # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys() # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(15)

        response_data = driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.flex.items-center.justify-center.text-xs.font-semibold.text-\[\#FF8181\].pb-4 > p").text

        self.assertIn(response_data, 'Diperlukan Email')
    
    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
