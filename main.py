try:
    import sys
    import tkinter as tk
    import tk.tkFileDialog
except ImportError as err:
    print(f'Could not load module. {err}')
    sys.exit(2)

main = tk.Tk()
text = tk.Text(main)
text.grid()

def save_as():
    global text
    t = text.get("1.0", "end-1c")
    save_location = tk.tkFileDialog.asksaveasfilename()
    file1 = open(save_location, "w+")
    file1.write(t)
    files1.close()
button = Button(root, text="Save", command=saveas)
button.grid()

main.mainloop()

