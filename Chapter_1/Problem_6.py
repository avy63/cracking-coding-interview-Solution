def string_comppression(string):
     temp_str=''
     i=0
     while i<len(string)-1:
          cn=1
          while i<len(string)-1 and string[i]==string[i+1] :
               i+=1
               cn+=1
          temp_str+=string[i]+str(cn)
          i+=1
     if string[-1]!=string[-2]:
          temp_str+=string[-1]+str(1)
     return temp_str if len(temp_str)<len(string) else string
print(string_comppression('aabcccccaaa'))
print(string_comppression('aabcccccaaab'))
print(string_comppression('abcdefghij'))
