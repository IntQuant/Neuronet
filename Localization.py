class localization:
	def __init__(self):
		self.localedict = {}
	
		self.localedict['en'] = {'b-predict':'Predict', 'b-show':'show', 'b-select':'select', 'b-exit':'exit'}
		self.localedict['en-style'] = {'b-predict':0, 'b-show':5, 'b-select':3, 'b-exit':10}
		
		self.localedict['ru'] = {'b-predict':'Предсказать', 'b-show':'Показать', 'b-select':'Выбрать', 'b-exit':'Выйти'}
		self.localedict['ru-style'] = {'b-predict':0, 'b-show':12, 'b-select':13, 'b-exit':19}
		
	def get(self):
		return self.localedict
