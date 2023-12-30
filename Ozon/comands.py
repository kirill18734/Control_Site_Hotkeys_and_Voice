from selenium.webdriver import ActionChains

from configs.base_sitings_run_driver import *


class Ozon:

    def __init__(self):
        self.driver = Top_driver().driver
        self.vars = self.driver.window_handles
        discriptor_windows.append(self.vars)

    # Ожидание
    def wait(self, By, value):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((By, value)))

    def close_driver(self):
        self.driver.close()
        self.driver.quit()

    # открывает сайт Озон
    def open_site_Ozon(self):
        self.driver.switch_to.window(self.vars[0])
        self.driver.get(url_Ozon)
        # self.wait(*open_site_Ozon).click()

    # "Выдача заказов"

    def issuing_orders(self):
        self.driver.switch_to.window(self.vars[0])
        self.wait(*open_site_Ozon).click()

        # "Прием отправлений "

    def receiving_shipments(self):
        self.driver.switch_to.window(self.vars[0])
        self.wait(*receiving_shipments).click()

        # Прием отправлений - ставит или убирает галочку

    def receiving_shipments_click(self):
        self.driver.switch_to.window(self.vars[0])
        # Прием отправлений - уберает галочку
        self.wait(*receiving_shipments_cancel).click()

    # Прием отправлений - ставит номер
    def receiving_shipments_click_number(self):
        self.driver.switch_to.window(self.vars[0])
        # Прием отправлений - уберает галочку
        self.wait(*receiving_shipments_cancel).click()
        # Прием отправлений - кликает на кнопку с номером
        self.wait(*receiving_shipments_cancel_number_1).click()
        # Прием отправлений - кликает на поиск
        self.wait(*receiving_shipments_cancel_number_2).click()
        # Прием отправлений - выбирает номер
        self.wait(*receiving_shipments_cancel_number_3).click()
        # Прием отправлений - кликает на кнопку с номером
        self.wait(*receiving_shipments_cancel_number_4)

        # "Отправка на склад" - тарные ящики

    def shipping_to_the_warehouse(self):
        self.driver.switch_to.window(self.vars[0])
        self.wait(*shipping_to_the_warehouse).click()
        element_to_double_click = self.wait(*shipping_to_the_warehouse_trash)
        ActionChains(self.driver).double_click(element_to_double_click).perform()

        # Отправка на склад - создание 2 перевозок для возвратов и для селлеров

    def shipping_to_the_warehouse_transportation(self):
        self.driver.switch_to.window(self.vars[0])
        # Отправка на склад
        self.wait(*shipping_to_the_warehouse).click()

        # Отправка на склад - перевозки
        element_to_double_click = self.wait(*shipping_to_the_warehouse_transportation)
        ActionChains(self.driver).double_click(element_to_double_click).perform()

        # Отправка на склад - перевозки - новая перевозка
        element_to_double_click = self.wait(*shipping_to_the_warehouse_transportation_create_transportation)
        ActionChains(self.driver).double_click(element_to_double_click).perform()

        # Отправка на склад - перевозки - новая перевозка - маршрут
        self.wait(*shipping_to_the_warehouse_transportation_create_transportation_route).click()

        # Отправка на склад - перевозки - новая перевозка - маршрут - возвраты
        self.wait(*shipping_to_the_warehouse_transportation_create_transportation_route_return).click()

        # Отправка на склад - перевозки - новая перевозка - маршрут - возвраты - создать
        self.wait(*shipping_to_the_warehouse_transportation_create_transportation_route_return_create).click()
        # Отправка на склад - перевозки - новая перевозка
        sleep(1)
        element_to_double_click_2 = self.wait(
            *shipping_to_the_warehouse_transportation_create_transportation_sellers)
        ActionChains(self.driver).double_click(element_to_double_click_2).perform()

        # Отправка на склад - перевозки - новая перевозка - маршрут
        self.wait(*shipping_to_the_warehouse_transportation_create_transportation_route).click()

        # Отправка на склад - перевозки - новая перевозка - маршрут - селлер
        self.wait(*shipping_to_the_warehouse_transportation_create_transportation_route_selleres).click()

        # Отправка на склад - перевозки - новая перевозка - маршрут - селлер - создать
        self.wait(*shipping_to_the_warehouse_transportation_create_transportation_route_return_create).click()

        # "Поиск отправлений"

    def search_for_shipments(self):
        self.driver.switch_to.window(self.vars[0])
        self.wait(*search_for_shipments).click()
        self.wait(*search_for_shipments_click).click()
