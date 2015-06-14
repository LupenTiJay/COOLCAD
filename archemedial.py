import math
import itertools
numOfVertex = 30000
step = 3 #dont change
dis = 0.9
heightFactor = 0.1
z=0
point = [[0,0,z],[1,0,z],[math.cos(math.radians(60)),math.sin(math.radians(60)),z]]
'''
print "{}:  {}".format("point[0]", point[0])
print "{}:  {}".format("point[1]", point[1])
print "{}:  {}".format("point[2]", point[2])
'''
for i in range (3,numOfVertex):
  xdiff = (point[i-3][0] - point[i-1][0])
  ydiff = (point[i-3][1] - point[i-1][1])
  '''
  print "{}:  {}".format("xdiff", xdiff)
  print "{}:  {}".format("ydiff", ydiff)
  '''
  angle = math.degrees(math.atan(ydiff / xdiff))
  '''
  print "{}:  {}".format("angle", angle)
  '''
  if(xdiff < 0 and ydiff < 0):
    angle = angle + 180 
    
  elif(xdiff < 0 and ydiff > 0):
    angle = angle + 180
    
  elif(xdiff >0 and ydiff <0):
    angle = angle + 360

  elif(xdiff > 0 and ydiff >0):
    '''
    print ("normal")
    '''
  else: '''
    print("check")
    '''
    
  x = point[i-3][0] + dis * math.cos(math.radians(angle))
  y = point[i-3][1] + dis * math.sin(math.radians(angle))
  '''
  print "{}:  {}".format("x", x)
  print "{}:  {}".format("y", y)
  print "{}:  {}".format("angle", angle)
  '''
  newPoint = [[x,y,0]]
  '''print (newPoint)'''
  point = point + newPoint

for k in range( 0,numOfVertex,step):
    point[k][2] = k / 3 * heightFactor
    point[k+1][2] = k/3 * heightFactor
    point[k+2][2] = k/3 * heightFactor
   # print()

face = [[0,1,2]]

for m in range(3,len(point),3):
  test = [[m,m+1,m+2]]
  face = face + test


for o in range(0,len(point),3):
  face = face + [[o , o+1, o + 3]]
  face = face + [[o+1,o+3,o+4]]

  face = face + [[o+2,o+4,o+5]]
  face = face + [[o+1,o+2,o+4]]

  face = face + [[o,o+5,o+3]]
  face = face + [[o+2, o, o+5]]
  
#print (point)
print("  ")
#print (face)

print "polyhedron ( points = {} , faces = {} );".format(point,face)









