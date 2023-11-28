from selenium.webdriver.common.by import By

# адрес Boxberry
url_Boxberry = 'https://spvz.boxberry.de/'

# Логин и пароль от аккаунта Boxberry для Кирилла
login_boxberry_Kirill = 'u57474'
password_boxberry_Kirill = 'P7onIo8M3v'

# На балансе
on_balance = (By.ID, "employee-e-parcel-index")
on_balance_text = (By.ID, "parcelsearch-search_str")

# Прием посылок

receiving_parcels = (By.ID, "employee-e-letters-and-parcels-sender-choice")
receiving_parcels_text = (By.ID, "expressInvoice")

# Горячие клавиши для Boxberry
hotkey_Boxberry = {
    # На балансе
    'on_balance_': 'alt + b',

    # Прием посылок
    'receiving_parcels': 'alt + p',
    # Прекращает выполнение программы
    'exit': 'alt + q'
}
