from PIL import Image, ImageDraw, ImageFont

width = 12000
height = 10000
HeightInit = height
img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)

def generate_image(input_str):
    InputLines = input_str.split('\n')
    Title = InputLines[0]
    StringElements = InputLines[1]
    Elements = StringElements.split(',')
    Font = ImageFont.truetype('arial.ttf', 20)

    FirstX = 100
    FirstY = (height - HeightInit) // 2 + 200

    draw.text((FirstX, FirstY - 50), Title, fill='black', font=Font)

    x = FirstX
    prev_element = None
    prev_rect = None
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
        RectW = max(Twidth+40,150)
        RectH = 100
        rect = (RectX, RectY, RectX + RectW, RectY + RectH)
        draw.rectangle(rect, outline='black')

        Tx = RectX + RectW / 2
        Ty = RectY + RectH / 2

        draw.text((Tx - Twidth / 2, Ty - Theight / 2), element, fill='black', font=Font)
        if Underlined:
            draw.line((Tx - Twidth / 2, Ty + Theight / 2 + 2, Tx + Twidth / 2, Ty + Theight / 2 + 2), fill='black', width=2)
        elif Dotted:
            for i in range(int(Twidth)):
                if i % 2 == 0:
                    draw.point((Tx - Twidth / 2 + i, Ty + Theight / 2 + 2), fill='black')
        if prev_element == element and prev_rect is not None:
            draw.line((prev_rect[2], prev_rect[1] + RectH // 2, rect[0], RectY + RectH // 2), fill='black', width=2)
        prev_element = element
        prev_rect = rect
        x += RectW


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        string = f.read()
        
    input_lines = string.split('\n')
    for i in range(0, len(input_lines), 2):
        generate_image(input_lines[i] + '\n' + input_lines[i+1])
        height += 500
    img.save('output.png')
