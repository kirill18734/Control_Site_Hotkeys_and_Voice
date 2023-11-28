from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import *


class Top_driver:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.options.add_argument('--user-data-dir=' + user_data_dir)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()

    def close_driver(self):
        self.driver.quit()

    def wait(self, By, value):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((By, value)))

    def del_addressable_storage(self):
        self.driver.get('https://pvz.ozon-dostavka.ru/address_storage/')
        #здесь с какого числа нужно начать удалять
        my_elements = 201
        #то есть мы удаляе с 201 до 499
        for i in range(my_elements, my_elements + 298):
            self.wait(By.CSS_SELECTOR, f'.island_\+P-k6:nth-child({my_elements}) svg').click()
            sleep(1)
            self.wait(By.CSS_SELECTOR, '.primary-negative_5dX6y > .content_PcVb1').click()
            sleep(1)

