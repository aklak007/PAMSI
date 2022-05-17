#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Stack_class:

    def __init__(self):
        self.content = []

    def __str__(self):# wypisywanie stosu
        return str(self.content)
    
    def empty(self):        # Sprawdza czy stos jest pusty
        if len(self.content) == 0 : return True
        else : return False

    def push(self, contents):#dodaje element
        self.content.append(contents)        

    def pop(self):#usuwa element                  
        return self.content.pop()         
        
    def size(self):# liczba elementow stosu
        return len(self.content)

    def pop_all(self):#usuwa wszystkie elementyelement
        while not self.empty():
            self.pop()  
