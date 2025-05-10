import subprocess

# Путь к исполняемому файлу
exe_path = r"C:\Users\user\AppData\Local\Programs\LM Studio\LM Studio.exe"

# Запуск приложения без окна
subprocess.Popen([exe_path], creationflags=subprocess.CREATE_NO_WINDOW)
