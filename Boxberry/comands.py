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

    # Далее - Фирменная упаковка
    def next_Branded_packaging(self):
        # кликает на "Далее"
        self.wait(*receiving_parcels_next).click()
        # Фирменная упаковка
        self.wait(*acceptance_of_parcels_further_branded_packaging).click()
        #Кликает на выбор упаковки
        self.wait(*Acceptance_of_mailingsdall_firm_package_packing).click()

    # Вложение соответсвует описанию - расчитать стоймость отправления
    def Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost(self):
        # Кликает на выбор упаковки
        self.wait(*Acceptance_of_mailingsdall_firm_package_packing).click()
        # Кликает на "Тип вложения"
        self.wait(*Receiving_parcels_Next_Type_of_enclosure).click()
        # Товары народного потребления (без техники, единичное количество)
        self.wait(*Receiving_parcels_Next_Type_of_enclosure_Consumer_goods).click()
        # Кликает на "Тип вложения"
        self.wait(*Receiving_parcels_Next_Type_of_enclosure).click()
        # кликает на "Вложение соответсвует описанию"
        self.wait(*Receiving_parcels_Next_Branded_packaging_Enclosure_matches_description).click()
        # Кликает на "расчитать стоймость отправления"
        self.wait(*Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost).click()

    # Прием посылок - Далее - Фирменная упаковка - упаковка - Конверт А4 для документов
    def Acceptance_of_parcels_Further_Branded_packaging_packaging_A4_envelope_for_documents(self):
        self.driver.switch_to.window(self.vars[0])
        self.next_Branded_packaging()
        # Конверт А4 для документов
        self.wait(*Acceptance_of_parcels_Further_Branded_packaging_packaging_A4_envelope_for_documents).click()
        self.Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost()

    # Прием посылок - Далее - Фирменная упаковка - упаковка - Короб L
    def Receiving_parcels_Next_Branded_packaging_Packaging_Box_L(self):
        self.driver.switch_to.window(self.vars[0])
        self.next_Branded_packaging()
        # Короб L
        self.wait(*Receiving_parcels_Next_Branded_packaging_Packaging_Box_L).click()
        self.Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost()

    # Прием посылок - Далее - Фирменная упаковка - упаковка - Короб S
    def Receiving_parcels_Next_Branded_packaging_Packaging_Box_S(self):
        self.driver.switch_to.window(self.vars[0])
        self.next_Branded_packaging()
        # Короб S
        self.wait(*Receiving_parcels_Next_Branded_packaging_Packaging_Box_S).click()
        self.Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost()

    # Прием посылок - Далее - Фирменная упаковка - упаковка - Короб TL
    def Receiving_parcels_Next_Branded_packaging_Packaging_Box_TL(self):
        self.driver.switch_to.window(self.vars[0])
        self.next_Branded_packaging()
        # Короб TL
        self.wait(*Receiving_parcels_Next_Branded_packaging_Packaging_Box_TL).click()
        self.Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost()

    # Прием посылок - Далее - Фирменная упаковка - упаковка - Короб XL
    def Receiving_parcels_Next_Branded_packaging_Packaging_Box_XL(self):
        self.driver.switch_to.window(self.vars[0])
        self.next_Branded_packaging()
        # Короб XL
        self.wait(*Receiving_parcels_Next_Branded_packaging_Packaging_Box_XL).click()
        self.Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost()

    # Прием посылок - Далее - Фирменная упаковка - упаковка - Короб ХS
    def Receiving_parcels_Next_Branded_packaging_Packaging_Box_XS(self):
        self.driver.switch_to.window(self.vars[0])
        self.next_Branded_packaging()
        # Короб ХS
        self.wait(*Receiving_parcels_Next_Branded_packaging_Packaging_Box_XS).click()
        self.Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost()

    # Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном L
    def Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_L(self):
        self.driver.switch_to.window(self.vars[0])
        self.next_Branded_packaging()
        # Пакет с клапаном L
        self.wait(*Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_L).click()
        self.Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost()

    # Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном M
    def Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_M(self):
        self.driver.switch_to.window(self.vars[0])
        self.next_Branded_packaging()
        # Пакет с клапаном M
        self.wait(*Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_M).click()
        self.Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost()

    # Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном S
    def Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_S(self):
        self.driver.switch_to.window(self.vars[0])
        self.next_Branded_packaging()
        # Пакет с клапаном S
        self.wait(*Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_S).click()
        self.Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost()

    # Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном XL
    def Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_XL(self):
        self.driver.switch_to.window(self.vars[0])
        self.next_Branded_packaging()
        # Пакет с клапаном XL
        self.wait(*Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_XL).click()
        self.Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost()

    # Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном XS
    def Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_XS(self):
        self.driver.switch_to.window(self.vars[0])
        self.next_Branded_packaging()
        # Пакет с клапаном XS
        self.wait(*Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_XS).click()
        self.Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost()

    # Прием посылок - Далее - Фирменная упаковка - упаковка - Короб M
    def Receiving_parcels_Next_Branded_packaging_Packaging_Box_M(self):
        self.driver.switch_to.window(self.vars[0])
        self.next_Branded_packaging()
        # Короб M
        self.wait(*Receiving_parcels_Next_Branded_packaging_Packaging_Box_M).click()
        self.Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost()

