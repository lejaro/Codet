import win32gui

def is_window_open(coding_app):
    found = []
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd) and not win32gui.IsIconic(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if coding_app and coding_app.lower() in title.lower():
                found.append(True)
    win32gui.EnumWindows(callback, None)
    return bool(found)

