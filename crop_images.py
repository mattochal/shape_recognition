import Tkinter as tk
from PIL import ImageTk as itk
from PIL import Image
import os, glob

#.  from math import abs

path = "/Users/mateuszochal/Documents/University/RoboSoc/images/"
images_filenames = glob.glob(path + "*.jpg")

class ExampleApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.x = self.y = 0
		self.canvas = tk.Canvas(self, width=400, height=400, cursor="cross")
		self.canvas.pack(side="top", fill="both", expand=True)
		self.canvas.bind("<ButtonPress-1>", self.on_button_press)
		self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
		self.canvas.bind('<Motion>', self.motion)
		self.canvas.focus_set()
		self.canvas.bind("<Key>", self.key_pressed)
		self.rect = self.canvas.create_rectangle(0,0,0,0, outline="")
		self.outline = 'cyan'
		self.cylinder_flag = True
		self.ball_count = 0
		self.cylinder_count = 0
		self.count = -1
		self.next_image()

	def on_button_press(self, event):
		self.pressed = True
		self.x = event.x
		self.y = event.y
		
	def motion(self, event):
		if self.pressed:
			x0, y0 = self.x, self.y
			x1,y1 = (event.x, event.y)
			self.canvas.delete(self.rect)
			self.rect = self.canvas.create_rectangle(x0,y0,x1,y1, outline=self.outline)

	def on_button_release(self, event):
		self.pressed = False
		x0,y0 = (self.x, self.y)
		x1,y1 = (event.x, event.y)
		self.canvas.delete(self.rect)
		# Save image
		if abs(x0 - x1) > 10 and abs(y1 - y0) > 10 and self.count >= 0:
			print (x0, y0, x1, y1)
			crop = self.image.crop((min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))
			filename = ""
			if self.cylinder_flag:
				filename = "cylinders/" + os.path.basename(images_filenames[self.count])[:-4] + "_cyln"+ str(self.cylinder_count) +".jpg"
				self.cylinder_count += 1
			else:
				filename = "balls/" + os.path.basename(images_filenames[self.count])[:-4] + "_ball" + str(self.ball_count)  +".jpg"
				self.ball_count += 1
			crop.save(path+filename)
		self.x = self.y = 0

	def key_pressed(self, event):
		if event.char == 'n':
			self.next_image()
		
		elif event.char == 'b':
			self.cylinder_flag = False
			self.outline = 'blue'
		
		elif event.char == 'c':
			self.cylinder_flag = True
			self.outline = 'cyan'

		elif event.char == 'd':
			self.delete_image()

		elif event.char == 'p':
			if self.count - 2 >= -1:
				self.count -= 2
				next_image()


	def next_image(self):
		if self.count < len(images_filenames):
			self.count += 1
			image_path = images_filenames[self.count]
			print (os.path.basename(image_path))
			self.photo = itk.PhotoImage(file = image_path)
			self.image = Image.open(image_path)
			self.canvas.config(width=self.image.size[0], height=self.image.size[1])
			self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
			self.ball_count = 0
			self.cylinder_count = 0

	def delete_image(self):
		image_to_detele = images_filenames[self.count]
		self.next_image()
		print ('deleting {}'.format(image_to_detele))
		os.remove(image_to_detele)

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()

