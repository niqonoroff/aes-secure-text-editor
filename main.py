from src.editor_window import create_window
from src.utils.editor_utils import open_file
import sys

def main():
    root, title, text = create_window()

    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        open_file(title, text, root, filepath)

    root.mainloop()

if __name__ == "__main__":
    main()