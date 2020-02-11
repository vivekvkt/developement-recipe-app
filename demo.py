# def reverse(str):
#     n = len(str)-1
#     rev = ""
#     while n>=0:
#         rev = rev +str[n]
#         n-=1
#     return rev
# s = "vivek"
# reverse(s)
# print(reverse(s))
#https://www.techbeamers.com/python-interview-questions-experienced/
# def reverse2(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
# s = "vivek"
# reverse2(s)
# print(reverse2(s))

# def reverseRecursive(str):
#     if len(str)==0:
#         return str
#     return  reverseRecursive(str[1:])+ str[0]
    
# s = "vivek"
# reverseRecursive(s)
# print(reverseRecursive(s))

# def isAlbhabet(x):
#     return x.isalpha()

# def reverse(str):
#     LIST = toList(str)
#     l = 0 
#     r = len(LIST)-1
    
#     while l<r:
        
#         if not isAlbhabet(LIST[l]):
#             l +=1
#         if not isAlbhabet(LIST[r]):
#             r -=1
#         else:
#             LIST[l],LIST[r] = swap(LIST[l],LIST[r])
#             l +=1
#             r -=1
#     return toString(LIST)

# def toList(str):
#     list = []
#     for i in str:
#         list.append(i)
#     return list
# def toString(list):
#     return ''.join(list)

# def swap(a,b):
#     return b, a

# s = 'v,i@vek'
# reverse(s)
# print(reverse(s))


# reverse word
# def wordReverse(str):
#     l1 = str.split()
#     len1 = len(l1)-1
#     list1 = []
#     while len1>=0:
#         list1.append(l1[len1])
#         len1 = len1-1
    
#     out = ' '.join(list1)
#     print(out)
# s = "hello vivek"
# wordReverse(s)


# def  placedReversed(str):
#     s = str.split()
#     i = 0
#     list1 = []
#     while i < len(s):
#         list1.append(s[i][::-1])
#         i +=1
        
#     out = ' '.join(list1)
#     print(out)
# s = "hello vivek"
# placedReversed(s)
        
#duplicate character
# string = "geeksforgeeks"
# for i in range(0, len(string)):  
#     count = 1;  
#     for j in range(i+1, len(string)):  
#         if(string[i] == string[j] and string[i] != ' '):  
#             count = count + 1  
#             #Set string[j] to 0 to avoid printing visited character  
#             string = string[:j] + '0' + string[j+1:] 
#     #A character is considered as duplicate if count is greater than 1  
#     if(count > 1 and string[i] != '0'):  
#         print(string[i])

# check to string anagram 

# def anagram(s1,s2):
    
#     if (sorted(s1)== sorted(s2)):
#         print("anagram")
#     else:
#         print("not anagram")
# s1 = "silent"
# s2 = "listen"
# anagram(s1,s2)

# max occurs characteers

# def maxOccurCharacter(str):
    
#     d = {}
#     for x in str:
#         if x in d.keys():
#             d[x] = d[x]+1
#         else:
#             d[x] = 1
#     for k,v in d.items():
#         print("{}-{}".format(k,v))

# s = "geekforgeeks"
# maxOccurCharacter(s)

 
class A:
    def m1(self):
         print("helo m1")
class B(A):
    def m1(self):
        print("hello chiled class m1")
        super().m1()
c = B()
c.m1()




    