import math
minx = -3
maxx = 3

precx = 0.2
precy = 0.2

lim = 999999

rangex = int((maxx - minx + 1) / precx)

def rawf(x):
    return math.sinh(x)

def plotf(x):
    try:
        f = rawf(x)
        if abs(f) > lim:
            raise Exception
        return f
    except Exception:
        return None


def minmax():
    maxy = -9999999
    miny = -maxy
    
    i = minx
    while i <= maxx:
        x = i
        y = plotf(x)
        if y != None:
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
        i += precx
    return miny, maxy


def plot():
    miny, maxy = minmax()
    rangey = int((maxy - miny + 1) / precy)
    array = [' '] * rangex * rangey
    prev = None
    i = minx
    while i <= maxx:
        x = i
        y = plotf(x)
        if y != None:
            xind = int((x - minx) / precx)
            yind = int((maxy - y) / precy)
            index = rangex * yind + xind
            if prev == None:
                if plotf(x + 1) != None and y < plotf(x + 1):
                    array[index] = '/'
                elif plotf(x + 1) != None and y > plotf(x + 1):
                    array[index] = '\\'
                else:
                    array[index] = '-'
            elif prev < y:
                array[index] = '/'
            elif prev > y:
                array[index] = '\\'
            else:
                array[index] = '-'
            prev = y
        i += precx
    return array


def drawplot(plot):
    md = 0
    for el in plot:
        md = (md + 1) % int((maxx - minx + 1) / precx)
        print(el, end=' ')
        if md == 0:
            print()


def main():
    p = plot()
    drawplot(p)


main()
