# coding:utf-8
from processor import *
import uuid #获取计算机IP地址的模块
import datetime #获取计算机时间的模块
from tkinter import messagebox
def get_ip():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
add = get_ip()
print(add)
def get_date():
    expire_date = datetime.datetime.now().date()
    str_date = str(expire_date)
    year = int(str_date[:4])
    month = int(str_date[5:7])
    day = int(str_date[8:10])
    return year, month, day
date = get_date()

local_host_ip='please insert your ip here'

if add ==local_host_ip  and date[0] < 2090:
    if __name__ == '__main__':
        Tj_doctor()
elif add ==local_host_ip  and 2090 <= date[0] < 2091:
    #月份要求
    if date[1] < 3:
        if __name__=='__main__':
            Tj_doctor()
    elif 3<=date[1]<4:
        #日期要求
        if date[2]<=1:
            if __name__=='__main__':
                Tj_doctor()
        else:
            messagebox.showwarning('Tj Doctor', '对不起，软件已到期!')
    else:
        messagebox.showwarning('Tj Doctor', '对不起，软件已到期!')
else:
    messagebox.showwarning('Tj Doctor', '请联系开发人员进行支援！')
