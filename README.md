# bitplotter
```
Terminal function plotter that I made with Termux and nano on my phone.¯\_(ツ)_/¯
```
## Usage
1. Set function to graph in plotf() **(Must return int)**
```
def plotf(x):
    return int(math.sinh(x))
```
2. Set bounds of graphing by changing minx and maxx **(They are also ints, minx <= maxx)**
```
minx = -3
maxx = 3
```
3. Save script and execute it in terminal.
```
python3 plotter.py
```
4. Enjoy!

![Screenshot](https://raw.githubusercontent.com/IngeniousA/bitplotter/master/img/screenshot.PNG)
