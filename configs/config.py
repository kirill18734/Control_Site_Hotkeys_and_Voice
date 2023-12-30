import os

# Определение относительного пути от папки AppData
user_data_dir = os.path.join(os.getenv('APPDATA'), 'Local', 'Google', 'Chrome', 'User Data')

# Использование переменной user_data_dir в вашем коде
# Например:
# chrome_options.add_argument(f"user-data-dir={user_data_dir}")

# Постоянная директория сохранненной ссесиии в браузере Chrome
# user_data_dir = r"C:\Users\kiraf\AppData\Local\Google\Chrome\User Data"

hotkeys_for_programm = {
    # Прекращает выполнение программы
    'exit': 'alt + q'
}

remote_debugging_port = 9999

discriptor_windows = []
discriptor_windows_2 = []

