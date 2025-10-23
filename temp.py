import tkinter as tk

root = tk.Tk()
root.title("Label Text Positioning")

# Label with text anchored to the top-left
label1 = tk.Label(root, text="Top-Left Anchored Text", anchor="nw", bg="lightblue")
label1.pack(pady=10, padx=10, fill="x")

# Label with multi-line text justified to the right
label2 = tk.Label(root, text="This is the first line.\nThis is the second line.",
                  justify="right", bg="lightgreen")
label2.pack(pady=10, padx=10, fill="x")

# Label with text centered within the label
label3 = tk.Label(root, text="Centered Text", anchor="center", bg="lightcoral")
label3.pack(pady=10, padx=10, fill="x")

root.mainloop()