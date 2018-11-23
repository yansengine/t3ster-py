# t3ster-py

t3ster master 是一个t3ster的后处理软件，是收费的，如果没有足够的经费，可以用python进行t3ster的数据处理，同样可以达到t3ster master一样的处理效果；

主要有以下几个步骤：

step1，读取.raw文件对电压瞬态结果进行显示 

step2，用温度-电压K系数，将电压瞬态结果转换为温度结果 

step3，去掉温度开始部分的noise 

step4，对温度瞬态结果进行微分和积分，得到结构函数 

