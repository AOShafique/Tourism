import tkinter as tk
import tkinter.ttk as ttk

prime = tk.Tk()
prime.title("AOSGo.Airlines.Net")
prime.geometry("1000x1000")
prime.configure(background = "deep sky blue")
r = tk.IntVar()
h = tk.IntVar()
f = tk.IntVar()
c = tk.IntVar()

def save():

    sp = tk.Tk()
    sp.title("Your Travel Information")
    sp.geometry("800x800")
    sp.configure(background = "medium blue")
    time = tk.Label(sp,text = "Time period:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 0 , column = 0)
    t1 = tk.Label(sp, text = f"Days: {day.get()} ;", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 0 , column = 1)
    t2 = tk.Label(sp, text = f" Nights: {night.get()}", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 0 , column = 2)
    if f == 1:

        seat = tk.Label(sp, text = "Seat type: economy class", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 2 , column = 0)

    else:

        seat = tk.Label(sp, text = "Seat type: business class", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 2 , column = 0) 

    if c == 1:

        city = tk.Label(sp, text = "City of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 0)
        stay = tk.Label(sp, text = " Dhaka", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 1)
    
    if c == 2:

        city = tk.Label(sp, text = "City of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 0)
        stay = tk.Label(sp, text = " Dhaka", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 1)
        
    if c == 3:

        city = tk.Label(sp, text = "City of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 0)
        stay = tk.Label(sp, text = " Chittagong", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 1)

    if c == 4:

        city = tk.Label(sp, text = "City of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 0)
        stay = tk.Label(sp, text = " Sylhet", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 1)

    if c == 5:

        city = tk.Label(sp, text = "City of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 0)
        stay = tk.Label(sp, text = " Khulna", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 1)

    if c == 6:

        city = tk.Label(sp, text = "City of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 0)
        stay = tk.Label(sp, text = " Rajshahi", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 1)

    if c == 7:

        city = tk.Label(sp, text = "City of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 0)
        stay = tk.Label(sp, text = " Mymensingh", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 1)

    else:

        city = tk.Label(sp, text = "City of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 0)
        stay = tk.Label(sp, text = " Barishal", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 4 , column = 1)


    if h == 1:

        city = tk.Label(sp, text = "Hotel of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 0)
        stay = tk.Label(sp, text = " Bd Grand", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 1)
    
    if h == 2:

        city = tk.Label(sp, text = "Hotel of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 0)
        stay = tk.Label(sp, text = " Sylhet Tea Greens", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 1)
        
    if h == 3:

        city = tk.Label(sp, text = "Hotel of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 0)
        stay = tk.Label(sp, text = " Rajshahi Royal Guest House", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 1)

    if h == 4:

        city = tk.Label(sp, text = "Hotel of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 0)
        stay = tk.Label(sp, text = " Chittagong Marine Lodge", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 1)

    if h == 5:

        city = tk.Label(sp, text = "Hotel of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 0)
        stay = tk.Label(sp, text = " Martins Shack", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 1)

    if h == 6:

        city = tk.Label(sp, text = "Hotel of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 0)
        stay = tk.Label(sp, text = " Rangpur Crimson Crown", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 1)

    if h == 7:

        city = tk.Label(sp, text = "Hotel of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 0)
        stay = tk.Label(sp, text = " Mymensingh Quorum Hotel", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 1)

    else:

        city = tk.Label(sp, text = "Hotel of stay:", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 0)
        stay = tk.Label(sp, text = " Barishal State Inn", font = ("time new roman",14),bg = "medium blue", fg = "lavender").grid(row = 6 , column = 1)
def bd():
    
    ban = tk.Tk()
    ban.title("Travel Package to Bangladesh")
    ban.geometry("1500x1500")
    ban.configure(background = "dark green")

    d = tk.Label(ban,text = "Days:",bg = 'deep sky blue', fg = 'snow',font = ("Times new roman",14)).grid(row = 0, column = 0)
  
    day = tk.Spinbox(ban,from_ = 1,to = 30,width = 20).grid(row = 0, column = 1)

    n = tk.Label(ban,text = "Nights:",bg = 'navy', fg = 'yellow',font = ("Times new roman",14)).grid(row = 0, column = 2)
    
    night = tk.Spinbox(ban,from_ = 1,to = 30,width = 20).grid(row = 0, column = 3)

    flight = tk.Label(ban,text = 'Available seats:',font = ("Times New Roman bold italic",14),fg = 'red',bg = 'dark green').grid(row = 3 , column = 2)

    econ = tk.Radiobutton(ban,text = "Economy",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = f,value = 1).grid(row = 4 , column = 0) 
    ep = tk.Label(ban,text = "$499",font = ("Times New Roman",14),bg = "dark green", fg = 'red').grid(row = 4 , column = 1) 
 
    fc = tk.Radiobutton(ban,text = "First class",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = f,value = 2).grid(row = 5 , column = 0)
    fcp = tk.Label(ban,text = "$999",font = ("Times New Roman",14),bg = "dark green", fg = 'red').grid(row = 5 , column = 1) 
    
    visit = tk.Label(ban,text = 'Cities to visit:',font = ("Times New Roman bold italic",14),fg = 'red',bg = 'dark green').grid(row = 8 , column = 2)

    dk = tk.Radiobutton(ban,text = "Dhaka",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = c,value = 1).grid(row = 9 , column = 0) 
    
    cg = tk.Radiobutton(ban,text = "Chittagong",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = c,value = 2).grid(row = 9 , column = 1)

    sy = tk.Radiobutton(ban,text = "Sylhet",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = c,value = 3).grid(row = 9 , column = 2)

    kh = tk.Radiobutton(ban,text = "Khulna",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = c,value = 4).grid(row = 9 , column = 3)

    rs = tk.Radiobutton(ban,text = "Rajshahi",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = c,value = 5).grid(row = 9 , column = 4)

    rp = tk.Radiobutton(ban,text = "Rangpur",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = c,value = 6).grid(row = 9 , column = 5)

    my = tk.Radiobutton(ban,text = "Mymensingh",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = c,value = 7).grid(row = 9, column = 6)

    bs = tk.Radiobutton(ban,text = "Barisal",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = c,value = 8).grid(row = 9 , column = 7)
    
    hotel = tk.Label(ban,text = 'Available hotels:',font = ("Times New Roman bold italic",14),fg = 'red',bg = 'dark green').grid(row = 12 , column = 2)

    h1 = tk.Radiobutton(ban,text = "Bd Grand",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = h,value = 1).grid(row = 13 , column = 0)
    
    h2 = tk.Radiobutton(ban,text = "Sylhet Tea Greens",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = h,value = 2).grid(row = 13 , column = 1)

    h3 = tk.Radiobutton(ban,text = "Rajshahi Royal Guest House",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = h,value = 3).grid(row = 13 , column = 2)

    h4 = tk.Radiobutton(ban,text = "Chittagong Marine Lodge",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = h,value = 4).grid(row = 13 , column = 3)

    h5 = tk.Radiobutton(ban,text = "Martins Shack",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = h,value = 5).grid(row = 13 , column = 4)

    h6 = tk.Radiobutton(ban,text = "Rangpur Crimson Crown",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = h,value = 6).grid(row = 13 , column = 5)

    h7 = tk.Radiobutton(ban,text = "Mymensingh Quorum Hotel",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = h,value = 7).grid(row = 13, column = 6)

    h8 = tk.Radiobutton(ban,text = "Barishal State Inn",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = h,value = 8).grid(row = 13 , column = 7)

    room = tk.Label(ban,text = 'Available rooms per purpose:',font = ("Times New Roman bold italic",14),fg = 'red',bg = 'dark green').grid(row = 16 , column = 2)

    sm = tk.Radiobutton(ban,text = "Nighter",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = r,value = 1).grid(row = 17 , column = 0) 
    smp = tk.Label(ban,text = "$399",font = ("Times New Roman",14),bg = "dark green", fg = 'red').grid(row = 17 , column = 1)

    rg = tk.Radiobutton(ban,text = "Stay",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = r,value = 2).grid(row = 18 , column = 0)
    rgp = tk.Label(ban,text = "$599",font = ("Times New Roman",14),bg = "dark green", fg = 'red').grid(row = 18 , column = 1)
  
    lg = tk.Radiobutton(ban,text = "Business",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = r,value = 3).grid(row = 19 , column = 0) 
    lgp = tk.Label(ban,text = "$799",font = ("Times New Roman",14),bg = "dark green", fg = 'red').grid(row = 19 , column = 1)
    
    gnd = tk.Radiobutton(ban,text = "Grande",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = r,value = 4).grid(row = 20 , column = 0)
    gndp = tk.Label(ban,text = "$999",font = ("Times New Roman",14),bg = "dark green", fg = 'red').grid(row = 20 , column = 1)

    prs = tk.Radiobutton(ban,text = "Presidential",font = ("Times New Roman",14),bg = "dark green", fg = 'red',variable = r,value = 5).grid(row = 21 , column = 0) 
    prsp = tk.Label(ban,text = "$1299",font = ("Times New Roman",14),bg = "dark green", fg = 'red').grid(row = 21 , column = 1)

    sc = tk.Button(ban,text = "Save & Create Ticket", font = ("Times New Roman",14),bg = 'red',fg = 'yellow',command = save).grid(row = 25, column = 7)

t0 = tk.Label(prime,text = "Welcome to AOSGo!",font = ("Times new roman",14),bg = "deep sky blue", fg = "snow").grid(row = 0, column = 0)
t1 = tk.Label(prime,text = "Choose your dream destination at your own comfort!",font = ("Times new roman",14),bg = "deep sky blue", fg = "snow").grid(row = 0, column = 1)
t2 = tk.Label(prime,text = "Destination Packages",font = ("Times new roman",14),bg = "deep sky blue", fg = "black").grid(row = 2, column = 1)
p1 = tk.Button(prime,font = ("Times New Roman",14),bg = "green",fg = "red",text = "Bangladesh",command = bd).grid(row = 3,column = 0)

prime.mainloop()