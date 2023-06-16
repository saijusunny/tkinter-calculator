from tkinter import *   
from tkinter import messagebox
top = Tk()  
top.geometry("310x440")  
top.title('Calculator')
top.configure(bg='#696969')

def btn_click(item):
    global exp
    exp=exp+str(item)
    txt.set(exp)
def clear():
    global exp
    exp=""
    txt.set(exp)
def equal():
    global exp
    if(exp==""):
        txt.set("Invalid expression!")   
    result=str(eval(exp))
    txt.set(result)
    exp=""

exp=""
txt=StringVar()

e1=Entry(top,textvariable=txt,width=46,bg='#424242',fg='white').grid(row=0,column=0,columnspan=4,pady=30,padx=7,ipady=15)

b1=Button(top,text='1',height=3,width=7,command=lambda: btn_click(1),fg='white',bg='#424242').grid(row=1,column=0,pady=6,padx=7)
b1=Button(top,text='2',height=3,width=7,command=lambda: btn_click(2),fg='white',bg='#424242').grid(row=1,column=1,pady=6,padx=7)
b1=Button(top,text='3',height=3,width=7,command=lambda: btn_click(3),fg='white',bg='#424242').grid(row=1,column=2,pady=6,padx=7)
b1=Button(top,text='C',height=3,width=7,command=clear,fg='white',bg='brown').grid(row=1,column=3,pady=6,padx=7)

b1=Button(top,text='4',height=3,width=7,command=lambda: btn_click(4),fg='white',bg='#424242').grid(row=2,column=0,pady=6,padx=7)
b1=Button(top,text='5',height=3,width=7,command=lambda: btn_click(5),fg='white',bg='#424242').grid(row=2,column=1,pady=6,padx=7)
b1=Button(top,text='6',height=3,width=7,command=lambda: btn_click(6),fg='white',bg='#424242').grid(row=2,column=2,pady=6,padx=7)
b1=Button(top,text='*',height=3,width=7,command=lambda: btn_click('*'),fg='white',bg='#424242').grid(row=2,column=3,pady=6,padx=7)

b1=Button(top,text='7',height=3,width=7,command=lambda: btn_click(7),fg='white',bg='#424242').grid(row=3,column=0,pady=6,padx=7)
b1=Button(top,text='8',height=3,width=7,command=lambda: btn_click(8),fg='white',bg='#424242').grid(row=3,column=1,pady=6,padx=7)
b1=Button(top,text='9',height=3,width=7,command=lambda: btn_click(9),fg='white',bg='#424242').grid(row=3,column=2,pady=6,padx=7)
b1=Button(top,text='/',height=3,width=7,command=lambda: btn_click('/'),fg='white',bg='#424242').grid(row=3,column=3,pady=6,padx=7)

b1=Button(top,text='0',height=3,width=7,command=lambda: btn_click(0),fg='white',bg='#424242').grid(row=4,column=0,pady=6,padx=7)
b1=Button(top,text='.',height=3,width=7,command=lambda: btn_click('.'),fg='white',bg='#424242').grid(row=4,column=1,pady=6,padx=7)
b1=Button(top,text='+',height=3,width=7,command=lambda: btn_click('+'),fg='white',bg='#424242').grid(row=4,column=2,pady=6,padx=7)
b1=Button(top,text='-',height=3,width=7,command=lambda: btn_click('-'),fg='white',bg='#424242').grid(row=4,column=3,pady=6,padx=7)

b1=Button(top,text='=',height=2,width=40,command=equal,fg='white',bg='#52528B').grid(row=5,column=0,columnspan=4,pady=6,padx=7)

top.mainloop()



# {%extends 'head/he_base.html'%}
# {%load static%}
# {%block content%}
# <div class="row pt-3" style="background-color: black;">
#   <div class="" style="font-size: 20px;font-weight: 600;color:#6C7293;">DAILY TASK</div>
# </div>
# <div class="row mt-4">
#   <div class="card">
#     <div class="card-body">
#       <input type="text" class="form-control text-light" id="search" placeholder="search...">
#       <div class="table-responsive">
#         <table class="table">
#           <thead>
#             <tr>
#               <th scope="col" style="color:#6C7293;">CLIENT NAME</th> 
#               <th scope="col" style="color:#6C7293;">WORKDONE</th> 
#               <th scope="col" style="color:#6C7293;">EXECUTIVE NAME</th> 
#               <th scope="col" style="color:#6C7293;">FILE</th> 
#               <th scope="col" style="color:#6C7293;">TARGET STATUS</th>
#               <th scope="col" style="color:#6C7293;">CORRECTION</th>  
#             </tr>
#           </thead>
#           <tbody id="myTable">
#             {% for i in work %}
#               <tr>
#               <td style="color:white;">{{i.work.client_name.client_name}}</td>
#               <td style="color:white;" data-toggle="modal" data-target="#workdetails{{i.id}}">{{i.task}}</td>
#               <td style="color:white;">{{i.user.fullname}}</td>
#               <td style="color:white;">
#                 {% for ss in i.json_testerscreenshot %}
#                 {% if ss %}
              
#                   <div class="badge badge-outline-primary"><a style="text-decoration: none;" href="{{ ss }}" download>
#                       Download</a></div>
                
#                   {% endif %}
#                   {% endfor %}
               
#               </td>
#               <td style="color:white;" data-toggle="modal" data-target="#status{{i.id}}">
#                <div class="badge badge-outline-success mt-1">Status</div>
#               </td> 
#               <td style="color:white;" data-toggle="modal" data-target="#correction{{i.id}}"><div class="badge badge-outline-danger mt-1">Correction</div></td>


#               <div class="rowmt-5 hidden modal fade" id="correction{{i.id}}">
#                 <div class="modal-dialog bd-example-modal-xl modal-dialog-centered" role="document" tabindex="-1" role="dialog"
#                   aria-labelledby="myLargeModalLabel" aria-hidden="true" >
#                   <div class="modal-content modal-xl" style="background-color: #191c24;">
#                     <div class="card ">
#                       <div class="card-body">
#                         <button type="button" class="close text-light" data-dismiss="modal" aria-label=""
#                           style="background-color: #191c24;border:none;float: right;font-size: 20px;">
#                           <span aria-hidden="true">&times;</span>
#                         </button>
#                         <div class="text-info" style="font-size: 20px;font-weight: 600;">CORRECTIONS</div>
              
#                         <form action="{% url 'he_add_correction_daily' i.id %}" method="post">{% csrf_token %}
#                           <div class="row pt-1">
#                             <div class="col">
#                               <textarea class="form-control ml-3 mt-2" name="cor" rows="8" cols="100" style="height: 100%; color:white"></textarea>
#                             </div>
#                         </div> 
#                         <div class="mt-2">
#                           <button  class="ml-3 mt-2 btn btn-outline-success">
#                             SUBMIT
#                             </button>
#                         </div>
#                       </form