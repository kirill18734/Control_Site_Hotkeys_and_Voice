from configs.base_sitings_run_driver import *


class Boxberry:
    def __init__(self):
        self.driver = Top_driver().driver
        self.vars = self.driver.window_handles
        discriptor_windows_2.append(self.vars)
        # Извлекаем значения из списков
        values_list1 = discriptor_windows[0]
        values_list2 = discriptor_windows_2[0]

        # Определение индекса, где отсутствует пара
        index_without_pair = None
        for i, element in enumerate(values_list2):
            if element not in values_list1:
                index_without_pair = i
                break

        self.index = index_without_pair
    def wait(self, By, value):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((By, value)))

    def close_driver(self):
        self.driver.close()
        self.driver.quit()

    def open_site_boxberry_Kirill(self):
        self.driver.switch_to.window(self.vars[self.index])
        self.driver.get(url_Boxberry)
        self.wait(By.ID, "loginform-username").click()
        self.wait(By.ID, "loginform-username").send_keys(login_boxberry_Kirill)
        self.wait(By.ID, "loginform-password").click()
        self.wait(By.ID, "loginform-password").send_keys(password_boxberry_Kirill)
        self.wait(By.CSS_SELECTOR, ".button").click()
        self.wait(By.CSS_SELECTOR, "div.flyHint_body").click()

    # "На балансе"
    def on_balance_(self):
        self.driver.switch_to.window(self.vars[self.index])
        self.wait(*on_balance).click()
        self.wait(*on_balance_text).click()

    # "Прием посылок"
    def receiving_parcels(self):
        self.driver.switch_to.window(self.vars[0])
        self.wait(*receiving_parcels).click()
        self.wait(*receiving_parcels_text).click()
