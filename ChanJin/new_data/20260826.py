def to_min(time_str):
    h, m = map(int, time_str.split(':'))
    return h*60 + m

def solution(book_time):
    
    times = [(to_min(s), to_min(e) + 10) for s, e in book_time]
    times.sort()
    
    rooms = []
    
    for start, end in times:
        used = False
        for i in range(len(rooms)):
            if rooms[i] <= start:
                rooms[i] = end
                used = True
                break
        if not used:
            rooms.append(end)
        
    return len(rooms)