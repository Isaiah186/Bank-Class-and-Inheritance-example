#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Bank:
    def __init__(self):
        pass
    
    def deposit(self,amount):
        print(f"You have deposited {amount} in your bank account.")
        
    def savings(self,amount):
        print(f"You have {amount} in your savings.")
        
    def withdrawal(self,amount):
        print(f"You have removed {amount} from your account")
    


# In[2]:


Bank_obj = Bank()


# In[4]:


Bank_obj.deposit(60)


# In[5]:


Bank_obj.savings(21)


# In[6]:


Bank_obj.withdrawal(31)


# In[ ]:




