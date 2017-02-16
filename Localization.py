class localization:
	def __init__(self):
		self.localedict = {}
	
		self.localedict['en'] = {'b-predict':'Predict', 'b-show':'show', 'b-select':'select', 'b-exit':'exit', 'b-locale':'EN', 'err-no-sfile':'No file selected'}
		self.localedict['en-style'] = {'b-predict':0, 'b-show':5, 'b-select':3, 'b-exit':10, 'b-locale':12}
			
		
		self.localedict['ru'] = {'b-predict':'Предсказать', 'b-show':'Показать', 'b-select':'Выбрать', 'b-exit':'Выйти', 'b-locale':'RU', 'err-no-sfile':'Файл не выбран'}
		self.localedict['ru-style'] = {'b-predict':0, 'b-show':15, 'b-select':15, 'b-exit':25, 'b-locale':20}
		
	def get(self):
		return self.localedict
