import subprocess as sp
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox

def retreive_url():
    url = url_entry.get()
    return url

def do_command(command):
    global command_textbox, url_val

    # If url_entry is blank, use localhost IP address 
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    with sp.Popen(command + ' ' + url_val, stdout = sp.PIPE, bufsize = 1, universal_newlines = True) as p:
        for line in p.stdout:
            command_textbox.insert(tk.END,line)
            command_textbox.update()

def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def Submit(): 
    global url_val
    res = messagebox.askquestion("POP UP BOX",
        "Are you sure that's the right url?")
    if res == "yes":
        url_val = url_entry.get()
        make_new_frame()
        
def make_new_frame():
    global frame1, root1, command_textbox
    frame.destroy()
    root.destroy()
    root1 = tk.Tk()
    frame1 = tk.Frame(root1)
    frame1.pack()
    command_textbox = tksc.ScrolledText(frame1, height=10, width=100)
    command_textbox.pack()
    ping_btn = tk.Button(frame1, text = "Ping", 
    command = lambda:do_command("ping"),
    compound = "center",
    font = ("comic sans", 12),
    bd = 5, 
    relief = "flat",
    cursor = "gumby",
    bg = "white", activebackground = "gray")
    ping_btn.pack()
# set up button to run the do_command function
# CODE TO ADD
# Makes the command button pass it's name to a function using lambda
# CODE TO ADD
# Modifies the ping button parameters.
submit_btn = tk.Button(frame, text="Check to see if a URL is up and active", 
    command = lambda:Submit(),
    compound = "center",
    font = ("comic sans", 12),
    bd = 5, 
    relief = "flat",
    cursor = "gumby",
    bg = "white", activebackground = "gray")
submit_btn.pack() 

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady = 10,  bg = "white") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound = "center",
    font = ("comic sans", 14),
    bd = 5, 
    relief = tk.FLAT, 
    cursor = "gumby",
    fg = "black",
    bg = "white")
url_label.pack(side = tk.LEFT)
url_entry = tk.Entry(frame_URL,  font = ("comic sans", 14), bd = 5) # change font
url_entry.pack(side = tk.LEFT)

frame = tk.Frame(root,  bg= " black") # change frame color
frame.pack()

# Adds an output box to GUI.

root.mainloop()
