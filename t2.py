stack = []

s = input()

for char in s:
   if char == '(':
       stack.append(char)
   elif char == ')':
       if not stack:
           print(False)
           break
       stack.pop()
else:
   if stack:
       print(False)
   else:
       print(True)