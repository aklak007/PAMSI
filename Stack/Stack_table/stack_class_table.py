#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Stack_class:

    def __init__(self, size=10):#inicjalizacja tablicy stosu
        self.content = size * [None]#zawiera 10 none'ow  
        self.number = 0# liczba elementów stosu                  
        self.size = size# liczba elementów stosu  
        
    def __str__(self):# wypisywanie stosu
        return str(self.content[:self.number])

    def empty(self):
        return self.number == 0

    def full(self):
        return self.size == self.number

    def push(self, data):
        self.content[self.number] = data
        self.number += 1

    def pop(self):
        self.number -= 1
        data = self.content[self.number]
        self.content[self.number] = None    # usuwam referencję
        return data

    def pop_all(self):#usuwa wszystkie elementy
        while not self.empty():
            self.pop()
           
