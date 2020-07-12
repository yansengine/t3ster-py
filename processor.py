# coding:utf-8
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import os
class Tj_doctor():
    def __init__(self):
        root = Tk()
        # 设置整体界面科技黑背景色
        root.configure(background='#434343')
        # 设置软件内的图片path路径
        self.open = PhotoImage(file='img/open_file.gif')
        self.save = PhotoImage(file='img/save.gif')
        self.update_co = PhotoImage(file='img/update_co.gif')
        self.cre_k=PhotoImage(file='img/create_k.gif')
        # 添加class中的函数
        self.window_init(root)
        self.create_menu(root)
        self.create_widget(root)
        root.mainloop()

    def window_init(self, root):
        root.title('Tj Doctor')
        width, height = root.maxsize()
        root.geometry('{}x{}'.format(width, height))
        root.iconbitmap('img/logo.ico')

    def create_menu(self, root):
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='打开', command=self.choose_raw_file)
        filemenu.add_command(label='另存为', command=self.save_tj)
        filemenu.add_command(label='退出', command=root.quit)
        menubar.add_cascade(label='文件', menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label='校准点', command=self.update_initial)
        editmenu.add_command(label='创建K系数文件', command=self.create_k)
        menubar.add_cascade(label='编辑', menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label='关于我', command=self.show_about)
        helpmenu.add_command(label='联系我', command=self.show_help)
        menubar.add_cascade(label='帮助', menu=helpmenu)
        root.config(menu=menubar, bg='#434343')

    def create_widget(self, root):
        messagebox.showinfo('Tj Doctor', "欢迎使用Tj Doctor!")

        # 定义全局字符变量
        self.correction = 100
        # 定义数学运算全局变量
        # 定义主界面的宽高，依据不同显示器，会有不同的显示效果，初步达到响应式布局
        self.width = root.winfo_width()
        self.height = root.winfo_height()
        # 定义主界面整体frame
        self.window_frame = Frame(root, bg='#434343')
        # 定义顶部hotkey快捷键栏
        self.hotkey_fm = Frame(self.window_frame, bg='#434343')
        self.open_button = Button(self.hotkey_fm,
                                  bd=0,
                                  image=self.open,
                                  bg='#434343',
                                  command=self.choose_raw_file)
        self.open_button.pack(side=LEFT, padx=2, pady=2)
        self.save_button = Button(self.hotkey_fm,
                                  bd=0,
                                  image=self.save,
                                  bg='#434343',
                                  command=self.save_tj)
        self.save_button.pack(side=LEFT,
                              padx=2,
                              pady=2)

        self.update_btn=Button(self.hotkey_fm,
                               bd=0,
                               image=self.update_co,
                               bg='#434343',
                               command=self.update_initial)
        self.update_btn.pack(side=LEFT,
                             padx=2,
                             pady=2)

        self.cre_k_btn=Button(self.hotkey_fm,
                              bd=0,
                              image=self.cre_k,
                              # bg='#434343',
                              command=self.create_k)
        self.cre_k_btn.pack(side=LEFT,
                        padx=2,
                        pady=2)

        self.hotkey_fm.pack(side=TOP,
                            anchor=NW,
                            padx=5,
                            pady=2,
                            fill=BOTH)
        # 中间整体为信息显示栏，分别为项目列表，图形，文字结果
        self.window_mid_fm = Frame(self.window_frame,
                                   bg='#434343')
        # 创建可移动的panewindow，主要是为了三列宽度可调
        separator = PanedWindow(self.window_mid_fm,
                                bg='#818181',
                                sashwidth=2)
        separator.pack()
        # 左边项目列表树状结果栏
        self.tree_fm = Frame(self.window_mid_fm,
                             width=self.width * 0.26,
                             height=self.height * 0.6,
                             bg='#434343')
        self.tree_title = Label(self.tree_fm,
                                text='Project >>',
                                bg='#434343',
                                fg='#E9E9E9')
        self.tree_title.pack(side=TOP, anchor=NW)
        # 设置tree的style
        style = ttk.Style()
        style.theme_use('default')
        style.configure("mystyle.Treeview",
                        highlightthickness=0,
                        bd=0,
                        background='#434343',
                        # foreground='red',
                        fieldbackground='#434343')
        self.project_tree = ttk.Treeview(self.tree_fm,
                                         style='mystyle.Treeview',
                                         show='tree',
                                         height=30)
        self.project_tree.tag_configure('bgb', background='#434343', foreground='white')
        # 在这里插入树形列表 #
        self.project_tree.pack(side=TOP,
                               fill=BOTH,
                               padx=2,
                               pady=2)
        self.tree_fm.pack_propagate(0)
        self.tree_fm.pack(side=LEFT,
                          anchor=NW,
                          padx=5,
                          pady=8)
        # 中间文字结果信息栏
        self.info_fm = Frame(self.window_mid_fm,
                             bg='#434343')
        self.txt_title1 = LabelFrame(self.info_fm,
                                     text='TSP K Factor Console>>',
                                     fg='#E9E9E9',
                                     bg='#434343',
                                     relief='flat')
        self.txt_title1.pack(side=TOP,
                             anchor=W)

        yscrollbar1 = Scrollbar(self.txt_title1,
                                width=12)
        self.txt_info1 = Text(self.txt_title1,
                              height=20,
                              bg='#434343',
                              foreground='#A9B7C6')
        yscrollbar1.pack(side=RIGHT, fill=Y)
        self.txt_info1.pack(side=TOP)
        yscrollbar1.config(command=self.txt_info1.yview)
        self.txt_info1.config(yscrollcommand=yscrollbar1.set)

        self.txt_title2 = LabelFrame(self.info_fm,
                                     text='Transient data Console>>',
                                     fg='#E9E9E9',
                                     bg='#434343',
                                     relief='flat')
        self.txt_title2.pack(side=TOP,
                             anchor=W)

        yscrollbar2 = Scrollbar(self.txt_title2,
                                width=12)
        self.txt_info2 = Text(self.txt_title2,
                              height=20,
                              bg='#434343',
                              foreground='#A9B7C6')
        yscrollbar2.pack(side=RIGHT, fill=Y)
        self.txt_info2.pack(side=TOP)
        yscrollbar2.config(command=self.txt_info2.yview)
        self.txt_info2.config(yscrollcommand=yscrollbar2.set)

        self.info_fm.pack(side=LEFT,
                          anchor=NE,
                          padx=5,
                          pady=6)
        # 图片结果信息栏
        self.right_fm = Frame(self.window_mid_fm,
                              width=0.35 * self.width,
                              background='#434343')
        self.pic_label = Label(self.right_fm,
                               text='Curves>>',
                               bg='#434343',
                               fg='#E9E9E9')
        self.pic_label.pack(side=TOP,
                            anchor=W)
        self.pic_fm = Frame(self.right_fm,
                            bg='#434343')
        self.fig = Figure(dpi=100,
                          figsize=(self.width / 200, self.height / 120),
                          facecolor='#434343')
        self.fig.subplots_adjust(hspace=0.5,
                                 wspace=0.3)
        self.ax_tsp = self.fig.add_subplot(211)
        self.ax_tsp.set(facecolor='#434343')
        self.ax_tsp.set_frame_on(False)
        self.ax_tsp.set_xticks([])
        self.ax_tsp.set_yticks([])
        self.ax_t = self.fig.add_subplot(212)
        self.ax_t.set(facecolor='#434343')
        self.ax_t.set_frame_on(False)
        self.ax_t.set_xticks([])
        self.ax_t.set_yticks([])
        self.canvas = FigureCanvasTkAgg(self.fig,
                                        self.pic_fm)
        self.canvas.get_tk_widget().pack()
        self.pic_fm.pack(side=TOP,
                         anchor=N,
                         padx=5,
                         pady=8)
        self.right_fm.pack_propagate(0)
        self.right_fm.pack(side=RIGHT,
                           fill=BOTH,
                           expand=YES)
        self.window_mid_fm.pack(side=TOP,
                                fill=BOTH)
        separator.add(self.tree_fm)
        separator.add(self.info_fm)
        separator.add(self.right_fm)
        # 底部版权栏
        self.bottom_fm = Frame(self.window_frame,
                               bg='#434343')
        self.left_label = Label(self.bottom_fm,
                                text='Tj Doctor，专业的半导体结温处理工具',
                                bg='#434343',
                                fg='#E9E9E9')
        self.left_label.pack(side=LEFT,
                             padx=10,
                             pady=5,
                             anchor=W)
        self.right_label = Label(self.bottom_fm,
                                 text='©严国鑫 All rights reserved',
                                 bg='#434343',
                                 fg='#E9E9E9')
        self.right_label.pack(side=RIGHT,
                              padx=10,
                              pady=5,
                              anchor=E)
        self.bottom_fm.pack(side=TOP,
                            fill=BOTH)
        self.window_frame.pack(fill=BOTH)

    def choose_raw_file(self):
        raw_path = filedialog.askopenfilename(filetypes=[('RAW', '*.raw')])
        raw_list = [raw_path, ]
        raw_name = os.path.basename(raw_path)
        self.project_tree.insert('', 'end', raw_path, text=raw_name, tags=('bgb'))
        UREF = self.Voltage_processor(raw_list)
        self.project_tree.insert(raw_path, 'end', text='参考电压：' + str(UREF[0]) + ' [V]', tags=('bgb'))
        self.project_tree.item(raw_path, open=True)
        self.project_tree.bind('<Button-3>', self.right_click_popup_menu)

    def choose_tco_file(self):
        tco_path = filedialog.askopenfilename(filetypes=[('TCO', '*.tco')])
        # tco_name = os.path.basename(tco_path)
        return tco_path

    def Voltage_processor(self, raw_path):
        time = []
        transient_bit = []
        transient_voltage = []
        if raw_path[0]:
            with open(raw_path[0], 'r') as raw_file:
                raw_data = []
                for line in raw_file.readlines():
                    lines = line.strip()
                    raw_data.append(lines)
            LSB_str = raw_data[6]
            Uref_str = raw_data[8]
            LSB = LSB_str[2:]
            Uref = Uref_str[2:]
            lsb = float(LSB)
            uref = float(Uref)
            v_range = lsb * 4095
            u_max = uref + v_range / 2
            u_min = uref - v_range / 2
            Bit = [0, 4095]
            Volt = [u_min, u_max]
            Volt_Bit = np.polyfit(Bit, Volt, 1)
            temp_data = raw_data[:]
            for r in raw_data:
                if r[0] == "#":
                    temp_data.remove(r)
                    raw_data = temp_data
            for r in raw_data:
                space_index = r.find(' ')
                time.append(r[:space_index])
                transient_bit.append(r[(space_index + 1):])
            for ti, us in enumerate(time):
                time_us = np.float64(us) / 10e5
                time[ti] = time_us
            for bi, bit_data in enumerate(transient_bit):
                transient_bit[bi] = float(bit_data)
            for tbi in transient_bit:
                transient_voltage.append(tbi * Volt_Bit[0] + Volt_Bit[1])
            # print(type(transient_voltage))
            return uref, time, transient_voltage
        else:
            messagebox.showinfo('提示', "文件格式错误，请选择.raw的后缀文件")

    def TSP_processor(self, tco_path):
        TSP_factor = []
        TSP_temperature = []
        # print(tco_path)
        if tco_path:
            with open(tco_path, 'r') as TSP_file:
                TSP_data = []
                TSP_temperature = []
                TSP_voltage = []
                TSP_dic={}
                for line in TSP_file.readlines():
                    lines = line.strip()
                    TSP_data.append(lines)
                temp_data_2 = TSP_data[:]
                for Ti in TSP_data:
                    if Ti[0] == "#":
                        temp_data_2.remove(Ti)
                        TSP_data = temp_data_2
                for Ti in TSP_data:
                    space_index = Ti.find('\t')
                    TSP_temperature.append(Ti[:space_index])
                    TSP_voltage.append(Ti[(space_index + 1):])
                for Ti, Tt in enumerate(TSP_temperature):
                    TSP_temperature[Ti] = float(Tt)
                for Ti, Tv in enumerate(TSP_voltage):
                    TSP_voltage[Ti] = float(Tv)
                TSP_factor = np.polyfit(TSP_voltage, TSP_temperature, 1)
                # 打印K系数结果
                self.txt_info1.delete(1.0, END)
                self.txt_info1.insert(END, tco_path + '\n')
                for i in range(0,len(TSP_temperature)):
                    TSP_dic[TSP_voltage[i]]=TSP_temperature[i]
                self.txt_info1.insert(INSERT, 'TSP_voltage[V]' +'\t'+'TSP_temperature[℃]' + '\n')
                for t,v in TSP_dic.items():
                    self.txt_info1.insert(END, str(t)+'\t\t\t'+str(v)+'\n')

                self.txt_info1.insert(END, '<' + 'Temperature=' + str(
                    '%.3f' % float(TSP_factor[0])) + '*Voltage' + '+' + str('%.3f' % TSP_factor[1]) + '>' + '\n')
                xv = np.array(TSP_voltage)
                yt = np.array(TSP_temperature)
                # 画图
                self.ax_tsp.clear()
                self.ax_tsp.set_frame_on(True)
                self.ax_tsp.plot(xv, yt, color='#6A8759')
                self.ax_tsp.scatter(xv, yt, marker='*',
                                    color='#434343')
                self.ax_tsp.set(title=os.path.basename(tco_path),
                                xlabel='TSP_Voltage[V]',
                                ylabel='TSP_Temperature[℃]')
                self.ax_tsp.grid(linestyle='-.')
                self.canvas.draw()
            return TSP_factor
        else:
            messagebox.showwarning('提示', '请选择K系数文件!')

    def Tj_processor(self, initial):
        time_temp={}
        # 将initial转换为整数
        newdata = int(initial)
        # 创建结温列表变量
        transient_temperature = []
        # 获取右键单击的父节点
        parent_node = self.project_tree.selection()
        # 获取父节点下的子节点
        children_node = self.project_tree.get_children(parent_node[0])
        # 若单击的是父节点（及就是存在子节点），则：
        if children_node:
            # 调用电压处理函数，得到函数返回值
            raw_data = self.Voltage_processor(parent_node)

            # 获取tsp中的K和B
            def get_tsp():
                for i in children_node:
                    tco_list = self.project_tree.item(i, 'text')
                    if tco_list[0] == 'K':
                        tco_path = tco_list[18:]
                        tsp_data = self.TSP_processor(tco_path)
                        return tsp_data

            # 调用函数
            tsp_data = get_tsp()
            # 通过K系数将电压变换为结温
            for tvi in raw_data[2]:
                transient_temperature.append(tsp_data[0] * tvi + tsp_data[1])
            # 删除结温打印文本框中的全部内容（内容太多，若打印全部结果，不方便保存）
            self.txt_info2.delete(1.0, END)

            # 打印时间和结温结果
            self.txt_info2.insert(INSERT, str(parent_node[0]) + '\n' + 'time[us]'+"\t\t\t"+'temperature[℃]' + '\n')
            for i in range(0,len(raw_data[1])):
                time_temp[raw_data[1][i]]=transient_temperature[i]
            for time,temp in time_temp.items():
                self.txt_info2.insert(END,str(time)+'\t\t\t'+str(temp)+'\n')


            # 定义自动打印最高结温程序函数,此函数不保证全部芯片结果都适用，但保证LED结温打印准确
            # 使用JESD51-14的方法打印,得到0时刻的结温
            def Tj_max():
                # 创建拟合区间列表，po_time和po_temp,以及po_time的开方列表
                po_time = raw_data[1][newdata:newdata + 30]
                po_temp = transient_temperature[newdata:newdata + 30]
                sqrt_po_time = []
                for i in po_time:
                    j = i ** 0.5
                    sqrt_po_time.append(j)
                po_temp_time = np.polyfit(sqrt_po_time, po_temp, 1)
                return po_temp_time[1]

            Tj_max = Tj_max()

            # 打印最高结温到列表中
            self.project_tree.insert(parent_node[0], 'end',
                                     text='结温：' + str(Tj_max)[0:7] + ' [℃]' + ' initial correction @' + str(
                                         self.correction) + 'us', tags=('bgb'))
            # 绘图
            xt = np.array(raw_data[1])
            yt = np.array(transient_temperature)
            x_max = np.max(xt)
            y_min = yt[-2:-1]
            y_max = np.max(yt)
            self.ax_t.clear()
            self.ax_t.set_frame_on(True)
            self.ax_t.scatter(xt, yt,
                              marker='.',
                              color='#AA4926')
            self.ax_t.set(title=os.path.basename(parent_node[0]),
                          xlabel='Time [s]',
                          ylabel='Temperature [℃]',
                          xscale='log',
                          xlim=(10e-7, x_max + 200),
                          ylim=(y_min - 10, y_max + 10))
            self.ax_t.grid(linestyle='-.')
            self.canvas.draw()
            return transient_temperature
        else:
            messagebox.showinfo('提示', "请右击文件名！")

    def import_TSP(self):
        parent_node = self.project_tree.selection()

        children_node = self.project_tree.get_children(parent_node[0])
        if children_node:
            for item in children_node:
                self.project_tree.delete(item)
            tco_data = self.choose_tco_file()
            tsp_data = self.TSP_processor(tco_data)
            k_factor = '%.3f' % (1000 * (1 / float(tsp_data[0])))
            raw_data = self.Voltage_processor(parent_node)
            self.project_tree.insert(parent_node[0], 'end', text='参考电压：' + str(raw_data[0]) + ' [V]', tags=('bgb'))
            self.project_tree.insert(parent_node[0], 'end', text='K系数：' + str(k_factor) + ' [mV/℃] ' + tco_data,
                                     tags=('bgb'))
            self.project_tree.item(parent_node[0], open=True)
            return parent_node
        else:
            pass

    def right_click_popup_menu(self, event):
        right_menu = Menu(self.project_tree, tearoff=0)
        right_menu.add_command(label='导入K系数', command=self.import_TSP)
        right_menu.add_command(label='计算结温', command=lambda: self.Tj_processor(self.correction))
        right_menu.add_command(label='删除', command=self.delete_item)
        right_menu.post(event.x_root, event.y_root)

    def delete_item(self):
        # 获取父节点
        _node = self.project_tree.selection()
        # 获取父节点的子节点
        # children_node = self.project_tree.get_children(parent_node[0])
        # 双击文件名导入K系数等结果
        if _node:
            for item in _node:
                self.project_tree.delete(item)
            self.txt_info1.delete(1.0, END)
            self.txt_info2.delete(1.0, END)
            # self.ax_tsp.clear()

    def save_tj(self):
        input_file = filedialog.asksaveasfilename(
            filetypes=[("文本文档", "*.txt")])
        if input_file:
            self.file_name = input_file
            self._write_to_file(self.file_name)

    def _write_to_file(self, file_name):
        try:
            content = self.txt_info2.get(1.0, 'end')
            with open(file_name + '.txt', 'w') as the_file:
                the_file.write(content)
        except IOError:
            messagebox.showwarning("保存", "保存失败！")

    def show_about(self):
        top = Toplevel()
        top.title('Tj Doctor')
        top.iconbitmap('img/logo.ico')
        self.about_info = Message(top,
                                  width=600,
                                  bg='#434343',
                                  fg='#E9E9E9',
                                  text='\n\n\n'
                                       'TjDoctor是由严国鑫开发的热瞬态测试仪器数据处理工具软件；'
                                       '\n适用于T3Ster等热瞬态测试仪器的测试结果的读取和处理;\n\n'
                                  )
        self.about_info.pack(side=TOP, anchor='w', fill=X, expand=YES)

    def show_help(self):
        top = Toplevel()
        top.title('Tj Doctor')
        top.iconbitmap('img/logo.ico')
        self.about_info = Message(top,
                                  width=600,
                                  bg='#434343',
                                  fg='#E9E9E9',
                                  text='\n\n\n使用本工具可享受终生免费的T3Ster售后服务\n'
                                       '联系方式：jet_yan@qq.com;\t \n\n\n')
        self.about_info.pack(side=TOP,
                             anchor='w',
                             fill=X,
                             expand=YES)

    def update_initial(self):
        top = Toplevel()
        top.geometry('400x300')
        top.title('Tj Doctor')
        top.iconbitmap('img/logo.ico')

        corect_label = LabelFrame(top, text='修正点')
        corect_label.pack(fill=X, padx=15, pady=8)

        top_fm = Frame(corect_label)
        top_fm.pack(fill=X, expand=YES, side=TOP, padx=15, pady=8)

        val = StringVar()
        self.entry = Entry(top_fm, textvariable=val)
        self.entry.insert(0, '100')
        self.entry.pack(side=LEFT, fill=X, expand=YES)
        unit_label = Label(top_fm, text='us')
        unit_label.pack(side=LEFT, padx=5)

        btn = Button(top_fm, text='修改', width=10, command=self.modify_initial)
        btn.pack(side=LEFT, anchor=N, padx=5, pady=5)

    def modify_initial(self):
        dat = self.entry.get()
        self.correction = dat
        messagebox.showinfo('Tj Doctor', '修改成功')
        return self.correction

    def create_k(self):
        top = Toplevel()
        # top.geometry('400x600')
        top.title('Tj Doctor')
        top.iconbitmap('img/logo.ico')

        temperature_voltage = {'50': '2.5182',
                               '60': '2.5063',
                               '70': '2.4945',
                               '80': '2.4823'}

        def removeItem():
            iids = tree.selection()
            for i in iids:
                tree.delete(i)

        def insertItem():
            temperature = tem_entry.get()
            voltage = vol_entry.get()
            if (len(temperature.strip()) == 0 or len(voltage.strip()) == 0):
                return
            tree.insert('', END, text=temperature, values=(voltage))
            tem_entry.delete(0, END)
            vol_entry.delete(0, END)

        def create_k_file():
            tsp_dic = {}
            t_list = []
            v_list = []
            file_list = ['#line1',
                         '#line2',
                         '#line3',
                         '#1',
                         '#   0']
            for child in tree.get_children():
                new_list = tree.item(child)['values']
                t_list.append(new_list[0])
                v_list.append(new_list[1])

            for i in range(0, len(t_list)):
                tsp_dic[t_list[i]] = v_list[i]
            temp_list = []
            for t in t_list:
                temp_list.append(float(t))
            volt_list = []
            for v in v_list:
                volt_list.append(float(v))
            tsp = np.polyfit(temp_list, volt_list, 1)

            k = tsp[0]
            b = tsp[1]
            # b = '%.3f' % (1000 * (1 / float(tsp[1])))

            file_list.append('#' + str(b))
            file_list.append('#' + str(k))

            for t, v in tsp_dic.items():
                file_list.append(str(t) + '\t' + str(v))

            input_file = filedialog.asksaveasfilename(
                filetypes=[("tco", "*.tco")])

            with open(input_file + '.tco', 'w') as the_file:
                for i in file_list:
                    # print(i + '\n')
                    the_file.write(i + '\n')

        top_fm = Frame(top)
        tem_label = Label(top_fm, text='温度')
        tem_label.pack(side=LEFT, padx=5, pady=5)
        tem_entry = Entry(top_fm)
        tem_entry.pack(side=LEFT, padx=5, pady=5)

        vol_label = Label(top_fm, text='电压')
        vol_label.pack(side=LEFT, padx=5, pady=5)
        vol_entry = Entry(top_fm)
        vol_entry.pack(side=LEFT, padx=5, pady=5)
        top_fm.pack(side=TOP, anchor=W)

        tree=ttk.Treeview(top, show='headings', columns=('temperature', 'voltage'), selectmode=EXTENDED)
        tree.heading('temperature', text='temperature[℃]')
        tree.heading('voltage', text='voltage[V]')

        tree.column('temperature', anchor=CENTER)
        tree.column('voltage', anchor=CENTER)

        for t, v in temperature_voltage.items():
            tree.insert('', index=END, text=(t, v), values=(t, v))

        tree.pack(side=TOP, anchor=W, padx=5, pady=5)

        btm_fm = Frame(top)
        inBtn = Button(btm_fm, text='插入', command=insertItem)
        inBtn.pack(side=LEFT, padx=5, pady=5)
        rmBtn = Button(btm_fm, text='删除', command=removeItem)
        rmBtn.pack(side=LEFT, padx=5, pady=5)
        cjBtn = Button(btm_fm, text='创建K系数文件', command=create_k_file)
        cjBtn.pack(side=LEFT, padx=5, pady=5)
        btm_fm.pack(side=TOP, anchor=W)