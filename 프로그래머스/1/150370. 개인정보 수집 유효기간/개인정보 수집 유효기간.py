import datetime

def solution(today, terms, privacies):
    answer = []
    dic = {}
    today_year = int(today[0:4])
    today_month = int(today[5:7])
    today_date = int(today[8:10])
    today_days = today_year * 12 * 28 + today_month * 28 + today_date
    
    # terms dictionary
    for t in terms:
        tterm = t[0:1]
        tmonth = int(t[2:]) * 28
        dic[tterm] = tmonth
    
    for i in range(len(privacies)):
        term = privacies[i][11:12]
        
        year = int(privacies[i][0:4])
        month = int(privacies[i][5:7])
        date = int(privacies[i][8:10])
        days = year * 12 * 28 + month * 28 + date
        
        period = today_days - days
        delayed = dic[term] - period
        
        if (delayed <= 0):
            answer.append(i + 1)
    
    print(answer)
    
    return answer