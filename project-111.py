import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd


df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean = statistics.mean(data)
print("population mean:- ",mean)
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,(len(data)-1))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
std =  statistics.stdev(data)
def show_fig(mean_list,sampling_mean):
    df = mean_list
    std = statistics.stdev(df)
    first_std_deviation_start, first_std_deviation_end = sampling_mean-std, sampling_mean+std
    second_std_deviation_start, second_std_deviation_end = sampling_mean-(2*std), sampling_mean+(2*std)
    third_std_deviation_start, third_std_deviation_end = sampling_mean-(3*std), sampling_mean+(3*std)
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.21], mode="lines", name="MEAN"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.21], mode="lines", name="STANDARD DEVIATION 1"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.21], mode="lines", name="STANDARD DEVIATION 1"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.21], mode="lines", name="STANDARD DEVIATION 2"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.21], mode="lines", name="STANDARD DEVIATION 2"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.21], mode="lines", name="STANDARD DEVIATION 3"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.21], mode="lines", name="STANDARD DEVIATION 3"))
    fig.show()


def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    sampling_mean = statistics.mean(mean_list)
    print(f"sampling mean:-{sampling_mean}")    
    show_fig(mean_list,sampling_mean)

    z_score = (sampling_mean-mean)/std
    print("z-score:- :=",z_score)
    
setup()


