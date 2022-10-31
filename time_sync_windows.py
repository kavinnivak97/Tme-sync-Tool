# Python program to create a simple GUI
# Time Sync Tool using Tkinter


from tkinter import *


# Create a GUI window
window = Tk()
window.title('Time Sync Tool')

# Function to convert host_time stamp
# to device_time stamp

def host_to_dev():
    offset = float(e2_value.get())
    host_time = float(e4_value.get())
    offset = offset/pow(10,6)
    device_time = host_time - offset
    t1.delete("1.0",END)
    t1.insert(END,device_time)
    device_time = device_time*pow(10,6)*19.2
    device_time = int(device_time)
    device_time = hex(device_time).upper()
    t2.delete("1.0", END)
    t2.insert(END,device_time)

# Function to convert device_time stamp
# to host_time stamp

def dev_to_host():
    offset = float(e2_value.get())
    device_time = float(e6_value.get())
    offset = offset/pow(10,6)
    host_time = device_time + offset
    t3.delete("1.0", END)
    t3.insert(END, host_time)
    host_time = host_time*pow(10,6)*19.2
    host_time = int(host_time)
    host_time = hex(host_time).upper()
    t4.delete("1.0", END)
    t4.insert(END, host_time)


# Create the Label widgets
e1 = Label(window, text = "Enter the Offset Value (in uSecs)")
e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e3 = Label(window, text = "Enter the Host time stamp (in seconds)")
e4_value = StringVar()
e4 = Entry(window, textvariable = e4_value)
e5 = Label(window, text = "Enter the Device time stamp (in seconds)")
e6_value = StringVar()
e6 = Entry(window, textvariable = e6_value)
e7 = Label(window, text = "Device Time(decimal)")
e8 = Label(window, text = "Device Time(Hex)")
e9 = Label(window, text = "Host Time(decimal)")
e10 = Label(window, text = "Host Time(Hex)")

# Create the Text Widgets
t1 = Text(window, height = 1, width = 20)
t2 = Text(window, height = 1, width = 20)
t3 = Text(window, height = 1, width = 20)
t4 = Text(window, height = 1, width = 20)

# Create the Button Widget
b1 = Button(window, text = "Convert", command = host_to_dev)
b2 = Button(window, text = "Convert", command = dev_to_host)

# grid method is used for placing
# the widgets at respective positions
# in table like structure
e1.grid(row = 0, column = 0)
e2.grid(row = 0, column = 1)
e3.grid(row = 1, column = 0)
e4.grid(row = 1, column = 1)
b1.grid(row = 1, column = 2)
e7.grid(row = 2, column = 0)
e8.grid(row = 2, column = 1)
t1.grid(row = 3, column = 0)
t2.grid(row = 3, column = 1)
e5.grid(row = 4, column = 0)
e6.grid(row = 4, column = 1)
b2.grid(row = 4, column = 2)
e9.grid(row = 5, column = 0)
e10.grid(row = 5, column = 1)
t3.grid(row = 6, column = 0)
t4.grid(row = 6, column = 1)


# Start the GUI
window.mainloop()


# offset = 27292.210550
#host_time = 29560.335514
#device_time = 2268.074430
