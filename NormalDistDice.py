import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics

count=[]
dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)
#calculate the mean=sumof all data points/no of data points in population
mean=sum(dice_result)/len(dice_result)
#mean=mean(dice_result)
# find standard Deviation
stddev=statistics.stdev(dice_result)
#calculating mode and median
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
print(median)
print(mode)
print(mean)
print(stddev)

#fig=px.bar(x=dice_result,y=count)
#fig.show()
fig=ff.create_distplot([dice_result],["Result"], show_hist= False)
fig.show()
