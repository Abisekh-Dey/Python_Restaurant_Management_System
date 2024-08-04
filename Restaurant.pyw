from tkinter import *
from datetime import datetime
import tkinter.messagebox as tmsg
from PIL import Image,ImageTk
customer_no=1
index=1
item_index=1
price = []
item = []
with open(r"restaurant_assets/restaurant_details.txt") as f:
    details=f.readlines()
    for i in details:
        w,x=i.split(",")
        y,z=x.split(": ")
    z=z[0:(len(z)-1)]
    z=int(z)/100
gst=z
        
def Create_order():
    root.withdraw()
    root1=Toplevel(root)
    root1.geometry("1280x800")
    root1.minsize(1280,800)
    root1.maxsize(1280,800)
    def rgb_to_hex(rgb):
        return '#{:02x}{:02x}{:02x}'.format(*rgb)#Converting rgb color into hexa deciaml string code
    rgb_color = (249, 232, 151)#Getting The color code from css 
    button_col=(18, 64, 118)
    inner_text_col=(255, 195, 116)
    head_col=(0, 223, 162)
    root1.configure(bg=rgb_to_hex(rgb_color))
    # root1.wm_iconbitmap(r"atmicon.ico")
    root1.title("Restaurant Ordering System")
    def update_clock():
        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
        label.config(text=current_time)
        label.after(1000, update_clock)  # Update every 1000 milliseconds (1 second)
    with open(r"restaurant_assets/restaurant_details.txt") as f:
        details=f.readlines()
        for i in details:
            a,b=i.split(",")
            c,d=a.split(": ")
    restaurant_name=d
    f=Frame(root1,bg=rgb_to_hex(head_col))
    f.pack(side="top",fill=X)
    Label(f,text=f"WELCOME TO THE {restaurant_name}",bg=rgb_to_hex(head_col),fg=rgb_to_hex(button_col),font="arial 28 bold").pack(anchor=CENTER)
    Label(f,text="Create Order",bg=rgb_to_hex(rgb_color),fg=rgb_to_hex(button_col),font="arial 20 bold").pack(anchor=CENTER,fill=X)
    ff=Frame(root1,bg=rgb_to_hex(rgb_color))
    ff.pack(fill=X)
    def search(event=None):#event=None Allows the function to be called with or without an event; if I only write event in the parameter then the function will work as an event but in this case the function can't be called using the search button so I did (event=None)
        if entry.get():
            if entry.get().isdigit()==False:
                dish=entry.get().lower()
                for i in frame.children.values():  
                    if isinstance (i,Label):
                        if i.cget("text").lower()==dish:
                            i.config(highlightthickness=5,highlightbackground="yellow")
                            canvas.update_idletasks()  # Update canvas to get the new bounding box
                            canvas.yview_moveto(i.winfo_y() / frame.winfo_height())
                            break
                else:
                    tmsg.askokcancel("Status","Sorry Item Not Found!")
            else:
                tmsg.askokcancel("Status","Please Search A Valid Item!")
        else:
            tmsg.askokcancel("Status","Please Search An Item!") 
                    
    var=StringVar()
    Label(ff,text="",font="arial 16 bold",bg=rgb_to_hex(rgb_color)).grid(row=0,column=0,padx=220,pady=5)
    entry=Entry(ff,textvariable=var,font="arial 17 bold",justify="center",relief=SOLID,bg="beige")
    entry.grid(row=0,column=1,padx=20)
    Button(ff,text="Search",bg=rgb_to_hex(head_col),fg=rgb_to_hex(button_col),font="arial 12 bold",relief=RAISED,command=search).grid(row=0,column=2)
    entry.bind("<Return>", search)
    # f1=Frame(root1,bg="black",height=300)
    # f1.pack(side="top",fill=X)
    f0 = Frame(root1)
    f0.pack(side="top", fill="x")

    # Create a canvas and a scrollbar
    canvas = Canvas(f0, bg="black",highlightthickness=0)
    scrollbar = Scrollbar(f0, orient="vertical", command=canvas.yview,highlightthickness=2)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Create a frame inside the canvas
    frame = Frame(canvas, bg="black")
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Configure the canvas' scroll region
    def onFrameConfigure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", onFrameConfigure)
    
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    
    # Enable scrolling with the arrow keys
    def on_up_arrow(event):
        canvas.yview_scroll(-1, "units")

    def on_down_arrow(event):
        canvas.yview_scroll(1, "units")
        
    def focus_canvas(event):
        canvas.focus_set()
        canvas.config(highlightbackground="black")
        
    canvas.bind("<MouseWheel>", on_mouse_wheel)
    canvas.bind("<Up>", on_up_arrow)
    canvas.bind("<Down>", on_down_arrow)
    canvas.bind("<Button-1>", focus_canvas)

    # Function to handle button click
    def button_2(l,p,q):
        global index
        l.config(highlightthickness=0)
        d1 = l.cget("text")
        d2 = p.cget("text")
        d3 = q.get()
        # fl=Frame(f2,bg="lavender")
        # fl.pack(side=LEFT)
        # fr=Frame(f2,bg="green")
        # fr.pack(side=RIGHT)
        def cancel():
            fl1.destroy()
            frame1.config(bg="beige")
            if len(frame1.children)==0:
                add.config(state="disabled")
        fl1=Frame(frame1,bg="beige")
        fl1.pack(fill=X)
        Label(fl1, text=f"{index}. Item Name:",bg="beige", font="arial 12 bold").grid(row=0, column=0,pady=5)
        Label(fl1, text=f"{d1}",bg="beige", font="arial 12 bold",fg="green").grid(row=0, column=1,pady=5)
        Label(fl1, text="Price:",bg="beige", font="arial 12 bold").grid(row=0, column=2,pady=5)
        Label(fl1, text=f"{d2}",bg="beige", font="arial 12 bold",fg="red").grid(row=0, column=3,pady=5)
        Label(fl1, text="Quantity:",bg="beige", font="arial 12 bold").grid(row=0, column=4,pady=5)
        Label(fl1,text=f"{d3}",bg="beige", font="arial 12 bold",fg="blue").grid(row=0, column=5,pady=5)
        Button(fl1,text="Cancel",bg="red",fg="white",relief="raised",command=cancel, font="arial 10 bold").grid(row=0,column=6,pady=5)
        index+=1
        add.config(state=NORMAL)
        
    with open(r"restaurant_assets/items.txt","r") as f:
        items=f.readlines()
        item_list=[]
        for i in items:
            i=i[0:(len(i)-2)]
            if "," in i:
                m,n=i.split(",")
                a=(m,n)
                item_list.append(a)
            else:
                item_list.append((i,))

    # Add items to the frame inside the canvas
    for i in range(len(item_list)):
        if len(item_list[i])==1:
            Label(frame,text=" ", font="arial 20 bold", fg="white", bg="black").grid(row=i, column=0,pady=5,padx=10)
            Label(frame,text=f"{item_list[i][0]}", font="arial 20 bold", fg="white", bg="black",highlightthickness=2).grid(row=i, column=1,pady=5,padx=10)
        else:
            global item_index
            Label(frame,text=f"{item_index}", font="arial 20 bold", fg="white", bg="black").grid(row=i, column=0,pady=5,padx=10)
            l = Label(frame, text=item_list[i][0], font="arial 20 bold", fg="white", bg="black")
            l.grid(row=i, column=1,pady=5,padx=10)
            Label(frame, text="Price:",bg="black", fg="white", font="arial 20 bold").grid(row=i, column=2,pady=5,padx=10)
            p = Label(frame, text=item_list[i][1], font="arial 20 bold", fg="white", bg="black")
            p.grid(row=i, column=3,pady=5,padx=10)
            Label(frame,text="Quantity:", font="arial 20 bold", fg="white", bg="black").grid(row=i, column=4,pady=5,padx=10)
            q = Spinbox(frame, from_=1, to=100, font="arial 18 bold", fg="white", bg="black",width=3,relief=SOLID,highlightthickness=2,highlightbackground="white",buttonbackground="red")
            q.grid(row=i, column=5,pady=5,padx=10)
            Button(frame, text="Add", bg=rgb_to_hex(head_col), font="arial 16 bold", fg=rgb_to_hex(button_col), relief="raised",
                    command=lambda l=l, p=p, q=q: button_2(l,p,q)).grid(row=i, column=6,pady=5,padx=10)
            item_index+=1

    # Configure the canvas and the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    f3=Frame(root1)
    f3.pack(fill=X)
    Label(f3,text="Cart",fg=rgb_to_hex(button_col),bg=rgb_to_hex(head_col),font="arial 20 bold",width=36,padx=2).grid(row=0,column=0)
    Label(f3,text="",font="arial 22 bold",width=4,padx=2,bg=rgb_to_hex(rgb_color)).grid(row=0,column=1)
    Label(f3,text="Order Summery",fg=rgb_to_hex(button_col),bg=rgb_to_hex(head_col),font="arial 20 bold",width=34).grid(row=0,column=2)
    
    #Cart and Order Summery Combined Frame
    f2 = Frame(root1,bg=rgb_to_hex(rgb_color))
    f2.pack(fill="x")
    #Cart Section
    fl=Frame(f2,bg=rgb_to_hex(rgb_color),width=38)
    fl.grid(row=0,column=0)
    canvas1 = Canvas(fl, bg="beige",width=601,height=190,highlightthickness=0)
    canvas1.pack(side="left",fill=Y)
    
    scrollbar1 = Scrollbar(fl, orient="vertical", command=canvas1.yview,highlightthickness=2)
    scrollbar1.pack(side="right", fill="y")
    
    canvas1.configure(yscrollcommand=scrollbar1.set)
    
    frame1 = Frame(canvas1, bg=rgb_to_hex(rgb_color),width=38)
    canvas1.create_window((0, 0), window=frame1, anchor="nw")
    def FrameConfigure(event):
        canvas1.configure(scrollregion=canvas1.bbox("all"))

    frame1.bind("<Configure>", FrameConfigure)
    
    def mouse_wheel(event):
        canvas1.yview_scroll(int(-1 * (event.delta / 120)), "units")
    
    # Enable scrolling with the arrow keys
    def up_arrow(event):
        canvas1.yview_scroll(-1, "units")

    def down_arrow(event):
        canvas1.yview_scroll(1, "units")
        
    def focuscanvas(event):
        canvas1.focus_set()
        canvas1.config(highlightbackground="beige")
        
    canvas1.bind("<MouseWheel>", mouse_wheel)
    canvas1.bind("<Up>", up_arrow)
    canvas1.bind("<Down>", down_arrow)
    canvas1.bind("<Button-1>", focuscanvas)

    fm=Frame(f2,bg=rgb_to_hex(rgb_color))
    fm.grid(row=0,column=1)
    def add_sum():
        # gst=.18
        index=1
        # price=[]
        for widget in frame1.children.values():
            l1=[]
            for i in widget.children.values():
                if isinstance(i,Label):
                    l1.append(i.cget("text"))
            # print(l1, l1[1], l1[3],l1[5])
            fl2=Frame(frame2,bg="beige")
            fl2.pack(fill=X)
            Label(fl2, text=f"{index}.{l1[1]}",bg="beige", font="arial 16 bold",fg="green").grid(row=0, column=0,pady=5)
            item.append(f"Item: {l1[1]}")
            Label(fl2, text="Price:",bg="beige", font="arial 16 bold").grid(row=0, column=1,pady=5)
            Label(fl2, text=f"{l1[3]}",bg="beige", font="arial 16 bold",fg="red").grid(row=0, column=2,pady=5)
            Label(fl2, text="X",bg="beige", font="arial 16 bold").grid(row=0, column=3,pady=5)
            Label(fl2,text=f"{l1[5]}",bg="beige", font="arial 16 bold",fg="blue").grid(row=0, column=4,pady=5)
            p,q=l1[3].split("/")
            item.append(f"price Rs: {p}")
            price.append(int(p)*int(l1[5]))
            add.config(state=DISABLED)
            b1.config(state="normal")
            b2.config(state="normal")
            index+=1
            
        # print(sum(price))
        fl3=Frame(frame2,bg="beige",highlightthickness=2,highlightbackground="black",pady=5)
        fl3.pack(fill=X)
        fl4=Frame(fl3,bg="beige")
        fl4.pack(fill=X)
        Label(fl4,text=f"Added GST: {gst}",bg="beige", font="arial 16 bold",fg="brown").grid(row=0,column=0)
        fl5=Frame(fl3,bg="beige")
        fl5.pack(fill=X)
        Label(fl5,text=f"Total: {sum(price)+(sum(price)*gst)}",bg="beige", font="arial 16 bold",fg="blue").grid(row=0,column=0)
            
    add=Button(fm,text="Add",bg=rgb_to_hex(head_col),fg=rgb_to_hex(button_col),font="arial 12 bold",command=add_sum,relief="raised")
    add.pack(expand="true",fill=X,pady=20)
    add.config(state=DISABLED)
    def clear_all():
        price.clear()
        global index
        index=1
        var.set("")
        widgets1 = list(frame1.children.values())
        widgets2 = list(frame2.children.values())
        for i in frame.children.values():  
            if isinstance (i,Label):
                if i.cget("text") in ["Starters","Vegetarian Main Courses","Non-Vegetarian Main Courses","Breads and Rice","Sides","Desserts","Beverages"]:
                    i.config(highlightbackground="white")
                    i.config(highlightthickness=2)
                else:    
                    i.config(highlightthickness=0)
        if (len(widgets1)>0 and len(widgets2)>0) or len(widgets1)>0 or len(widgets2)>0:
            for i in widgets1:
                i.destroy()
                frame1.config(bg="beige")
                add.config(state="disabled")
            for j in widgets2:
                j.destroy()
                frame2.config(bg="beige")
        else:
            tmsg.askokcancel("Status","Please Add Atleast An Item !")
    clear=Button(fm,text="Clear All",bg="red",fg="white",font="arial 12 bold",command=clear_all,relief="raised")
    clear.pack()
    
    #Order Summery Section
    fr=Frame(f2,bg="beige")
    fr.grid(row=0,column=2)
    canvas2 = Canvas(fr, bg="beige",width=560,height=190,highlightthickness=0)
    canvas2.pack(side="left",fill=Y)
    
    scrollbar2 = Scrollbar(fr, orient="vertical", command=canvas2.yview,highlightthickness=2)
    scrollbar2.pack(side="right", fill="y")
    
    canvas2.configure(yscrollcommand=scrollbar2.set)
    
    frame2 = Frame(canvas2, bg=rgb_to_hex(rgb_color),width=38)
    canvas2.create_window((0, 0), window=frame2, anchor="nw")
    def frameConfigure(event):
        canvas2.configure(scrollregion=canvas2.bbox("all"))

    frame2.bind("<Configure>", frameConfigure)
    
    
    def Mouse_wheel(event):
        canvas2.yview_scroll(int(-1 * (event.delta / 120)), "units")
    
    # Enable scrolling with the arrow keys
    def Up_arrow(event):
        canvas2.yview_scroll(-1, "units")

    def Down_arrow(event):
        canvas2.yview_scroll(1, "units")
        
    def Focus_canvas(event):
        canvas2.focus_set()
        canvas2.config(highlightbackground="beige")
        
    canvas2.bind("<MouseWheel>", Mouse_wheel)
    canvas2.bind("<Up>", Up_arrow)
    canvas2.bind("<Down>", Down_arrow)
    canvas2.bind("<Button-1>", Focus_canvas)

    Label(f2,text="",bg="beige",width=43,font="arial 17 bold",padx=6).grid(row=1,column=0)
    Label(f2,text="",font="arial 17 bold",width=5,padx=2,bg=rgb_to_hex(rgb_color)).grid(row=1,column=1)
    sub_fr=Frame(f2,bg="beige")
    sub_fr.grid(row=1,column=2)
    
    def cancel_ord():
        price.clear()
        widgets = list(frame2.children.values())  # Create a list of the widgets
        if widgets:
            for i in widgets:
                i.destroy()
                frame2.config(bg="beige")
                add.config(state=NORMAL)
                b1.config(state="disabled")
                b2.config(state="disabled")
        # else:
        #     tmsg.askokcancel("Status","Order Summery Is Empty !")
    b1=Button(sub_fr,text="Cancel Order",bg="red",fg="white",font="arial 12 bold",command=cancel_ord)
    b1.grid(row=0,column=0)
    b1.config(state="disabled")
    Label(sub_fr,text="",font="arial 12 bold").grid(row=0,column=1,padx=172)
    def payment():
        root1.withdraw()
        root2=Toplevel(root1)
        root2.geometry("1280x800")
        root2.minsize(1280,800)
        root2.maxsize(1280,800)
        image=Image.open(r"restaurant_assets/a.jpg")
        photo=ImageTk.PhotoImage(image)
        
        def update_clock():
            current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
            label.config(text=current_time)
            label.after(1000, update_clock)
        
        def validate_input(new_value):
                return len(new_value) <= 10
        
        background_label =Label(root2, image=photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        Label(root2,text="PAYMENT WINDOW",font="arial 28 bold",fg="blue",bg="yellow").pack(fill=X)
        
        f0=Frame(root2,bg=rgb_to_hex(rgb_color))
        f0.pack(pady=48)
        Label(f0,text=f"Pay Rs: {sum(price)+(sum(price)*gst)}",font="arial 28 bold",fg="blue",bg="yellow").pack(fill=X)
        f=Frame(f0,bg="lightblue",relief=SOLID)
        f.pack()
        label1=Label(f,text="Enter Name: ",bg="lightblue",fg="black",font="arial 18 bold")
        label1.grid(row=0,column=0,padx=15,pady=5)
        v1=StringVar()
        e1=Entry(f,textvariable=v1,font="arial 18 bold",justify="center",relief=SOLID)
        e1.grid(row=0,column=1,padx=15,pady=5)
        label2=Label(f,text="Enter Mobile No: ",bg="lightblue",fg="black",font="arial 18 bold")
        label2.grid(row=1,column=0,padx=15,pady=5)
        v2=StringVar()
        e2=Entry(f,textvariable=v2,font="arial 18 bold",justify="center",relief=SOLID, validate="key", validatecommand=(root.register(validate_input), "%P"))
        e2.grid(row=1,column=1,padx=15,pady=5)
        f1=Frame(f0,bg="lightblue")
        f1.pack(fill=X)
        Label(f1,text=f"Scan The Qr to Pay Rs: {sum(price)+(sum(price)*gst)}",bg="lightblue",fg="black",font="arial 18 bold",highlightthickness=2,highlightbackground="red").pack(fill=X)
        qr=Image.open(r"qr2.png")
        qr=qr.resize((250,250))
        qr=ImageTk.PhotoImage(qr)
        Label(f1,image=qr).pack(pady=8)
        def proceed(event=None):
            global customer_no
            global index
            n.config(state="normal")
            date=datetime.now().strftime("[Date: %d-%m-%Y , Time: %H:%M:%S]")
            if e1.get():
                a,b=e1.get().split()
                name=a+b
                if name.isalpha():
                    if e2.get():
                        if e2.get().isdigit():
                            with open(r"order.txt","a") as file:
                                file.write(f"{customer_no}, {date}, Customer Name: {e1.get()}, Customer Mobile Number: {e2.get()},{item}, Total Paid Amount: Rs: {sum(price)+(sum(price)*gst)}\n")
                            price.clear()
                            item.clear()
                            index=1
                            customer_no+=1
                            tmsg.askokcancel("Status","Order Added Successfully!")
                        else:
                            tmsg.askokcancel("Status","Mobile Number Should Contain Numbers Only!")
                    else:
                        tmsg.askokcancel("Status","Please Enter The Mobile Number!")
                else:
                    tmsg.askokcancel("Status","Name Should Contain Characters Only!")
            else:
                tmsg.askokcancel("Status","Please Enter The Name!")
        b=Button(f1,text="PROCEED",bg=rgb_to_hex(head_col),fg=rgb_to_hex(button_col),font="arial 14 bold",relief="raised",command=proceed)
        b.pack(pady=10)
        e2.bind("<Return>", proceed)
        
        f2=Frame(root2,bg="yellow",highlightthickness=2,highlightbackground="black")
        f2.pack()
        
        def back():
            root2.destroy()
            root1.deiconify()
        Button(f2,text="<<Back",bg=rgb_to_hex(head_col),fg=rgb_to_hex(button_col),font="arial 12 bold",command=back).grid(row=0,column=0)
        Label(f2,bg="yellow").grid(row=0,column=1,padx=566)
        def next():
            root2.destroy()
            root.deiconify()
        n=Button(f2,text="Next>>",bg=rgb_to_hex(button_col),fg=rgb_to_hex(inner_text_col),font="arial 12 bold",command=next)
        n.grid(row=0,column=2)
        n.config(state="disabled")
        
        f3=Frame(root2,bg="yellow")
        f3.pack(fill=X)
        label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
        label.pack(fill=X)
        update_clock()
        root2.mainloop()
    b2=Button(sub_fr,text="Payment",bg=rgb_to_hex(head_col),fg=rgb_to_hex(button_col),font="arial 12 bold",padx=16,command=payment)
    b2.grid(row=0,column=2)
    b2.config(state="disabled")
    
    f5=Frame(root1,bg=rgb_to_hex(rgb_color))
    f5.pack()
    
    def back():
        root1.destroy()
        root.deiconify()
    Button(f5,text="<<Back",bg=rgb_to_hex(head_col),fg=rgb_to_hex(button_col),font="arial 12 bold",command=back).grid(row=0,column=0)
    Label(f5,bg=rgb_to_hex(rgb_color)).grid(row=0,column=1,padx=548)
    Button(f5,text="Instructions",bg=rgb_to_hex(button_col),fg=rgb_to_hex(inner_text_col),font="arial 12 bold").grid(row=0,column=2)
    f4=Frame(root1,bg="yellow")
    f4.pack(fill=X)
    label=Label(f4,fg="blue",bg="yellow",font="arial 20 bold")
    label.pack(fill=X)
    update_clock()
    root1.mainloop()
def find_order():
    root.withdraw()
    root1=Toplevel(root)
    root1.geometry("1280x800")
    root1.minsize(1280,800)
    root1.maxsize(1280,800)
    root1.configure(bg="lavender")
    def rgb_to_hex(rgb):
        return '#{:02x}{:02x}{:02x}'.format(*rgb)#Converting rgb color into hexa deciaml string code
    rgb_color = (249, 232, 151)#Getting The color code from css 
    button_col=(18, 64, 118)
    inner_text_col=(255, 195, 116)
    head_col=(0, 223, 162)
    # root.wm_iconbitmap(r"atmicon.ico")
    root1.title("Restaurant Ordering System")
    
    f=Frame(root1,bg=rgb_to_hex(head_col))
    f.pack(side="top",fill=X)
    date=datetime.now().strftime("Date: %d-%m-%Y")
    def back():
        root1.destroy()
        root.deiconify()
    def Total():
        with open(r"order.txt","r") as f:
            data=f.readlines()
        total=[]
        for i in data:
            j=i.split(",")
            if date in j[1]:
                a,b=i.split("Total Paid Amount: Rs: ")
                p,q=b.split("\n")
                total.append(float(p))
        tmsg.askokcancel("Total Sells",f"Congratulations! Sales of Rs: {sum(total)}/- has done on {date}")
        total.clear()
    Button(f,text="Back",bg="red",fg="white",font="arial 16 bold",relief="raised",command=back).grid(row=0,column=0)
    Label(f,text=f"All Orders Of {date}",bg=rgb_to_hex(head_col),fg=rgb_to_hex(button_col),font="arial 20 bold").grid(row=0,column=1,padx=370)
    Button(f,text="Total",bg=rgb_to_hex(button_col),fg=rgb_to_hex(inner_text_col),font="arial 16 bold",relief="raised",command=Total).grid(row=0,column=2)
    
    with open(r"order.txt","r") as f:
        data=f.readlines()
    
    scrollbar3=Scrollbar(root1)
    scrollbar3.pack(side=RIGHT,fill=Y)

    Lbx=Listbox(root1,yscrollcommand=scrollbar3.set,font="arial 16 bold")
    Lbx.pack(fill=BOTH,expand=True)

    scrollbar3.config(command=Lbx.yview)
    l=[]
            
    for i in data:
        i=i[0:len(i)-1]
        j=i.split(",")
        if date in j[1]:
            Lbx.insert(END,f"{i}")
            l.append("Y")
    if len(l)==0:
        tmsg.askokcancel("Status",f"Sorry No Order Has Done On {date} Till Now!")
        root1.destroy()
        root.deiconify()
    root1.mainloop()
def end():
    x=tmsg.askyesno("Status","Do You Want To Exit?")
    if x==True:
        root.withdraw()
        root1=Toplevel(root)
        root1.geometry("1280x800")
        root1.minsize(1280,800)
        root1.maxsize(1280,800)
        root1.configure(bg="lavender")
        # root1.wm_iconbitmap(r"atmicon.ico")
        root1.title("Restaurant Ordering System")
        
        def update_clock():
            current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
            label.config(text=current_time)
            label.after(1000, update_clock)  # Update every 1000 milliseconds (1 second)
        
        def validate_input(new_value):
            return len(new_value) <= 4
        
        def return_to_root():
            root1.destroy()
            root.deiconify()
            tmsg.showinfo("Status","Session Time-out!...")
            
        image=Image.open(r"restaurant_assets/a.jpg")
        photo=ImageTk.PhotoImage(image)
                                                                                                            
        background_label =Label(root1, image=photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
                                                                                        
        f=Frame(root1,bg="light blue",relief="solid",borderwidth=4)
        f.pack(expand=True)
        Label(f,text="Enter Application Password",font="arial 28 bold",bg="light blue",padx=20).pack(pady=30,fill=X)
        varr=StringVar()
        acn_k=Entry(f,textvariable=varr,font="arial 40 bold",relief="solid",width=16,bg="light blue",justify="center",borderwidth=4,validate="key", validatecommand=(root.register(validate_input), "%P"),show="*",fg="red")
        acn_k.pack(pady=30,padx=20)
        f2=Frame(f,bg="light blue")
        f2.pack()
                                                                                    
        def ext1():
            root1.destroy()
            root.deiconify()
                                                                                        
        def sub():
            if acn_k.get():
                if acn_k.get().isdigit() and len(acn_k.get())==4:
                    if acn_k.get()=="0000":
                        root.destroy()
                    else:
                        tmsg.askokcancel("Status","Wrong Password!...")
                        root1.destroy()
                        root.deiconify()
                else:
                    tmsg.askokcancel("Status","Please Enter A Valid Password!...")
                    varr.set("")
            else:
                tmsg.askokcancel("Status","Please Enter The Password!...")
            
        Button(f2,text="Cancel",font="arial 20 bold",relief="raised",bg="Red",command=ext1,padx=5).grid(row=0,column=0,pady=30)
        Label(f2,text="",font="arial 20 bold",bg="light blue").grid(row=0,column=1,padx=90)
        Button(f2,text="Submit",bg="light green",font="arial 20 bold",relief="raised",command=sub).grid(row=0,column=2,pady=30)
        f3=Frame(f,bg="yellow")
        f3.pack(fill=X)
        label=Label(f3,fg="blue",bg="yellow",font="arial 20 bold")
        label.pack(fill=X)
        update_clock()
        root1.after(15000,return_to_root)
                                                                                    
        root1.mainloop()

if __name__=="__main__":
    #First Window
    root=Tk()
    root.geometry("1280x800")
    root.minsize(1280,800)
    root.maxsize(1280,800)
    def rgb_to_hex(rgb):
        return '#{:02x}{:02x}{:02x}'.format(*rgb)#Converting rgb color into hexa deciaml string code
    rgb_color = (249, 232, 151)#Getting The color code from css 
    button_col=(18, 64, 118)
    inner_text_col=(255, 195, 116)
    head_col=(0, 223, 162)
    root.configure(bg=rgb_to_hex(rgb_color))
    # root.wm_iconbitmap(r"atmicon.ico")
    root.title("Restaurant Ordering System")
    
    def update_clock():
        current_time = datetime.now().strftime("Date: %Y-%m-%d & Time: %H:%M:%S")
        label.config(text=current_time)
        label.after(1000, update_clock)  # Update every 1000 milliseconds (1 second)

    with open(r"restaurant_assets/restaurant_details.txt") as f:
        details=f.readlines()
        for i in details:
            a,b=i.split(",")
            c,d=a.split(": ")
    restaurant_name=d
    f=Frame(root,bg=rgb_to_hex(head_col))
    f.pack(side="top",fill=X)
    l=Label(f,text=f"WELCOME TO THE {restaurant_name}",bg=rgb_to_hex(head_col),fg=rgb_to_hex(button_col),font="arial 28 bold")
    l.pack(anchor="center")
    f1=Frame(root,bg=rgb_to_hex(rgb_color))
    f1.pack(side="top",fill=X,pady=60)
    b1=Button(f1,text="Click Here",relief="raised",bg=rgb_to_hex(button_col),fg=rgb_to_hex(inner_text_col),font="arial 20 bold",command=Create_order)
    b1.pack(side="right",padx=10,pady=20)
    l1=Label(f1,text="Create New Order->",font="arial 20 bold",bg=rgb_to_hex(rgb_color),fg=rgb_to_hex(button_col),padx=15)
    l1.pack(side="right")
    f2=Frame(root,bg=rgb_to_hex(rgb_color))
    f2.pack(side="top",fill=X,pady=46)
    b2=Button(f2,text="Click Here",relief="raised",bg=rgb_to_hex(button_col),fg=rgb_to_hex(inner_text_col),font="arial 20 bold",command=find_order)
    b2.pack(side="right",padx=10,pady=20)
    l2=Label(f2,text="Find Order->",font="arial 20 bold",bg=rgb_to_hex(rgb_color),fg=rgb_to_hex(button_col),padx=15)
    l2.pack(side="right")
    f3=Frame(root,bg=rgb_to_hex(rgb_color))
    f3.pack(side="top",fill=X,pady=60)
    b3=Button(f3,text="Click Here",relief="raised",bg=rgb_to_hex(button_col),fg=rgb_to_hex(inner_text_col),font="arial 20 bold",command=end)
    b3.pack(side="right",padx=10,pady=30)
    l3=Label(f3,text="EXIT->",font="arial 20 bold",bg=rgb_to_hex(rgb_color),fg=rgb_to_hex(button_col),padx=15)
    l3.pack(side="right")
    f4=Frame(root,bg="yellow")
    f4.pack(fill=X)
    x=datetime.now()
    label=Label(f4,bg="yellow",font="arial 20 bold",fg="blue")
    label.pack(fill=X)
    update_clock()
    root.mainloop()