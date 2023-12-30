from Boxberry.comands import *
from Ozon.comands import *
# Это
while True:
    action = check_hotkeys()
    # OZON
    # Открывает браузер и входит на сайт Озон
    # try:
    if action == 'open_site_Ozon':
        app = Ozon()
        app.open_site_Ozon()
        app_b = Boxberry()
        app_b.open_site_boxberry_Kirill()
    # Выдача заказов
    elif action == 'issuing_orders':
        app.issuing_orders()

    # Прием отправлений
    elif action == 'receiving_shipments':
        app.receiving_shipments()
    # Прием отправлений - уберает галочку или ставит ее обратно
    elif action == 'receiving_shipments_click':
        app.receiving_shipments_click()
    #Прием отправклений - ставит номер в приеме отправлений
    elif action == 'receiving_shipments_click_number':
        app.receiving_shipments_click_number()

    # Отправка на склад - тарные ящики
    elif action == 'shipping_to_the_warehouse':
        app.shipping_to_the_warehouse()
    # Отправка на склад - перевозки - создает 2 перевозки для селлеров и для возвратов
    elif action == 'shipping_to_the_warehouse_transportation':
        app.shipping_to_the_warehouse_transportation()

    # Поиск отправлений
    elif action == 'search_for_shipments':
        app.search_for_shipments()

    # BOXBERRY

    # На балансе
    elif action == 'on_balance_':
        app_b.on_balance_()

    # Прием посылок
    elif action == 'receiving_parcels':
        app_b.receiving_parcels()

    elif action == 'exit':
        app.close_driver()
        break
    # except:
    #     continue