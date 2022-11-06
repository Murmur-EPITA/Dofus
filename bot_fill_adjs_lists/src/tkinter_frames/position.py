import tkinter as tk


def ask_pos():
    '''
    Open a tkinter_frames dialog to ask for current position.
    :return: int, int
    '''
    def handle_focus(event):
        if event.widget == root:
            root.focus_set()
            entry_x.focus_set()

    def get_pos():
        global x, y
        x = int(entry_x.get())
        y = int(entry_y.get())
        root.destroy()

    msg = "Player's position"
    root = tk.Tk()
    root.title(msg)

    frame = tk.Frame(root)
    frame.winfo_toplevel().geometry("300x100")
    frame.pack()

    entry_x = tk.Entry(frame, width=40)
    entry_x.insert(tk.INSERT, "X position")
    entry_x.pack(ipadx=30)

    entry_y = tk.Entry(frame, width=40)
    entry_y.insert(tk.INSERT, "Y position")
    entry_y.pack(ipadx=30, ipady=10)

    B1 = tk.Button(frame, text="Ok", command=get_pos)
    B1.pack()

    root.lift()
    root.attributes("-topmost", True)

    root.bind("<FocusIn>", handle_focus)

    print("Position window has spawned.")
    tk.mainloop()
    return int(x), int(y)
