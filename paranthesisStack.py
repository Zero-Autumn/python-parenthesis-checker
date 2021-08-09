
li = input().split()

open = '[ { ( <'.split()
close = ') } ] >'.split()
print('input ',li)

class Stack:
    def __init__(self,si):
        self.size = si
        self.top = -1
        self.stack = ['']*self.size
    
    def push(self,data):
        if self.top >= self.size-1:
            raise Exception('Stack Full')
        else:
            self.top += 1
            self.stack[self.top] = data
            print('one push',st.stack)

    def pop(self):
        if self.top <0:
            raise Exception('Stack Empty')
        else:
            self.stack[self.top] = ''
            self.top -= 1
    
st = Stack(len(li))
print('start',st.stack)
def bracketOp(bracket):
    if bracket == ']':
        return '['
    elif bracket == ')':
        return '('
    elif bracket == '}':
        return '{'
    elif bracket == '>':
        return '<'
    

for bracket in li:
    print(1,bracket)
    if bracket in open:
        st.push(bracket)

    
    print(bracketOp(bracket))
    
    if bracket in close and bracketOp(bracket) != st.stack[st.top]:
        print('this')
        st.push(bracket)
    if bracket in close and bracketOp(bracket) == st.stack[st.top]:
        st.pop()
    print('1top',st.stack[st.top])
    

    print('top',st.stack[st.top])
print('resut')
if st.top>-1:
    print('Unbalanced')
    print(st.stack)
else:
    
    print('Balanced')
    print(st.stack)
