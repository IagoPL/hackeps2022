#!/usr/bin/env python
# coding: utf-8

# In[206]:


import pandas as pd


# In[207]:


df = pd.read_csv("img_tag.csv")
df = df.dropna()


# In[208]:


dades = list(zip(df.name, df.text))
columns = ["Name", "Defect"]
lst = []


# In[209]:


id_defectos = {
    "agujeros": ["grieta", "agujero"],
    "marcas": ["defecto"],
    "manchas": ["mancha"],
    "pliegues": ["pliegue"],
    "rayas_colores": ["raya", "franja"],
    "ignore": ["cámara", "luz", "lámpara", "corta"]
}


# In[210]:


def check_id(value, text):
    if any(word in text for word in value):
        return True
    else:
        return False


# In[211]:


for name, desc in dades:
    other = True
    for key, value in id_defectos.items():
        desc = desc.lower()
        if check_id(value, desc):
            other = False
            if key != "ignore":
                lst.append([name, key])
                break
    if other:
        lst.append([name, "other"])
    
df2 = pd.DataFrame(lst, columns=columns)       
            


# In[212]:


df2.to_csv('vermella.csv')

