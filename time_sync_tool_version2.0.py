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

# Function to convert hex_device_time stamp
# to hex_host_time stamp

def hex_dev_to_host():
    offset = float(e2_value.get())
    offset = offset/pow(10,6)
    hex_dev_time = e14_value.get()
    int_dev_time = int(hex_dev_time, base=16)
    dec_dev_time = float(int_dev_time/19.2)/pow(10,6)
    t5.delete("1.0", END)
    t5.insert(END, dec_dev_time)
    host_time = dec_dev_time + offset
    t6.delete("1.0", END)
    t6.insert(END, host_time)
    hex_host_time = hex(int(host_time*19.2 *pow(10,6)))
    t7.delete("1.0", END)
    t7.insert(END, hex_host_time)
    
# Function to convert hex_host_time stamp
# to hex_dev_time stamp

def hex_host_to_dev():
    offset = float(e2_value.get())
    offset = offset/pow(10,6)
    hex_host_time = e20_value.get()
    int_host_time = int(hex_host_time, base=16)
    dec_host_time = float(int_host_time/19.2)/pow(10,6)
    t8.delete("1.0", END)
    t8.insert(END, dec_host_time)
    device_time = dec_host_time - offset
    t9.delete("1.0", END)
    t9.insert(END, device_time)
    hex_dev_time = hex(int(device_time*19.2*pow(10,6)))
    t10.delete("1.0", END)
    t10.insert(END, hex_dev_time)
    
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
e11 = Label(window, text = "")
e12 = Label(window, text = "Direct Hex to Hex converions")
e13 = Label(window, text = "Enter Device time stamp in Hex")
e14_value = StringVar()
e14 = Entry(window, textvariable = e14_value)
e15 = Label(window, text = "Device time stamp in decimal")
e16 = Label(window, text = "Host time stamp in decimal")
e17 = Label(window, text = "Host time stamp in Hex")
e18 = Label(window, text = "")
e19 = Label(window, text = "Enter Host time stamp in Hex")
e20_value = StringVar()
e20 = Entry(window, textvariable = e20_value)
e21 = Label(window, text = "Host time stamp in decimal")
e22 = Label(window, text = "Device time stamp in decimal")
e23 = Label(window, text = "Device time stamp in Hex")

# Create the Text Widgets
t1 = Text(window, height = 1, width = 20)
t2 = Text(window, height = 1, width = 20)
t3 = Text(window, height = 1, width = 20)
t4 = Text(window, height = 1, width = 20)
t5 = Text(window, height = 1, width = 20)
t6 = Text(window, height = 1, width = 20)
t7 = Text(window, height = 1, width = 20)
t8 = Text(window, height = 1, width = 20)
t9 = Text(window, height = 1, width = 20)
t10 = Text(window, height = 1, width = 20)

# Create the Button Widget
b1 = Button(window, text = "Convert", command = host_to_dev)
b2 = Button(window, text = "Convert", command = dev_to_host)
b3 = Button(window, text = "Convert", command = hex_dev_to_host)
b4 = Button(window, text = "Convert", command = hex_host_to_dev)

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
e11.grid(row = 7, column = 0)
e12.grid(row = 8, column = 0)
e13.grid(row = 9, column = 0)
e14.grid(row = 9, column = 1)
b3.grid(row = 9, column = 2)
e15.grid(row = 10,column = 0)
e16.grid(row = 10,column = 1)
e17.grid(row = 10,column = 2)
t5.grid(row = 11,column = 0)
t6.grid(row = 11,column = 1)
t7.grid(row = 11,column = 2)
e18.grid(row = 12,column = 0)
e19.grid(row = 13,column = 0)
e20.grid(row = 13,column = 1)
b4.grid(row = 13, column = 2)
e21.grid(row = 14,column = 0)
e22.grid(row = 14,column = 1)
e23.grid(row = 14,column = 2)
t8.grid(row = 15,column = 0)
t9.grid(row = 15,column = 1)
t10.grid(row = 15,column = 2)


# Start the GUI
window.mainloop()

# use XO(19.2 MHz) and Seconds XO in crashscope to view time stamps
# offset = 27292.210550
#host_time = 29560.335514
#device_time = 2268.074430
