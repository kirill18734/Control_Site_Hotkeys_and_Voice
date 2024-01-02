# Постоянная директория сохранненной ссесиии в браузере Chrome
# user_data_dir = r"C:\Users\kiraf\AppData\Local\Google\Chrome\User Data"
import os

# Определение относительного пути от папки AppData для сохранения пользовательских данных в Chrome
user_data_dir = os.path.join(os.getenv('APPDATA'), 'Local', 'Google', 'Chrome', 'User Data')
hotkeys_for_programm = {
    # Прекращает выполнение программы
    'exit': 'alt + q',
    # открывает сайт boxberry и Озон (2 отдельных окна)
    'open_site_Ozon': 'ctrl + shift + o + i',
}

remote_debugging_port = 9999

discriptor_windows = []
discriptor_windows_2 = []

