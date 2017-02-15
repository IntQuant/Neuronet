import sys
import math
import tkinter as tk
from tkinter import messagebox

from Localization import localization
from INeuronet import GetModel
import numpy as np

from skimage import io, transform

with open('settings','r') as f:
	locale = f.read(2)

if locale not in ['ru', 'en']:
	locale = 'en'
localestyle=locale+'-style'

ldict = localization().get()



def selectfile():
	global sfile
	sfile = tk.filedialog.askopenfilename()
def predict():
	if 'sfile' in globals():
		global sfile
		print(sfile)
		udata = io.imread(sfile)
		udata = transform.resize(udata, output_shape=(28, 28, 4))
		data = np.empty((28, 28))
		for i in range(28):
			for j in range(28):		
				data[i][j]=min(max(udata[i][j][3], 0), 1)
		result = model.predict(data.reshape(1, 28, 28, 1))
		cmax = 0
		print(result[0])
		for i, v in enumerate(result[0]):
			if v > result[0][cmax]:
				cmax = i
		
		messagebox.showinfo(title='Predicted', message=str(cmax))
def viev():	
	if 'sfile' in globals():
		global sfile
		udata = io.imread(sfile)
		udata = transform.resize(udata, output_shape=(28, 28, 4))
		io.imshow(udata)
		io.show()
def changelocale():
	global locale
	with open('settings','w') as f:
		if locale=='ru':
			locale='en'
		else:
			locale='ru'
		updatetext(mainw)
		f.write(locale)


	

def createbutton(widget, command, name):
	widget.buttons[name] = tk.Button(widget, fg='#0ff0ff', bg='#000000')
	widget.buttons[name]['command'] = command
	widget.buttons[name]['text'] = ldict[locale]['b-'+name]	
	widget.buttons[name].pack(fill='both')
def updatetext(widget):
	for name in widget.buttons:
		widget.size = 10, 10
		widget.buttons[name]['text'] = ldict[locale]['b-'+name]		
mainw = tk.Tk()
mainw.title('Predicter')
mainw.buttons = {}

createbutton(mainw, predict, 'predict')
createbutton(mainw, viev, 'show')
createbutton(mainw, selectfile, 'select')
createbutton(mainw, changelocale, 'locale')
createbutton(mainw, exit, 'exit')

model = GetModel.getmodel()


model.load_weights('Weights.hd5')
io.use_plugin('matplotlib')

mainw.mainloop()








