"""
* This code was developed by: mathgmc @github *
"""
import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np


# Get the lower position on the axis
def getLowerNum(x1, x2, x3):
   if x1 < x2: 
      if x1 < x3:
         return x1 
      else:
         return x3 
   elif x2 < x3:
      return x2 
   else:
      return x3 


# Get the higher position on the axis
def getHigherNum(x1, x2, x3):
   if x1 > x2:
      if x1 > x3:
         return x1
      else:
         return x3
   elif x2 > x3:
      return x2
   else:
      return x3


# Return 10% of the higher number
def getHigherNum10Percent(x1, x2, x3):
   x1 = abs(x1)
   x2 = abs(x2)
   x3 = abs(x3)
   if x1 > x2:
      if x1 > x3:
         return abs(x1*0.2)
      else:
         return abs(x3*0.2)
   elif x2 > x3:
      return abs(x2*0.2)
   else:
      return abs(x3*0.2)


# Define the position
theTitle        = input("Title: ")
hostileX        = input("Value of X for the Hostile Airplane: ")
hostileY        = input("Value of Y for the Hostile Airplane: ")
hunterX         = input("Value of X for the Hunter Airplane: " )
hunterY         = input("Value of Y fot the Hunter Airplane: " )
interceptX      = input("Value of X for the Intercept Point: ")
interceptY      = input("Value of Y for the Intercept Point: ")
hunterSpeed     = input("Value of the Hunter Speed: ")
hostileSpeed    = input("Value of the Hostile Speed: ")
hostileSpeedX    = input("Value of the Hostile Speed in X: ")
hostileSpeedY    = input("Value of the Hostile Speed in Y: ")
timeToIntercept = input("Time to Intercept: ")


# Creating plot
plt = pg.plot()
plt.showGrid(x=True, y=True)
plt.addLegend()


# Setting properties
plt.setLabel('left', 'Y')
plt.setLabel('bottom', 'X')

tenPercentX= getHigherNum10Percent(float(hostileX), float(hunterX), float(interceptX))
low  = getLowerNum(float(hostileX), float(hunterX), float(interceptX)) - tenPercentX
high = getHigherNum(float(hostileX), float(hunterX), float(interceptX)) + tenPercentX
plt.setXRange( low, high )

tenPercentY= getHigherNum10Percent(float(hostileY), float(hunterY), float(interceptY))*1.5
low  = getLowerNum( float(hostileY), float(hunterY), float(interceptY)) - tenPercentY
high = getHigherNum( float(hostileY), float(hunterY), float(interceptY)) + tenPercentY
plt.setYRange( low, high )

plt.setWindowTitle(theTitle)


# Adding info text
text = pg.TextItem("X: " + str(hostileX) + "\nY: " + str(hostileY) + "\nSpeed: "+ str(hostileSpeed) + "\nSpeed (X): "+ str(hostileSpeedX) + "\nSpeed(Y): "+ str(hostileSpeedY), (255, 255, 255), anchor=(0, 0))
text.setPos(float(hostileX)-(tenPercentX), float(hostileY)- 0.5)
plt.addItem(text)

text = pg.TextItem("X: "+ str(hunterX) + "\nY: " + str(hunterY) + "\nSpeed: "+ str(hunterSpeed) , (255, 255, 255), anchor=(0, 0))
text.setPos(float(hunterX)-(tenPercentX), float(hunterY)- 0.5)
plt.addItem(text)

text = pg.TextItem("Time: "+ str(timeToIntercept) + "\nX: " + str(interceptX) + "\nY: " + str(interceptY), (255, 255, 255), anchor=(0, 0))
text.setPos(float(interceptX)-(tenPercentX), float(interceptY)- 0.5)
plt.addItem(text)


# Creating Lines
x     = [hostileX , interceptX]
y     = [hostileY , interceptY]
x2    = [hunterX  , interceptX]
y2    = [hunterY  , interceptY]


# Plotting
line1 = plt.plot(x, y, pen='b', symbol='o', symbolPen='b', symbolBrush=0.2, name='- Hostile')
line2 = plt.plot(x2, y2, pen='r', symbol='o', symbolPen='r', symbolBrush=0.2, name='- Hunter')


# Exporting image
exporter = pg.exporters.ImageExporter(plt.plotItem)
exporter.export(theTitle + '.png')


## Start Qt event loop.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()

