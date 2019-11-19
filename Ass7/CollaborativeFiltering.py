#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
  
 
column_names = ['user_id', 'item_id', 'rating', 'timestamp'] 
  
path = 'https://media.geeksforgeeks.org/wp-content/uploads/file.tsv'
  
df = pd.read_csv(path, sep='\t', names=column_names) 
  
df.head() 


# In[3]:


movie_titles = pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/Movie_Id_Titles.csv') 
movie_titles.head() 


# In[4]:


data = pd.merge(df, movie_titles, on='item_id') 
data.head() 


# In[5]:


data.groupby('title')['rating'].mean().sort_values(ascending=False).head()


# In[6]:


data.groupby('title')['rating'].count().sort_values(ascending=False).head()


# In[7]:


ratings = pd.DataFrame(data.groupby('title')['rating'].mean())  
  
ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count()) 
  
ratings.head() 


# In[8]:


moviemat = data.pivot_table(index ='user_id', 
              columns ='title', values ='rating') 
  
moviemat.head() 
  
ratings.sort_values('num of ratings', ascending = False).head(10) 


# In[10]:


starwars_user_ratings = moviemat['Star Wars (1977)'] 
liarliar_user_ratings = moviemat['Liar Liar (1997)'] 
  
starwars_user_ratings.head() 


# In[11]:


similar_to_starwars = moviemat.corrwith(starwars_user_ratings) 
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings) 
  
corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation']) 
corr_starwars.dropna(inplace = True) 
  
corr_starwars.head() 


# In[12]:


corr_starwars.sort_values('Correlation', ascending = False).head(10) 
corr_starwars = corr_starwars.join(ratings['num of ratings']) 
  
corr_starwars.head() 
  
corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head() 


# In[13]:


corr_liarliar = pd.DataFrame(similar_to_liarliar, columns =['Correlation']) 
corr_liarliar.dropna(inplace = True) 
  
corr_liarliar = corr_liarliar.join(ratings['num of ratings']) 
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation', ascending = False).head() 


# In[ ]:




