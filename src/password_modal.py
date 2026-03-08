from tkinter import *
from .utils import password_utils as exec
from .utils.common_utils import start_move, do_move

def create_window(root):
    # Создание окна ввода пароля
    pwin = Toplevel(root)

    # Параметры окна
    pwin.grab_set()
    pwin.focus_force()
    pwin.attributes("-topmost", True)
    pwin.title("NQ Editor")
    pwin.configure(bg="#1e1e1e")
    pwin.overrideredirect(True)
    # Центрирование окна
    window_width = 200
    window_height = 100
    screen_width = pwin.winfo_screenwidth()
    screen_height = pwin.winfo_screenheight()
    pos_x = (screen_width // 2) - (window_width // 2)
    pos_y = (screen_height // 2) - (window_height // 2)
    pwin.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")
    
    # Создание панели заголовка
    titlebar = Frame(pwin, bg="#111111", height=30)
    title = Label(titlebar, text="NQ Editor", bg="#111111", fg="white")

    # Размещение элементов
    titlebar.pack(fill="x")
    title.pack(side="left", padx=10)
    Label(pwin, text="Enter password:", bg="#1e1e1e", fg="White").pack(pady=10)
    entry = Entry(pwin, show="*")
    entry.pack()

    # Привязка событий
    titlebar.bind("<Button-1>", lambda e: start_move(e))
    titlebar.bind("<B1-Motion>", lambda e: do_move(e, pwin))
    title.bind("<Button-1>", lambda e: start_move(e))
    title.bind("<B1-Motion>", lambda e: do_move(e, pwin))
    pwin.bind("<Return>", lambda e: exec.get_password(entry, pwin))

    # Блокировка внешнего вызова пока не разрушится окно
    pwin.wait_window()

    return exec.password