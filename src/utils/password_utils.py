from tkinter import END

result = None

# Выброс данных для открытия файла
def get_data(entry, e_time, e_mem, e_par, e_salt, e_nonce, root):
    global result
    result = {
        "password": entry.get(),
        "argon_time": e_time.get(),
        "argon_memory": e_mem.get(),
        "argon_parallel": e_par.get(),
        "salt": e_salt.get(),
        "nonce": e_nonce.get()
    }
    root.destroy()

# Выброс данных для сохранения файла
def submit(pwin, entry1, entry2, e_time, e_mem, e_par, e_salt, e_nonce):
    global result
    p1 = entry1.get()
    p2 = entry2.get()
    if not p1 or p1 != p2:
        entry2.delete(0, END)
        entry2.config(bg="#552222")
        entry2.after(200, lambda: entry2.config(bg="#2b2b2b"))
        return
    result = {
        "password": p1,
        "argon_time": e_time.get(),
        "argon_memory": e_mem.get(),
        "argon_parallel": e_par.get(),
        "salt": e_salt.get(),
        "nonce": e_nonce.get()
    }
    pwin.destroy()