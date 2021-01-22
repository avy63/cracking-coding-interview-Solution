def one_away(string1,string2):
     dic1={}
     dic2={}
     if len(string2)>len(string1):
          string1,string2=string2,string1
     for s in string1:
          if s in dic1:
               dic1[s]+=1
          else:
               dic1[s]=1
     for s in string2:
          if s in dic2:
               dic2[s]+=1
          else:
               dic2[s]=1
     cn=0
     for key in dic1:
          if key in dic2:
               cn=cn+abs(dic2[key]-dic1[key])
          else:
               cn=cn+dic1[key]
     return cn<=1
# Time complexity O(max(N,M))
# Space compexity O(N+M)
def one_away_without_space(string1,string2):
     if abs(len(string1)-len(string2)>1):
          return False
     string1="".join(sorted(string1))
     string2="".join(sorted(string2))
     if len(string2)>len(string1):
          string1,string2=string2,string1
     i=0
     j=0
     cn=0
     while i<len(string1) and j<len(string2):
          if cn>1:
               return False
          if string1[i]!=string2[j] and string1[i]==string[j+1]:
               j=j+1
          elif string1[i]!=string2[j]:
               i=i+1
               j=j+1
               cn+=1
          else:
               i=i+1
               j=j+1
               
          
     
s1='pale'
s2='bake'
print(one_away(s1,s2))
s1='pale'
s2='ple'
print(one_away(s1,s2))
s1='pale'
s2='pales'
print(one_away(s1,s2))
s1='pale'
s2='bale'
print(one_away(s1,s2))
