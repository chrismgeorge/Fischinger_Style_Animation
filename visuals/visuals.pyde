import os

#########################################################################################################
########################################## Shapes ######################################################
#########################################################################################################

class MyShapes(object):
    def __init__(self, name):
        self.name = name
        self.delete = False
        self.opacity = 255
        self.angle = 0
    
    def update(self):
        assert(False,  "You have not implemented the UPDATE function for "+self.name+".")
        
    def setDrawingProperties(self):
        assert(False,  "You have not implemented the SETPROPERTIES function for "+self.name+".")
        
    def drawShape(self):
        assert(False,  "You have not implemented the DRAWSHAPE function for "+self.name+".")

# Circle
class Circle(MyShapes):
    def __init__(self, val, name='Circle'):
        super(Circle, self).__init__(name)
        self.x = int(random(0, width))
        self.y = int(random(0, height))
        self.r = val
        self.rgb = [val, 255, 255-val]
        
    def update(self):
        self.r *= 19
        self.r //= 20
        
        self.opacity -= 5
        self.rgb[0] -= 1
        self.rgb[0] = max(0, self.rgb[0])
        
        if (self.opacity <= 1 or self.r <= 1):
            self.delete = True
            
    def setDrawingProperties(self):
        ellipseMode(CENTER)
        fill(self.rgb[0], self.rgb[1], self.rgb[2], self.opacity)
        stroke(255, 255, 255, 255) 
        strokeWeight(4) # tune this
        #rotate(radians(self.angle))

    def drawShape(self):
        diameter = 2 * self.r
        ellipse(self.x, self.y, diameter, diameter)
        
class CircleGrow(Circle):
    def __init__(self, val, name='Circle'):
        super(CircleGrow, self).__init__(val)
        self.rgb = [200, 0, val]
        
    def update(self):
        self.r += 5
        self.opacity -= 15
        self.rgb[2] -= 1
        self.rgb[2] = max(0, self.rgb[2])
            
        if (self.opacity <= 1):
            self.delete = True

# Lines, default line is vertical
class Line(MyShapes):
    def __init__(self, val, name='Line'):
        super(Line, self).__init__(name)
        self.x1 = int(random(0, width))
        self.y1 = 0
        self.x2 = self.x1
        self.y2 = height
        self.rgb = [val, 0, 255]
        self.stroke_weight = val // 10

    def update(self):
        self.y1 += 20
        self.y2 -= 20
        self.opacity -= 15
        self.rgb[0] -= 5
        self.rgb[0] = max(0, self.rgb[0])
        self.stroke_weight -= 1
        self.stroke_weight = max(1, self.stroke_weight)
        
        if (self.opacity <= 1):
            self.delete = True

    def setDrawingProperties(self):
        stroke(self.rgb[0], self.rgb[1], self.rgb[2], self.opacity) # keeps opacity
        strokeWeight(self.stroke_weight)
        #rotate(radians(self.angle))

    def drawShape(self):
        line(self.x1, self.y1, self.x2, self.y2)
        
# Line Horizontal
class LineHoriz(Line):
    def __init__(self, val, name='Line'):
        super(LineHoriz, self).__init__(val)
        self.x1 = 0
        self.y1 = int(random(0, height))
        self.x2 = width
        self.y2 = self.y1
        self.rgb = [200, val, 200]
    
    def update(self):
        self.x1 += 20
        self.x2 -= 20
        self.opacity -= 15
        self.rgb[1] -= 5
        self.rgb[1] = max(0, self.rgb[1])
        self.stroke_weight -= 1
        self.stroke_weight = max(1, self.stroke_weight)
        if (self.opacity <= 1):
            self.delete = True
    
        
# Lines, default line is vertical
class Rect(MyShapes):
    def __init__(self, val, name='Rect'):
        super(Rect, self).__init__(name)
        self.x = int(random(0, width))
        self.y = int(random(0, height))
        self.r_width = val
        self.r_height = val
        self.rotateSpeed = val // 10
        self.rgb = [val, 0, 255]
        self.stroke_weight = 2

    def update(self):
        self.r_width -= 5
        self.r_height -= 5
        self.opacity -= 5
        self.rgb[0] -= 1
        self.rgb[0] = max(0, self.rgb[0])
        self.angle += self.rotateSpeed
        
        if (self.opacity <= 1 or self.r_width <= 0):
            self.delete = True

    def setDrawingProperties(self):
        fill(self.rgb[0], self.rgb[1], self.rgb[2], self.opacity)
        stroke(255, 255, 255, 255) 
        strokeWeight(self.stroke_weight)

    def drawShape(self):
        pushMatrix()
        translate(self.x, self.y)
        rotate(radians(self.angle))
        rectMode(CENTER)
        rect(0, 0, self.r_width, self.r_height)
        popMatrix()

#########################################################################################################
########################################## Shapes ######################################################
#########################################################################################################

def setup():
    size(1280, 720)
    colorMode(RGB)

def getDataFromFile(fileName):
    with open(fileName, 'r') as f:
        data = eval(f.read())
    return data

def getSongs():
    song_folder = os.listdir('/Users/chris/Documents/Git_Folders/Audio_Visuals/visuals/data/')
    songs = []
    for s in song_folder:
        if '.txt' in s:
            songs.append(getDataFromFile('/Users/chris/Documents/Git_Folders/Audio_Visuals/visuals/data/'+s))
    return songs

# a 2-D list of all of the songs, all of the song data
all_songs = getSongs()
all_shapes = []

def draw():
    global all_songs, all_shapes
    
    background(255, 255, 255)
    
    # have (21 indexes) / (1 second)
    if (frameCount >= len(all_songs[0])):
        print('Done!')
        exit(0)
        return
    
    # get the next size in the audio files and append the corresponding values
    for index, song in enumerate(all_songs):
        current_val = int(song[frameCount])
        if (current_val > 1):
            if index == 0:
                all_shapes.append(Circle(current_val))
            elif index == 1:
                all_shapes.append(Rect(current_val))
            elif index == 2:
                all_shapes.append(CircleGrow(current_val))
            elif index == 3:
                all_shapes.append(LineHoriz(current_val))
            else:
                all_shapes.append(Line(current_val))
    
    # update elements properties, if the new object wouldn't draw correctly, get the index to delete later, otherwise, 
    # reset the drawing properties and then draw the shape
    indexes_to_remove = []
    for index, s in enumerate(all_shapes):
        s.update()
        if (s.delete == True):
            indexes_to_remove.append(index)
        else:
            s.setDrawingProperties()
            s.drawShape()
            
    # remove any objects as necessary
    for index in sorted(indexes_to_remove, reverse=True):
        del all_shapes[index]    
            
    name = '{num:0{width}}'.format(num=frameCount, width=6)
    saveFrame('frames/'+name+'.png')
