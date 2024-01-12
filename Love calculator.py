#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Welcome to the Love Calculator!")
name1 = input("What is your name ? \n")
name2 = input("What is their name ? \n")
l = 0
t = 0

name = name1+name2
name = name.lower()
love = "love"
true = "true"
for i in love:
    l = l + name.count(i)
    
for j in true:
    t = t+name.count(j)
    
total = str(t)+str(l)
total = int(total)
if (total <10 or total >90 ):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif (40<total>50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")


# In[ ]:




