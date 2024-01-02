from selenium.webdriver.common.by import By
# адрес Ozon
url_Ozon = 'https://pvz.ozon-dostavka.ru/'
# Горячие клавиши для Озона
hotkey_Ozon = {
    # Выдача заказов
    'issuing_orders': 'alt + g',
    # закрывает активную карточку клиента ------------------
    'close_the_active_customer_card': 'ctrl + shift + g',
    # закрывает все карточки закаказов -------------------------
    'close_all_order_cards': 'ctrl + shift + g + f',

    # Прием отправлений
    'receiving_shipments': 'alt + v',
    # Прием отправлений - уберает галочку или ставит ее обратно
    'receiving_shipments_click': 'alt + c',
    # Прием отправлений - уберает галочку - ставит нужный нам номер
    'receiving_shipments_click_number': 'alt + shift + v + n',
    # Принимает все товары, которые есть в "Прием отправлений" -------------------------------------
    'Accept_all_products': 'ctrl + shift + y + u',

    # Отправка на склад - перевозки
    'sending_to_the_transportation_warehouse': 'alt + p',
    # Отправка на склад - перевозки - создает 2 перевозки для селлеров и для возвратов
    'shipping_to_the_warehouse_transportation': 'ctrl + shift + q + w',
    # Отправка на склад - коробки
    'boxesshipping_to_the_warehouse_of_the_box': 'alt + b',
    # Отправка на склад - тареые ящики----
    'shipping_to_the_warehouse': 'alt+ n',

    # Поиск отправлений
    'search_for_shipments': 'alt+ s',

}

# Выдача заказов
open_site_Ozon = (By.CLASS_NAME, 'menuGroup_TyWeY')

# Прием отправлений
receiving_shipments = (
    By.CSS_SELECTOR, '.menuGroup_TyWeY:nth-child(2) > .linkNuxt_nW8Ek:nth-child(2) > .dataCell_aI4s1')
# Прием отправлений - уберает галочку или ставит ее обратно
receiving_shipments_cancel = (By.CSS_SELECTOR, 'label.container_-FEFS')
# Прием отправлений - уберает галочку - ставит нужный нам номер
#Отсканируйте штрихкод ячейки или выберите номер вручную
receiving_shipments_cancel_number_1 = (By.ID, "baseInput___OEmaB")
# кликает на поиск
receiving_shipments_cancel_number_2 = (By.ID, "baseInput___twcBZ")
#выбераем номер
receiving_shipments_cancel_number_3 = (By.CSS_SELECTOR, ".dropdownItem_jiQ0c:nth-child(1)")
# Ставим номер
receiving_shipments_cancel_number_4 = (By.ID, "baseInput___twcBZ")


# Отправка на склад
shipping_to_the_warehouse = (
    By.CSS_SELECTOR, '.menuGroup_TyWeY:nth-child(2) > .linkNuxt_nW8Ek:nth-child(4) > .dataCell_aI4s1')
# Отправка на склад - тарные ящики
shipping_to_the_warehouse_trash = (
    By.CSS_SELECTOR, '.element_WxsuC:nth-child(3) .titleWrap_47n0s')
# Отправка на склад - перевозки
shipping_to_the_warehouse_transportation = (
    By.CSS_SELECTOR, 'div.element_WxsuC:nth-child(1)')
# Отправка на склад - коробки
boxesshipping_to_the_warehouse_of_the_box = (By.CSS_SELECTOR, '.element_WxsuC:nth-child(2) .titleWrap_47n0s')
# Отправка на склад - перевозки - создать перевозки (для возвратов)
shipping_to_the_warehouse_transportation_create_transportation = (
    By.CSS_SELECTOR, 'div.titleWrap_47n0s')
# Отправка на склад - перевозки - создать перевозки (для селлеров)
shipping_to_the_warehouse_transportation_create_transportation_sellers = (
    By.CSS_SELECTOR, 'div.titleWrap_47n0s')
# Отправка на склад - перевозки - создать перевозки - маршрут
shipping_to_the_warehouse_transportation_create_transportation_route = (
    By.CSS_SELECTOR, '.pointer_Tj\+JZ > .size-500_96uu5')
# Отправка на склад - перевозки - создать перевозки - маршрут - возвраты
shipping_to_the_warehouse_transportation_create_transportation_route_return = (
    By.CSS_SELECTOR, '.dropdownItem_jiQ0c:nth-child(1) .label_kE3Rx')
# Отправка на склад - перевозки - создать перевозки - маршрут - селлеры
shipping_to_the_warehouse_transportation_create_transportation_route_selleres = (
    By.CSS_SELECTOR, '.dropdownItem_jiQ0c:nth-child(2) .label_kE3Rx')
# Отправка на склад - перевозки - создать перевозки - маршрут - возвраты - создать
shipping_to_the_warehouse_transportation_create_transportation_route_return_create = (
    By.CSS_SELECTOR, '.controls_a3-Kt > .primary_FaJYp > .content_PcVb1')

# Поиск отправлений
search_for_shipments = (By.CSS_SELECTOR, '.menuGroup_TyWeY:nth-child(4) > .linkNuxt_nW8Ek:nth-child(2) .label_kE3Rx')
# Поиск отправлений - курсор на поиск
search_for_shipments_click = (By.CSS_SELECTOR, '.input_6j-46 > .size-500_96uu5')

