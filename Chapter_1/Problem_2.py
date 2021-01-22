#Sort 2 string then just compare 2 string
def isPermutation(string1,string2):
     string1="".join(sorted(string1))
     string2="".join(sorted(string2))
     return string1==string2
#Time complexity O(nlogn)
#space complexity O(1)
#can we do better?
#Yes... using hashmap
def isPermutation_extra_space(string1,string2):
     dic={}
     for s in string1:
          if s in dic:
               dic[s]+=1
          else:
               dic[s]=1
     for s in string2:
          if s in dic:
               dic[s]=dic[s]-1
               if dic[s]==0:
                    del dic[s]
          else:
               return False
     return len(dic)==0
# Time complexity= O(n)
# Space compexity = O(n)
string1="abcdef"
string2="cdabfea"
print(isPermutation(string1,string2))
print(isPermutation_extra_space(string1,string2))
