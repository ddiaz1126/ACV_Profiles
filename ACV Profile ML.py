import pandas as pd
import numpy as np # arrays
from sklearn.linear_model import LinearRegression
lin = LinearRegression()
from matplotlib import style
from matplotlib import pyplot as plt
from statistics import mean
from sklearn.metrics import r2_score


style.use('fivethirtyeight')

# Reading File
Name = 'File'
df = pd.read_csv(Name)
# plt.scatter(df['RIR'],df['Velocity'])
xs = df['RIR']
ys = df['Velocity']

# Linear Regression

def best_fit_slope(xs,ys):
    m = ( ((mean(xs) * mean(ys)) - mean(xs*ys)) /
        ((mean(xs)*mean(xs)) - mean(xs*xs)))
    return m

m = best_fit_slope(xs,ys)

def best_fit_slope_and_intercept(xs,ys):
    m = ( ((mean(xs) * mean(ys)) - mean(xs*ys)) /
        ((mean(xs)*mean(xs)) - mean(xs*xs)))
    b = mean(ys) - m*mean(xs)
    return m,b
m,b = best_fit_slope_and_intercept(xs,ys)

regression_line = [(m*x)+b for x in xs]

predict_x = 0
predict_y = (m*predict_x)+b
predict_y

def squared_error(ys_orig, ys_line): #actual y itself and y on the linear
    return sum((ys_line-ys_orig)**2)
def coefficient_of_determination(ys_orig,ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean)

r_squared = coefficient_of_determination(ys, regression_line)
r_squared

# Polynomial Regression

mymodel = np.poly1d(np.polyfit(xs, ys, 2))
mymodel
r2_score(ys,mymodel(xs))
myline = np.linspace(0, 20, 100).reshape(-1,1)

predict_0 = mymodel(0)
predict_0

predict_1 = mymodel(1)
predict_1

predict_2 = mymodel(2)
predict_2

predict_3 = mymodel(3)
predict_3

predict_4 = mymodel(4)
predict_4

predict_5 = mymodel(5)
predict_5

predict_6 = mymodel(6)
predict_6

predict_7 = mymodel(7)
predict_7

predict_8 = mymodel(8)
predict_8

predict_9 = mymodel(9)
predict_9

predict_10 = mymodel(10)
predict_10

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y, color='g')
plt.plot(xs, regression_line)
plt.plot(myline, mymodel(myline))
plt.xlabel('Reps In Reserve')
plt.ylabel('Velocity (m/s)')
plt.grid(True)
plt.xticks(range(21))
plt.ylim(0.1,.6)
plt.xlabel('Reps In Reserve')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Reps In Reserve', fontsize=25)

data = [['0', round(predict_0, 2)], ['1', round(predict_1, 2)], ['2', round(predict_2, 2)], ['3', round(predict_3, 2)], ['4', round(predict_4, 2)], ['5', round(predict_5, 2)], ['6', round(predict_6, 2)], ['7', round(predict_7, 2)], ['8', round(predict_8, 2)], ['9', round(predict_9, 2)], ['10', round(predict_10, 2)]]

fig, axs = plt.subplots(1, 1)
columns = ("RIR", "Velocity")
axs.axis('tight')
axs.axis('off')
the_table = axs.table(cellText=data, colLabels=columns, loc='center')
plt.show