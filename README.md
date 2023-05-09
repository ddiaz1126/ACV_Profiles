# ACV_Profiles
This is an older and first of my projects working with an accelerometer to measure bar velocity on the back squat and bench presss. 
The files were based on actual training sessions that had a standardized warm up and load increase increments based on load relative to the individual.
It was based on the 4-point method where 4 loads were used. The file creates a scatter plot with both the linear and polynomial regressions. 
Finally, a table is created to the correlated repititions in reserve (RIR) to velocities. RIR is a subjected method controlling an exercise session. 

Code:

In this project, I utilize libraries such as pandas, scikit-learn, numpy, and matplotlib.
The data was digitalized on a csv file and read on python by pandas (pd.read_csv). Functions were created to calculate the best fit line, y-intercept, squared error, and the coeficient of determination. The best fit line is the predicted model that is created using the x and y componenets. The squared error and coefficeient metrics tell us how well the model is fit to the data. A polynomial regression is also created as in most of the research literature currently uses both regression models. The polynomial regression is differs from the linear regression in that it is non-linear and the primary reason for being used with velocity profiles is that there are individual differences at where and when an indivual will have supstantial decline in velocity, if they do. This is outside the scope of this project but is primarily due to muslce fiber type composition and training history.
 
 The final part of the code is the predicting of values (RIR & Velocity) using the model that was trained. There is also a scatterplot showing the model with the predictions. There is a visual table showing the correlated velocity with RIR that is specific to the individual that will aid their training intensity.
