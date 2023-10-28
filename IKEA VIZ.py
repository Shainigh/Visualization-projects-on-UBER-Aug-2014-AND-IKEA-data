#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from math import radians,cos,sin,asin,sqrt


# In[6]:


data_ikea = pd.read_csv(r"C:\Users\HP\Downloads\ikea.csv",index_col=0)


# In[9]:


data_ikea.head(10)


# In[57]:


1. #top 3 highest selling categories.
top3_category = data_ikea.groupby("category")['price'].sum().reset_index()
sorted_values = top3_category.sort_values(by='price',ascending =False)
#print(sorted_values)

### TOP 3 HIGHEST SELLING CATEGORY
b= sorted_values.head(3) 

###VIZ 
plt.figure(figsize=(8,6))
plt.bar(b['category'], b['price'], color='skyblue')  ###FOR SHOWING BOTH CATEGORY AS WELL PRICE 
plt.xlabel('category')
plt.ylabel('sales')
plt.title('top 3 highest selling category for IKEA')

plt.show()


# In[83]:


2.#TOP DESIGNERS FOR EACH CATEGORY based on HIGHEST SALES

top_d = data_ikea.groupby(['designer','category'])['price'].sum().reset_index()
sorted_values = top_d.sort_values(by=['price','category'],ascending =False)
#print(sorted_values)

#top designer per category

top_d_per_c= sorted_values.groupby('category').head(1)
#print(top_d_per_c)

###VIZ

plt.figure(figsize=(8,6))
plt.bar(top_d_per_c['designer'],top_d_per_c['price'],color= 'green')
plt.xlabel('designer')
plt.ylabel('category')
plt.title('TOP DESIGNERS OF EACH CATEGORY IN IKEA')
plt.xticks(rotation=90)
plt.show()



# In[100]:


#3. HOW MANY FURNITURES ARE SOLD IN EACH CATEGORY?

furn_count = data_ikea.groupby('category').size().reset_index(name ='furnc')

sorted_furn = furn_count.sort_values(by='furnc', ascending = False)

b= sorted_furn.head(10)

plt.figure(figsize=(8,6))
plt.bar(b['category'],b[''], color="yellow")
plt.xlabel('category')
plt.ylabel('count')
plt.title('furnitures sold in each category')
plt.show()









#plt.pie(sorted_furn, sorted_furn.index, colors = ['skyblue', 'lightgreen', 'orange', 'salmon', 'lightpink', 'lightyellow', 'lightblue'])
#plt.axis('equal')
#plt.title('furniture distribution of each category')


# In[82]:


#4.TOP 3 HIGHST CATEGORY WITH ONLINE PRESENCE (BASED ON SALES)

data_online = data_ikea[data_ikea['sellable_online']==True]
#print(data_online)

cat_online= data_online.groupby('category')['price'].sum().reset_index()
#print(cat_online)
sorted_values = cat_online.sort_values(by= "price",ascending= False)
#print(sorted_values)
t=sorted_values.head(3)

###VIZ 
plt.figure(figsize=(8,6))
plt.bar(t['category'],t['price'],color='lightgreen')
plt.xlabel('category')
plt.ylabel('price')
plt.title('top 3 category with online presence -sales based')
plt.show()


# In[112]:


#5.TOP 5 HIGHEST CATEGORY FOR OFFLINE PRESENCE (SALES BASED)

offline_p = data_ikea[data_ikea['sellable_online']==False]
#print(offline_p)
top5_highest_cat = offline_p.groupby('category')['price'].sum().reset_index()
sorted_values = top5_highest_cat.sort_values(by="price",ascending=False)
#print(sorted_values)
b =sorted_values.head(5)

plt.figure(figsize=(8,6))
plt.bar(b['category'],b['price'], color= 'orange')
plt.xlabel('category')
plt.ylabel('price')
plt.title('top 5 highest category for offline presence')
plt.show()


# In[115]:


#6.CORELATION BETWEEN THE COLUMNS OF DATASET USINF HEATMAP
 
import warnings
warnings.filterwarnings("ignore")
corr = data_ikea.corr()
corr


# In[116]:


sns.heatmap(corr, annot = True,cmap = 'coolwarm')


# sns.relplot(x ='price',y='item_id',hue = 'category',data= data_ikea[:200])

# In[191]:


#INSIGHT 7.
sns.scatterplot(x ='price',y='category',hue= 'designer',data= data_ikea[:20])


# In[187]:


#8.Visualize the distribution of the 'price'
sns.histplot(data_ikea['price'],bins=20)


# In[145]:


#9.AVERAGE PRICE OF FURNITURE IN EACH CATEGORY.

data = data_ikea.groupby('category')['price'].mean().reset_index()
#print(data)
sorted_values = data.sort_values(by='price',ascending=False)
b= sorted_values.head()

plt.figure(figsize=(8,6))
plt.bar(b['category'],b['price'],color='yellow')
plt.xlabel('category')
plt.ylabel('price')
plt.title('avg price for each category')
plt.xticks(rotation=30)
plt.show()


# In[149]:


#10.CREATING CORELATION BETWEEN 'price', 'depth', 'height', and 'width' columns 


heatmap_data = data_ikea[['price', 'depth', 'height','width']]

plt.figure(figsize=(8,6))
sns.heatmap(heatmap_data.corr(),annot =True,cmap="coolwarm",fmt='.2f',center=0)


plt.xlabel('features')
plt.ylabel('features')
plt.title('Corelation Heatmap')
plt.show()


# In[177]:


#11.Create a pie chart to show the proportion of 'sellable_online' and 'not sellable_online' furniture.

##ONLINE
data_online = data_ikea[data_ikea['sellable_online']==True]
furn_online = data_online['sellable_online'].value_counts()
#print(furn_online)

##OFFLINE
data_offline = data_ikea[data_ikea['sellable_online']==False]
furn_offline = data_offline['sellable_online'].value_counts()
#print(furn_offline)

labels = ['online', 'offline']
sizes = [furn_online,furn_offline]
colors= ['coral','lightblue']


plt.pie(sizes,labels= labels,colors = colors,shadow= True)
plt.axis('equal')
plt.title('Proportion of Sellable and Not Sellable Furniture')

plt.show()


# In[185]:


#MULTIPLE BOX PLOTS
##12.Visualize the distribution of 'price' for each 'category' using box plots.

data= data_ikea.groupby('category')['price'].sum().reset_index()
sns.boxplot(d=data[['price','category']],orient= 'vertical')

plt.figure(figsize=(8,6))
plt.title('distribution for price in each category')
plt.xlabel('variable')
plt.ylabel('value')
plt.show()  


# In[ ]:




