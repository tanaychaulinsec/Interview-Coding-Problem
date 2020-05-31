from collections import deque
def floodFill(image, sr, sc, newColor):
    color = image[sr][sc]
    q = deque()
    q.append((sr, sc))
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if color != newColor:
        while q:
            r, c = q.popleft()
            image[r][c] = newColor
            for dx, dy in dir:
                if 0 <= r + dx < len(image) and 0 <= c + dy < len(image[0]):
                    if image[r + dx][c + dy] == color:
                        q.append((r + dx, c + dy))
    return image

image=[[1,1,1],[1,1,0],[1,0,1]]
sr=1
sc=1
newColor=2
print (floodFill(image,sr,sc,newColor))
