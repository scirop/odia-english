
# coding: utf-8

# In[1]:


import flask


# In[ ]:


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

