import pandas as pd
import csv
import statistics

df= pd.read_csv("data.csv")
heightList= df["Height(Inches)"].to_list()
weightList= df["Weight(Pounds)"].to_list()
heightMean= statistics.mean(heightList)
weightMean= statistics.mean(weightList)
heightMedian= statistics.median(heightList)
weightMedian= statistics.median(weightList)
heightMode= statistics.mode(heightList)
weightMode= statistics.mode(weightList)
print("Mean, Median and Mode of students height is {},{} and{} rescpectively".format(heightMean,heightMedian,heightMode))
print("Mean, Median and Mode of students weight is {},{} and{} rescpectively".format(weightMean,weightMedian,weightMode))
heightstdDeviation=statistics.stdev(heightList)
weightstdDeviation=statistics.stdev(weightList)
height1ststdDeviationstart,height1ststdDeviationend=heightMean-heightstdDeviation,heightMean+heightstdDeviation
height2ndstdDeviationstart,height2ndstdDeviationend=heightMean-(2*heightstdDeviation),heightMean+(2*heightstdDeviation)
height3rdstdDeviationstart,height3rdstdDeviationend=heightMean-(3*heightstdDeviation),heightMean+(3*heightstdDeviation)
weight1ststdDeviationstart,weight1ststdDeviationend=weightMean-weightstdDeviation,weightMean+weightstdDeviation
weight2ndstdDeviationstart,weight2ndstdDeviationend=weightMean-(2*weightstdDeviation),weightMean+(2*weightstdDeviation)
weight3rdstdDeviationstart,weight3rdstdDeviationend=weightMean-(3*weightstdDeviation),weightMean+(3*weightstdDeviation)

height_list_of_data_within_1_std_deviation=[result for result in heightList if result>height1ststdDeviationstart and result<height1ststdDeviationend]
height_list_of_data_within_2_std_deviation=[result for result in heightList if result>height2ndstdDeviationstart and result<height2ndstdDeviationend]
height_list_of_data_within_3_std_deviation=[result for result in heightList if result>height3rdstdDeviationstart and result<height3rdstdDeviationend]
weight_list_of_data_within_1_std_deviation=[result for result in weightList if result>weight1ststdDeviationstart and result<weight1ststdDeviationend]
weight_list_of_data_within_2_std_deviation=[result for result in weightList if result>weight2ndstdDeviationstart and result<weight2ndstdDeviationend]
weight_list_of_data_within_3_std_deviation=[result for result in weightList if result>weight3rdstdDeviationstart and result<weight3rdstdDeviationend]
print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(heightList)))
print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(heightList)))
print("{}% of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(heightList)))
print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weightList)))
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weightList)))
print("{}% of data for weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weightList)))