import matplotlib.pyplot as plt

def labeling(**options):
    plt.close("all")
    plt.figure(1)
    if "title" in options:
        plt.title(options["title"])
    if "xlabel" in options:
        plt.xlabel(options["xlabel"])
    if "ylabel" in options:
        plt.ylabel(options["ylabel"])
    if "xmin" in options:
        plt.xlim(xmin=options["xmin"])
    if "xmax" in options:
        plt.xlim(xmax=options["xmax"])
    if "ymin" in options:
        plt.ylim(ymin=options["ymin"])
    if "ymax" in options:
        plt.ylim(ymax=options["ymax"])
    if "grid" in options:
        plt.grid(options["grid"])

def histogram(data,**options):
    labeling(**options)
    hop = dict()
    if "bins" in options:
        hop["bins"] = options["bins"]
    if "color" in options:
        hop["color"] = options["color"]
    if "normalized" in options:
        hop["normed"] = options["normalized"]
    if "log" in options:
        hop["log"] = options["log"]
    if "grid" in options:
        if options["grid"]==True:
            hop["alpha"] = 0.75
    plt.hist(data,**hop)
    plt.show()

def makeSingleAxisBins(dmin,dmax,dCount):
    dd = float(dmax-dmin) / float(dCount)
    points = []
    for i in range(dCount+1):
        points.append(dmin+(dd*i))
    ou = []
    for i in range(len(points)-1):
        small = points[i]
        big = points[i+1]
        middle = float(big+small) / float(2)
        ou.append([small,middle,big])
    return dd,ou

def makeGrid(xCount,yCount):
    ou = []
    k = []
    for i in range(xCount):
        for j in range(yCount):
            k.append(int(0))
        ou.append(k)
        k = []
    return ou

def TwoAxisSort(data,xmin,dx,xCount,ymin,dy,yCount):
    z = makeGrid(xCount,yCount)
    for dataPoint in data:
        xNum = float(dataPoint[0]-xmin) / float(dx)
        if xNum<0:
            continue
        if xNum>(xCount-1):
            continue
        yNum = float(dataPoint[1]-ymin) / float(dy)
        if yNum<0:
            continue
        if yNum>(yCount-1):
            continue
        xNum = int(xNum)
        yNum = int(yNum)
        z[xNum][yNum] = z[xNum][yNum]+1
    return z

def stripChop(chop):
    ou = []
    for x in chop:
        ou.append(x[1])
    return ou

def twoAxis(data,**options):
    labeling(**options)
    if "xCount" not in options:
        options["xCount"] = 10
    if "yCount" not in options:
        options["yCount"] = 10
    dx,xChop = makeSingleAxisBins(options["xmin"],options["xmax"],options["xCount"])
    dy,yChop = makeSingleAxisBins(options["ymin"],options["ymax"],options["yCount"])
    z = TwoAxisSort(data,options["xmin"],dx,options["xCount"],options["ymin"],dy,options["yCount"])
    cmap = plt.get_cmap("plasma")
    xChop = stripChop(xChop)
    yChop = stripChop(yChop)
    plt.contourf(xChop,yChop,z,100)
    plt.show()
