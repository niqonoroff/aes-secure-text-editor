from tkinter import *
import tkinter.font as tkFont
from .utils import editor_utils as exec
from .utils.common_utils import start_move, do_move
from src.calculator import open_calc

def create_window():
    # Создание главного окна приложения
    root = Tk()

    # Параметры окна
    root.title("NQ Editor")
    root.configure(bg="#1e1e1e")
    root.overrideredirect(True)
    # Центрирование окна
    window_width = 1430
    window_height = 740
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    pos_x = (screen_width // 2) - (window_width // 2)
    pos_y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")
    
    # Создание панели заголовка
    titlebar = Frame(root, bg="#111111", height=25)
    title = Label(titlebar, text="NQ Editor", bg="#111111", fg="white")

    # Основное текстовое поле редактора
    text = Text(
        root,
        bg="#1e1e1e",
        fg="#d4d4d4",
        padx=10,
        pady=10,
        insertbackground="white",
        wrap="word",
        undo=True,
        bd=0,
        highlightthickness=0
    )
    font_size = 14
    text_font = tkFont.Font(size=font_size)
    text.configure(font=text_font)
    text.focus()

    # Нижняя панель
    statusbar = Frame(root, bg="#111111", height=25)
    status_label_l = Label(
        statusbar,
        text="| Ctrl + O — Open | Ctrl + S — Save | Ctrl + Q — Close without saving | F1 — Full‑screen mode | F2 — System border | F3 — Calculator",
        bg="#111111",
        fg="#777777"
    )
    status_label_r = Label(
        statusbar,
        bg="#111111",
        fg="#777777"
    )
    exec.update_time(status_label_r, root)
    status_save_label = Label(
        statusbar,
        text="ᗜ",
        width=1,
        bg="#111111",
        fg="#777777"
    )

    # Размещение элементов
    titlebar.pack(fill="x")
    titlebar.pack_propagate(False)
    title.pack(side="left", padx=10)
    text.pack(fill="both", expand=True)
    text.pack_propagate(False)
    statusbar.pack(fill="x", side="bottom", before=text)
    statusbar.pack_propagate(False)
    status_save_label.pack(side="left", padx=(10, 5))
    status_label_l.pack(side="left")
    status_label_r.pack(side="right", padx=10)

    # Привязка событий
    titlebar.bind("<Button-1>", lambda e: start_move(e))
    titlebar.bind("<B1-Motion>", lambda e: do_move(e, root))
    title.bind("<Button-1>", lambda e: start_move(e))
    title.bind("<B1-Motion>", lambda e: do_move(e, root))
    text.bind("<Control-MouseWheel>", lambda e: exec.zoom(e, text_font))
    root.bind("<Control-KeyPress>", lambda e: exec.on_ctrl_key(e, title, text, status_save_label, root))
    text.bind("<<Modified>>", lambda e: exec.on_text_change(text, status_save_label, e))
    root.bind("<F1>", lambda e: exec.toggle_fullscreen(root, e))
    root.bind("<F2>", lambda e: exec.toggle_window_mode(root, e))
    root.bind("<F3>", lambda e: open_calc(root))

    return root, title, text