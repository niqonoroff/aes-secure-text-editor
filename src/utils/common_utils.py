# Логика перемещения окна
offset_x = 0
offset_y = 0
def start_move(event):
    global offset_x, offset_y
    offset_x = event.x
    offset_y = event.y
def do_move(event, root):
    root.geometry(f"+{event.x_root - offset_x}+{event.y_root - offset_y}")