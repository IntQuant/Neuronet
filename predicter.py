import sys
import math
import tkinter as tk
from tkinter import messagebox

from Localization import localization

from keras.models import Sequential
from keras.layers import Dense, Activation, normalization
from keras.layers.pooling import MaxPooling1D
from keras.layers.core import Flatten, Reshape
from keras.layers.recurrent import LSTM
from keras.layers.convolutional import Convolution1D
from keras.utils.np_utils import to_categorical
from keras.layers.advanced_activations import PReLU
import numpy as np

from skimage import io, transform

with open('settings','r') as f:
	locale = f.read(2)
	localestyle=locale+'-style'

ldict = localization().get()



def selectfile():
	globals()['sfile'] = tk.filedialog.askopenfilename()
def predict():
	if 'sfile' in globals():
		print(globals()['sfile'])
		udata = io.imread(globals()['sfile'])
		udata = transform.resize(udata, output_shape=(28, 28, 4))
		data = np.empty((28, 28), dtype = np.uint8)
		for i in range(28):
			for j in range(28):		
				data[i][j]=min(max(udata[i][j][3], 0), 1)*255
		result = float(model.predict(np.array([data])))
		intresult = int(result+0.5)
		resrange = abs(intresult - result)
		percvalid = 100 - ((resrange / 0.5) * 100)
		print('Result', intresult, 'Validness', percvalid, sep='\n')
		messagebox.showinfo(title='Predicted', message=str(intresult))
def viev():
	if 'sfile' in globals():
		udata = io.imread(globals()['sfile'])
		udata = transform.resize(udata, output_shape=(28, 28, 4))
		io.imshow(udata)
		io.show()


	

def createbutton(widget, command, name):
	widget.buttons[name] = tk.Button(widget, fg='#0ff0ff', bg='#000000')
	widget.buttons[name]['command'] = command
	widget.buttons[name]['text'] = ldict[locale]['b-'+name]
	widget.buttons[name].pack(ipadx=ldict[localestyle]['b-'+name])

mainw = tk.Tk()
mainw.title('Predicter')
mainw.buttons = {}

createbutton(mainw, predict, 'predict')
createbutton(mainw, viev, 'show')
createbutton(mainw, selectfile, 'select')
createbutton(mainw, exit, 'exit')

model = Sequential()
model.add(Flatten(input_shape = (28, 28)))
model.add(Dense(output_dim=28*8))
model.add(Activation("sigmoid"))
model.add(Dense(output_dim=1))
model.add(PReLU())
model.load_weights('Weights/Weights-auto5320.hd5')
io.use_plugin('matplotlib')

mainw.mainloop()








