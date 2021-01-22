def palindrome_permutation(string):
     dic={}
     string=string.lower()
     for char in string:
          if char.isalpha():
               if char in dic:
                    dic[char]+=1
               else:
                    dic[char]=1
     
     cn=0
     for key in dic:
         if dic[key]%2==1:
              cn+=1
     return cn<=1
string="Tact coapp"
          
print(palindrome_permutation(string))
