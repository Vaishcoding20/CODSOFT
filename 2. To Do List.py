import tkinter as tk
import tkinter.messagebox
from tkinter import *

root = Tk()
root.title("To Do List")
root.config(bg="pink")
root.geometry("500x500+950+150")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(pady=10)

task_box = tk.Listbox(frame, width=60,height=20,font=("Arial",10))
task_box.pack(side=tk.LEFT)

sb = tk.Scrollbar(frame)
sb.pack(side=tk.RIGHT, fill=tk.Y)

task_entry = tk.Entry(root, width=40,bd=2,font=("Arial", 10, 'bold'))
task_entry.pack(pady=10)

def addtask():
    task=task_entry.get()
    if task=="":
        alert("Please try to give some task")
    else:
        task_box.insert(tk.END, task)
        task_entry.delete(0, END)

def deletetask():
    try:
        selected_task_index = task_box.curselection()[0]
        task_box.delete(selected_task_index)
    except IndexError:
        alert("Please select a task to delete")

def alert(message):
    alert = tk.Toplevel()
    alert.title("warning")
    alert.geometry("300x150+600+300")

    message_label = tk.Label(alert, text=message, padx=20, pady=20)
    message_label.pack()

    ok_button = tk.Button(alert, text="Ok", command=alert.destroy, padx=20, pady=5)
    ok_button.pack()

    ok_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

add_button = Button(root, text="Add Task", command=addtask, font= ('Arial',15))
add_button.pack(pady=5)

delete_button = Button(root, text="Delete Task", command=deletetask, font= ('Arial',15))
delete_button.pack(pady=5)


if __name__=="__main__":
    print("Thanking you for visiting")
    mainloop()
    print("I hope your task is be easily accesible to you")

root.mainloop()