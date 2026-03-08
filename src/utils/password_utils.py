# Выброс пароля
password = ""
def get_password(entry, root):
    global password
    password = entry.get()
    root.destroy()