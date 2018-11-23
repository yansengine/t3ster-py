import matplotlib
import matplotlib.pyplot as plt
def read_raw():
    x = []
    #可以更改以下打开文档路径
    with open(r'G:\py_work\t3_processor\t3_data\1#_grease_h60s_r120s_4a_10ma.raw','r') as x_file:
    #因为.raw文档内为多行文本，采用readlines方法进行读取
        for line in x_file.readlines():
            lines=line.strip()
            x.append(lines)
        y=x[:]
        for i in x:
            if i[0]=='#':
                y.remove(i)
                x=y
    time=[]
    Voltage=[]
    for i in x:
        space_index=i.find(' ')
        time.append(i[:space_index])
        Voltage.append(i[(space_index+1):])
    # 接下来是数据可视化部分
    plt.plot(time,Voltage,'r')
    plt.xlabel('time')
    plt.ylabel('Voltage')
    plt.show()