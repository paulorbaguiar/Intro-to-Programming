progress = 0
gameRun = True
setLocal = int(input())

while gameRun == True:
    mapLoc = int(input())
    if mapLoc >= 0:
        for i in range(0, mapLoc + 1):
            progress = progress + i
    else:
        gameRun = False

print(progress)
