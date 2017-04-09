from PIL import Image,ImageDraw
from collections import namedtuple
import os
radius=2  #yuan de ban jing
jointcolor="blue"
bonewidth=2
bonecolor="green"
width=1980
height=768
filepath=r'.\visualization'
connecting_joint =[2,1,21,3,21,5,6,7,21,9,10,11,1,13,14,15,1,17,18,19,2,8,8,12,12]
# class Joint(object):
#     def __init__(self,X,Y,Z):
#         self.X = X
#         self.Y = Y
#         self.Z = Z
Joint=namedtuple('Joint',['X','Y','Z'])

class Body(object):
    def __init__(self,Joints):
        self.Joints=Joints
        bones=[]
        for i in range(25):
            bones.append([Joints[i],Joints[connecting_joint[i]-1]])
        self.Bones=bones

def drawJoint(draw,joint):
    x=joint.X
    y=joint.Y
    draw.ellipse((x-radius,y-radius,x+radius,y+radius),fill=jointcolor)

def drawBone(draw,bone):
    joint1=bone[0]
    joint2=bone[1]
    draw.line((joint1.X,joint1.Y,joint2.X,joint2.Y),fill=bonecolor,width=bonewidth)

def drawBody(draw,body):
    for joint in body.Joints:
        drawJoint(draw,joint)
    for bone in body.Bones:
        drawBone(draw,bone)

def readData(filename):
    with open(filename,'r') as f:
        framecount=int(f.readline())
        # minx = width
        # maxx = 0
        # miny = height
        # maxy = 0
        for i in range(framecount):
            f.readline()
            f.readline()
            f.readline()
            Joints=[]
            for j in range(25):
                line=(f.readline()).split()
                line=map(float,line)
                x,y=line[5],line[6]
                Joints.append(Joint(x,y,0))
                # if x<minx:
                #     minx=x
                # if x>maxx:
                #     maxx=x
                # if y<miny:
                #     miny=y
                # if y>maxy:
                #     maxy=y
            body=Body(Joints)
            blank = Image.new("RGB", [width, height], "white")
            draw = ImageDraw.Draw(blank)
            drawBody(draw,body)
            blank=blank.crop((850,250,1250,850))
            if os.path.exists(filepath)==False:
                os.mkdir(filepath)
            blank.save(os.path.join(filepath,str(i)+'.png'))



if __name__=='__main__':
    readData(r".\data\S001C001P001R001A024.skeleton.txt")