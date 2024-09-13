#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs
# 
# Import the libraries needed for the success of our code.

# In[1]:


#Medical Insurance Costs project
#Made by Luis Zúñiga Araya

#Import libraries needed


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error 


us_insurance_df = pd.read_csv(r"https://github.com/LuisZCR/US_Medical_Insurance_Costs/blob/main/insurance.csv")


# Import our **Class** created for making filters on the Dataframe.

# In[2]:


from DataFilter import DataFilter
    
DataR = DataFilter(us_insurance_df)


# Show the first 5 rows of the data set to see what the variables are and their content.

# In[3]:


#First we plot the fisrt 5 rows to see wich variables we have
print(us_insurance_df.head())


# Look for the type of the variables we have, this is important to know if data agress with the variable type showed.

# In[4]:


#Look for the type of the variables we have
print(us_insurance_df.dtypes)


# Call the info method of the `DataFilter` Class that show some usefull information.

# In[5]:


DataR.info()


# In order to analyze the relationship between the data in a simpler way, we use the `get_dummies` method to separate our variables **sex**, **smoker**, and **region** into columns with boolean features.

# In[6]:


#Use get_dummies to find the correlation matrix
corr = pd.get_dummies(us_insurance_df, columns = ['sex','smoker','region'])
corr.corr()
#The variables which have a higher correlation between them are 'charges' and 'smoker'


# In the following two graphs, a certain variability in the data can be observed. When analyzing the correlation matrix, we realize that what is affecting these the most is **age**, since neither **sex** nor the **number of children** has a high correlation factor with insurance costs.

# In[7]:


#Separate data per sex
plt.figure(figsize=(10, 6))
p = sns.lineplot(x="age", y="children", hue="sex", data=us_insurance_df, marker = 'o')
#Customize the chart
plt.title('Number of Children vs Age by Sex')
plt.xlabel('Age')
plt.ylabel('Number of Children')
plt.legend(title='Sex')
plt.show()
print(us_insurance_df['children'].max())


# In[8]:


#Separate data per sex
plt.figure(figsize=(10, 6))
p = sns.lineplot(x="age", y="charges", hue="sex", data=us_insurance_df)
#Customize the chart
plt.title('Insurance cost vs Age by Sex')
plt.xlabel('Age of the person')
plt.ylabel('Insurance cost')
plt.legend(title='Sex')
plt.show()


# In the following graph it can be observed that the changes in the **cost of insurance** by **region** and **sex** are not significant enough.

# In[9]:


#Separate data per sex
plt.figure(figsize=(10, 6))
p = sns.barplot(x="region", y="charges", hue="sex", data=us_insurance_df)
#Customize the chart
plt.title('Insurance cost vs Region by Sex')
plt.xlabel('Region')
plt.ylabel('Insurance cost')
plt.legend(title='Sex')
plt.show()


# As the correlation matrix showed, **BMI**, **sex** and **smoking** status do not seem to have any relationship with each other.

# In[10]:


#Separate data per sex
plt.figure(figsize=(10, 6))
p = sns.barplot(x="smoker", y="bmi", hue="sex", data=us_insurance_df)
#Customize the chart
plt.title('BMI vs Smoker Condition by Sex')
plt.xlabel('Smoker Condition')
plt.ylabel('BMI')
plt.legend(title='Sex')
plt.show()


# At the following bar plot, the behavior of the graphs tells that the **smoker condition** influences in **insurance cost** amount.

# In[11]:


#To confirm the correlation on smoker and charges
p = sns.barplot(x="smoker", y="charges", data=us_insurance_df)
#Customize the chart
plt.title('Smoker vrs Insurance cost')
plt.xlabel('Smoker')
plt.ylabel(' Insurance cost')
plt.show()


# Method from the `DataFilter` Class used for only showing patients with a specific age.

# In[12]:


DataR.filter_age(40)


# Separate the dataframe into **features** and **output**.

# In[13]:


#Separate the dataframe in features and output
X = corr.drop(columns = 'charges')
y = corr['charges']


# Split data into **train** and **test** sets.

# In[14]:


#Split data into train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101) 


# Create a `LinearRegression` model.

# In[15]:


#Creating a regression model
model = LinearRegression() 
#Fit the model with training data
model.fit(X_train, y_train)


# Make predictions on the test data set.

# In[16]:


# making predictions 
y_pred = model.predict(X_test)


# Evaluate the model to see how good it turned out to be.

# In[17]:


# model evaluation 
print('Mean_squared_error : ', mean_squared_error(y_test, y_pred)) 
print('Mean_absolute_error : ', mean_absolute_error(y_test, y_pred)) 
print('Model score: ', model.score(X_test, y_test))


# With the correlation matrix we found out that **sex**, **number of children** and **regions** are features with not much weight on charges so we proceed to drop them to optimize our model.

# In[18]:


new_X = corr.drop(columns=['sex_male','sex_female','children','region_northeast','region_northwest','region_southwest','region_southeast'])


# We proceed to create our model and evaluate if it really improved.

# In[19]:


#Split the data with the new dataframe
X_train, X_test, y_train, y_test = train_test_split(new_X, y, test_size=0.3, random_state=101) 
#Creating a regression model
model = LinearRegression() 
#Fit the new model with training data
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# model evaluation 
print('Mean_squared_error : ', mean_squared_error(y_test, y_pred)) 
print('Mean_absolute_error : ', mean_absolute_error(y_test, y_pred)) 
print('Model score: ', model.score(X_test, y_test))


# With these simple methods we observed that our model became more rigid, having a score of **1** and extremely small **errors**.
