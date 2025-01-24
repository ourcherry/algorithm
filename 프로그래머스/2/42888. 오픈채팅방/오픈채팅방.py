def solution(record):
    preanswer = []
    answer = []
    accounts = {}
    
    # data 가공
    for i in range(len(record)):
        rec = record[i].split()
        if rec[0] == "Enter":
            accounts[rec[1]] = rec[2]
            item = rec[1] + "님이 들어왔습니다."
            preanswer.append(item)
        elif rec[0] == "Leave":
            item = rec[1] + "님이 나갔습니다."
            preanswer.append(item)
        elif rec[0] == "Change":
            accounts[rec[1]] = rec[2]
    
    for i in range(len(preanswer)):
        id = preanswer[i].split("님")[0]
        answer.append(preanswer[i].replace(id, accounts[id]))
        
    # print(answer)
    
    return answer