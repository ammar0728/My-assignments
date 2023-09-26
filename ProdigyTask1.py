#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

# Sample data
categories = ["Male", "Female", "Non-binary"]
counts = [250, 300, 50]

# Create a bar chart
plt.bar(categories, counts, color=['blue', 'pink', 'purple'])

# Customize the chart
plt.title("Distribution of Genders")
plt.xlabel("Gender")
plt.ylabel("Count")

# Show the chart
plt.show()


# In[3]:


import pandas as pd

# Sample dataset for age distribution
age_data = [25, 30, 35, 40, 42, 45, 50, 52, 55, 60, 65, 70, 75, 80]

# Histogram for age distribution
plt.figure(figsize=(8, 6))
plt.hist(age_data, bins=5, edgecolor='k', color='skyblue')  # Adjust the number of bins as needed
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Show the histogram
plt.show()


# In[ ]:




