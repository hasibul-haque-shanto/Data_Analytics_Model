# Import Libraries
# To use mathematics in the programming, we need numpy. To use it faster, we are taking it as np
import numpy as np
# to import and manage dataset, we need pandas. To use it faster, we are taking it as pd
import pandas as pd

# Import dataset
dataset = pd.read_csv('user_table.csv')

#----------------------------Task-1 Question-1---------------------------------
#------------What is the number of unique name combinations?-------------------

# Combining Surname and Name in one column and " " uses this for having a space between them and adding it into the dataset as Fullname
dataset["Fullname"] = dataset["Surname"] + " "+ dataset["Name"]
# Search for unique names and storing it in unique_names variable
unique_names = dataset['Fullname'].unique()

# (That is the answer)
    # len() function counts total row and then printing it as string
print("Total unique name" + " " + str(len(unique_names)))

#----------------------------Task-1 Question-2---------------------------------
#---------------Who is the oldest user, who is the youngest?-------------------

# There are two ways of thinking who is oldest and who is youngest. 
#Two different types of approach may be required for different purposes. So, I am solving it in both ways

# First one is based on Age

    # It finds out the responsible UserID's for highest age but will generate nan for rest of the UserID's
        # dataset["Age"].max() = highest value of age column of dataset = max age
        # dataset['Fullname'].where(dataset['Age'], that part means if the max value of age column appear the fullname will be added in the variable
oldest_raw = (dataset['Fullname'].where(dataset['Age'] == dataset["Age"].max()))

    #It cleans nan values from the list
    # (That is the answer)
answer_2_1_oldest_users = [x for x in oldest_raw if str(x) != 'nan']

    # printing the answer
print("Oldest User/s" + " " + str(answer_2_1_oldest_users))

    # It finds out the responsible UserID's for lowest age but will generate nan for rest of the UserID's
        # dataset["Age"].min() = lowest value of age column of dataset = min age
        # dataset['Fullname'].where(dataset['Age'], that part means if the min value of age column appear the fullname will be added in the variable
youngest_raw = (dataset['Fullname'].where(dataset['Age'] == dataset["Age"].min()))

    #It cleans nan values from the list
    # (That is the answer)
answer_2_2_youngest_users = [x for x in youngest_raw if str(x) != 'nan']

    # printing the answer
print("Youngest User/s" + " " + str(answer_2_2_youngest_users))

# Second and last one is based on Subscription_date
    # Here higher value means newer and lower means older. so max and min need to be interchanged

    # It finds out the responsible UserID's for lowest value in Subscription_Date but will generate nan for rest of the UserID's
        # dataset["Subscription_Date"].min() = lowest value of Subscription_Date column of dataset = oldest
        # dataset['Fullname'].where(dataset['Subscription_Date'], that part means if the min value of Subscription_Date column appear the fullname will be added in the variable
oldest_sub_raw = (dataset['Fullname'].where(dataset['Subscription_Date'] == dataset["Subscription_Date"].min()))

    #It cleans nan values from the list
    # (That is the answer)
answer_2_3_oldest_users_sub = [x for x in oldest_sub_raw if str(x) != 'nan']

    # printing the answer
print("Oldest User/s_sub" + " " + str(answer_2_3_oldest_users_sub))
   
     # It finds out the responsible UserID's for lowest value in Subscription_Date but will generate nan for rest of the UserID's
        # dataset["Subscription_Date"].max() = lowest value of age column of dataset = youngest
        # dataset['Fullname'].where(dataset['Subscription_Date'], that part means if the min value of Subscription_Date column appear the fullname will be added in the variable

youngest_sub_raw = (dataset['Fullname'].where(dataset['Subscription_Date'] == dataset["Subscription_Date"].max()))

    #It cleans nan values from the list
    # (That is the answer)
answer_2_4_youngest_users_sub = [x for x in youngest_sub_raw if str(x) != 'nan']

    # printing the answer
print("Youngest User/s_sub" + " " + str(answer_2_4_youngest_users_sub))