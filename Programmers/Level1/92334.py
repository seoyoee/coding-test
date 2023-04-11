def solution(id_list, report, k):
    count = {id : 0 for id in id_list}
    reports = [[] for _ in range(len(id_list))]
    answer = [0] * len(id_list)
    
    for case in set(report):
        user, reported = case.split()
        count[reported] += 1
        reports[id_list.index(user)].append(reported)
        
    for i in range(len(count)):
        mail = 0
        for user in reports[i]:
            if count[user] >= k:
                mail += 1
        answer[i] = mail
    
    return answer