from time import sleep

import keyboard
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Boxberry.config import *
from Ozon.config import *
from configs.config import *


class Top_driver:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=' + user_data_dir)
        self.options.add_experimental_option('detach', True)
        self.options.add_argument(f'--remote-debugging-port={remote_debugging_port}')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()

    def wait(self, By, value):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((By, value)))

    # закрывает браузер и завершает работу программы


def check_hotkeys():
    hotkeys = {**hotkey_Ozon, **hotkey_Boxberry, **hotkeys_for_programm}

    while True:
        for action, hotkey in hotkeys.items():
            if keyboard.is_pressed(hotkey):
                sleep(1)
                return action

