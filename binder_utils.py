import win32gui
import psutil
import win32con

def get_window_coordinates(window_handle):
    try:
        # Получаем координаты окна (левый, верхний, правый, нижний)
        left, top, right, bottom = win32gui.GetWindowRect(window_handle)
        return left, top, right, bottom
    except Exception as e:
        print(f"Ошибка при получении координат окна: {e}")
        return None
    

def get_process(process_name):
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and proc.info['name'].lower() == process_name.lower():
                return proc
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return None

def has_border(window_handle):
    try:
        style = win32gui.GetWindowLong(window_handle, win32con.GWL_STYLE)
        # Проверяем наличие стандартной рамки или заголовка
        if style & win32con.WS_BORDER or style & win32con.WS_CAPTION:
            return True
        return False
    except Exception as e:
        print(f"Ошибка при определении рамки окна: {e}")
        return False