arr = []
def queue(command, n):
    length = len(arr)
    
    if command == "push":
        arr.append(n)
        
    elif command == "pop":
        if length == 0:
            print(-1)
        else:
            print(arr[0])
            del arr[0]
    
    elif command == "size":
        print(length)
        
    elif command == "empty":
        if length == 0:
            print(1)
        else:
            print(0)
            
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
    user_input = input().split()
    if len(user_input) == 1:
        user_input.append(0)
        
    queue(user_input[0], int(user_input[1]))
