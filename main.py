from Boxberry.comands import Boxberry,check_hotkeys
from Ozon.comands import Ozon
app = None
app_b = None

while True:
    action = check_hotkeys()
    # OZON
    # Открывает браузер и входит на сайт Озон и Boxberry
    try:
        if action == 'open_site_Ozon_and_boxberry':
            app = Ozon()
            app.open_site_Ozon()
            app_b = Boxberry()
            app_b.open_site_boxberry_Kirill()
        # Выдача заказовI
        elif action == 'issuing_orders':
            app.issuing_orders()
        # закрывает активную карточку клиента ------------------
        elif action == 'close_the_active_customer_card':
            pass
        # закрывает все карточки закаказов -------------------------
        elif action == 'close_all_order_cards':
            pass

        # Прием отправлений
        elif action == 'receiving_shipments':
            app.receiving_shipments()
        # Прием отправлений - уберает галочку или ставит ее обратно
        elif action == 'receiving_shipments_click':
            app.receiving_shipments_click()
        #Прием отправклений - ставит номер в приеме отправлений
        elif action == 'receiving_shipments_click_number':
            app.receiving_shipments_click_number()

        # Отправка на склад - перевозки
        elif action == 'sending_to_the_transportation_warehouse':
            app.sending_to_the_transportation_warehouse()
        # Отправка на склад - перевозки - создает 2 перевозки для селлеров и для возвратов
        elif action == 'shipping_to_the_warehouse_transportation':
            app.shipping_to_the_warehouse_transportation()
        # Отправка на склад - коробки
        elif action == 'boxesshipping_to_the_warehouse_of_the_box':
            app.boxes()
        # Отправка на склад - тарные ящики
        elif action == 'shipping_to_the_warehouse':
            app.shipping_to_the_warehouse()

        # Поиск отправлений
        elif action == 'search_for_shipments':
            app.search_for_shipments()

        # BOXBERRY
        # На балансе
        elif action == 'on_balance_':
            app_b.on_balance_()
            continue

        # Прием посылок
        elif action == 'receiving_parcels':
            app_b.receiving_parcels()
            continue
        elif action == 'Acceptance_of_parcels_Further_Branded_packaging_packaging_A4_envelope_for_documents':
            # Прием посылок - Далее - Фирменная упаковка - упаковка - Конверт А4 для документов
            app_b.Acceptance_of_parcels_Further_Branded_packaging_packaging_A4_envelope_for_documents()
            continue
        elif action == 'Receiving_parcels_Next_Branded_packaging_Packaging_Box_L':
            # Прием посылок - Далее - Фирменная упаковка - упаковка - Короб L
            app_b.Receiving_parcels_Next_Branded_packaging_Packaging_Box_L()
            continue
        elif action == 'Receiving_parcels_Next_Branded_packaging_Packaging_Box_S':
            # Прием посылок - Далее - Фирменная упаковка - упаковка - Короб S
            app_b.Receiving_parcels_Next_Branded_packaging_Packaging_Box_S()
        elif action == 'Receiving_parcels_Next_Branded_packaging_Packaging_Box_TL':
            # Прием посылок - Далее - Фирменная упаковка - упаковка - Короб TL
            app_b.Receiving_parcels_Next_Branded_packaging_Packaging_Box_TL()
        elif action == 'Receiving_parcels_Next_Branded_packaging_Packaging_Box_XL':
            # Прием посылок - Далее - Фирменная упаковка - упаковка - Короб XL
            app_b.Receiving_parcels_Next_Branded_packaging_Packaging_Box_XL()
        elif action == 'Receiving_parcels_Next_Branded_packaging_Packaging_Box_XS':
            # Прием посылок - Далее - Фирменная упаковка - упаковка - Короб XS
            app_b.Receiving_parcels_Next_Branded_packaging_Packaging_Box_XS()
        elif action == 'Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_L':
            # Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном L
            app_b.Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_L()
        elif action == 'Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_M':
            # Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном M
            app_b.Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_M()
        elif action == 'Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_S':
            # Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном S
            app_b.Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_S()
        elif action == 'Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_XL':
            # Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном XL
            app_b.Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_XL()
        elif action == 'Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_XS':
            # Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапан
            app_b.Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_XS()
        elif action == 'Receiving_parcels_Next_Branded_packaging_Packaging_Box_M':
            # Прием посылок - Далее - Фирменная упаковка - упаковка - Короб M
            app_b.Receiving_parcels_Next_Branded_packaging_Packaging_Box_M()
        elif action == 'exit':
            app.close_driver()
            break
    except:
        continue