# ACV_Profiles
This is an older and first of my projects working with an accelerometer to measure bar velocity on the back squat and bench press. 
The files were based on training sessions with a standardized warm-up and load increase increments based on load relative to the individual.
It was based on the 2-point method where 2 loads were used. The file creates a scatter plot with both the linear and polynomial regressions. 
Finally, a table is created for the correlated repetitions in reserve (RIR) to velocities. RIR is a subjective method of controlling an exercise session. 

Code:

I utilize libraries such as pandas, sci-kit-learn, numpy, and matplotlib in this project.
The data was digitalized on a CSV file and read on Python by pandas (pd.read_csv). Functions were created to calculate the best-fit line, y-intercept, squared error, and coefficient of determination. The best-fit line is the predicted model that is created using the x and y components. The squared error and coefficient metrics tell us how well the model is fit to the data. A polynomial regression is also created as in most of the research literature currently uses both regression models. The polynomial regression differs from the linear regression in that it is non-linear and the primary reason for being used with velocity profiles is that there are individual differences in where and when an individual will have a substantial decline in velocity if they do. This is outside the scope of this project but is primarily due to muscle fiber type composition and training history.
 
The final part of the code is predicting values (RIR & Velocity) using the model that was trained. There is also a scatterplot showing the model with the predictions. There is a visual table showing the correlated velocity with RIR that is specific to the individual that will aid their training intensity.
