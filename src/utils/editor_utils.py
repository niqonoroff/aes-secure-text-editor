from tkinter import filedialog
from tkinter import END
from src.password_modal import create_window
from src.new_password_modal import create_window as cw_new_password
from src.crypto import encrypt_text, dectypt_text
import time

# Развернуть окно во весь экран
def toggle_fullscreen(root, event=None):
    if root.attributes("-fullscreen"):
        root.attributes("-fullscreen", False)
        root.overrideredirect(True)
    else:
        root.overrideredirect(False)
        root.attributes("-fullscreen", True)
        
# Включение системной рамки
def toggle_window_mode(root, event=None):
    root.overrideredirect(not root.overrideredirect())

# Логика масштабирования текста
def zoom(event, text_font):
    size = text_font['size']
    size += 1 if event.delta > 0 else -1
    size = max(6, min(60, size))
    text_font.configure(size=size)

# Ctrl обработчик
def on_ctrl_key(event, title, text, status_save_label, root):
    match event.keycode:
        case 83:
            save_file(title, text, root)
            status_save_label.config(text="ᗜ")
        case 79:
            open_file(title, text, root)
        case 81:
            close_app(root)

# Смена статуса сохранения файла
def on_text_change(text, status_save_label, event=None):
    if text.edit_modified():
        status_save_label.config(text="●")
        text.edit_modified(False)

# Работа с файлом
current_file = None # Путь

def open_file(title, text, root, path="", event=None):
    global current_file
    if path:
        filepath = path
    else:
        filepath = filedialog.askopenfilename(
            filetypes=[("TXT Encrypted", "*.nqtxt"), ("All files", "*.*")]
        )
        if not filepath:
            return

    with open(filepath, "rb") as f:
        content = f.read()

    data = create_window(root)
    if not data:
        return
    try:
        decrypted_text = dectypt_text(
            content,
            data["password"],
            int(data["argon_time"]),
            int(data["argon_memory"]),
            int(data["argon_parallel"]),
            int(data["salt"]),
            int(data["nonce"])
        )
    except:
        text.delete("1.0", END)
        text.insert("1.0", "Invalid password | Invalid file format | Corrupted file")
        return

    text.delete("1.0", END)
    text.insert("1.0", decrypted_text)
    current_file = filepath
    title.config(text=current_file)

def save_file(title, text, root, event=None):
    global current_file
    if current_file is None:
        filepath = filedialog.asksaveasfilename(
            defaultextension=".nqtxt",
            filetypes=[("TXT Encrypted", "*.nqtxt"), ("All files", "*.*")]
        )
        if not filepath:
            return
        current_file = filepath

    data = cw_new_password(root)
    if not data:
        return

    encrypted_text = encrypt_text(
        text.get("1.0", END),
        data["password"],
        int(data["argon_time"]),
        int(data["argon_memory"]),
        int(data["argon_parallel"]),
        int(data["salt"]),
        int(data["nonce"])
    )

    with open(current_file, "wb") as f:
        f.write(encrypted_text)

    title.config(text=current_file)

# Отображение времени и текущей версии приложения
def update_time(status_label_r, root):
    now = time.strftime("%H:%M:%S")
    status_label_r.config(text=f"{now} | V1.1.0")
    root.after(1000, update_time, status_label_r, root)

# Закрытие окна
def close_app(root, event=None):
    root.destroy()