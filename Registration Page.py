from tkinter import *

root = Tk()


    


root.geometry("800x800")


root.title('Registration Form')

label_0 =Label(root,text="Registration Form", width=20,font=("bold",20))


label_0.place(x=90,y=60)


label_1 =Label(root,text="Full Name", width=20,font=("bold",10))
label_1.place(x=80,y=130)

entry_1=Entry(root)
entry_1.place(x=240,y=130)


label_3 =Label(root,text="Email", width=20,font=("bold",10))
label_3.place(x=68,y=180)

entry_3=Entry(root)
entry_3.place(x=240,y=180)


label_4 =Label(root,text="Gender", width=20,font=("bold",10))
label_4.place(x=70,y=230)


var=IntVar()


Radiobutton(root,text="Male",padx= 5, variable= var, value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx= 20, variable= var, value=2).place(x=290,y=230)

 


list_of_state=['AP|Andhra Pradesh',
'AR|Arunachal Pradesh',
'AS|Assam',
'BR|Bihar',
'CT|Chhattisgarh',
'GA|Goa',
'GJ|Gujarat',
'HR|Haryana',
'HP|Himachal Pradesh',
'JK|Jammu & Kashmir',
'JH|Jharkhand',
'KA|Karnataka',
'KL|Kerala',
'MP|Madhya Pradesh',
'MH|Maharashtra',
'MN|Manipur',
'ML|Meghalaya',
'MZ|Mizoram',
'NL|Nagaland',
'OR|Odisha',
'PB|Punjab',
'RJ|Rajasthan',
'SK|Sikkim',
'TN|Tamil Nadu',
'TG|Telangana',
'TR|Tripura',
'UT|Uttarakhand',
'UP|Uttar Pradesh',
'WB|West Bengal',
'AN|Andaman and Nicobar Islands',
'CH|Chandigarh',
'DN|Dadra and Nagar Haveli',
'DD|Daman and Diu',
'DL|Delhi',
'LD|Lakshadweep',
'PY|Puducherry'
 ]
label_5=Label(root,text="State",width=20,font=("bold",10))
label_5.place(x=70,y=280)

c=StringVar()
droplist=OptionMenu(root,c, *list_of_state)
droplist.config(width=15)
c.set('Please select')
droplist.place(x=240,y=280)






label_6=Label(root,text="Language",width=20,font=('bold',10))
label_6.place(x=75,y=330)



var1=IntVar()

Checkbutton(root,text="English", variable=var1).place(x=230,y=330)




Button(root, text='Submit' , width=20,bg="black",fg='white').place(x=180,y=380)



root.mainloop()
