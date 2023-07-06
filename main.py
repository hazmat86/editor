try:
    import sys
    import tkinter as tk
except ImportError as err:
    print(f'Could not load module. {err}')
    sys.exit(2)

main = tk.Tk()
text = tk.Text(main)
text.grid()

main.mainloop()

