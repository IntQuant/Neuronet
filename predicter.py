#!/usr/bin/env python3
import sys
import math
import tkinter as tk
from tkinter import messagebox

from CharDiv import NumberDivide

from Localization import localization
from INeuronet import GetModel
import numpy as np

from skimage import io, transform
#Декораторы
def nocrash(func):
	""" Убирает любые ошибки функции """
	def dec(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except:
			pass
	return dec

def logres(func):
	""" Записывает результат выполнени функции """
	def dec(*args, **kwargs):
		log = func(*args, **kwargs)
		print(log)
		return log
	return dec

def logerr(func):
	""" Аналогино, но вывод в stderr """
	def dec(*args, **kwargs):
		log = func(*args, **kwargs)
		if log is not None:
			print(log, file=sys.stderr)
		return log
	return dec


def nocrash_log(func):
	""" Вывод ошибок """
	def dec(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except Exception as e:
			print(e, file=sys.stderr)
	return dec

# Чтение файла настроек
with open('settings','r') as f:
	locale = f.read(2)

if locale not in ['ru', 'en']:
	locale = 'en'
localestyle=locale+'-style'

ldict = localization().get()
ND = NumberDivide()

@nocrash_log
def selectfile():
	""" Функция, которая активируется при нажатии кнопки "выбрать файл" """
	global sfile
	sfile = tk.filedialog.askopenfilename()

def predict():
	""" Функция, которая активируется при нажатии кнопки "предсказать" """
	global ND
	
	if 'sfile' in globals():
		global sfile
		print(sfile)
		print('Reading image')
		udata = io.imread(sfile)
		udata = np.pad(udata, ((100, 100), (100, 100), (0, 0)), 'constant', constant_values=0)
		print('Removing additional channels')
		data = np.empty((udata.shape[0], udata.shape[1]))
		for i in range(udata.shape[0]):
			for j in range(udata.shape[1]):
				data[i][j]=udata[i][j][3]*255
		print('Hightlighting')
		matrix, objects = ND.Hightlight(data)

		pdata = []

		coords = ND.Divide(matrix)
		print(len(coords))
		for (x1, y1, x2, y2) in coords:
			
			(cx, cy) = ((x1 + x2) // 2, (y1 + y2) // 2)
			
			hdx = max(abs(cx - x1), abs(cx - x2)) // 2
			hdy = max(abs(cy - y1), abs(cy - y2)) // 2
			
			if hdx > hdy:
				y1 -= hdx
				y2 += hdx
			else:
				x1 -= hdy
				x2 += hdy		
			
			
			rawimg = data[x1:x2,y1:y2]
			img = transform.resize(rawimg, output_shape=(28, 28)).reshape(28, 28, 1)
			
			pdata.append(img)
		
		print(len(pdata))
		print(pdata[0].shape)
				
		result = model.predict_classes(np.array(pdata), verbose=1)
		
		messagebox.showinfo(title='Predicted', message=str(result))
	else:
		messagebox.showerror(title='Error', message=ldict[locale]['err-no-sfile'])

@nocrash_log
def viev():	
	""" Функция, которая активируется при нажатии кнопки "показать" """
	if 'sfile' in globals():
		global sfile
		udata = io.imread(sfile)
		io.imshow(udata)
		io.show()
	else:
		messagebox.showerror(title='Error', message=ldict[locale]['err-no-sfile'])

@nocrash_log
def changelocale():
	""" Функция, которая активируется при нажатии кнопки, которая изменяет язык """
	global locale
	with open('settings','w') as f:
		if locale=='ru':
			locale='en'
		else:
			locale='ru'
		updatetext(mainw)
		f.write(locale)



@nocrash_log
def createbutton(widget, command, name):
	""" Создаёт кнопки """
	widget.buttons[name] = tk.Button(widget, fg='#0ff0ff', bg='#000000')
	widget.buttons[name]['command'] = command
	widget.buttons[name]['text'] = ldict[locale]['b-'+name]	
	widget.buttons[name].pack(fill='both')

@nocrash_log
def updatetext(widget):
	""" Обновляет текст кнопок """
	for name in widget.buttons:
		widget.size = 10, 10
		widget.buttons[name]['text'] = ldict[locale]['b-'+name]		
mainw = tk.Tk()
mainw.title('Predicter')
mainw.buttons = {}

#создание кнопок
createbutton(mainw, predict, 'predict')
createbutton(mainw, viev, 'show')
createbutton(mainw, selectfile, 'select')
createbutton(mainw, changelocale, 'locale')
createbutton(mainw, exit, 'exit')


#подгрузка модели и весов
model = GetModel.getmodel()
model.load_weights('Weights.hd5')


io.use_plugin('matplotlib')

mainw.mainloop()








