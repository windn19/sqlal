class StackMax:
   def __init__(self):
       self.stack = []
       self.maxs = []
       self.len = 0

   def push(self, value):
       self.stack.append(value)
       if self.maxs == [] or value >= self.maxs[-1]:
           self.maxs.append(value)
       self.len += 1

   def pop(self):
       if self.stack:
           temp = self.stack.pop()
           if not self.stack:
               self.maxs = []
           elif temp == self.maxs[-1]:
               self.maxs.pop()
           self.len -= 1
       else:
           print('error')

   def size(self):
       print(self.len)

   def get_max(self):
       return self.maxs[-1] if self.maxs else None


n = int(input())
stack = StackMax()
for i in range(n):
   commands = input().split()
   if commands[0] == 'get_max':
       print(stack.get_max())
   elif commands[0] == 'size':
       stack.size()
   elif commands[0] == 'pop':
       stack.pop()
   elif commands[0] == 'push':
       stack.push(int(commands[1]))