#Not a great solution
def URLify(string):
     string=string.strip()
     string=list(string)
     tempstr=""
     for s in string:
          if s==' ':
               tempstr+='%20'
          else:
               tempstr+=s
     return tempstr
# Time complexity O(N)
# space complexity O(N)

def URLify_without_extra_mem(string):
     string=string.strip()
     string=string.replace(' ',"%20")
     return string
# Time complexity O(N)
# space complexity O(1)
string="Mr John Smith"
print(URLify(string))
print(URLify_without_extra_mem(string))
