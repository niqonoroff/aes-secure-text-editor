from tkinter import *
from .utils.common_utils import start_move, do_move
from .utils import password_utils as exec
from src.crypto import ARGON_TIME, ARGON_MEMORY, ARGON_PARALLELISM, SALT_SIZE, NONCE_SIZE

def create_window(root):
    # Создание окна
    pwin = Toplevel(root)

    # Параметры окна
    pwin.grab_set()
    pwin.focus_force()
    pwin.attributes("-topmost", True)
    pwin.title("NQ Editor")
    pwin.configure(bg="#1e1e1e")
    pwin.overrideredirect(True)
    # Центрирование
    window_width = 200
    window_height = 350
    screen_width = pwin.winfo_screenwidth()
    screen_height = pwin.winfo_screenheight()
    pos_x = (screen_width // 2) - (window_width // 2)
    pos_y = (screen_height // 2) - (window_height // 2)
    pwin.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

    # Создание панели заголовка
    titlebar = Frame(pwin, bg="#111111", height=30)
    title = Label(titlebar, text="Save Settings", bg="#111111", fg="white")
    titlebar.pack(fill="x")
    title.pack(side="left", padx=10)

    # Создание полей ввода
    Label(pwin, text="New password:", bg="#1e1e1e", fg="white").pack(pady=(4,0))
    entry1 = Entry(pwin, show="*", bg="#2b2b2b", fg="white", insertbackground="white", relief="flat")
    entry1.pack()
    Label(pwin, text="Confirm password:", bg="#1e1e1e", fg="white").pack(pady=(4,0))
    entry2 = Entry(pwin, show="*", bg="#2b2b2b", fg="white", insertbackground="white", relief="flat")
    entry2.pack()
    entry1.focus()
    Label(pwin, text="Argon time:", bg="#1e1e1e", fg="white").pack(pady=(4,0))
    e_time = Entry(pwin, bg="#2b2b2b", fg="white", relief="flat")
    e_time.insert(0, str(ARGON_TIME))
    e_time.pack()
    Label(pwin, text="Argon memory:", bg="#1e1e1e", fg="white").pack(pady=(4,0))
    e_mem = Entry(pwin, bg="#2b2b2b", fg="white", relief="flat")
    e_mem.insert(0, str(ARGON_MEMORY))
    e_mem.pack()
    Label(pwin, text="Argon parallelism:", bg="#1e1e1e", fg="white").pack(pady=(4,0))
    e_par = Entry(pwin, bg="#2b2b2b", fg="white", relief="flat")
    e_par.insert(0, str(ARGON_PARALLELISM))
    e_par.pack()
    Label(pwin, text="Salt size (bytes):", bg="#1e1e1e", fg="white").pack(pady=(4,0))
    e_salt = Entry(pwin, bg="#2b2b2b", fg="white", relief="flat")
    e_salt.insert(0, str(SALT_SIZE))
    e_salt.pack()
    Label(pwin, text="Nonce size (bytes):", bg="#1e1e1e", fg="white").pack(pady=(4,0))
    e_nonce = Entry(pwin, bg="#2b2b2b", fg="white", relief="flat")
    e_nonce.insert(0, str(NONCE_SIZE))
    e_nonce.pack()

    # Привязка событий
    titlebar.bind("<Button-1>", lambda e: start_move(e))
    titlebar.bind("<B1-Motion>", lambda e: do_move(e, pwin))
    title.bind("<Button-1>", lambda e: start_move(e))
    title.bind("<B1-Motion>", lambda e: do_move(e, pwin))
    pwin.bind("<Return>", lambda e: exec.submit(pwin, entry1, entry2, e_time, e_mem, e_par, e_salt, e_nonce))

    # Блокировка внешнего вызова пока не разрушится окно
    pwin.wait_window()

    return exec.result
