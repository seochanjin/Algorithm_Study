from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progress_q = deque(progresses)
    speed_q = deque(speeds)
    
    while progress_q:
        for i in range(len(progress_q)):
            progress_q[i] += speed_q[i]
        
        count = 0
        
        while progress_q and progress_q[0] >= 100:
            progress_q.popleft()
            speed_q.popleft()
            count += 1
            
        if count > 0:
            answer.append(count)
    
    return answer