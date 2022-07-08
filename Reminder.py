from datetime import *
from tkinter import *
from plyer import notification

main = Tk()
main.geometry("200x70")

x_split = {}
with open(".\Reminder.txt") as f:
    for line in f:
        (key, value) = line.split(" - ")
        x_split[key] = value

def Notify():
    global p1
    time_now = datetime.now().strftime("%H:%M:%S")
    my_label.config(text = time_now)
    my_label.after(1000,Notify)
    for key, value in x_split.items():
        if key+":01" == datetime.now().strftime("%H:%M:%S"):
            notification.notify(
				title = "Reminder!",
				message = value,
                timeout = 3,
                app_icon = "warning.ico",
			)

my_label = Label(main, font = ('calibri', 40, 'bold'),
                background = 'purple',
                foreground = 'white' )
my_label.pack()	

Notify()
mainloop()