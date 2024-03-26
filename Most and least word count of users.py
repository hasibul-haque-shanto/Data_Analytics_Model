# Import Libraries
# To use mathematics in the programming, we need numpy. To use it faster, we are taking it as np
import numpy as np
# to import and manage dataset, we need pandas. To use it faster, we are taking it as pd
import pandas as pd
# Import dataset
dataset = pd.read_csv('postings_table.csv')

#----------------------------Task-2 Question-3---------------------------------
#------------------Which user has "written" most words?------------------------

# It adds a new column called Totalwords which contains number of words = space +1 of Content column in each row.
dataset['Totalwords'] = dataset['Content'].str.count(' ') + 1
# It counts total word wriiten by a particular UserID
word_count = dataset.groupby('UserID')['Totalwords'].agg(['sum','count']).reset_index()

# It finds out the responsible UserID's for highest number of words but will generate nan for rest of the UserID's
        # word_count["sum"].max() = highest value of sum column in word_count
        # word_count['UserID'].where(word_count['sum'], that part means if the max value of sum column appear UserID will be added in the variable
most_words_raw = (word_count['UserID'].where(word_count['sum'] == word_count["sum"].max()))

#It cleans nan values from the list
# (That is the answer)
answer_5_most_words_User_ID = [x for x in most_words_raw if str(x) != 'nan']

# printing the answer
print("Most words posted by user" + " " + str(answer_5_most_words_User_ID))

#----------------------------Task-2 Question-4---------------------------------
#------------------Which one has written the least?----------------------------

# It finds out the responsible UserID's for lowest number of words but will generate nan for rest of the UserID's
        # word_count["sum"].min() = lowest value of sum column in word_count
        # word_count['UserID'].where(word_count['sum'], that part means if the min value of sum column appear UserID will be added in the variable
least_words_raw = (word_count['UserID'].where(word_count['sum'] == word_count["sum"].min()))

#It cleans nan values from the list
# (That is the answer)
answer_6_least_words_User_ID = [x for x in least_words_raw if str(x) != 'nan']

# printing the answer
print("Least words posted by user/s" + " " + str(answer_6_least_words_User_ID))