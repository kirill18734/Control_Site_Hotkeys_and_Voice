from selenium.webdriver.common.by import By

# адрес Boxberry
url_Boxberry = 'https://spvz.boxberry.de/'

# Логин и пароль от аккаунта Boxberry для Кирилла
login_boxberry_Kirill = 'u57474'
password_boxberry_Kirill = 'P7onIo8M3v'

# Горячие клавиши для Boxberry
hotkey_Boxberry = {
    # На балансе
    'on_balance_': 'ctrl + shift + b',
    # Прием посылок
    'receiving_parcels': 'ctrl + y',
    'Acceptance_of_parcels_Further_Branded_packaging_packaging_A4_envelope_for_documents': 'alt + 2',  # Конверт А4 для документов
    'Receiving_parcels_Next_Branded_packaging_Packaging_Box_L': 'alt + 3',  # Короб L
    'Receiving_parcels_Next_Branded_packaging_Packaging_Box_S': 'alt + 4',  # Короб S
    'Receiving_parcels_Next_Branded_packaging_Packaging_Box_TL': 'alt + 5',  # Короб TL
    'Receiving_parcels_Next_Branded_packaging_Packaging_Box_XL': 'alt + 6',  # Короб XL
    'Receiving_parcels_Next_Branded_packaging_Packaging_Box_XS': 'alt + 7',  # Короб XS
    'Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_L': 'alt + 8',  # Пакет с клапаном L
    'Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_M': 'alt + 9',  # Пакет с клапаном M
    'Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_S': 'alt + q',  # Пакет с клапаном S
    'Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_XL': 'alt + w',  # Пакет с клапаном XL
    'Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_XS': 'alt + r',  # Пакет с клапаном XS
    'Receiving_parcels_Next_Branded_packaging_Packaging_Box_M': 'alt + t',  # Короб M

}

# На балансе
on_balance = (By.ID, "employee-e-parcel-index")
on_balance_text = (By.ID, "parcelsearch-search_str")

# Прием посылок
receiving_parcels = (By.ID, "employee-e-letters-and-parcels-sender-choice")
# Ставит курсор на поиске
receiving_parcels_text = (By.ID, "expressInvoice")

# Прием посылок - Далее
receiving_parcels_next = (By.CSS_SELECTOR, 'button.btn-block')

# Прием посылок - Далее - Фирменная упавовка
acceptance_of_parcels_further_branded_packaging = (By.CSS_SELECTOR, 'a#package-paid-tab')

# Прием посылок - Далее - Фирменная упаковка - упаковка
Acceptance_of_mailingsdall_firm_package_packing = (By.CSS_SELECTOR, 'select#packages-paid-dropdown')

# Прием посылок - Далее - Фирменная упаковка - упаковка - Конверт А4 для документов
Acceptance_of_parcels_Further_Branded_packaging_packaging_A4_envelope_for_documents = (By.CSS_SELECTOR, '#packages-paid-dropdown > option:nth-child(2)')
# Прием посылок - Далее - Фирменная упаковка - упаковка - Короб L
Receiving_parcels_Next_Branded_packaging_Packaging_Box_L = (By.CSS_SELECTOR, '#packages-paid-dropdown > option:nth-child(3)')
# Прием посылок - Далее - Фирменная упаковка - упаковка - Короб S
Receiving_parcels_Next_Branded_packaging_Packaging_Box_S= (By.CSS_SELECTOR, '#packages-paid-dropdown > option:nth-child(4)')
# Прием посылок - Далее - Фирменная упаковка - упаковка - Короб TL
Receiving_parcels_Next_Branded_packaging_Packaging_Box_TL= (By.CSS_SELECTOR, '#packages-paid-dropdown > option:nth-child(5)')
# Прием посылок - Далее - Фирменная упаковка - упаковка - Короб XL
Receiving_parcels_Next_Branded_packaging_Packaging_Box_XL= (By.CSS_SELECTOR, '#packages-paid-dropdown > option:nth-child(6)')
# Прием посылок - Далее - Фирменная упаковка - упаковка - Короб ХS
Receiving_parcels_Next_Branded_packaging_Packaging_Box_XS= (By.CSS_SELECTOR, '#packages-paid-dropdown > option:nth-child(7)')
# Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном L
Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_L= (By.CSS_SELECTOR, '#packages-paid-dropdown > option:nth-child(8)')
# Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном M
Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_M= (By.CSS_SELECTOR, '#packages-paid-dropdown > option:nth-child(9)')
# Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном S
Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_S= (By.CSS_SELECTOR, '#packages-paid-dropdown > option:nth-child(10)')
# Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном XL
Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_XL= (By.CSS_SELECTOR, '#packages-paid-dropdown > option:nth-child(11)')
# Прием посылок - Далее - Фирменная упаковка - упаковка - Пакет с клапаном XS
Receiving_parcels_Next_Branded_packaging_Packaging_Envelope_XS= (By.CSS_SELECTOR, '#packages-paid-dropdown > option:nth-child(12)')
# Прием посылок - Далее - Фирменная упаковка - упаковка - Короб M
Receiving_parcels_Next_Branded_packaging_Packaging_Box_M= (By.CSS_SELECTOR, '#packages-paid-dropdown > option:nth-child(13)')
# Прием посылок - Далее - Фирменная упаковка - тип вложения
Receiving_parcels_Next_Type_of_enclosure = (By.CSS_SELECTOR, '#attachments-dropdown')
# Прием посылок - Далее - Фирменная упаковка - тип вложения - Товары народного потребления (без техники, единичное количество)
Receiving_parcels_Next_Type_of_enclosure_Consumer_goods = (By.CSS_SELECTOR, '#attachments-dropdown > option:nth-child(2)')
# Прием посылок - Далее - Фирменная упаковка - Вложение соответствует описанию
Receiving_parcels_Next_Branded_packaging_Enclosure_matches_description = (By.CSS_SELECTOR, '#attachments-accept-btn')
# Прием посылок - Далее - Фирменная упаковка - Рассчитать стоимость отправления
Receiving_parcels_Next_Branded_packaging_Calculate_shipping_cost  = (By.CSS_SELECTOR, '#calculate-btn')
