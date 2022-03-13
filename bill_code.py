#CODE WRITTEN BY VINAYAK NAGAR

from tkinter import*
import math,random,os
from tkinter import messagebox
class bill_app:
      def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        #...............variable....................
        #...............cosmetic...................
        self.soap=IntVar()
        self.face_soap=IntVar()
        self.face_wash=IntVar()
        self.face_creem=IntVar()
        self.hair_wash=IntVar()
        self.hair_creem=IntVar()
        
                #...............Grocery...................
        self.suger=IntVar()
        self.daal=IntVar()
        self.tea=IntVar()
        self.wheat=IntVar()
        self.coffee=IntVar()
        self.salt=IntVar()
        
                #...............Cold Drink...................
        self.maza=IntVar()
        self.coca_cola=IntVar()
        self.papasi=IntVar()
        self.red_bull=IntVar()
        self.limca=IntVar()
        self.frooti=IntVar()
        
                #...............Total Product price & Tax variable ...................
        self.cos_price=StringVar()
        self.gro_price=StringVar()
        self.cold_price=StringVar()
        
        self.cos_tax=StringVar()
        self.gro_tax=StringVar()
        self.cold_tax=StringVar()
        
        
                #...............Customer...................
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        
        
        #.................Customer Details Frame.......................
        f1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        f1.place(x=0,y=80,relwidth=1 )
        
        Cname=Label(f1,text="Customer Name:",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        Cname_text=Entry(f1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        Cphone=Label(f1,text="Phone Number:",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        C_phone=Entry(f1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        Cbill=Label(f1,text="Bill Number:",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        C_bill=Entry(f1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn=Button(f1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)
        
        #..............cosmetics frame............................
        f2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        f2.place(x=5,y=180,width=325,height=380)
       
        bath=Label(f2,text="Bath Shop:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_text=Entry(f2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        face=Label(f2,text="Face Shop:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_text=Entry(f2,width=10,textvariable=self.face_soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        facew=Label(f2,text="Face Wash:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        facew_text=Entry(f2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
       
        facec=Label(f2,text="Face Creem:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        facec_text=Entry(f2,width=10,textvariable=self.face_creem,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        hairw=Label(f2,text="Hair Wash:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hairw_text=Entry(f2,width=10,textvariable=self.hair_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        hairc=Label(f2,text="Hair Creem:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        hairc_text=Entry(f2,width=10,textvariable=self.hair_creem,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        
        
        #..............Grocery frame............................
        f3=LabelFrame(self.root,text="Grocery",bd=10,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        f3.place(x=340,y=180,width=325,height=380)
       
        suger=Label(f3,text="Suger:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        suger_text=Entry(f3,width=10,textvariable=self.suger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        daal=Label(f3,text="Daal:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        daal_text=Entry(f3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        tea=Label(f3,text="Tea:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        tea_text=Entry(f3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
       
        wheat=Label(f3,text="wheat:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        wheat_text=Entry(f3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        coffee=Label(f3,text="Coffee:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        coffee_text=Entry(f3,width=10,textvariable=self.coffee,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        salt=Label(f3,text="Salt:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        salt_text=Entry(f3,width=10,textvariable=self.salt,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        
         
        
        #..............Cold Drink frame............................
        f4=LabelFrame(self.root,text="Cold Drink",bd=10,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        f4.place(x=670,y=180,width=325,height=380)
       
        maza=Label(f4,text="Maza:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        maza_text=Entry(f4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        coca=Label(f4,text="Coca Cola:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coca_text=Entry(f4,width=10,textvariable=self.coca_cola,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
        
        papasi=Label(f4,text="Papasi:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        papasi_text=Entry(f4,width=10,textvariable=self.papasi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
       
        redbull=Label(f4,text="Red Bull:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        redbull_text=Entry(f4,width=10,textvariable=self.red_bull,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
        
        limca=Label(f4,text="Limca:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        limca_text=Entry(f4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
        
        frooti=Label(f4,text="Frooti:",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        frooti_text=Entry(f4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
        
        #..................Bill Area................
        f5=Frame(self.root,bd=10,relief=GROOVE)
        f5.place(x=1010,y=180,width=350,height=380)
       
        bill_title=Label(f5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #....................Button Frame..................
        f6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        f6.place(x=0,y=560,relwidth=1,height=140)
        
        b1=Label(f6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        b1_text=Entry(f6,width=18,textvariable=self.cos_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        b2=Label(f6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        b2_text=Entry(f6,width=18,textvariable=self.gro_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        
        b3=Label(f6,text="Total Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        b3_text=Entry(f6,width=18,textvariable=self.cold_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1=Label(f6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_text=Entry(f6,width=18,textvariable=self.cos_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2=Label(f6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_text=Entry(f6,width=18,textvariable=self.gro_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
        
        c3=Label(f6,text="Cold Drink Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_text=Entry(f6,width=18,textvariable=self.cold_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        
        btn_f=Frame(f6,bd=7,relief=GROOVE)
        btn_f.place(x=740,width=585,height=105)
        
        total_btn=Button(btn_f,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,width=11,font="arial 12 bold",bd=5).grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_f,command=self.bill_aera,text="Generate Bill",bg="cadetblue",fg="white",pady=15,width=11,font="arial 12 bold",bd=5).grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,command=self.clear_data,text="Clear",bg="cadetblue",fg="white",pady=15,width=11,font="arial 12 bold",bd=5).grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_f,text="Exit",command=self.exit_app,bg="cadetblue",fg="white",pady=15,width=11,font="arial 12 bold",bd=5).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
        
        #.......................Function.........................
      def total(self):    
          self.c_s_p=self.soap.get()*40
          self.c_f_s_p=self.face_soap.get()*120
          self.c_f_w_p=self.face_wash.get()*60
          self.c_f_c_p=self.face_creem.get()*40
          self.c_h_w_p=self.hair_wash.get()*40
          self.c_h_c_p=self.hair_creem.get()*40
          self.total_cos_price=float(
                                    self.c_s_p+
                                    self.c_f_s_p+
                                    self.c_f_w_p+
                                    self.c_f_c_p+
                                    self.c_f_c_p+
                                    self.c_h_w_p+
                                    self.c_h_c_p
                                    )
          self.cos_price.set("Rs. "+str(self.total_cos_price))
          self.c_tax=self.total_cos_price*0.05
          self.cos_tax.set("Rs. "+str(self.c_tax))
          
          
          self.g_s=self.suger.get()*120
          self.g_d=self.daal.get()*120
          self.g_t=self.tea.get()*60
          self.g_w=self.wheat.get()*40
          self.g_c=self.coffee.get()*40
          self.g_sa=self.salt.get()*40
          self.total_gro_price=float(
                            self.g_s+
                            self.g_d+
                            self.g_t+
                            self.g_w+
                            self.g_c+
                            self.g_sa
                            )
          self.gro_price.set("Rs. "+str(self.total_gro_price))
          self.g_tax=self.total_gro_price*0.05
          self.gro_tax.set("Rs. "+str(self.g_tax))
        
        
          self.c_m=self.maza.get()*120
          self.c_c=self.coca_cola.get()*120
          self.c_p=self.papasi.get()*60
          self.c_r=self.red_bull.get()*40
          self.c_l=self.limca.get()*40
          self.c_f=self.frooti.get()*40
                                    
          self.total_cold_price=float(
                                    
                                self.c_m+
                                self.c_c+
                                self.c_p+
                                self.c_r+
                                self.c_l+
                                self.c_f
                                    )
          self.cold_price.set("Rs. "+str(self.total_cold_price))
          self.co_tax=self.total_cold_price*0.10
          self.cold_tax.set("Rs. "+str(self.co_tax))
          
          self.total_bill=float(self.total_cos_price+
                                self.total_gro_price+
                                self.total_cold_price+
                                self.c_tax+
                                self.g_tax+
                                self.co_tax
                                )
          
      def welcome_bill(self):
              self.txtarea.delete('1.0',END)
              self.txtarea.insert(END,"\tWelcome Home Reatil Shop")
    
              self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
    
              self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
    
              self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
              
              self.txtarea.insert(END,f"\n *************************************")
              self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
              self.txtarea.insert(END,f"\n *************************************")
     
      def bill_aera(self):
          
          if self.c_name.get()=="" or self.c_phone.get()=="":
              messagebox.showerror("Error","Customer Details Are Must")
          elif self.cos_price.get()=="Rs. 0.0" and self.gro_price.get()=="Rs. 0.0" and self.cold_price.get()=="Rs. 0.0" :
              messagebox.showerror("Error","No product Purchased")
          else:
              
              self.welcome_bill()
              #......................Cosmetic.....................
              
              if self.soap.get()!=0:
                  self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
              if self.face_soap.get()!=0:
                  self.txtarea.insert(END,f"\n Face Soap\t\t{self.face_soap.get()}\t\t{self.c_f_s_p}")
              if self.face_wash.get()!=0:
                  self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_f_w_p}")
              if self.face_creem.get()!=0:
                  self.txtarea.insert(END,f"\n Face Creem\t\t{self.face_creem.get()}\t\t{self.c_f_c_p}")
              if self.hair_wash.get()!=0:
                  self.txtarea.insert(END,f"\n Hair Wash\t\t{self.hair_wash.get()}\t\t{self.c_h_w_p}")
              if self.hair_creem.get()!=0:
                  self.txtarea.insert(END,f"\n Hair Creem\t\t{self.hair_creem.get()}\t\t{self.c_h_c_p}")
                
              #......................Grocery.....................
              
              if self.suger.get()!=0:
                  self.txtarea.insert(END,f"\n Suger\t\t\t{self.suger.get()}\t\t{self.g_s}")
              if self.daal.get()!=0:
                  self.txtarea.insert(END,f"\n Daal\t\t\t{self.daal.get()}\t\t{self.g_d}")
              if self.tea.get()!=0:
                  self.txtarea.insert(END,f"\n Tea\t\t\t{self.tea.get()}\t\t{self.g_t}")
              if self.wheat.get()!=0:
                  self.txtarea.insert(END,f"\n Wheat\t\t\t{self.wheat.get()}\t\t{self.g_w}")
              if self.coffee.get()!=0:
                  self.txtarea.insert(END,f"\n Coffee\t\t\t{self.coffee.get()}\t\t{self.g_c}")
              if self.salt.get()!=0:
                  self.txtarea.insert(END,f"\n Salt\t\t\t{self.salt.get()}\t\t{self.g_sa}")
              
              #......................Cold Drink.....................
              
              if self.maza.get()!=0:
                  self.txtarea.insert(END,f"\n Maza\t\t\t{self.maza.get()}\t\t{self.c_m}")
              if self.coca_cola.get()!=0:
                  self.txtarea.insert(END,f"\n Coca_Cola\t\t{self.coca_cola.get()}\t\t{self.c_c}")
              if self.papasi.get()!=0:
                  self.txtarea.insert(END,f"\n Papasi\t\t\t{self.papasi.get()}\t\t{self.c_p}")
              if self.red_bull.get()!=0:
                  self.txtarea.insert(END,f"\n Red Bull\t\t{self.red_bull.get()}\t\t{self.c_r}")
              if self.limca.get()!=0:
                  self.txtarea.insert(END,f"\n Limca\t\t\t{self.limca.get()}\t\t{self.c_l}")
              if self.frooti.get()!=0:
                  self.txtarea.insert(END,f"\n Frooti\t\t\t{self.frooti.get()}\t\t{self.c_f}")
                  
              self.txtarea.insert(END,f"\n *************************************")
              if self.cos_tax.get()!="Rs. 0.0":
                  self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cos_tax.get()}")
          
              if self.gro_tax.get()!="Rs. 0.0":
                  self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.gro_tax.get()}")
            
              if self.cold_tax.get()!="Rs. 0.0":
                  self.txtarea.insert(END,f"\n Cold Drink Tax\t\t\t{self.cold_tax.get()}")
    
              self.txtarea.insert(END,f"\n Total Bill Is : \t\t\tRs. {self.total_bill}")
              self.txtarea.insert(END,f"\n *************************************")
              self.save_bill()
          
      def save_bill(self):
           op=messagebox.askyesno("Save Bill","Do You Want To Save Bill?")
           if op>0:
               self.bill_data=self.txtarea.get('1.0',END)
               f1=open("bills/"+str(self.bill_no.get())+".txt","w")
               f1.write(self.bill_data)
               f1.close()
               messagebox.showinfo("Saved",f"Bill No. : {self.bill_no.get()} Bill Saved Successfully.")
           else:
               return
      
      def find_bill(self):
          present="no"
          for i in os.listdir("bills/"):
              if i.split('.')[0]==self.search_bill.get():
                  f1=open(f"bills/{i}","r")
                  self.txtarea.delete("1.0",END)
                  for d in f1:
                      self.txtarea.insert(END,d)
                  f1.close;
                  present="yes"
          if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
         
      def clear_data(self):
        op=messagebox.askyesno("Exit","Do You Want To Clear All The Data?")
        if op>0:
                
            self.soap.set(0)
            self.face_soap.set(0)
            self.face_wash.set(0)
            self.face_creem.set(0)
            self.hair_wash.set(0)
            self.hair_creem.set(0)
            
                    #...............Grocery...................
            self.suger.set(0)
            self.daal.set(0)
            self.tea.set(0)
            self.wheat.set(0)
            self.coffee.set(0)
            self.salt.set(0)
            
                    #...............Cold Drink...................
            self.maza.set(0)
            self.coca_cola.set(0)
            self.papasi.set(0)
            self.red_bull.set(0)
            self.limca.set(0)
            self.frooti.set(0)
            
                    #...............Total Product price & Tax variable ...................
            self.cos_price.set("")
            self.gro_price.set("")
            self.cold_price.set("")
            
            self.cos_tax.set("")
            self.gro_tax.set("")
            self.cold_tax.set("")
            
            
                    #...............Customer...................
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            
            self.welcome_bill()
       
      def exit_app(self):
          op=messagebox.askyesno("Exit","Do You Want To Exit?")
          if op>0:
              self.root.destroy()
              
root=Tk()
obj=bill_app(root)
root.mainloop()
