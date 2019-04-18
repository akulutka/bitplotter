# bitplotter
```
Terminal function plotter that I made with Termux and nano on my phone.¯\_(ツ)_/¯
```
## Usage
1. Set function to graph in rawf()
```
def rawf(x):
    return math.sinh(x)
```
2. Set bounds of graphing by changing minx and maxx **(minx <= maxx)**
```
minx = -3
maxx = 3
```
3. Set precision of x-axis and y-axis values **(0 < precx, precy < maxx - minx)**
```
precx = precy = 0.1
```
4. Save script and execute it in terminal.
```
python3 plotter.py
```
5. Enjoy!

![Screenshot](https://raw.githubusercontent.com/IngeniousA/bitplotter/master/img/screenshot.PNG)
