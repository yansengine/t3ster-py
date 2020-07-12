# t3ster-py

T3Ster是 MicRed公司开发的热瞬态测试仪，T3Ster master是专门用来打印和处理T3ster测试结果的后处理软件；

部分封装芯片厂商反映T3Ster master不能自动打印最高结温，需要人工选择最高结温，不同的人选择的最高结温会有差异；

本软件开发了基于JEDEC JESD51-14的Square root算法，可自动打印LED、MOSFET、IGBT等大部分器件的最高结温，省去了人工选择的过程；

另外，部分客户选用了非Micred接口的国产恒温箱，K系数只能用excel处理后再用windows自带的记事本来创建tco文件，容易出错；
本软件基于此需求开发了自动创建K系数文件功能，输入温度和电压结果后，一键导出K系数文件，方便管理。

本软件开发采用了python内置的tkinter GUI库，matplotlib进行绘图，numpy做数据拟合；

由于时间精力和我自身的数学能力有限，结构函数功能暂时还不能加入进来，希望后期各位同仁能帮助加入此功能；

README are Chinese language,if you're English or other language reader,please use Google translate to read;

if you have any question or just wanna discuss with me on T3ster,Please feel free to contact me,

e_mail:yanguoxin89@foxmail.com or jet-yan@qq.com
wechat:sk8yan
