#!/usr/bin/env python
# coding: utf-8

# In[ ]:

class sort_class:
    
    def merge(self, l_side, r_side):
        l_index=0
        r_index=0
        array=[]
        
        while l_index < len(l_side) and r_index < len(r_side):
            if l_side[l_index][2]<r_side[r_index][2]:
                array.append(l_side[l_index])
                l_index=l_index+1
            else:
                array.append(r_side[r_index])
                r_index=r_index+1
        while l_index < len(l_side):
            array.append(l_side[l_index])
            l_index=l_index+1
        while r_index < len(r_side):
            array.append(r_side[r_index])
            r_index=r_index+1
        return array
    
    def merge_sort(self, data_list):
    
        if len(data_list) <=1:
            return data_list
        else:
            middle = len(data_list)//2 
            left=data_list[:middle]
            right=data_list[middle:]

            left=self.merge_sort(left)
            right=self.merge_sort(right)
        return self.merge(left, right)

    
    def partition(self, data_list, low, high):

        pivot = data_list[high][2]
        j = low 

        for i in range(low, high):
            if data_list[i][2] <= pivot:     
                data_list[j], data_list[i] = data_list[i], data_list[j]
                j = j + 1

        data_list[j ], data_list[high] = data_list[high], data_list[j ]

        return j 

    def quick_sort(self, data_list, low, high):
        if len(data_list)<=1:
            return data_list
        if low < high:
            pivot = self.partition(data_list, low, high)

            self.quick_sort(data_list, low, pivot - 1)

            self.quick_sort(data_list, pivot + 1, high)
        return data_list
    
    
    def insertion_sort(self,data_list):
        for i in range(1, len(data_list)):
            up = data_list[i]
            j = i - 1
            while j >= 0 and data_list[j][2] > up[2]:
                data_list[j + 1] = data_list[j]
                j = j - 1
            data_list[j + 1] = up    
        return data_list    

    def bucket_sort(self,data_list):
        array = []
        slots = 10 
        for i in range(slots):
            array.append([])

        for j in data_list:
            index = int(slots * j[2]/10.0000001)
            array[index].append(j)

        for i in range(slots):
            array[i] = self.insertion_sort(array[i])

        k = 0
        for i in range(slots):
            for j in range(len(array[i])):
                data_list[k] = array[i][j]
                k = k+ 1
        return data_list

             
                
        