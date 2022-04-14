## Data Preparation
#1. Import Libraries
#2. Import Data
#3 Data Exploration
#4. Data Cleaning
#5. Data Tokenization


#1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt # For visualizations
import seaborn as sns
from transformers import AutoTokenizer
#from wordcloud import WordCloud
#from bertopic import BERTopic

#2. Import Data
raw_data = pd.read_csv("C:/Users/norap/Documents/GitHub/Machine Learning NLP TU Wien/data/raw/okcupid_profiles.csv")
raw_data.head()

#3. Data Exploration
raw_data.isnull().sum() #are there null values in the dataset? YES Lots

#boxplot to see age distribution for each gender
sns.boxplot(x='sex', y='age', data=raw_data)
plt.show()
df_essay1 = raw_data[raw_data.essay1.notnull()]

#4. Data Cleaning
#we try 2 versions: Light and heavy cleaning, and then see which one performs best
#3.1 Light cleaning
#Make list out of essay1

#lowercase everything
#x = x.lower()

#remove unicode
#x = x.encode('ascii', 'ignore').decode()  # remove unicode



#5. Data Tokenization

#BERTopic
#topic_model = BERTopic(language="english", calculate_probabilities=True, verbose=True)
#topics, probs = topic_model.fit_transform(docs)
