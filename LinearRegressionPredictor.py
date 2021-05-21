#-------------------------------------LinearRegressionPredictor.py-------------------------------------#
'''
Importing modules:
-plotly.express (px)
-numpy (np)
-pandas (pd)
-time (tm)
'''
import plotly.express as px
import numpy as np
import pandas as pd
import time as tm

#Defining a function to find the y value with the x value which is an input
def PredictYValue(slope_arg,intercept_arg,field_choice_1_arg,field_choice_2_arg):
  x_arg=float(input("Enter the X-axis-value of the data whose Y-axis-value is to be predicted:".format(field_choice_1_arg,field_choice_2_arg)))
  y_arg=(slope_arg*x_arg)+intercept_arg

  print("The {} for {} at {} is {} ".format(field_choice_2_arg,field_choice_1_arg,float(x_arg),round(y_arg,2)))

  request_further_prediction=input("Continue furhter prediction?(:-Yes or No)")

  #Verifying the user's request wehter to continue with further prediction
  #Case-1
  if(request_further_prediction=="Yes" or request_further_prediction=="yes"):
    PredictYValue(slope_arg,intercept_arg,field_choice_1_arg,field_choice_2_arg)

  #Case-2
  else:
    
    #Printing the ending message
    return print("Request Accepted"),print("Thank you for using LinearRegressionPredictor.py")


#Reading data from the file 
df=pd.read_csv("data.csv")

#Introductory message 
print("Welcome to LinearRegressionPredictor.py. We provide data prediction through linear regression of a particular dataset.")
tm.sleep(2.3)


view_information=input("Do not know what Linear Regression is?(:- I Know, I Don't Know)")

#Verifying wether the user desires to view information aout linear regression or not
#Case-1
if(view_information=="I Don't Know" or view_information=="i don't know" or view_information=="I don't know"):
  print("What is linear regression?")
  tm.sleep(3.2)

  print("Linear regression is a method of prediction where two values are related in the form of a linear equation, y=mx+c.")
  tm.sleep(3.0)

  print("The dependent variable y can be predicted using the equation with the help of the indpendent variable x.")
  tm.sleep(2.3)

  print("Where is linear regression used?")
  tm.sleep(1.8)

  print("Linear regression is the most common type of data prediction.")
  tm.sleep(2.1)

  print("It is used in several fields, such as:")
  tm.sleep(1.2)

  print("1. Predicting the value of a product by corporations to modify their sales plans accordingly.")
  tm.sleep(2.3)

  print("2. Estimating demographic data by demographers to prepare and inform the government accordingly.")
  tm.sleep(2.3)

  print("3. Estimating values in sceintific equations and calculus by the scientific community.")
  tm.sleep(2.3)

  print("Linear regression harbors much more uses and possibilities.")
  tm.sleep(2.4)
  
  print("To know more about linear regression, visit:'https://en.wikipedia.org/wiki/Linear_regression' for more")
  tm.sleep(2.8)


print("Loading Data...")
tm.sleep(2.3)

#Displaying all choices for field 1 and accquiring the user input
field_1_list=["Unusable_Element","GRE Score","TOEFL Score","University Rating","SOP","LOR ","CGPA","Chance of Admit "]
field_count=0

for field_1 in field_1_list[1:]:
  field_count+=1
  print(str(field_count)+":"+field_1)

field_input_1=int(input("Please enter the index of the field preferred to be the X-axis:"))
field_choice_1=field_1_list[field_input_1]

field_2_list=["Unusable_Element","GRE Score","TOEFL Score","University Rating","SOP","LOR ","CGPA","Chance of Admit "]
field_count=0

#Displaying all choices for field 2 and accquiring the user input
for field_2 in field_2_list[1:]:
  field_count+=1
  print(str(field_count)+":"+field_2)

field_input_2=int(input("Please enter the index of the field preferred to be the Y-axis:"))
field_choice_2=field_2_list[field_input_2]

df_field_1=df[field_choice_1].tolist()
df_field_2=df[field_choice_2].tolist()

#Verifying wether the both are fields are not equal
#Case-1
if(field_input_1!=field_input_2):
  
  field_1=np.array(df_field_1)
  field_2=np.array(df_field_2)

  slope,intercept=np.polyfit(field_1,field_2,1)
  y=[]

  for value in field_1:
    y_value=(slope*value)+intercept
    y.append(y_value)

  print("Generating Graph...")
  tm.sleep(3.9)
  print("Graph Generated")

  scatter_graph=px.scatter(df,x=df_field_1,y=df_field_2,color=df_field_2)
  scatter_graph.update_layout(shapes=[dict(type="line",x0=min(df_field_1),x1=max(df_field_1),y0=min(y),y1=max(y))])
  scatter_graph.show() 

  print("The y-axis-values of the data can be predicted with the x-axis-values through the equation:{}=({}x{})+{}".format(field_choice_2,round(slope,2),field_choice_1,round(intercept,2))) 
  
  correlation_coef=np.corrcoef(field_1,field_2)
  correlation_coef_range=round(correlation_coef[0,1],3)
  correlation_coef_percentage_square=(correlation_coef_range**2)*100
  
  #Verifying wether the correlation coefficient is lesser or greater than 0
  #Case-1
  if(correlation_coef_range<0):
    print("'{}' and '{}' share an inverse proportion".format(field_choice_1,field_choice_2))
    correlation_coef_range=correlation_coef_range*-1
    correlation_coef_percentage=(correlation_coef_range*100)/1
    print("The veracity of correct prediction through the equation is {}".format(round(correlation_coef_percentage,2)))

  #Case-2
  elif(correlation_coef_range>0):
    print("'{}' and '{}' share a direct proportion".format(field_choice_1,field_choice_2))
    correlation_coef_percentage=(correlation_coef_range*100)/1
    print("The veracity of correct prediction through the equation is {}%".format(round(correlation_coef_percentage,2))) 
  
  print("{}% of differences in '{}' can be explained and predicted by '{}' thorugh the equation(Coefficient of determination)".format(round(correlation_coef_percentage_square,2),field_choice_2,field_choice_1))
  
  request_prediction=input("Predict the value of {}?(:-Yes or No)".format(field_choice_2))

  #Verifying the user's input on predicting the y value or not
  #Case-1
  if(request_prediction=="Yes" or request_prediction=="yes"):
    PredictYValue(slope,intercept,field_choice_1,field_choice_2)
  #Case-2  
  else:
    print("Request Accepted.")

    #Printing the ending message
    print("Thank you for using LinearRegressionPredictor.py")  

#Case-2
else:
  print("Request Termianted.")
  print("Invalid Field Choices.")
  print("Please choose different fields for the x and y axes.")

  #Printing the ending message
  print("Thank you for using LinearRegressionPredictor.py")

#-------------------------------------LinearRegressionPredictor.py-------------------------------------#

