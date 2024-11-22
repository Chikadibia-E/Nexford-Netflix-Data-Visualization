#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing required modules:

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Data Preparation:

# In[2]:


# Reading or importing csv file to dataframe:

df = pd.read_csv('C:\\Users\\e_chi\\OneDrive - Nexford University\\BAN6420_Assignments\\Netflix Data Visualization\\Netflix_shows_movies.csv')


# # Data Exploration: 

# In[8]:


# Descriptive statistics including all (numeric and non-numeric):

df.describe(include= 'all')


# In[9]:


# Descriptive statistics including object (non-numeric):

df.describe(include= 'object')


# In[4]:


# Checking for missing values in data frame:
df.isna()


# In[90]:


# Summary of missing values:
df.isna().sum()


# # Data Cleaning:

# In[10]:


# Dropping selected columns not required for visualisation 
# and having too many missing values:

df.drop(['director', 'cast', 'country'], axis = 1, inplace= True)


# In[12]:


# Dropping other rows with missing values:

df.dropna(inplace = True)


# In[13]:


# Summary of missing values after removing missing values:

df.isna().sum()


# In[15]:


# saving the cleaned data frame to csv:

df.to_csv('Netflix_shows_movies_clean.csv', index = False)


# In[17]:


# Importing the clean data set in readiness for visualisation:

df_clean = pd.read_csv('Netflix_shows_movies_clean.csv')


# In[32]:


listed_in_counts = df_clean['listed_in'].value_counts()
listed_in_counts


# In[41]:


# defining a function to group genres to more manageable categories:

def group_genres(genre):
    if 'Documentaries' in genre:
        return 'Documentaries'
    elif 'Stand-Up Comedy' in genre:
        return 'Comedy'
    elif 'Dramas' and 'International Movies' in genre:
        return 'Drama'
    elif 'TV' in genre:
        return 'TV Show'
    elif 'Horror' in genre:
        return 'Horror'
    elif 'Action & Adventure' in genre:
        return 'Action'
    elif 'Children & Family' in genre:
        return 'Family'
    elif 'Docuseries' in genre:
        return 'Docuseries'
    elif 'Romantic Movies' in genre:
        return 'Romance'
    elif 'Thrillers' in genre:
        return 'Thrillers'
    else:
        return 'Others'
        


# In[42]:


# Applying the function to create a new genre column:

df_clean['genres'] = df_clean['listed_in'].apply(group_genres)


# In[43]:


# Genres frequency:

genre_counts = df_clean['genres'].value_counts()
genre_counts


# In[23]:


# Ratings frequency:

rating_counts = df_clean['rating'].value_counts()
rating_counts


# # Data Visualization:

# ## 1. Most Watched Genres:

# In[45]:


# Using matplotlib:

plt.figure(figsize=(10,6))
genre_counts.plot(kind = 'bar')
plt.title('Most Watched Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show()


# In[86]:


# Using Seaborn:

plt.figure(figsize=(10, 6))
sns.barplot(x=genre_counts.index, y=genre_counts.values)
plt.title('Most Watched Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show()


# ## 2. Ratings Distribution

# In[87]:


# Using Matplotlib:

plt.figure(figsize=(10, 6))
df_clean['rating'].hist(bins=30)
plt.title('Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.grid(False)
plt.show()


# In[82]:


# Using Seaborn:

plt.figure(figsize=(10, 6))
sns.histplot(df_clean['rating'], bins=30)
plt.title('Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()


# ## 2b. Trying bar plots for ratings distribution

# In[88]:


# Using matplotlib:

plt.figure(figsize=(10,6))
rating_counts.plot(kind = 'bar')
plt.title('Most Watched Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show()


# In[89]:


# Using Seaborn:

plt.figure(figsize=(10, 6))
sns.barplot(x= rating_counts.index, y=rating_counts.values)
plt.title('Most Watched Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show()


# In[ ]:




