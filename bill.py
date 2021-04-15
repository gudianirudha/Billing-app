from tkinter import*
class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1380x760+0+0")
        self.root.resizable(False, False)
        self.root.title("Billing Software")
        bg_color = "#ffd390"
        title = Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="red",font=('Open sans',30,'bold'),pady=2).pack(fill=X)
        
        #variables
        self.cafe = IntVar()
        self.filter = IntVar()
        self.capp = IntVar()
        self.kaapi = IntVar()
        self.esp = IntVar()
        self.frap = IntVar()
        self.brew = IntVar()
        
        self.pizza = IntVar()
        self.tango = IntVar()
        self.veggie = IntVar()
        self.paneer = IntVar()
        self.veg = IntVar()
        self.extra = IntVar()
        self.jala = IntVar()
        
        self.pepsi = IntVar()
        self.coca = IntVar()
        self.slice = IntVar()
        self.sprite = IntVar()
        self.limca = IntVar()
        self.fanta = IntVar()
        self.up = IntVar()
        
        A1= LabelFrame(self.root,text="Customer Details",font=('Open sans',20,"bold"),bg=bg_color,fg="black")
        A1.place(x=0,y=80,relwidth=1)
        
        cname = Label(A1,text="Name",font=('Open sans',18,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,padx=20,pady=5)
        cname_txt = Entry(A1,width=15,font=("arial 14"),bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphone = Label(A1,text="Phone Number",font=('Open sans',18,"bold"),fg="white",bg=bg_color).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt = Entry(A1,width=15,font=("arial 14"),bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        cbill = Label(A1,text="Bill",font=('Open sans',18,"bold"),fg="white",bg=bg_color).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt = Entry(A1,width=15,font=("arial 14"),bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn =Button(A1,text="Search",width=5,bd=7,font=("arial 13 bold")).grid(row=0,column=6,padx=10,pady=10)
        
        # Coffee 
        A2 = LabelFrame(self.root,text="Coffee",relief=GROOVE,bd=10,font=('Open sans',20,"bold"),bg=bg_color,fg="black")
        A2.place(x=5,y=170,width=390,height=430)
        
        
        ame = Label(A2,font=('Open sans',13,"bold"),text="Cafe Americano",fg="red",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        ame_txt = Entry(A2,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        filter_c= Label(A2,font=('Open sans',13,"bold"),text="Filter Coffee",fg="red",bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        filter_c_txt = Entry(A2,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        cappuccino = Label(A2,font=('Open sans',13,"bold"),text="Cappuccino",fg="red",bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        cappuccino_txt = Entry(A2,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        
        Kaapi_Nirvana = Label(A2,font=('Open sans',13,"bold"),text="Kaapi Nirvana",fg="red",bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Kaap_Nirvana_txt = Entry(A2,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        expresso = Label(A2,font=('Open sans',13,"bold"),text="Espresso",fg="red",bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        expreso_txt = Entry(A2,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        Frap= Label(A2,font=('Open sans',13,"bold"),text="Coffee Frappuccino",fg="red",bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Frap_text = Entry(A2,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        
        Brewed =Label(A2,font=('Open sans',13,"bold"),text="Brewed Coffee",fg="red",bg=bg_color).grid(row=6,column=0,padx=10,pady=10,sticky="w")
        Brewed_text = Entry(A2,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,pady=10,padx=10)
          
        #
        A3 = LabelFrame(self.root,text="Pizza",relief=GROOVE,bd=10,font=('Open sans',20,"bold"),bg=bg_color,fg="black")
        A3.place(x=340,y=170,width=390,height=430)
      
        Margherita = Label(A3,font=('Open sans',13,"bold"),text="Margherita",fg="red",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Margherita_txt = Entry(A3,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        Tango= Label(A3,font=('Open sans',13,"bold"),text="Spicy Triple Tango",fg="red",bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Tango_txt = Entry(A3,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        Veggie = Label(A3,font=('Open sans',13,"bold"),text="Veggie Paradise",fg="red",bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Veggie_txt = Entry(A3,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        
        Paneer = Label(A3,font=('Open sans',13,"bold"),text="Paneer",fg="red",bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Paneer_txt = Entry(A3,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        Veg = Label(A3,font=('Open sans',13,"bold"),text="Veg Wonder",fg="red",bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Veg_txt = Entry(A3,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        extra= Label(A3,font=('Open sans',13,"bold"),text="Extravaganza",fg="red",bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        extra_text = Entry(A3,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        
        Jalapeno =Label(A3,font=('Open sans',13,"bold"),text="Jalapeno",fg="red",bg=bg_color).grid(row=6,column=0,padx=10,pady=10,sticky="w")
        Jalapeno_text = Entry(A3,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,pady=10,padx=10)
        
      
        A4 = LabelFrame(self.root,text="Drinks",relief=GROOVE,bd=10,font=('Open sans',20,"bold"),bg=bg_color,fg="black")
        A4.place(x=670,y=170,width=390,height=430)
        
        Pepsi = Label(A4,font=('Open sans',13,"bold"),text="Pepsi",fg="red",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Pepsi_txt = Entry(A4,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        coca = Label(A4,font=('Open sans',13,"bold"),text="Coca Cola",fg="red",bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coca_txt = Entry(A4,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        Slice = Label(A4,font=('Open sans',13,"bold"),text="Slice",fg="red",bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Slice_txt = Entry(A4,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
        
        Sprite = Label(A4,font=('Open sans',13,"bold"),text="Sprite",fg="red",bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Sprite_txt = Entry(A4,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        Limca = Label(A4,font=('Open sans',13,"bold"),text="Limca",fg="red",bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Limca = Entry(A4,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        Fanta = Label(A4,font=('Open sans',13,"bold"),text="Fanta",fg="red",bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Fanta_text = Entry(A4,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        
        Up=Label(A4,font=('Open sans',13,"bold"),text="7 Up",fg="red",bg=bg_color).grid(row=6,column=0,padx=10,pady=10,sticky="w")
        Up_text = Entry(A4,width=10,font=("Open sans",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,pady=10,padx=10)
        
        
        A5 = LabelFrame(self.root,relief=GROOVE,bd=10)
        A5.place(x=990,y=180,width=380,height=540)
        bill_title = Label(A5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(A5,orient=VERTICAL)
        self.txtarea = Text(A5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        A6 = LabelFrame(self.root,text="Billing Area",relief=GROOVE,bd=8,font=('Open sans',20,"bold"),bg=bg_color,fg="black")
        A6.place(x=0,y=590,relwidth=1,height=140)
        
        m1_lbl = Label(A6,text="Total Coffee Price",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_text = Entry(A6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2_lbl = Label(A6,text="Total Pizza Price",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m3_text = Entry(A6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        
        m3_lbl = Label(A6,text="Total Drinks Price",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_text = Entry(A6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        
        c1_lbl = Label(A6,text="Total Coffee Tax",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_text = Entry(A6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2_lbl = Label(A6,text="Total Pizza Tax",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_text = Entry(A6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
        
        c3_lbl = Label(A6,text="Total Drinks Tax",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_text = Entry(A6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        
        btn_F = Frame(A6,bd=7,relief=GROOVE)
        btn_F.place(x=710,width=650,height=95)
        
        total_btn = Button(btn_F,text="Total",bg="cadetblue",fg="white",pady=15,width=15,font="arial 13 bold").grid(row=0,column=0,padx=5,pady=5)
        generate_btn = Button(btn_F,text="Generate Bill",bg="cadetblue",fg="white",pady=13,width=15,font="arial 13 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn = Button(btn_F,text="Clear",bg="cadetblue",fg="white",pady=15,width=13,font="arial 13 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn = Button(btn_F,text="Exit",bg="cadetblue",fg="white",pady=15,width=13,font="arial 13 bold").grid(row=0,column=3,padx=5,pady=5)
        
        
        
        
        
        
root=Tk()
obj = Bill_App(root)
root.mainloop()