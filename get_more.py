from PIL import Image, ImageDraw


original_big_image = Image.open('./PiCam/Images/set2/img2_51.jpg')
big_image = original_big_image.convert('LA')
big_size = big_image.size
sub_image = Image.open ('./PiCam/Images/cylinders/img2_51_cyln0.jpg').convert('LA')
sub_size = sub_image.size
x0, y0 = sub_size[0], sub_size[1]
x1, y1 = big_size[0], big_size[1]

def diff(a, b):
    return sum ((a - b) ** 2 for a, b in zip (a, b) )

min_d_total = 100000

best = (100000, 0, 0)
for x in range (big_size[0] - sub_size[0]):
    for y in range (big_size[1] - sub_size[1]):
    	d_total = 100000
    	break_flag = False
    	for i in range (0,sub_size[0], 5):
    		for j in range (0,sub_size[1], 5):
       			ipixel = big_image.getpixel((x+i, y+j))
       			pixel = sub_image.getpixel((i,j))
        		d = diff (ipixel, pixel)
        		if d < 700:
        			d_total -= d
        			min_d_total = min(min_d_total, d_total)
        		else:
        			break_flag = True
        			break

        	if break_flag:
        		break
        if d_total < best[0] and not break_flag: 
        	best = (d_total, x, y)

print(min_d_total)

draw = ImageDraw.Draw(original_big_image)
x, y = best [1:]
draw.rectangle((x, y, x + x0, y + y0), outline = 'red')
original_big_image.save('out.png')