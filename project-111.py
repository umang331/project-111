import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd


df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
std = statistics.stdev(data)
fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()
mean = str(statistics.mean(data))
print("population mean:- "+mean)
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    sampling_mean = statistics.mean(mean_list)
    print("sampling mean:- "+sampling_mean)
    z_score = (sampling_mean-mean)/std
    print("z-score:- ",z_score)
    show_fig(mean_list)
setup()


