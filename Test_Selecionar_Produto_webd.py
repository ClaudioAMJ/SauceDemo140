import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_produto():

    url = "https://www.saucedemo.com"

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_selecionarProduto_webd(self):
        self.driver.get(self.url)
        self.driver.set_window_size(1552, 832)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click