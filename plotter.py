import math
minx = -3
maxx = 3

rangex = maxx - minx + 1

def plotf(x):
    return int(math.sinh(x))


def minmax():
    maxy = -9999999
    miny = -maxy
    for i in range(minx, maxx + 1):
        x = i
        y = plotf(x)
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y
    return miny, maxy


def plot():
    miny, maxy = minmax()
    rangey = maxy - miny + 1
    array = [' '] * rangex * rangey
    for i in range(minx, maxx + 1):
        x = i
        y = plotf(x)
        xind = x - minx
        yind = maxy - y
        index = rangex * yind + xind
        array[index] = '#'
    return array


def drawplot(plot):
    md = 0
    for el in plot:
        md = (md + 1) % (maxx - minx + 1)
        print(el, end=' ')
        if md == 0:
            print()


def main():
    p = plot()
    drawplot(p)


main()