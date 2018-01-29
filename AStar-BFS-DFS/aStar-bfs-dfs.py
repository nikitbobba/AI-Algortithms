def getNeighboursDFS(lst, testmap):
        nLst = []
        pathLst = []
        mapH = len(testmap)
        mapW = len(testmap[0])
        y = lst[0][0]
        x = lst[0][1]
        currPath = lst[1]
        pathLst = currPath

        if y - 1 < mapH and y - 1 >= 0:
                if testmap[y-1][x] not in (1,2,4):
                        cor = (y - 1, x)
                        path4 = currPath + [cor]
                        nLst.append((cor,path4))


        if x - 1 < mapW and x - 1 >= 0:
                if testmap[y][x-1] not in (1,2,4):
                        cor = (y, x - 1)
                        path3 = currPath + [cor]
                        nLst.append((cor,path3))
        

        if y + 1 < mapH:
                if testmap[y+1][x] not in (1,2,4):
                        cor = (y + 1, x)
                        path2 = currPath + [cor]
                        nLst.append((cor,path2))


        if x + 1 < mapW:
                if testmap[y][x+1] not in (1,2,4):
                        cor = (y, x + 1)
                        path1 = currPath + [cor]
                        nLst.append((cor,path1))
        
        
        
 
        return nLst

def dfs(testmap):
        mapH = len(testmap)
        mapW = len(testmap[0])
        startPos = findStart(testmap)
        q = []
        path = []
        q.append((startPos, [(startPos)]))
        while (len(q) > 0):
                temp = q.pop()
                yCor = temp[0][0]
                xCor = temp[0][1]
                if testmap[yCor][xCor] == 0:
                        testmap[yCor][xCor] = 4
                if testmap[yCor][xCor] == 3:
                        testmap[yCor][xCor] = 5
                        path = temp[1]
                        break

                neighbours = getNeighboursDFS(temp, testmap)
                q.extend(neighbours)
        
        pathLen = len(path)
        for i in range(0, pathLen):
                tempCor = path[i]
                tempY = tempCor[0]
                tempX = tempCor[1]
                testmap[tempY][tempX] = 5
        return testmap





def findStart(testmap):
        rows = len(testmap)
        cols = len(testmap[0])
        for y in range(0, rows -1):
                for x in range(0, cols -1):
                        if testmap[y][x] == 2:
                                #testmap[y][x] = 4
                                return (y, x)
    

def getNeighbours(lst, testmap):
        nLst = []
        pathLst = []
        mapH = len(testmap)
        mapW = len(testmap[0])
        y = lst[0][0]
        x = lst[0][1]
        currPath = lst[1]
        pathLst = currPath
        if x + 1 < mapW:
                if testmap[y][x+1] != 1 and testmap[y][x+1] != 4:
                        cor = (y, x + 1)
                        path1 = currPath + [cor]
                        nLst.append((cor,path1))
        if y + 1 < mapH:
                if testmap[y+1][x] != 1 and testmap[y+1][x] != 4:
                        cor = (y + 1, x)
                        path2 = currPath + [cor]
                        nLst.append((cor,path2))
        if x - 1 < mapW and x - 1 >= 0:
                if testmap[y][x-1] != 1 and testmap[y][x-1] != 4:
                        cor = (y, x - 1)
                        path3 = currPath + [cor]
                        nLst.append((cor,path3))
        if y - 1 < mapH and y - 1 >= 0:
                if testmap[y-1][x] != 1 and testmap[y-1][x] != 4:
                        cor = (y - 1, x)
                        path4 = currPath + [cor]
                        nLst.append((cor,path4))
 
        return nLst

                

def bfs(testmap):
        mapH = len(testmap)
        mapW = len(testmap[0])
        startPos = findStart(testmap)
        q = []
        path = []
        q.append((startPos, [(startPos)]))
        while (len(q) > 0):
                temp = q.pop(0)
                yCor = temp[0][0]
                xCor = temp[0][1]
                if testmap[yCor][xCor] == 0: #might want to have check for 2 here
                        testmap[yCor][xCor] = 4
                if testmap[yCor][xCor] == 3:
                        testmap[yCor][xCor] = 5
                        path = temp[1]
                        break

                neighbours = getNeighbours(temp, testmap)
                q.extend(neighbours)
        
        pathLen = len(path)
        for i in range(0, pathLen):
                tempCor = path[i]
                tempY = tempCor[0]
                tempX = tempCor[1]
                testmap[tempY][tempX] = 5
      
        return testmap




def expandNeighbours(curr, dis_map, time_map, end):
        key,val = curr.items()[0]
        fVal = val
        name = key
        gVal = fVal - dis_map[name][end]
        
        nList = {}
        for k in time_map[name]:
                if time_map[name].get(k) != None:
                        newGVal = time_map[name][k]
                        hVal = dis_map[k][end]
                        newFVal = gVal+newGVal+hVal
                        temp = {k: newFVal}
                        nList[k] = newFVal

        return nList
        

def findMin(OPEN):
        curr = {}
        minVal = 10000000000
        for i in OPEN.items():
                if i[1] < minVal:
                    minVal = i[1]
                    curr = {i[0]:i[1]}
                elif i[1] == minVal:
                    alphaMin = min({i[0]:i[1]}, curr)
                    curr = alphaMin
                #else:
                    #break

        return curr


def buildOpen(neighbours, CLOSED):
    n = neighbours.items()
    new = {}
    for i in n:
        if i[0] not in CLOSED: 
            new[i[0]] = i[1]

    return new
                

def a_star_search (dis_map, time_map, start,end):
        curr = {start: dis_map[start][end]}
        closedQ = {}
        openQ = curr
        score = {}
        while bool(openQ):
                curr = findMin(openQ)
                key,val = curr.items()[0]
                if key == end:
                        return score

                
                del openQ[key] 
                closedQ[key] = val 
                neighbours = expandNeighbours(curr,dis_map,time_map,end)
                score[key] = neighbours
                n = buildOpen(neighbours,closedQ)
                openQ.update(n)
                
                
                
                

        return score


