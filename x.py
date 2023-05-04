from random import randint
from math import dist
import svgwrite
import re
from svgwrite import cm, mm
from PIL import Image, ImageDraw, ImageFont


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
        if(elm:= re.findall(r'{(.*?)}', element)):
            if(elm[0].startswith('(') and elm[0].endswith(')') or elm[0].startswith('_') and elm[0].endswith('_')):
                Twidth, Theight = draw.textsize(elm[0][1:-1], font=Font)
            else:
                Twidth, Theight = draw.textsize(elm[0], font=Font)
        else:
            Twidth, Theight = draw.textsize(element, font=Font)
        RectX = x
        RectY = FirstY
        RectW = max(Twidth + 40, 150)
        RectH = 50

        num = []
        if '{' in element and '}' in element:
            for item in element.split('{'):
                if('}' in item):
                    continue
                for _ in item.split('-'):
                    num.append(_)

        if num:
            for n in num:
                b = False
                if n[-1] == 'A':
                    b = True
                    n = int(n[0:-1])
                else:
                    n = int(n)
                if n not in Lines:
                    Lines[n] = [RectX,RectY,RectW,RectH,b]
                else:
                    Lines[n]+=[RectX,RectY,RectW,RectH,b]
        if(elm:= re.findall(r'{(.*?)}', element)):
            if(elm[0].startswith('(') and elm[0].endswith(')') or elm[0].startswith('_') and elm[0].endswith('_')):
                Twidth, Theight = draw.textsize(elm[0][1:-1], font=Font)
            else:
                Twidth, Theight = draw.textsize(elm[0], font=Font)
        else:
            Twidth, Theight = draw.textsize(element, font=Font)
        RectX = x
        RectY = FirstY
        RectW = max(Twidth + 40, 150)
        RectH = 50

        num = []
        if '{' in element and '}' in element:
            for item in element.split('{'):
                if('}' in item):
                    continue
                for _ in item.split('-'):
                    num.append(_)

        if num:
            for n in num:
                b = False
                if n[-1] == 'A':
                    b = True
                    n = int(n[0:-1])
                else:
                    n = int(n)
                if n not in Lines:
                    Lines[n] = [RectX,RectY,RectW,RectH,b]
                else:
                    Lines[n]+=[RectX,RectY,RectW,RectH,b]
        Underlined = False
        if elm:
            element = elm[0]
        if elm:
            element = elm[0]
        if element.startswith('(') and element.endswith(')'):
            Underlined = True
            element = element[1:-1]
        Dotted = False
        if element.startswith('_') and element.endswith('_'):
            Dotted = True
            element = element[1:-1]

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
        Rx1, Ry1, Rw1, Rh1,R1a, Rx2, Ry2, Rw2, Rh2,R2a = Lines[key]
        Rx1, Ry1, Rw1, Rh1,R1a, Rx2, Ry2, Rw2, Rh2,R2a = Lines[key]
        R1lvl = int(Ry1/(VerticalDistance/2))
        R2lvl = int(Ry2/ (VerticalDistance/2))

        randStart = randint(5,FirstX-5)
        
        randR1x = randint(-int(Rw1/4), int(Rw1/4))
        randR2x = randint(-int(Rw2/4), int(Rw1/4))

        randRy = randint(-int((((VerticalDistance/2)-Rh1)/2)/2), int((((VerticalDistance/2)-Rh1)/2)/2))

        randStart = randint(5,FirstX-5)
        
        randR1x = randint(-int(Rw1/4), int(Rw1/4))
        randR2x = randint(-int(Rw2/4), int(Rw1/4))

        randRy = randint(-int((((VerticalDistance/2)-Rh1)/2)/2), int((((VerticalDistance/2)-Rh1)/2)/2))

        if(R2lvl-R1lvl == 1):
            points = [
                (Rx1+randR1x+Rw1/2, Ry1+Rh1),
                (Rx1+randR1x+Rw1/2, randRy+(Ry1+Rh1)+((VerticalDistance/2)-Rh1)/2),
                (Rx2+randR2x+Rw2/2, randRy+(Ry1+Rh1)+((VerticalDistance/2)-Rh1)/2),
                (Rx2+randR2x+Rw2/2, Ry2)
            
            ]
            points = [
                (Rx1+randR1x+Rw1/2, Ry1+Rh1),
                (Rx1+randR1x+Rw1/2, randRy+(Ry1+Rh1)+((VerticalDistance/2)-Rh1)/2),
                (Rx2+randR2x+Rw2/2, randRy+(Ry1+Rh1)+((VerticalDistance/2)-Rh1)/2),
                (Rx2+randR2x+Rw2/2, Ry2)
            
            ]
        else:
            maxX = 0
            for i in range(R1lvl+1, R2lvl):
                if levels[i-1] > maxX:
                    maxX = levels[i-1]

            maxX += randint(10, 50)
            maxX += randint(10, 50)

            points1 = [
                    (Rx1+randR1x+Rw1/2, Ry1+Rh1),
                    (Rx1+randR1x+Rw1/2, randRy+(Ry1+Rh1)+((VerticalDistance/2)-Rh1)/2),
                    (randStart, randRy+(Ry1+Rh1)+((VerticalDistance/2)-Rh1)/2),
                    (randStart, randRy+(Ry2)-((VerticalDistance/2)-Rh2)/2),
                    (Rx2+randR2x+Rw2/2, randRy+(Ry2)-((VerticalDistance/2)-Rh2)/2),
                    (Rx2+randR2x+Rw2/2, Ry2),
                ]
            points2 = [
                    (Rx1+randR1x+Rw1/2, Ry1+Rh1),
                    (Rx1+randR1x+Rw1/2, randRy+(Ry1+Rh1)+((VerticalDistance/2)-Rh1)/2),
                    (maxX, randRy+(Ry1+Rh1)+((VerticalDistance/2)-Rh1)/2),
                    (maxX, randRy+(Ry2)-((VerticalDistance/2)-Rh2)/2),
                    (Rx2+randR2x+Rw2/2, randRy+(Ry2)-((VerticalDistance/2)-Rh2)/2),
                    (Rx2+randR2x+Rw2/2, Ry2),   
                ]
            points1 = [
                    (Rx1+randR1x+Rw1/2, Ry1+Rh1),
                    (Rx1+randR1x+Rw1/2, randRy+(Ry1+Rh1)+((VerticalDistance/2)-Rh1)/2),
                    (randStart, randRy+(Ry1+Rh1)+((VerticalDistance/2)-Rh1)/2),
                    (randStart, randRy+(Ry2)-((VerticalDistance/2)-Rh2)/2),
                    (Rx2+randR2x+Rw2/2, randRy+(Ry2)-((VerticalDistance/2)-Rh2)/2),
                    (Rx2+randR2x+Rw2/2, Ry2),
                ]
            points2 = [
                    (Rx1+randR1x+Rw1/2, Ry1+Rh1),
                    (Rx1+randR1x+Rw1/2, randRy+(Ry1+Rh1)+((VerticalDistance/2)-Rh1)/2),
                    (maxX, randRy+(Ry1+Rh1)+((VerticalDistance/2)-Rh1)/2),
                    (maxX, randRy+(Ry2)-((VerticalDistance/2)-Rh2)/2),
                    (Rx2+randR2x+Rw2/2, randRy+(Ry2)-((VerticalDistance/2)-Rh2)/2),
                    (Rx2+randR2x+Rw2/2, Ry2),   
                ]
            
            distance1 =0
            distance2 =0
            for i in range(1,len(points1)):
                distance1 += dist(points1[i],points1[i-1])

            for i in range(1,len(points2)):
                distance2 += dist(points2[i],points2[i-1])
            distance1 =0
            distance2 =0
            for i in range(1,len(points1)):
                distance1 += dist(points1[i],points1[i-1])

            for i in range(1,len(points2)):
                distance2 += dist(points2[i],points2[i-1])

            if distance1 < distance2:
                points = points1
            if distance1 < distance2:
                points = points1
            else:
                points =points2

        polyline = dwg.polyline(points=points, stroke='black', stroke_width=2,fill='none')
        arrow = dwg.path(d="M 0 0 L 10 5 L 0 10 L 2.5 5 Z")

        if R2a:
            marker = dwg.marker(insert=(9.5, 5), size=(15, 15), orient='auto')
            marker.add(arrow)
            dwg.defs.add(marker)
            polyline['marker-end'] = marker.get_funciri()
        if R1a:
            marker2 = dwg.marker(insert=(9.5, 5), size=(15, 15), orient='-90')
            marker2.add(arrow)
            dwg.defs.add(marker2)
            polyline['marker-start'] = marker2.get_funciri()
        dwg.add(polyline)

        if R2a:
            marker = dwg.marker(insert=(9.5, 5), size=(15, 15), orient='auto')
            marker.add(arrow)
            dwg.defs.add(marker)
            polyline['marker-end'] = marker.get_funciri()
        if R1a:
            marker2 = dwg.marker(insert=(9.5, 5), size=(15, 15), orient='-90')
            marker2.add(arrow)
            dwg.defs.add(marker2)
            polyline['marker-start'] = marker2.get_funciri()
        dwg.add(polyline)


# if __name__ == '__main__':
#     with open('input.txt', 'r') as f:
#         string = f.read()
#     input_lines = string.split('\n')
#     print(string)
#     for i in range(0, len(input_lines), 2):
#         generate_image(input_lines[i] + '\n' + input_lines[i+1])
#         height += VerticalDistance
#         dwg['height'] = (height) * mm
#     DrawLines()
#     dwg.save()

def begin(string):
    global height
    global width
    global HeightInit
    global FirstX
    global VerticalDistance
    global dwg
    global img
    global draw
    global Lines
    global levels

    height = 1000
    width = 2400
    HeightInit = height 
    FirstX = 100
    VerticalDistance = 350

    dwg = svgwrite.Drawing('output2.svg', size=(width, height), profile='full')
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    Lines = {}
    levels = []

    input_lines = string.split('\n')
    print(string)
    for i in range(0, len(input_lines), 2):
        generate_image(input_lines[i] + '\n' + input_lines[i+1])

        height += VerticalDistance
        dwg['height'] = (height) * mm
    DrawLines()
    return dwg.tostring()

    # dwg.save()