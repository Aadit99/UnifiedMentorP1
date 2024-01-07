#!/usr/bin/env python
# coding: utf-8

# # Amazon Sales Data Analysis Unified Mentor Project 1

# ### Importing necessary libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Loading the dataset

# In[2]:


sales_data = pd.read_csv("Amazon Sales data.csv")
sales_data.head()


# ### Checking for null values for data cleaning

# In[3]:


sales_data.isna().sum()


# In[4]:


sales_data.describe()


# In[5]:


sales_data.info()


# ### Adding Year and month column to the dataset

# In[6]:


sales_data["Year"] = pd.to_datetime(sales_data["Order Date"]).dt.year
sales_data["Month"] = pd.to_datetime(sales_data["Order Date"]).dt.month
sales_data.head()


# In[7]:


yearly_figures = sales_data.groupby("Year")[["Total Revenue","Total Cost","Total Profit"]].sum().reset_index()
yearly_figures.head()


# ### Visualising the Trends year wise

# In[8]:


plt.plot(yearly_figures.Year,yearly_figures["Total Revenue"])
plt.xlabel("Year")
plt.ylabel("Total Revenue (in tens of millions)")
plt.title("Yearly Revenue")
plt.show()


# In[9]:


plt.plot(yearly_figures.Year,yearly_figures["Total Profit"])
plt.xlabel("Year")
plt.ylabel("Total Profite (in millions)")
plt.title("Yearly Profit")
plt.show()


# In[10]:


plt.plot(yearly_figures.Year,yearly_figures["Total Cost"])
plt.xlabel("Year")
plt.ylabel("Total Cost (in tens of millions)")
plt.title("Yearly Costs")
plt.show()


# In[11]:


width=0.40
plt.bar(yearly_figures.Year-0.2,yearly_figures["Total Revenue"],width,label="Total Revenue")
plt.bar(yearly_figures.Year+0.2,yearly_figures["Total Profit"],width,label="Total Profit")
plt.legend()
plt.title("Total Revenue and Profit Year Wise")
plt.ylabel("Tens of Millions ($)")
plt.xlabel("Year")
plt.show()


# ### Dividing the data Yearly-month wise and analyzing the trends

# In[12]:


yearlymonth_figures = sales_data.groupby(["Year","Month"])[["Total Revenue","Total Cost","Total Profit"]].sum().reset_index()
yearlymonth_figures["Yearmonth"] = yearlymonth_figures["Year"].astype(str) + '_' + yearlymonth_figures["Month"].astype(str)
yearlymonth_figures = yearlymonth_figures[["Yearmonth","Total Revenue","Total Cost","Total Profit"]]
yearlymonth_figures.head()


# In[13]:


plt.figure(figsize=(15, 5), dpi=80)
plt.ylabel("Millions ($)")
plt.title("Total Revenue Year_month Wise")
plt.xlabel("Yearmonth")
plt.plot(yearlymonth_figures["Yearmonth"],yearlymonth_figures["Total Revenue"])
plt.xticks(rotation=90)
plt.show()


# In[14]:


plt.figure(figsize=(15, 5), dpi=80)
plt.ylabel("Millions ($)")
plt.title("Total Profit Year_month Wise")
plt.xlabel("Yearmonth")
plt.plot(yearlymonth_figures["Yearmonth"],yearlymonth_figures["Total Profit"])
plt.xticks(rotation=90)
plt.show()


# ### Country wise trend analysis

# In[15]:


country_figures = sales_data.groupby("Country")[["Total Revenue","Total Cost","Total Profit"]].sum().reset_index()
country_figures.head()


# In[16]:


country_figures[country_figures["Total Revenue"]==country_figures["Total Revenue"].max()]


# In[17]:


country_figures[country_figures["Total Profit"]==country_figures["Total Profit"].max()]


# In[18]:


country_figures[country_figures["Total Cost"]==country_figures["Total Cost"].max()]


# ### Item type wise trend analysis

# In[19]:


item_type_figures = sales_data.groupby("Item Type")[["Total Revenue","Total Cost","Total Profit"]].sum().reset_index()
item_type_figures.head()


# In[20]:


x=np.arange(12)
plt.bar(x-0.2,item_type_figures["Total Revenue"],width,label="Total Revenue")
plt.bar(x+0.2,item_type_figures["Total Profit"],width,label="Total Profit")
plt.legend()
plt.ylabel("Tens of Millions ($)")
plt.title("Total Revenue and Profit Item Type Wise")
plt.xlabel("Item Type")
plt.xticks(ticks=x,labels=item_type_figures["Item Type"],rotation=90)
plt.show()


# ### Sales Channel Wise trend analysis 

# In[21]:


sales_channel_figures = sales_data.groupby("Sales Channel")[["Total Revenue","Total Cost","Total Profit"]].sum().reset_index()
sales_channel_figures.head()


# In[23]:


x=np.arange(2)
width=0.4
plt.bar(x-0.2,sales_channel_figures["Total Revenue"],width,label="Total Revenue")
plt.bar(x+0.2,sales_channel_figures["Total Profit"],width,label="Total Profit")
plt.legend()
plt.title("Total Revenue and Profit Sales Channel Wise")
plt.ylabel("Tens of Millions ($)")
plt.xlabel("Sales Channel")
plt.xticks(ticks=x,labels=sales_channel_figures["Sales Channel"])
plt.show()

