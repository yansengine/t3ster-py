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

if add == '8c:ec:4b:14:fe:e8' and date[0] < 2030:
    if __name__ == '__main__':
        Tj_doctor()
elif add == '8c:ec:4b:14:fe:e8' and 2030 <= date[0] < 2031:
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
            messagebox.showwarning('Tj Doctor', '对不起，软件已到期，请联系销售人员续费')
    else:
        messagebox.showwarning('Tj Doctor', '对不起，软件已到期，请联系销售人员续费')
else:
    messagebox.showwarning('Tj Doctor', '你正在非法使用！请联系销售人员购买')
