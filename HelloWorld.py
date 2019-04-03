import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10.0,8.0);
import seaborn as sns
from scipy import stats
from scipy.stats import norm

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
train = pd.read_csv(url, names=names)

#train = pd.read_csv("/data/Housing/train.csv");
#test = pd.read_csv("/data/Housing/test.csv");
train.head()
print ('The train data has {0} rows and {1} columns'.format(train.shape[0],train.shape[1]))
print ('----------------------------')
#print ('The test data has {0} rows and {1} columns'.format(test.shape[0],test.shape[1]))
