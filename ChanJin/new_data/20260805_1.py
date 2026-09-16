def solution(arr):
    
    n = len(arr)
    count = [0, 0]
    
    def compress(x, y, size):
        first = arr[x][y]
        same = True
        for i in range(x, x+size):
            for j in range(y, y+size):
                if arr[i][j] != first:
                    same = False
                    break
            if not same:
                break
            
        if same:
            count[first] += 1
        else:
            half = size // 2
            compress(x, y, half)
            compress(x, y+half, half)
            compress(x+half, y, half)
            compress(x+half, y+half, half)
    
    compress(0,0,n)
    
    return count