#!/usr/bin/env python
# coding: utf-8

# # This file is in charge of filtering the data
# First we show the user that the data was imported

# In[9]:


print ('Successfully imported')


# **Class** and **methods** are created to make a correct data filtering

# In[22]:


#Made by Luis Zúñiga Araya

#Class creation
class DataFilter:
    
    def __init__(self,data):
        self.data = data
   
    #method that filter the data by age
    def filter_age(self,age):
        ##Create a new dataframe with only rows matching the specific age
        self.age = age
        self.data = self.data[self.data["age"] == self.age]
        print(f'Data for patients with {self.age} years')
        return self.data
    
    #method that filter the data by sex
    def filter_sex(self,sex):
        ##Create a new dataframe with only rows matching the specific sex
        self.sex = sex
        self.data = self.data[self.data["sex"] == self.sex]
        print(f'Data for {self.sex} patients ')
        return self.data
   
    #method that filter the data by sex
    def filter_sex(self,sex):
        ##Create a new dataframe with only rows matching the specific sex
        self.sex = sex
        self.data = self.data[self.data["sex"] == self.sex]
        print(f'Data for {self.sex} patients ')
        return self.data


    #method that filter the data by number of childrens
    def filter_children_n(self,children):
        ##Create a new dataframe with only rows matching the specific number of childrens
        self.children = children
        self.data = self.data[self.data["children"] == self.children]
        print(f'Data for patients with {self.age} children')
        return self.data

    #method that filter the data by non-smoking or smoking patients
    def filter_smoker(self,smoker):
        ##Create a new dataframe with only rows matching the specific number of childrens
        self.smoker = smoker
        self.data = self.data[self.data["smoker"] == self.smoker]
        if self.smoker == 'no':
            print('Data for non smoking patients')
        else:
            print('Data for smoking patients')
        return self.data
    
    #method that filter the data by region
    def filter_region(self,region):
        ##Create a new dataframe with only rows matching the inputed region
        self.region = region
        self.data = self.data[self.data["region"] == self.region]
        print(f'Data for patients of {self.age} region')
        return self.data
    
    def info(self):
        ## return some values that will be important at the moment of the data analysis
        
        self.qty_indv = len(self.data['age'])
        print('The ammount of patients at the study are', self.qty_indv)
        
        #Check the amount of females and males
        self.total_sex = self.data['sex'].value_counts()
        print('Amount of male patients: ', self.total_sex[0])
        print('Amount of female patients: ', self.total_sex[1])
        
        #Check the average age for each sex
        self.total_age = self.data.groupby(['sex'])['age'].sum()
        self.avg_male_age = self.total_age[0]/self.total_sex[0]
        self.avg_female_age = self.total_age[1]/self.total_sex[1]
        print('Average age for males of the data is: ', self.avg_male_age)
        print('Average age for females of the data is: ', self.avg_female_age)
        
        #Check the total bmi for each sex
        self.total_bmi = self.data.groupby(['sex'])['bmi'].sum()
        self.avg_male_bmi = self.total_bmi[0]/self.total_sex[0]
        print('Average BMI for males is', self.avg_male_bmi)
        self.avg_female_bmi = self.total_bmi[1]/self.total_sex[1]
        print('Average BMI for females is', self.avg_female_bmi)
        #Check which sex has a higher BMI
        if self.avg_male_bmi > self.avg_female_bmi:
            print('On this data BMI on males tends to be higher than for females')
        else:
            print('On this data BMI on females tends to be higher than for males')
            
        #Check the amount of nonsmoking and smoking patients
        self.total_smokers = self.data['smoker'].value_counts()
        print('The number of non-smoking patients is: ', self.total_smokers[0])
        print('The number of non-smoking patients is: ', self.total_smokers[1])
        
        #Check the number of patients per region
        self.per_region = self.data['region'].value_counts()
        print(f'The number of patients per region is: {self.per_region[0]} southeast, {self.per_region[1]} southwest, {self.per_region[2]} northwest, {self.per_region[3]} northeast')
        

