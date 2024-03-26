# Import Libraries
# To use mathematics in the programming, we need numpy. To use it faster, we are taking it as np
import numpy as np
# to import and manage dataset, we need pandas. To use it faster, we are taking it as pd
import pandas as pd

# Import dataset
dataset = pd.read_csv('postings_table.csv')

#----------------------------Task-2 Question-1---------------------------------
#------------------Who is the user with most postings?-------------------------

# dataset['UserID'].value_counts(),  creates a series of frequencies of UserID's 
# .reset_index(), it converts the variable into dataframe
posting_frequency = dataset['UserID'].value_counts().reset_index()

# It finds out the responsible userid's for highest number of post but will generate nan for rest of the userid's
        # posting_frequency["UserID"].max() = highest value of UserId column in posting_frequency 
        # posting_frequency['index'].where(posting_frequency['UserID'], that part means if the max value of UserID column appear index will be added in the variable
most_posted_raw = (posting_frequency['index'].where(posting_frequency['UserID'] == posting_frequency["UserID"].max()))
#It cleans nan values from the list
# (That is the answer)
answer_3_most_posted_User_ID = [x for x in most_posted_raw if str(x) != 'nan']

    # printing the answer
print("Highest amount of posting by user/s" + " " + str(answer_3_most_posted_User_ID))

#----------------------------Task-2 Question-2---------------------------------
#------------------Who has the least amount of postings?-----------------------


# It finds out the responsible userid's for lowest number of post but will generate nan for rest of the userid's
        # posting_frequency["UserID"].min() = lowest value of UserId column in posting_frequency 
        # posting_frequency['index'].where(posting_frequency['UserID'], that part means if the min value of UserID column appear index will be added in the variable
least_posted_raw = (posting_frequency['index'].where(posting_frequency['UserID'] == posting_frequency["UserID"].min()))
#It cleans nan values from the list
# (That is the answer)
answer_4_least_posted_User_ID = [x for x in least_posted_raw if str(x) != 'nan']

 # printing the answer
print("Least amount of posting by user/s" + " " + str(answer_4_least_posted_User_ID))