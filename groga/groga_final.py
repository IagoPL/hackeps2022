#!/usr/bin/env python
# coding: utf-8

# In[94]:


import pandas as pd
import os
pd.__version__


# In[95]:


types = ["liso", "punto", "tejido_sofa", "mimbre", "cuadros", "rayas", "estampado_floral1", "estampado_floral2"]
prefix = ["c1r1", "c1r3", "c2r2", "c2r3", "c3r1", "c3r3", "c4r1", "c4r3"]
conection = list(zip(prefix, types))
columns = ["Name", "Pattern"]
Y_list_names = []
lst = []


# In[96]:


for (dir_path, dir_names, file_names) in os.walk("files/A1/A1/"): 
		for files in file_names:
			if files.endswith(".tif"):
				Y_list_names.append(files)


# In[97]:


for prefix, pattern in conection:
    for name in Y_list_names:
        if name.startswith(prefix):
            lst.append([name, pattern])
df = pd.DataFrame(lst, columns=columns)


# In[100]:


df.to_csv("groga.csv")


# In[101]:


df

