import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv('data.csv')
data=df["Math_score"].tolist()

fig=ff.create_distplot([data],["mathscore"],show_hist=False)
#fig.show()
#mean=statistics.mean(data)
#sd=statistics.stdev(data)
#print(mean)
#print(sd)

def random_set_of_mean(counter): 
    dataset = [] 
    for i in range(0, counter): 
        random_index= random.randint(0,len(data)-1) 
        value = data[random_index] 
        dataset.append(value) 
    mean = statistics.mean(dataset) 
    return mean

#calling random set of mean thousand time and will store thousand mean in an array
mean_list = [] 
for i in range(0,1000): 
    set_of_means= random_set_of_mean(100) 
    mean_list.append(set_of_means)

sd=statistics.stdev(mean_list)
mean=statistics.mean(mean_list)    
fig=ff.create_distplot([mean_list],["mathscore"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean"))
#fig.show()
## findig the standard deviation starting and ending values 
first_std_deviation_start, first_std_deviation_end = mean-sd, mean+sd 
second_std_deviation_start, second_std_deviation_end = mean-(2*sd), mean+(2*sd) 
third_std_deviation_start, third_std_deviation_end = mean-(3*sd), mean+(3*sd)

# finding the mean of the first data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot. # 
df = pd.read_csv("sample1.csv") 
data = df["Math_score"].tolist()  
mean_of_sample1 = statistics.mean(data) 
print("Mean of sample1:- ",mean_of_sample1)  
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False) 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) # 
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE")) # 
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) # 
fig.show()

# finding the mean of the second data(STUDENTS WHO EXTRA CLASSES) and plotting it on the plot. # 
df = pd.read_csv("sample2.csv") 
data = df["Math_score"].tolist()  
mean_of_sample2 = statistics.mean(data) 
print("Mean of sample2:- ",mean_of_sample2)  
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False) 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) # 
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE")) # 
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) # 
fig.show()

# finding the mean of the first data(STUDENTS WHO had received extra sheets) and plotting it on the plot. # 
df = pd.read_csv("sample3.csv") 
data = df["Math_score"].tolist()  
mean_of_sample3 = statistics.mean(data) 
print("Mean of sample3:- ",mean_of_sample3)  
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False) 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) # 
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE")) # 
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) # 
fig.show()

zscore1=(mean-mean_of_sample1)/sd
zscore2=(mean-mean_of_sample2)/sd
zscore3=(mean-mean_of_sample3)/sd
print(zscore1,zscore2,zscore3)