#!/usr/bin/env python
# coding: utf-8

# In[1]:


#example 21
a=["ahmed","mohamed","omar"]
list(a)


# In[2]:


#example 21


def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
list=["ahmed","mohamed","mahmoud"]

pos1, pos2  = 1, 3
 
print(swapPositions(list, pos1-1, pos2-1))


# In[3]:


#example 22

def swapposition(list,pos1,pos2):
 list[pos1],list[pos2]=list[pos2],list[pos1]
 return list
list = [23, 65, 19, 90]
pos1, pos2  = 1, 3
print(swapPositions(list, pos1-1, pos2-1))


# In[4]:


#example 23
a="lionel messi"
len(a)
print(len(a))


# In[5]:


#example 25
a=[22,90,199]
print(max(a))


# In[6]:


#example 27
a=["mohamed","ahmed","yasser"]
a.remove("ahmed")
print(a)


# In[7]:


#example 32
n = 6
a1 = [1,2,2,3,4,5]
a2 = []
for i in range(1, n):
    r = max(a1[i], a1[i-1])
    a2.append(r)
for i in a2 :
    print(i)


# In[8]:


#example 33
def comb(L):
      
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i!=j and j!=k and i!=k):
                    print(L[i], L[j], L[k])


# In[9]:


#example 34
x=["a","b"]
y=[1,2]
print(x[0],y[0])
print(x[1],y[1])
print(x[0],y[1])
print(x[1],y[0])


# In[10]:


#example 35
list=[1,1,2,3,4,5,1,2,1 ]
l=1
x=[i for i in list if i!=l]
print(x)
    


# In[11]:


#example 37
list1=['Gfg', 'is', 'best']
list2=[0,1,2,1,0,0,0,2, 1, 1, 2, 0]
for item in list1:
    print(list1[0],list1[1],list1[2],list1[1],list1[0],list1[0],list1[0],list1[2],list1[1],list1[1],list1[2],list1[0])


# In[12]:


#example 41
test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘geeks’ : ‘CS’},\n",
for item in test_dict :
    if item<7:
        print(item)


# In[17]:


#example 48
a=("mohamed",22,"cairo")
(name,age,univercity)=a
print(name)
print(age)
print(univercity)


# In[18]:


#example 49
a=(1,2,3)
b=(6,7,)
a=a+b
print(a)


# In[19]:


#example 50
a=('a','e','f','y')
str=''.join(a)
print(str)


# In[22]:


#example 51
list=[1,10,20]
tuple=tuple(list)
print(tuple)



# In[29]:


#example 52
tuple1=(10,20,40)
list1=list(tuple)
list1[2]=100
tuple1=tuple(list)
print(tuple1)


# In[32]:


#example 54
x = ("mohamed", "ahmed", "yasser")
y = list(x)
y[1] = "mahmoud"
x = tuple(y)
print(x)


# In[40]:


#example 55
x=(1,2,3,4)
print(sum(x)/len(x))
 


# In[41]:


#exaple 56
x=(1,10,20)
b=(40,)
x=x+b
print(x)


# In[45]:


#EXAMPLE 57
x = ["mohamed", "ahmed", "yasser"]
x.remove("ahmed")
print(x)


# In[47]:


#example 58
a={1,2,3,4}
b={5,4,3,98,10}
print(a|b)
print(a-b)
print(a&b)
print(a^b)


# In[ ]:




