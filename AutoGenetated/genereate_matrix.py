from PIL import Image, ImageFilterimport globpath = "/Users/mateuszochal/Documents/University/RoboSoc/ShapeRecognition/Images/Transformed/"file = open(path + "matrix.m", 'w')X_line = "X = ["Y_line = "y = ["for background_filename in glob.glob(path + "Background/*.png"):    background = Image.open(background_filename)    width, height = background.size    for j in range(0, height):        for i in range(0, width):            if not (i == 0 and j == 0):                X_line += ", "            X_line += str(background.getpixel((i, j))[0])    file.write(X_line + ";\n")    X_line = ""    Y_line += "0;"Y_line += "\n"for cylinder_filename in glob.glob(path + "Cylinders/*.png"):    cylinder = Image.open(cylinder_filename)    width, height = cylinder.size    for j in range(0, height):        for i in range(0, width):            if not (i == 0 and j == 0):                X_line += ", "            X_line += str(cylinder.getpixel((i, j))[0])    file.write(X_line + ";\n")    X_line = ""    Y_line += "1;"Y_line += "\n"for ball_filename in glob.glob(path + "Balls/*.png"):    ball = Image.open(ball_filename)    width, height = ball.size    for j in range(0, height):        for i in range(0, width):            if not (i == 0 and j == 0):                X_line += ", "            X_line += str(ball.getpixel((i, j))[0])    file.write(X_line + ";\n")    X_line = ""    Y_line += "2;"Y_line += "];"file.write("];\n")file.write(Y_line);