from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry

class User:
      def __init__(self,root):
          self.root=root
          self.root.geometry("1530x790+0+0")
          self.root.title('User Management system')

          # Variables     
          self.var_email=StringVar() 
          self.var_cut=StringVar()
          self.var_name=StringVar() 
          self.var_texture=StringVar()
          self.var_whatsapp=StringVar()
          self.var_volume=StringVar()
          self.var_dob=StringVar() 
          self.var_scalp=StringVar()
          self.var_placeofbirth=StringVar() 
          self.var_combinghair=StringVar()
          self.var_year=StringVar()
          self.var_heat=StringVar()
          self.var_colour=StringVar()
          self.var_hairtangle=StringVar()
          self.var_oil=StringVar()
          self.var_hairfall=StringVar()
          self.var_shampoo=StringVar()
          self.var_oilweek=StringVar()
          self.var_conditioner=StringVar()
          self.var_haircomb=StringVar()
          self.var_hairwash=StringVar()
          self.var_chemicaltreatment=StringVar()
          self.var_hairdry=StringVar()
          self.var_treatment=StringVar()

          lbl_title=Label(self.root,text='USER MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='darkblue',bg='white')
          lbl_title.place(x=0,y=0,width=1530,height=50)

          # logo
          img_logo=Image.open('user_images/1.png')
          img_logo=img_logo.resize((50,50),Image.LANCZOS)
          self.photo_logo=ImageTk.PhotoImage(img_logo)

          self.logo=Label(self.root,image=self.photo_logo)
          self.logo.place(x=350,y=0,width=50,height=50)

          # Image Frame
          img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
          img_frame.place(x=0,y=50,width=1530,height=160)
          
          # 1st
          img1=Image.open('user_images/2.png')
          img1=img1.resize((500,170),Image.LANCZOS)
          self.photo1=ImageTk.PhotoImage(img1)

          self.img_1=Label(self.root,image=self.photo1)
          self.img_1.place(x=0,y=50,width=500,height=170)

        # 2nd
          img_2=Image.open('user_images/3.jpeg')
          img_2=img_2.resize((480,170),Image.LANCZOS)
          self.photo2=ImageTk.PhotoImage(img_2)

          self.img_2=Label(self.root,image=self.photo2)
          self.img_2.place(x=500,y=50,width=480,height=170)
 

         # 3rd
          img_3=Image.open('user_images/4.jpeg')
          img_3=img_3.resize((520,170),Image.LANCZOS)
          self.photo_3=ImageTk.PhotoImage(img_3)

          self.img_3=Label(self.root,image=self.photo_3)
          self.img_3.place(x=900,y=50,width=520,height=170)

          # Main Frame
          Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
          Main_frame.place(x=10,y=220,width=1500,height=560)       
          
          # upper Frame
          upper_frame = Frame(Main_frame, bd=2, relief=RIDGE, bg='white')
          upper_frame.place(x=10, y=10, width=1480, height=270)
          lbl_emp_info = Label(upper_frame, text='User Information', font=('times new roman', 20, 'bold'), fg='red', bg='white')
          lbl_emp_info.grid()

          # # Create a canvas
          canvas = Canvas(upper_frame, bg='white')
          canvas.place(x=0, y=0, height=270, width=1000)

          # Add a scrollbar
          v_scrollbar = Scrollbar(upper_frame, orient=VERTICAL, command=canvas.yview)
          v_scrollbar.place(x = 1000, y=0, width=10, height=250)

          h_scrollbar = Scrollbar(upper_frame, orient=HORIZONTAL, command=canvas.xview)
          h_scrollbar.place(x=0, y=260, width=1000, height=20)

        # Configure the canvas to use the scrollbar
          canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Create a frame inside the canvas
          inner_frame = Frame(canvas, bg='white')
          canvas.create_window((0, 0), window=inner_frame, anchor='nw')

        # Function to update the scroll region
          def configure_scroll_region(event):
              canvas.configure(scrollregion=canvas.bbox("all"))

          inner_frame.bind("<Configure>", configure_scroll_region)

          # Email
          lbl_email = Label(inner_frame, font=("arial", 12, "bold"), text="Email:", bg="white")
          lbl_email.grid(row=1, column=0, sticky=W, padx=2, pady=7)
          txt_email = ttk.Entry(inner_frame,textvariable=self.var_email,width=22, font=('arial', 11, "bold"))
          txt_email.grid(row=1, column=1, padx=2, pady=7)

          #  Cut
          lbl_cut = Label(inner_frame, font=("arial", 12, "bold"), text="Have you ever cut your hair?", bg="white")
          lbl_cut.grid(row=1, column=2, sticky=W, padx=2, pady=7)
          combo_txt_cut=ttk.Combobox(inner_frame,state="readonly",
                                       font=('arial', 12, 'bold'), width=17)
          
          combo_txt_cut['value'] = ("select Yes or No", "yes","no")
          combo_txt_cut.current(0)
          combo_txt_cut.grid(row=1, column=3, padx=2, pady=10, sticky=W)
         
          # Name
          lbl_name = Label(inner_frame, text='Name', font=('arial', 11, 'bold'), bg='white')
          lbl_name.grid(row=2, column=0, padx=2, sticky=W)
          txt_name= ttk.Entry(inner_frame, textvariable=self.var_name, width=22, font=('arial', 11, "bold"))
          txt_name.grid(row=2, column=1, padx=2, pady=7)

          # texture
          lbl_texture = Label(inner_frame, font=("arial", 12, "bold"), text="what is the texture of your hair?", bg="white")
          lbl_texture.grid(row=2, column=2, sticky=W, padx=2, pady=7)
          combo_txt_texture=ttk.Combobox(inner_frame,state="readonly",
                                       font=('arial', 12, 'bold'), width=17)
          
          combo_txt_texture['value'] = ("select texture", "straight","wavy","curly")
          combo_txt_texture.current(0)
          combo_txt_texture.grid(row=2, column=3, padx=2, pady=10, sticky=W)

          # whatsapp
          lbl_whatsapp = Label(inner_frame, font=("arial", 12, "bold"), text="whatsapp:", bg="white")
          lbl_whatsapp.grid(row=3, column=0, sticky=W, padx=2, pady=7)
          txt_whatsapp = ttk.Entry(inner_frame,textvariable=self.var_whatsapp,width=22, font=('arial', 11, "bold"))
          txt_whatsapp.grid(row=3, column=1, padx=2, pady=7)

          # volume
          lbl_volume = Label(inner_frame, font=("arial", 12, "bold"), text="volume", bg="white")
          lbl_volume.grid(row=3, column=2, sticky=W, padx=2, pady=7)
          combo_txt_volume=ttk.Combobox(inner_frame,state="readonly",
                                       font=('arial', 12, 'bold'), width=17)
          
          combo_txt_volume['value'] = ("volume of your hair", "less","normal","good")
          combo_txt_volume.current(0)
          combo_txt_volume.grid(row=3, column=3, padx=2, pady=10, sticky=W)

          # DOB
          lbl_dob = Label(inner_frame, font=("arial", 12, "bold"), text="Date of Birth:", bg="white")
          lbl_dob.grid(row=4, column=0, sticky=W, padx=2, pady=7)

          txt_dob = DateEntry(inner_frame,textvariable=self.var_dob,width=22, font=('arial', 11, "bold"), date_pattern="dd/mm/yyyy")
          txt_dob.grid(row=4, column=1, padx=2, pady=7)

          # scalp
          lbl_scalp = Label(inner_frame, font=("arial", 12, "bold"), text="scalp", bg="white")
          lbl_scalp.grid(row=4, column=2, sticky=W, padx=2, pady=7)
          combo_txt_scalp=ttk.Combobox(inner_frame,state="readonly",
                                       font=('arial', 12, 'bold'), width=17)
          
          combo_txt_scalp['value'] = ("scalp", "normal","dry","oily")
          combo_txt_scalp.current(0)
          combo_txt_scalp.grid(row=4, column=3, padx=2, pady=10, sticky=W)

          # place of birth
          lbl_placeofbirth = Label(inner_frame, font=("arial", 12, "bold"), text="Place of birth:", bg="white")
          lbl_placeofbirth.grid(row=5, column=0, sticky=W, padx=2, pady=7)
          txt_placeofbirth = ttk.Entry(inner_frame,textvariable=self.var_placeofbirth,width=22, font=('arial', 11, "bold"))
          txt_placeofbirth.grid(row=5, column=1, padx=2, pady=7)

          # combing hair
          lbl_combinghair = Label(inner_frame, font=("arial", 12, "bold"), text="Direction of combing hair?", bg="white")
          lbl_combinghair.grid(row=5, column=2, sticky=W, padx=2, pady=7)
          combo_txt_combinghair=ttk.Combobox(inner_frame,state="readonly",
                                       font=('arial', 12, 'bold'), width=17)
          
          combo_txt_combinghair['value'] = ("roots to end", "end to roots")
          combo_txt_combinghair.current(0)
          combo_txt_combinghair.grid(row=5, column=3, padx=2, pady=10, sticky=W)

          # year
          lbl_year = Label(inner_frame, font=("arial", 12, "bold"), text="since how many years are you growing your hair?", bg="white")
          lbl_year.grid(row=6, column=0, sticky=W, padx=2, pady=7)
          txt_year = ttk.Entry(inner_frame,textvariable=self.var_year,width=22, font=('arial', 11, "bold"))
          txt_year.grid(row=6, column=1, padx=2, pady=7)

          # Heat style tool
          lbl_heat = Label(inner_frame, font=("arial", 12, "bold"), text="Use of any heat styling tool?", bg="white")
          lbl_heat.grid(row=6, column=2, sticky=W, padx=2, pady=7)
          combo_txt_heat=ttk.Combobox(inner_frame,state="readonly",
                                       font=('arial', 12, 'bold'), width=17)
          
          combo_txt_heat['value'] = ("Heat style tool", "yes", "no", "rarely")
          combo_txt_heat.current(0)
          combo_txt_heat.grid(row=6, column=3, padx=2, pady=10, sticky=W)
        
         # colour
          lbl_colour = Label(inner_frame, font=("arial", 12, "bold"), text="what is the colour of your hair?", bg="white")
          lbl_colour.grid(row=7, column=0, sticky=W, padx=2, pady=7)
          txt_colour = ttk.Entry(inner_frame,textvariable=self.var_colour,width=22, font=('arial', 11, "bold"))
          txt_colour.grid(row=7, column=1, padx=2, pady=7)

          # hair tangle
          lbl_hairtangle = Label(inner_frame, font=("arial", 12, "bold"), text="hair tangle?", bg="white")
          lbl_hairtangle.grid(row=7, column=2, sticky=W, padx=2, pady=7)
          combo_txt_hairtangle=ttk.Combobox(inner_frame,state="readonly",
                                       font=('arial', 12, 'bold'), width=17)
          
          combo_txt_hairtangle['value'] = ("select hair tangle", "no","yes")
          combo_txt_hairtangle.current(0)
          combo_txt_hairtangle.grid(row=7, column=3, padx=2, pady=10, sticky=W)

          # Oil
          lbl_oil = Label(inner_frame, font=("arial", 12, "bold"), text="which oil do you use?", bg="white")
          lbl_oil.grid(row=8, column=0, sticky=W, padx=2, pady=7)
          txt_oil = ttk.Entry(inner_frame,textvariable=self.var_oil,width=22, font=('arial', 11, "bold"))
          txt_oil.grid(row=8, column=1, padx=2, pady=7)
        
         # hair fall
          lbl_hairfall = Label(inner_frame, font=("arial", 12, "bold"), text="hair fall?", bg="white")
          lbl_hairfall.grid(row=8, column=2, sticky=W, padx=2, pady=7)
          combo_txt_hairfall=ttk.Combobox(inner_frame,state="readonly",
                                       font=('arial', 12, 'bold'), width=17)
          
          combo_txt_hairfall['value'] = ("select hair fall", "no","yes","normal")
          combo_txt_hairfall.current(0)
          combo_txt_hairfall.grid(row=8, column=3, padx=2, pady=10, sticky=W)

          # shampoo
          lbl_shampoo = Label(inner_frame, font=("arial", 12, "bold"), text="which shampoo do you use?", bg="white")
          lbl_shampoo.grid(row=9, column=0, sticky=W, padx=2, pady=7)
          txt_shampoo = ttk.Entry(inner_frame,textvariable=self.var_shampoo,width=22, font=('arial', 11, "bold"))
          txt_shampoo.grid(row=9, column=1, padx=2, pady=7)

          # oil week
          lbl_oilweek = Label(inner_frame, font=("arial", 12, "bold"), text="how many times in week do you oil your hair?", bg="white")
          lbl_oilweek.grid(row=9, column=2, sticky=W, padx=2, pady=7)
          txt_oilweek = ttk.Entry(inner_frame,textvariable=self.var_oilweek,width=22, font=('arial', 11, "bold"))
          txt_oilweek.grid(row=9, column=3, padx=2, pady=7)

          # conditioner
          lbl_conditioner = Label(inner_frame, font=("arial", 12, "bold"), text="which conditioner do you use?", bg="white")
          lbl_conditioner.grid(row=10, column=0, sticky=W, padx=2, pady=7)
          txt_conditioner = ttk.Entry(inner_frame,textvariable=self.var_conditioner,width=22, font=('arial', 11, "bold"))
          txt_conditioner.grid(row=10, column=1, padx=2, pady=7)

          # haircomb
          lbl_haircomb = Label(inner_frame, font=("arial", 12, "bold"), text="how many times in a day do you comb your hair?", bg="white")
          lbl_haircomb.grid(row=10, column=2, sticky=W, padx=2, pady=7)    
          txt_haircomb = ttk.Entry(inner_frame,textvariable=self.var_haircomb,width=22, font=('arial', 11, "bold"))
          txt_haircomb.grid(row=10, column=3, padx=2, pady=7)

          # hair wash
          lbl_hairwash = Label(inner_frame, font=("arial", 12, "bold"), text="how many times in week do you wash your hair?", bg="white")
          lbl_hairwash.grid(row=11, column=0, sticky=W, padx=2, pady=7)
          txt_hairwash = ttk.Entry(inner_frame,textvariable=self.var_hairwash,width=22, font=('arial', 11, "bold"))
          txt_hairwash.grid(row=11, column=1, padx=2, pady=7)
         
          # chemical treatment
          lbl_chemicaltreatment = Label(inner_frame, font=("arial", 12, "bold"), text="chemical treatment?", bg="white")
          lbl_chemicaltreatment.grid(row=11, column=2, sticky=W, padx=2, pady=7)
          combo_txt_chemicaltreatment=ttk.Combobox(inner_frame,state="readonly",
                                       font=('arial', 12, 'bold'), width=17)
          
          combo_txt_chemicaltreatment['value'] = ("select chemical treatment", "no","yes")
          combo_txt_chemicaltreatment.current(0)
          combo_txt_chemicaltreatment.grid(row=11, column=3, padx=2, pady=10, sticky=W)

          # hair dry
          lbl_hairdry = Label(inner_frame, font=("arial", 12, "bold"), text="how much time it takes for your hair to dry?", bg="white")
          lbl_hairdry.grid(row=12, column=0, sticky=W, padx=2, pady=7)
          txt_hairdry = ttk.Entry(inner_frame,textvariable=self.var_hairdry,width=22, font=('arial', 11, "bold"))
          txt_hairdry.grid(row=12, column=1, padx=2, pady=7)
         
          # treatment
          lbl_treatement = Label(inner_frame, font=("arial", 12, "bold"), text="which chemical treatment had you done?", bg="white")
          lbl_treatement.grid(row=12, column=2, sticky=W, padx=2, pady=7)
          txt_treatement = ttk.Entry(inner_frame,textvariable=self.var_treatment,width=22, font=('arial', 11, "bold"))
          txt_treatement.grid(row=12, column=3, padx=2, pady=7)

          # down Frame
          down_frame = Frame(Main_frame, bd=2, relief=RIDGE, bg='white')
          down_frame.place(x=10, y=280, width=1480, height=270)
          lbl_emp_table = Label(down_frame, text='User Information Table', font=('times new roman', 20, 'bold'), fg='red', bg='white')
          lbl_emp_table.grid()  
          
           # search Frame
          search_frame=Frame(down_frame,bd=2,relief=RIDGE,bg='white')
          search_frame.place(x=0,y=30,width=1470,height=60)     

          search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",fg="white", bg="black")
          search_by.grid(row=0,column=0,sticky=W,padx=5)

          # search
          self.var_com_search=StringVar()
          com_txt_search=ttk.Combobox(search_frame,state="readonly",
                                                           font=("arial",12,"bold"),width=2)
          com_txt_search['value']=("select option","phone","id_proof")
          com_txt_search.current(0)
          com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

          self.var_search=StringVar()
          txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
          txt_search.grid(row=0,column=2,padx=5)

          btn_search=Button(search_frame,text="search",command=self.search_data,font=("arial",11,"bold"),width=14,bg='blue',fg='white')
          btn_search.grid(row=0,column=3,padx=1,pady=5)
          
          btn_ShowAll=Button(search_frame,text="Show All",font=("arial",11,"bold"),width=14,bg='blue',fg='white')
          btn_ShowAll.grid(row=0,column=4,padx=5)

          stayhome=Label(search_frame,text="wear a mask",font=("times new roman",30,"bold"),width=14,bg='yellow',fg='red')
          stayhome.place(x=780,y=0,width=600,height=55)

          img_logo=mask=Image.open('user_images/1.png')
          img_logo=mask=img_logo.resize((50,50),Image.LANCZOS)
          self.photoimg_logo_mask=ImageTk.PhotoImage(img_logo)
                                                    
          self.logo=Label(search_frame,image=self.photoimg_logo_mask)
          self.logo.place(x=900,y=0,width=50,height=50)
         
          # mask image
          img_mask=Image.open('user_images/mask.jpg')
          img_mask=img_mask.resize((150,220),Image.LANCZOS)
          self.photomask=ImageTk.PhotoImage(img_mask)

          self.img_mask=Label(upper_frame,image=self.photomask)
          self.img_mask.place(x=1030,y=20,width=150,height=200)

          # Button Frame
          button_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
          button_frame.place(x=1200,y=250,width=300,height=200)     
          
          btn_add=Button(button_frame,text="Save",command=self.add_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
          btn_add.grid(row=0,column=0,padx=1,pady=5)
          
          btn_update=Button(button_frame,text="Update",command=self.update_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
          btn_update.grid(row=1,column=0,padx=1,pady=5)
          
          btn_delete=Button(button_frame,text="delete",command=self.delete_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
          btn_delete.grid(row=2,column=0,padx=1,pady=5)
          
          btn_clear=Button(button_frame,text="clear",command=self.reset_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
          btn_clear.grid(row=3,column=0,padx=1,pady=5)

          # =================Emloyee table===========================
          # Table frame
          table_frame=Frame(down_frame,bd=3,relief=RIDGE,bg='white')
          table_frame.place(x=0,y=90,width=1330,height=100)       
          
          Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
          Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

          self.user_table=ttk.Treeview(table_frame,column=("email","cut","name","texture","whatsapp","volume","dob","scalp","place of birth","combing hair","year","heat","colour","hair tangle","oil","hairfall","shampoo","oil week","conditioner", "hair comb", "hair wash", "chemical treatment", "hair dry", "treatment"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

          Scroll_x.pack(side=BOTTOM,fill=X)
          Scroll_y.pack(side=RIGHT,fill=Y)

          Scroll_x.config(command=self.user_table.xview)
          Scroll_y.config(command=self.user_table.yview)

          self.user_table.heading('email',text='Email')
          self.user_table.heading('cut',text='cut')
          self.user_table.heading('name',text='name')
          self.user_table.heading('texture',text='texture')
          self.user_table.heading('whatsapp',text='whatsapp')
          self.user_table.heading('volume',text='volume')
          self.user_table.heading('dob',text='Dob')
          self.user_table.heading('scalp',text='scalp')
          self.user_table.heading('place of birth',text='place of birth')
          self.user_table.heading('combing hair',text='combing hair')
          self.user_table.heading('year',text='year')
          self.user_table.heading('heat',text='heat')
          self.user_table.heading('colour',text='colour')
          self.user_table.heading('hair tangle',text='hair tangle')
          self.user_table.heading('oil',text='oil')
          self.user_table.heading('hairfall',text='hair fall')
          self.user_table.heading('shampoo',text='shampoo')
          self.user_table.heading('oil week',text='oilweek')
          self.user_table.heading('conditioner',text='conditioner')
          self.user_table.heading('hair comb',text='haircomb')
          self.user_table.heading('hair wash',text='hairwash')
          self.user_table.heading('chemical treatment',text='chemical treatment')
          self.user_table.heading('hair dry',text='hair dry')
          self.user_table.heading('treatment',text='treatment')

          
          self.user_table['show']='headings'

          self.user_table.column("email",width=100)
          self.user_table.column("cut",width=100)
          self.user_table.column("name",width=100)
          self.user_table.column("texture",width=100)
          self.user_table.column("whatsapp",width=100)
          self.user_table.column("volume",width=100)
          self.user_table.column("dob",width=100)
          self.user_table.column("scalp",width=100)
          self.user_table.column("place of birth",width=100)
          self.user_table.column("combing hair",width=100)
          self.user_table.column("year",width=100)
          self.user_table.column("heat",width=100)
          self.user_table.column("colour",width=100)
          self.user_table.column("hair tangle",width=100)
          self.user_table.column("oil",width=100)
          self.user_table.column("hairfall",width=100)
          self.user_table.column("shampoo",width=100)
          self.user_table.column("oil week",width=100)
          self.user_table.column("conditioner",width=100)
          self.user_table.column("hair comb",width=100)
          self.user_table.column("hair wash",width=100)
          self.user_table.column("chemical treatment",width=100)
          self.user_table.column("hair dry",width=100)
          self.user_table.column("treatment",width=100)

          self.user_table.pack(fill=BOTH,expand=1)
          self.user_table.bind("<ButtonRelease>",self.get_cursor)

          self.fetch_data()
          
          # **************function Declarations*************

      def add_data(self):
        if self.var_name.get()==""or self.var_email.get()=="":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
              conn=mysql.connector.connect(host='localhost',user='root',password='H@irCo@cti0n',database='user')
              my_cursor=conn.cursor()
              whatsapp_value = int(self.var_whatsapp.get())
              my_cursor.execute('INSERT INTO user (email, name, texture, whatsapp, volume, dob, scalp, placeofbirth, combinghair, year, cut, heat, colour, hairtangle, oil, hairfall, shampoo, oilweek, conditioner, haircomb, hairwash, chemicaltreatment, hairdry, treatment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
                                   
                                                                                        self.var_email.get(), 
                                                                                        self.var_name.get(), 
                                                                                        self.var_texture.get(),
                                                                                        whatsapp_value, 
                                                                                        self.var_volume.get(),
                                                                                        self.var_dob.get(), 
                                                                                        self.var_scalp.get(),
                                                                                        self.var_placeofbirth.get(), 
                                                                                        self.var_combinghair.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_cut.get(),
                                                                                        self.var_heat.get(),
                                                                                        self.var_colour.get(),
                                                                                        self.var_hairtangle.get(),
                                                                                        self.var_oil.get(),
                                                                                        self.var_hairfall.get(),
                                                                                        self.var_shampoo.get(),
                                                                                        self.var_oilweek.get(),
                                                                                        self.var_conditioner.get(),
                                                                                        self.var_haircomb.get(),
                                                                                        self.var_hairwash.get(),
                                                                                        self.var_chemicaltreatment.get(),
                                                                                        self.var_hairdry.get(),
                                                                                        self.var_treatment.get()                                        
                         ))
                                                                                                                                                                                                                                    
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo('Success','user has been added!',parent=self.root)
            except Exception as es:
              messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

      # fetch data
      def fetch_data(self):
              conn=mysql.connector.connect(host='localhost',user='root',password='H@irCo@cti0n',database='user')
              my_cursor=conn.cursor()
              my_cursor.execute('select * from user')
              data=my_cursor.fetchall()
              if len(data)!=0:
                  self.user_table.delete(*self.user_table.get_children())
                  for i in data:
                      self.user_table.insert("",END,values=i)
                  conn.commit()
              conn.close()

        # Get cursor

      def get_cursor(self, event=""):
          cursor_row=self.user_table.focus()
          content=self.user_table.item(cursor_row)
          data = content['values']

          self.var_email.set(data[0]) 
          self.var_name.set(data[1]) 
          self.var_texture.set(data[2])
          self.var_whatsapp.set(data[3]) 
          self.var_volume.set(data[4])
          self.var_dob.set(data[5]) 
          self.var_scalp.set(data[6])
          self.var_placeofbirth.set(data[7]) 
          self.var_combinghair.set(data[8])
          self.var_year.set(data[9])
          self.var_cut.set(data[10])
          self.var_heat.set(data[11])
          self.var_colour.set(data[12])
          self.var_hairtangle.set(data[13])
          self.var_oil.set(data[14])
          self.var_hairfall.set(data[15])
          self.var_shampoo.set(data[16])
          self.var_oilweek.set(data[17])
          self.var_conditioner.set(data[18])
          self.var_haircomb.set(data[19])
          self.var_hairwash.set(data[20])
          self.var_chemicaltreatment.set(data[21])
          self.var_hairdry.set(data[22])
          self.var_treatment.set(data[23])    
          
      def update_data(self):
        if self.var_name.get() == "" or self.var_email.get() == "":
          messagebox.showerror('Error', 'All fields are required')
        else:
          try:
            update = messagebox.askyesno('Update', 'Are you sure you want to update this user data?')
            if update > 0:
                conn = mysql.connector.connect(host='localhost', user='root', password='H@irCo@cti0n', database='user')
                my_cursor = conn.cursor()
                my_cursor.execute('UPDATE user SET Name=%s, place of birth=%s, whatsapp=%s, Email=%s, Address=%s, Dob=%s,phone=%s,cut=%s,year=%s,colour=%s,oil=%s,oilweek=%s,hairwash=%s,shampoo=%s,haircomb=%s,treatment=%s,conditioner=%s,hairdry=%s', (
                    self.var_email.get(), 
                    self.var_name.get(), 
                    self.var_texture.get(),
                    self.var_whatsapp.get(), 
                    self.var_volume.get(),
                    self.var_dob.get(), 
                    self.var_scalp.get(),
                    self.var_placeofbirth.get(), 
                    self.var_combinghair.get(),
                    self.var_year.get(),
                    self.var_cut.get(),
                    self.var_heat.get(),
                    self.var_colour.get(),
                    self.var_hairtangle.get(),
                    self.var_oil.get(),
                    self.var_hairfall.get(),
                    self.var_shampoo.get(),
                    self.var_oilweek.get(),
                    self.var_conditioner.get(),
                    self.var_haircomb.get(),
                    self.var_hairwash.get(),
                    self.var_chemicaltreatment.get(),
                    self.var_hairdry.get(),
                    self.var_treatment.get()  
                ))
            else:
                if not update:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Success', 'user data successfully updated', parent=self.root)
          except Exception as es:
            messagebox.showerror('Error', f'Due to {str(es)}', parent=self.root)

      # Delete
      def delete_data(self):
        if self.var_name.get() == "":
          messagebox.showerror('Error', 'Please enter name to delete')
        else:
          try:
            delete = messagebox.askyesno('Delete', 'Are you sure you want to delete this user?', parent=self.root)
            if delete > 0:
                conn = mysql.connector.connect(host='localhost', user='root', password='H@irCo@cti0n', database='user')
                my_cursor = conn.cursor()
                sql = 'DELETE FROM user WHERE name=%s'
                value = (self.var_name.get(),)
                my_cursor.execute(sql, value)
            else:
                if not delete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Deleted', 'user data deleted successfully', parent=self.root)
          except Exception as es:
            messagebox.showerror('Error', f'Due to {str(es)}', parent=self.root)

   # reset

      def reset_data(self):
          self.var_email.set("")
          self.var_cut.set("")
          self.var_name.set("")
          self.var_texture.set("")
          self.var_whatsapp.set("")
          self.var_volume.set("")
          self.var_dob.set("")
          self.var_scalp.set(""),
          self.var_placeofbirth.set(""),
          self.var_combinghair.set(""),
          self.var_year.set(""),
          self.var_heat.set(""),
          self.var_colour.set(""),
          self.var_hairtangle.set(""),
          self.var_oil.set(""),
          self.var_hairfall.set(""),
          self.var_shampoo.set(""),
          self.var_oilweek.set(""),      
          self.var_conditioner.set(""),
          self.var_haircomb.set(""),
          self.var_hairwash.set(""),
          self.var_chemicaltreatment.set(""),
          self.var_hairdry.set(""),
          self.var_treatment.set("")
          
      
   # search
      def search_data(self):
        if self.var_com_search.get() == '' or self.var_search.get() == '':
          messagebox.showerror('Error', 'Please select an option to search')
        else:
          try:
            conn = mysql.connector.connect(host='localhost', user='root', password='H@irCo@ctiOn', database='user')
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM user WHERE " + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.user_table.delete(*self.user_table.get_children())
                for i in rows:
                    self.user_table.insert("", END, values=i)
                conn.commit()
                conn.close()
          except Exception as es:
            messagebox.showerror('Error', f'Due to {str(es)}', parent=self.root)

if __name__ == "__main__":
     root=Tk()
     obj = User(root)
     root.mainloop()