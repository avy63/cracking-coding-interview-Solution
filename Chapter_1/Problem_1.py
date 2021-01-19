#traverse all the elements in  a string and store the element in a dictionary
#if it already presents return False
# Last return True as no repited elemnet
def isUnique(string):
     dic={}
     for s in string:
          if s in dic:
               return False
          else:
               dic[s]=1
     return True
#Time complexity  O(n)
#Space complexity O(n)
# can we do better in space complexity?
#Ofcourse using sort
def isUnique_without_extraspace(string):
     
     string=sorted(string)
     for i in range(len(string)-1):
          if string[i]==string[i+1]:
               return False
     return True
#Time complexity: O(nlogn)
#Space complexity: O(1)
string1 ="abcdebcd"
string2="aaaaa"
string3="abcdefghijklmnopqrstuvwxyz"
print(isUnique(string1))
print(isUnique(string2))
print(isUnique(string3))

print(isUnique_without_extraspace(string1))
print(isUnique_without_extraspace(string2))
print(isUnique_without_extraspace(string3))
