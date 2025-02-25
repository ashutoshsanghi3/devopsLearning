#Create a list of fruits and sort it
from heapq import heappop,heappush,heapify 
list=["apple","grapes","banana","mango","kiwi"]
list.sort()  #it modifies and sorts the original list and return None
#it works only on lists
# sorted(list) #it returns a new sorted list
#it works on list,tuples,etc.
list.reverse()
# print(list)

list=[5,2,7,4,8,1]
# list.sort()
# print(f"Smallest is {list[0]}\nLargest is {list[len(list)-1]}")


#Get second largest and second smallest element in list

#heap is like binary tree where smallest is at top and we only have information regarding the top
#element
def second_smallest(arr):
    heap=[]
    heapify(heap)
    for i in arr:
        heappush(heap,i)
    
    heappop(heap)
    return heappop(heap)

def second_largest(arr):
    heap=[]
    heapify(heap)
    for i in arr:
        heappush(heap,-1*i)
    heappop(heap)
    return -1*heappop(heap)
# print(second_smallest(list))
# print(second_largest(list))

def second_largest_element(arr):

    first_max=-1e9
    sec_max=-1e9
    for i in arr:
        if first_max == -1e9:
            first_max=i
        elif sec_max == -1e9:
            if(first_max<i):
                sec_max=first_max
                first_max=i
            else:
                sec_max=i
        else:
            if(first_max<i):
                sec_max=first_max
                first_max=i
            elif(sec_max<i and i>first_max):
                sec_max=i

    return sec_max

# print(second_largest_element(list))

#print character repeating the most in list
def most_repeated_element(word):
    freq=[0]*26
    ind=0
    max_freq=0
    for i in word:
        freq[ord(i)-ord('a')]+=1
    
    for i in range(0,26):
        if(max_freq<freq[i]):
            max_freq=freq[i]
            ind=i

    return chr(ord('a')+ind)

# print(most_repeated_element("ssaahhsss"))

#Print list of strings where you remove first and last string
word_arr=["sbc","fds","efa","adw","fkk","mcd","mcd"]
# print(word_arr[1:-1])



# word_arr.pop(0)  #it will pop at 0th index
# word_arr.append("trw") #it will insert at last index
# word_arr.insert(3,"few")  #it will insert at 3rd index
# del word_arr[2] #it will delete the 2nd index element
# word_arr.clear() #it will delete the entire list
# print(word_arr.count("mcd")) #it will give occurence of word in list
print(word_arr)

#print first,middle,last element in list
n=len(word_arr)-1
mid=n//2
print(word_arr[0])
print(word_arr[mid])
print(word_arr[n])

