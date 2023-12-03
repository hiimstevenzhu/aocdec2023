with open("day3/day3input.txt", "r") as file:
    content = file.read()
    
    

            
def findClusters(pos, mtx):
    visited = []
    clusters = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= pos[0] < len(mtx) and 0 <= pos[1] < len(mtx[0]):
                if mtx[pos[0]+i][pos[1]+j].isdigit():
                    data = spread(mtx, pos[0] + i, pos[1] +j)
                    print(data)
                    cluster = data[0]
                    if data[1] not in visited:
                        clusters.append(cluster)
                        print(clusters)
                        visited.append(data[1])
    return clusters

def spread(mtx, ypos, xpos):
    maxlen = len(mtx[ypos])
    cur = mtx[ypos][xpos]
    flagneg = 0
    flagpos = 0
    maxpos = xpos
    maxneg = xpos
    for i in range(1,maxlen):
        if xpos + i < maxlen:
            if mtx[ypos][xpos + i].isdigit() and not flagpos:
                cur = cur + mtx[ypos][xpos + i]
                maxpos = xpos+i
            else:
                flagpos = 1
        if xpos - i >= 0:
            if mtx[ypos][xpos - i].isdigit() and not flagneg:
                cur = mtx[ypos][xpos - i] + cur
                maxneg = xpos-i
            else:
                flagneg = 1
    return (cur, (ypos, (maxpos, maxneg)))

lines = content.split('\n')
mtx = [0] * len(lines)
for idx in range(len(lines)):
    mtx[idx] = lines[idx]
sum = 0
print(mtx)
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] == "*":
            clusters = findClusters((i, j), mtx)
            if len(clusters) == 2:
                total = 1
                for k in clusters:
                    total *= int(k)
                sum += total
print(sum)