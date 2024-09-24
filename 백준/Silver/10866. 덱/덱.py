import sys

arr = []

def deque(command, n):
    global arr
    length = len(arr)
    
    if command == "push_front":
        arr = [n] + arr
    
    elif command == "push_back":
        arr.append(n)
        
    elif command == "pop_front":
        if length == 0:
            print(-1)
        else: 
            print(arr[0])
            del arr[0]
        
    elif command == "pop_back":
        if length == 0:
            print(-1)
        else: 
            print(arr[length - 1])
            arr.pop()
            
    elif command == "size":
        print(length)
        
    elif command == "empty":
        if length > 0:
            print(0)
        else:
            print(1)
            
    elif command == "front":
        if length == 0:
            print(-1)
        else:
            print(arr[0])
        
    elif command == "back":
        if length == 0:
            print(-1)
        else:
            print(arr[length - 1])


cnt = int(input())

for i in range(cnt):
    user_input = sys.stdin.readline().split()
    if len(user_input) == 1:
        user_input.append("0")
        
    deque(user_input[0], int(user_input[1]))
    