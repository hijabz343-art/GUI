import tkinter as tk
window=tk.Tk()
label = tk.Label(window, text= "HELLOW HIJAB!", fg="black", bg="pink", padx=10,pady=5)
label.pack()

button = tk.Button(window, text="Click Me", width=15, command=lambda:
print("Button clicked!"))
button.pack(padx=0,pady=20)

window.mainloop()

import tkinter as tk
window = tk.Tk()
label = tk.Label(window, text="Initial Text")
label.pack()
current_text = label.cget("text") # Using cget()
print(f"Current text: {current_text}")
current_bg = label.config()["bg"][-1] # Using config() and dictionary access
print(f"Current background: {current_bg}")
window.mainloop()


import tkinter as tk
def change_colour():
    current_colour=window.cget("bg")
    if current_colour=="red":
        window.config(bg="green")
        button.config(bg="green")
    else:
        window.config(bg="red")
        button.config(bg="red")
window=tk.Tk()
window.title("color toggle button")
button=tk.Button(window,text="CLICK HERE",bg="red", command=change_colour)
button.pack(pady=20)
window.mainloop()




