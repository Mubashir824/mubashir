#!/usr/bin/env python
# coding: utf-8

# In[3]:


Quiz = [
    {
        "qu": "Qno1)What is the Capital of pakistan",
         "op": ["a)Islamabad"  , "b)karachi", "c) balochistan"  "d) Lahore"  ], 
    },   
    {
         "Q2": "Qno2)The first mechanical computer designed by charles babbage was called", 
        "op":["a)Calculator" , "b)analytical ingine", "c) Abacus"  "d) processor"],        
    },
    { 
        "Q3": "www stand for?",
        "op":["a)Wan wide world" , "b)world wide wed", "c) World Wan wed "  "d) white"], 
    }, 
    { 
        "Q4": "which theory is known as Eistein theory ?",
        "op":["a)evolution theory" , "b)Big bang theory",  "c) Theory of relativily", "d) newton's theory"], 
    }, 
    { 
        "Q5": "Which of this number is not even?",
        "op":["a)2" , "b)6", "c) 9"  "d) 12"], 
    }, 
]
ans = ["a" , "b" ,"b" ,"c", "c"]
i=0

for question in Quiz:
    answer = input(question)
    
    if answer ==ans[i]:
        i = i+1
        print("\n correct answer: ")
    else:    
        print("\n wrong answer")


# In[ ]:





# In[ ]:





# In[ ]:




