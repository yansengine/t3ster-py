from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import numpy as np
def removeItem():
    iids=tree.selection()
    for i in iids:
        tree.delete(i)
def insertItem():
    temperature=tem_entry.get()
    voltage=vol_entry.get()
    if (len(temperature.strip())==0 or len(voltage.strip())==0):
        return
    tree.insert('',END,text=temperature,values=(voltage))
    tem_entry.delete(0,END)
    vol_entry.delete(0,END)
def create_k_file():
    tsp_dic={}
    t_list=[]
    v_list=[]
    file_list=['#line1',
               '#line2',
               '#line3',
               '#1',
               '#   0']
    for child in tree.get_children():
        new_list=tree.item(child)['values']
        t_list.append(new_list[0])
        v_list.append(new_list[1])

    for i in range(0,len(t_list)):
        tsp_dic[t_list[i]]=v_list[i]
    temp_list=[]
    for t in t_list:
        temp_list.append(float(t))
    volt_list=[]
    for v in v_list:
        volt_list.append(float(v))
    tsp=np.polyfit(temp_list,volt_list,1)

    k = tsp[0]
    b = tsp[1]
    # b = '%.3f' % (1000 * (1 / float(tsp[1])))


    file_list.append('#'+str(b))
    file_list.append('#'+str(k))


    for t,v in tsp_dic.items():
        file_list.append(str(t)+'\t'+str(v))



    input_file = filedialog.asksaveasfilename(
        filetypes=[("tco", "*.tco")])

    with open(input_file + '.tco', 'w') as the_file:
        for i in file_list:
            # print(i + '\n')
            the_file.write(i+'\n')


root=Tk()
root.title('Tjdoctor')

temperature_voltage={'50':'2.5182',
                     '60':'2.5063',
                     '70':'2.4945',
                     '80':'2.4823'}

top_fm=Frame(root)
tem_label=Label(top_fm,text='温度')
tem_label.pack(side=LEFT,padx=5,pady=5)
tem_entry=Entry(top_fm)
tem_entry.pack(side=LEFT,padx=5,pady=5)

vol_label=Label(top_fm,text='电压')
vol_label.pack(side=LEFT,padx=5,pady=5)
vol_entry=Entry(top_fm)
vol_entry.pack(side=LEFT,padx=5,pady=5)
top_fm.pack(side=TOP,anchor=W)


tree=Treeview(root,show='headings',columns=('temperature','voltage'),selectmode=EXTENDED)
tree.heading('temperature',text='temperature[℃]')
tree.heading('voltage',text='voltage[V]')

tree.column('temperature',anchor=CENTER)
tree.column('voltage',anchor=CENTER)


for t,v in temperature_voltage.items():
    tree.insert('',index=END,text=(t,v),values=(t,v))

tree.pack(side=TOP,anchor=W,padx=5,pady=5)

btm_fm=Frame(root)
inBtn=Button(btm_fm,text='插入',command=insertItem)
inBtn.pack(side=LEFT,padx=5,pady=5)
rmBtn=Button(btm_fm,text='删除',command=removeItem)
rmBtn.pack(side=LEFT,padx=5,pady=5)
cjBtn=Button(btm_fm,text='创建K系数文件',command=create_k_file)
cjBtn.pack(side=LEFT,padx=5,pady=5)
btm_fm.pack(side=TOP,anchor=W)

root.mainloop()

