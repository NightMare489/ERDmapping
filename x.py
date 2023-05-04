from random import randint
from math import dist
import svgwrite
import re
from svgwrite import cm, mm
from PIL import Image, ImageDraw, ImageFont


width = 2400
height = 1000
HeightInit = height 
FirstX = 100
VerticalDistance = 550

dwg = svgwrite.Drawing('output2.svg', size=(width, height), profile='full')
img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)

Lines = {}
levels = []

def generate_image(input_str):
    InputLines = input_str.split('\n')
    Title = InputLines[0]
    StringElements = InputLines[1]
    Elements = StringElements.split(',')
    FontSize = 20
    Font = ImageFont.truetype('arial.ttf', 20)
    FirstY = (height - HeightInit) // 2 + VerticalDistance/2
    dwg.add(dwg.text(Title, insert=(FirstX, FirstY - 25), fill='black', font_size=FontSize))
    x = FirstX
    for element in Elements:
        Underlined = False
        if element.startswith('(') and element.endswith(')'):
            Underlined = True
            element = element[1:-1]
        Dotted = False
        if element.startswith('_') and element.endswith('_'):
            Dotted = True
            element = element[1:-1]

        Twidth, Theight = draw.textsize(element, font=Font)
        RectX = x
        RectY = FirstY
        RectW = max(Twidth + 40, 150)
        RectH = 50

        # Check if the element has a number and store it in a dictionary
        num = re.findall(r'^(\d+)\{.*\}$', element)
        if num:
            num = int(num[0])
            if num not in Lines:
                Lines[num] = [RectX,RectY,RectW,RectH]
            else:
                Lines[num]+=[RectX,RectY,RectW,RectH]

        rect = dwg.rect(insert=(RectX, RectY), size=(RectW, RectH), stroke='black', fill='none')
        dwg.add(rect)

        Tx = RectX + RectW / 2
        Ty = RectY + RectH / 2

        text = dwg.text(element, insert=(Tx - Twidth / 2, Ty), fill='black', font_size=FontSize)
        dwg.add(text)
        if Underlined:
            line = dwg.line(start=(Tx - Twidth / 2, Ty + Theight / 2 + 2), end=(Tx + Twidth / 2, Ty + Theight / 2 + 2), stroke='black', stroke_width=2)
            dwg.add(line)
        elif Dotted:
            for i in range(int(Twidth)):
                if i % 4 == 0:
                    point = dwg.circle(center=(Tx - Twidth / 2 + i, Ty + Theight / 2 + 2), r=1, fill='black')
                    dwg.add(point)
        
        x += RectW
    levels.append(x)


def DrawLines():
    for key in Lines:
        Rx1, Ry1, Rw1, Rh1, Rx2, Ry2, Rw2, Rh2 = Lines[key]
        R1lvl = int(Ry1/(VerticalDistance/2))
        R2lvl = int(Ry2/ (VerticalDistance/2))

        if(R2lvl-R1lvl == 1):
            rand = randint(-80,80)
            line1 = dwg.line(start=(Rx1+rand+Rw1/2, Ry1+Rh1), end=((Rx1+rand+Rw1/2), Ry1+rand+(Ry2-Ry1)/2), stroke='black', stroke_width=2)           
            line2 = dwg.line(start=(Rx2+Rw2/2, Ry2), end=(Rx2+Rw2/2, Ry1+rand+(Ry2-Ry1)/2), stroke='black', stroke_width=2)
            line3 = dwg.line(start=(Rx1+rand+Rw1/2, Ry1+rand+(Ry2-Ry1)/2), end=(Rx2+Rw2/2, Ry1+rand+(Ry2-Ry1)/2), stroke='black', stroke_width=2)
            dwg.add(line1)
            dwg.add(line2)
            dwg.add(line3)
        else:
            rand = randint(10,FirstX-10)
            maxX = 0
            for i in range(R1lvl+1, R2lvl):
                if levels[i-1] > maxX:
                    maxX = levels[i-1]

            maxX+=rand

            distance = dist((Rx1+rand+Rw1/2, Ry1+Rh1),((Rx1+rand+Rw1/2), Ry1+rand+VerticalDistance/4))
            distance+= dist((Rx2+Rw2/2, Ry2),(Rx2+Rw2/2, Ry2-VerticalDistance/4))
            distance += dist((Rx1+rand+Rw1/2, Ry1+rand+VerticalDistance/4),(rand, Ry1+rand+VerticalDistance/4))
            distance += dist((Rx2+Rw2/2, Ry2-VerticalDistance/4),(rand, Ry2-VerticalDistance/4))
            distance += dist((rand, Ry1+rand+VerticalDistance/4),(rand, Ry2-VerticalDistance/4))
            
            distance2 = dist((Rx1+rand+Rw1/2, Ry1+Rh1),((Rx1+rand+Rw1/2), Ry1+rand+VerticalDistance/4))
            distance2+= dist((Rx2+Rw2/2, Ry2),(Rx2+Rw2/2, Ry2-VerticalDistance/4))
            distance2 += dist((Rx1+rand+Rw1/2, Ry1+rand+VerticalDistance/4),(maxX, Ry1+rand+VerticalDistance/4))
            distance2 += dist((Rx2+Rw2/2, Ry2-VerticalDistance/4),(maxX, Ry2-VerticalDistance/4))
            distance2 += dist((maxX, Ry1+rand+VerticalDistance/4),(maxX, Ry2-VerticalDistance/4))

            if distance < distance2:
                line1 = dwg.line(start=(Rx1+rand+Rw1/2, Ry1+Rh1), end=((Rx1+rand+Rw1/2), Ry1+rand+VerticalDistance/4), stroke='black', stroke_width=2)   
                line2 = dwg.line(start=(Rx2+Rw2/2, Ry2), end=(Rx2+Rw2/2, Ry2-VerticalDistance/4), stroke='black', stroke_width=2)
                line3 = dwg.line(start=(Rx1+rand+Rw1/2, Ry1+rand+VerticalDistance/4), end=(rand, Ry1+rand+VerticalDistance/4), stroke='black', stroke_width=2)           
                line4 = dwg.line(start=(Rx2+Rw2/2, Ry2-VerticalDistance/4), end=(rand, Ry2-VerticalDistance/4), stroke='black', stroke_width=2)
                line5 = dwg.line(start=(rand, Ry1+rand+VerticalDistance/4), end=(rand, Ry2-VerticalDistance/4), stroke='black', stroke_width=2)
            else:
                line1 = dwg.line(start=(Rx1+rand+Rw1/2, Ry1+Rh1), end=((Rx1+rand+Rw1/2), Ry1+rand+VerticalDistance/4), stroke='black', stroke_width=2)   
                line2 = dwg.line(start=(Rx2+Rw2/2, Ry2), end=(Rx2+Rw2/2, Ry2-VerticalDistance/4), stroke='black', stroke_width=2)
                line3 = dwg.line(start=(Rx1+rand+Rw1/2, Ry1+rand+VerticalDistance/4), end=(maxX, Ry1+rand+VerticalDistance/4), stroke='black', stroke_width=2)           
                line4 = dwg.line(start=(Rx2+Rw2/2, Ry2-VerticalDistance/4), end=(maxX, Ry2-VerticalDistance/4), stroke='black', stroke_width=2)
                line5 = dwg.line(start=(maxX, Ry1+rand+VerticalDistance/4), end=(maxX, Ry2-VerticalDistance/4), stroke='black', stroke_width=2)
              
            dwg.add(line1)
            dwg.add(line2)
            dwg.add(line3)
            dwg.add(line4)
            dwg.add(line5)




if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        string = f.read()
    input_lines = string.split('\n')
    for i in range(0, len(input_lines), 2):
        generate_image(input_lines[i] + '\n' + input_lines[i+1])
        height += VerticalDistance
        dwg['height'] = (height) * mm
    DrawLines()
    dwg.save()
