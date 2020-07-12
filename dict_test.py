# temperature_voltage={'50':'2.5555',
#                      '60':'2.4444',
#                      '70':'2.3333',
#                      '80':'2.2222'}
#
# for t,v in temperature_voltage.items():
#     print(t,v)



# 创建time和temp字典
time=[1,2,3,4]
temp=[10,20,30,40]

tt={}

for i in range(0,len(time)):
    tt[time[i]]=temp[i]
print(tt)
# 遍历字典的键
for i in tt.keys():
    print(i)
for j in tt.values():
    print(j)