
# coding: utf-8

# In[3]:

movies_path='C:\\Users\\shris\\Desktop\\ml-20m\\ml-20m\\movies.csv'
import pandas as pd
from pandas import DataFrame as df
movies_df=pd.read_csv(movies_path)
movies_df.head()


# In[4]:

len(movies_df.index)


# In[5]:

movies_df.shape


# In[6]:

len(movies_df.movieId)


# In[8]:

print (movies_df.loc[0][0])
print (movies_df.loc[0][1])


# In[11]:

movies_df['genres_arr'] = movies_df['genres'].str.split('|')
movies_df.head()


# In[18]:

masala_lambda=lambda x:set(['Romance','Comedy','Action','Thriller']).issubset(x)
masala_movies=movies_df[movies_df.genres_arr.map(masala_lambda)]



# In[19]:

print('# of masala movies', len(masala_movies.index))


# In[20]:

masala_movies


# In[21]:

counter_lambda = lambda x:len(x)


# In[22]:

movies_df['genre_count']=movies_df.genres_arr.apply(counter_lambda)


# In[23]:

movies_df.head()


# In[39]:

#how many genres do various movies have by plotting histogram
#introducing matplotlib package which allow us plot charts graphs in python


import matplotlib.pyplot as plt

plt.hist(movies_df.genre_count)
plt.hist(movies_df.genre_count, edgecolor='black', linewidth=1.2)
plt.title("Genres Histogram")
plt.xlabel("# of genres")
plt.ylabel("# of movies")
plt.axis([0 , 9 , 0 , 15000])
plt.show()


# In[ ]:



