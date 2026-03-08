from tkinter import *
from .utils.common_utils import start_move, do_move

def open_calc(root):
    # Создание окна калькулятора
    calc = Toplevel(root)

    # Параметры окна
    calc.focus_force()
    calc.attributes("-topmost", True)
    calc.overrideredirect(True)
    calc.configure(bg="#1e1e1e")
    # Центрирование окна
    w, h = 260, 360
    sw, sh = calc.winfo_screenwidth(), calc.winfo_screenheight()
    x = (sw // 2) - (w // 2)
    y = (sh // 2) - (h // 2)
    calc.geometry(f"{w}x{h}+{x}+{y}")

    # Создание панели заголовка
    titlebar = Frame(calc, bg="#111111", height=30)
    title = Label(titlebar, text="Calculator", bg="#111111", fg="white")

    # Создание поля ввода
    entry = Entry(
        calc,
        font=("", 20),
        justify="right",
        bg="#2b2b2b",
        fg="white",
        insertbackground="white",
        relief="flat"
    )
    entry.focus()

    # Создание сетки для кнопок
    grid = Frame(calc, bg="#1e1e1e")

    # Размещение элементов
    titlebar.pack(fill="x")
    title.pack(side="left", padx=10)
    entry.pack(fill="x", padx=10, pady=10)
    grid.pack(expand=True, fill="both", padx=10, pady=5)

    # Привязка событий
    titlebar.bind("<Button-1>", lambda e: start_move(e))
    titlebar.bind("<B1-Motion>", lambda e: do_move(e, calc))
    title.bind("<Button-1>", lambda e: start_move(e))
    title.bind("<B1-Motion>", lambda e: do_move(e, calc))
    calc.bind("<F3>", lambda e: calc.destroy())
    calc.bind("<Escape>", lambda e: calc.destroy())

    # Логика
    def add(symbol):
        entry.insert(END, symbol)

    def backspace():
        text = entry.get()
        entry.delete(0, END)
        entry.insert(0, text[:-1])

    def clear():
        entry.delete(0, END)

    def calculate():
        expression = entry.get().replace("%", "/100")
        try:
            result = eval(expression, {"__builtins__": None}, {})
            entry.delete(0, END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, END)
            entry.insert(0, "Error")

    # Расположение кнопок на сетке
    btns = [
        ("(", 1, 0), (")", 1, 1), ("%", 1, 2), ("←", 1, 3),
        ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
        ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
        ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
        ("0", 5, 0), (".", 5, 1), ("C", 5, 2), ("+", 5, 3),
        ("=", 6, 0, 4)
    ]

    for btn in btns:
        text = btn[0]
        r = btn[1]
        c = btn[2]
        cs = btn[3] if len(btn) == 4 else 1

        match text:
            case "C":
                cmd = clear
            case "←":
                cmd = backspace
            case "=":
                cmd = calculate
            case _:
                cmd = lambda t=text: add(t)

        b = Button(
            grid,
            font=("", 14),
            text=text,
            command=cmd,
            bg="#2b2b2b",
            fg="white",
            activebackground="#3c3c3c",
            relief="flat"
        )
        b.grid(row=r, column=c, columnspan=cs, sticky="nsew", padx=3, pady=3)

    # Занятие свободного пространства в окне
    for i in range(4):
        grid.grid_columnconfigure(i, weight=1)
    for i in range(1, 7):
        grid.grid_rowconfigure(i, weight=1)
