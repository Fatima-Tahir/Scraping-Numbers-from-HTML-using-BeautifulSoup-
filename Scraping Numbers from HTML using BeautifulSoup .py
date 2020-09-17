#!/usr/bin/env python
# coding: utf-8

# In[19]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
add=0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    x=(tag.contents)
    print (x[0])
    add=add+int(x[0])
print(add)
    
  
    


# In[ ]:





# In[ ]:




