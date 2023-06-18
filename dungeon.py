from random import randint

def createEmptyDungeon():
    dungeon = []
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append("     ")
        dungeon.append(temp)
    return dungeon

def createRooms(dungeon):
    dungeon[0][0] = "room"

    coords = []
    with open("doors.txt", "r") as D:
        d = D.readlines()
        for k in d:
            k = k.split(":")
            coords.append(k)
            
    howMany = randint(0, 11)
    s = 0
    while s < howMany:
        which = randint(1, 11)
        for i, row in enumerate(coords):
            if i == which:
                coords[i][0] = 0
                s += 1

    for i, row in enumerate(coords):
        if coords[i][0] != 0:
            coords[i][0] = 1

    for i, rooms in enumerate(dungeon):
        for j, room in enumerate(rooms):
            s = str(i) + ";" + str(j)
            for y, row in enumerate(coords):
                if coords[y][1] == s and coords[y][0] == 1:
                    A = coords[y][1].split(';')[:1]
                    B = coords[y][1].split(';')[1:]
                    C = coords[y][2].split(';')[:1]
                    D = coords[y][2].split(';')[1:]
                    a = int(A[0])
                    b = int(B[0])
                    c = int(C[0])
                    d = int(D[0])
                    for k, rooms in enumerate(dungeon):
                        for l, room in enumerate(rooms):
                            if dungeon[c][d] != "room" and dungeon[a][b] == "room":
                                dungeon[c][d] = "room"
                                continue
    dungeon[0][0] = "entry"
    return dungeon

def createDungeon():
    emptyDungeon=createEmptyDungeon()
    dungeon=createRooms(emptyDungeon)
    return dungeon
    

dungeon=createDungeon()
#print(dungeon)
x=0
y=0
pozice=dungeon[x][y]
listPozic=[[0, 0]]

def dopredu(dungeon, x, listPozic):
    if x+1>len(dungeon)-1: print("konec mapy")
    elif dungeon[x+1][y]=="     ": print("konec mapy")
    else: x+=1; listPozic+=[[x, y]]
    return x, listPozic

def dozadu(x, listPozic):
    if x-1<0: print("konec mapy")
    elif dungeon[x-1][y]=="     ": print("konec mapy")
    else: x-=1; listPozic+=[[x, y]]
    return x, listPozic

def doleva(dungeon, x, y, listPozic):
    if y+1>len(dungeon[x])-1: print("konec mapy")
    elif dungeon[x][y+1]=="     ": print("konec mapy")
    else: y+=1; listPozic+=[[x, y]]
    return y, listPozic

def doprava(x, y, listPozic):
    if y-1<0: print("konec mapy")
    elif dungeon[x][y-1]=="     ": print("konec mapy")
    else: y-=1; listPozic+=[[x, y]]
    return y, listPozic

def zpet(listPozic):
    if len(listPozic)>1: listPozic.pop(); x=listPozic[-1][0]; y=listPozic[-1][1]
    else: x=listPozic[-1][0]; y=listPozic[-1][1]
    return x, y, listPozic

def pohyb(dungeon, x, y, listPozic, konec):
    prikaz=input("Quo Vadis? (dopredu/dozadu/doleva/doprava/zpet) ")
    if prikaz=="dopredu": x, listPozic=dopredu(dungeon, x, listPozic)
    elif prikaz=="dozadu": x, listPozic=dozadu(x, listPozic)
    elif prikaz=="doleva": y, listPozic=doleva(dungeon, x, y, listPozic)
    elif prikaz=="doprava": y, listPozic=doprava(x, y, listPozic)
    elif prikaz=="zpet": x, y, listPozic=zpet(listPozic)
    elif prikaz=="konec": konec=True
    elif prikaz=="mapa":
        for rooms in dungeon:
            for room in rooms:
                print(room + "     ", end=" ")
            print(end="\n")
    else: print("špatný příkaz")
    return x, y, listPozic, konec

konec=False
while konec==False: x, y, listPozic, konec=pohyb(dungeon, x, y, listPozic, konec); pozice=dungeon[x][y]#; print(pozice)

