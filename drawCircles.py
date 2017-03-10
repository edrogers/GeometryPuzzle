#!/usr/bin/python

import Image, ImageDraw, ImageFont
import sys
from math import pi, cos, sin, radians, sqrt

alphaDeg=float(sys.argv[1])
alpha=radians(alphaDeg)

circleAcentX=0
circleAcentY=0
circleAradius=200

pointAX=circleAcentX-circleAradius
pointAY=circleAcentY

pointBX=circleAcentX-circleAradius*cos(alpha)
pointBY=circleAcentY-circleAradius*sin(alpha)

pointCX=circleAcentX-circleAradius*cos(2*alpha)
pointCY=circleAcentY-circleAradius*sin(2*alpha)

circleBcentX=pointBX
circleBcentY=pointBY
circleBradius=sqrt(2*(1-cos(alpha)))*200

circleCcentX=pointAX
circleCcentY=pointAY
circleCradius=2*sqrt(2*(1-cos(alpha)))*(cos(alpha/2))*200

pointDX=pointAX
pointDY=pointAY-circleCradius

circleAcentX+=400
circleAcentY+=600
circleBcentX+=400
circleBcentY+=600
circleCcentX+=400
circleCcentY+=600
pointAX+=400
pointAY+=600
pointBX+=400
pointBY+=600
pointCX+=400
pointCY+=600
pointDX+=400
pointDY+=600


image = Image.new('RGB', (1024, 768),(255,255,255))
draw = ImageDraw.Draw(image)

draw.ellipse((circleAcentX-circleAradius, circleAcentY-circleAradius, circleAcentX+circleAradius, circleAcentY+circleAradius), outline ='blue')
draw.ellipse((circleBcentX-circleBradius, circleBcentY-circleBradius, circleBcentX+circleBradius, circleBcentY+circleBradius), outline ='blue')
draw.ellipse((circleCcentX-circleCradius, circleCcentY-circleCradius, circleCcentX+circleCradius, circleCcentY+circleCradius), outline ='blue')
draw.ellipse((pointAX-5,pointAY-5,pointAX+5,pointAY+5), fill='red', outline ='red')
draw.ellipse((pointBX-5,pointBY-5,pointBX+5,pointBY+5), fill='red', outline ='red')
draw.ellipse((pointCX-5,pointCY-5,pointCX+5,pointCY+5), fill='red', outline ='red')
draw.ellipse((pointDX-5,pointDY-5,pointDX+5,pointDY+5), fill='red', outline ='red')
draw.line((pointDX,pointDY-100, pointAX,pointAY+100), fill='green')
image_font = ImageFont.truetype('/usr/share/fonts/truetype/josefin/JosefinSans-Bold.ttf', 28)
#draw.text((pointAX+15,pointAY-15),"A",fill='red',font=image_font)
#draw.text((pointBX,   pointBY-30),"B",fill='red',font=image_font)
#draw.text((pointCX+15,pointCY+5), "C",fill='red',font=image_font)
#draw.text((pointDX-25,pointDY-25),"D",fill='red',font=image_font)
image.save('test.png')

quit()
