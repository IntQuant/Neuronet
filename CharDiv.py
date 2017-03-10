import numpy as np
from skimage import io, transform



io.use_plugin('matplotlib')

MAGICKCONF = {"treshold":20, "step":80, "debug":False, "minlen":50}

class NumberDivide:
	def recDiv(self, image):
		global segmentmask
		segmentmask = np.zeros(image.shape, dtype=np.uint8)
		currentobj = 1
		steptreshold = MAGICKCONF['step']
		for i in range(image.shape[0]):
			for j in range(image.shape[1]):
				if (segmentmask[i][j] == 0) and (image[i][j]>0):
					if self.findFill(image, i, j, steptreshold, segmentmask, currentobj):
						currentobj += 1
		return segmentmask
	
	def findFill(self, image, i, j, treshold, segmentmask, currentobj):
		candidates = []		
		self.findI(image, i, j, image[i][j], treshold, candidates)
		x = i
		y = j
		
		if x>=image.shape[0]:			
			return
		if y>=image.shape[1]:
			return
		
		valid = [i for i in candidates if segmentmask[i] == 0]
		if len(valid) == 0:
			return
		if len(valid) >= MAGICKCONF['minlen']:
			for i in valid:
				segmentmask[i] = currentobj
			print('Added obj', currentobj,
				  'with', len(valid), 'points',
				  'and', len(candidates), 'candidates'
				  
				  )
		
			return True
	
	def check(self, image, i, j, basevalue, treshold, candidates):
		global segmentmask
		if (i<0) or (j<0):
			return False
		if (i>=image.shape[0]) or (j>=image.shape[1]):
			return False
		if image[i][j] < treshold:
			return False
		if segmentmask[i][j]>0:
			return False
		return (i, j) not in candidates
	
	
	def findI(self, image, i, j, basevalue, treshold, candidates):
		FoundAll = False
		candidates.append((i, j))
		
		NotWathed = [True] * len(candidates)
		
		while not FoundAll:
			FoundAll = True
			
			for i, (candidate, notwatched) in enumerate(zip(candidates, NotWathed)):
				if not notwatched:
					continue
				
				x = candidate[0]
				y = candidate[1]

				if x>=image.shape[0]:
					continue
				if y>=image.shape[1]:
					continue
				cvalue = image[x][y]

				if self.check(image, x+1, y, cvalue, treshold, candidates):
					candidates.append((x+1, y))
					FoundAll = False
					NotWathed.append(True)
				if self.check(image, x-1, y, cvalue, treshold, candidates):
					candidates.append((x-1, y))
					FoundAll = False
					NotWathed.append(True)
				if self.check(image, x, y+1, cvalue, treshold, candidates):
					candidates.append((x, y+1))
					FoundAll = False
					NotWathed.append(True)
				if self.check(image, x, y-1, cvalue, treshold, candidates):
					candidates.append((x, y-1))
					FoundAll = False
					NotWathed.append(True)				
				NotWathed[i] = False
	
	def Hightlight(self, image):
		image = transform.rotate(image, -90, resize=True)*255
		treshold = MAGICKCONF['treshold']
		tresholdmask = image < treshold
		for i in range(image.shape[0]):
			for j in range(image.shape[1]):
				if tresholdmask[i][j]:
					image[i][j] = 0
		segmentmask = self.recDiv(image)
		if 'debug' in MAGICKCONF and MAGICKCONF['debug']:
			io.imshow(segmentmask)
			io.show()
		segmentmask = transform.rotate(segmentmask, 90, resize=True) * 255
		return segmentmask, 1
		
	def Divide(self, segmentmatrix):
		objects = set(map(lambda x:int(x+0.5), segmentmatrix.flatten()))
		
		objects.remove(0)
		
		coords = []
		
		print(objects)
		
		for cobject in objects:
			allpoints = []
			for i in range(segmentmatrix.shape[0]):
				for j in range(segmentmatrix.shape[1]):
					if  segmentmatrix[i][j] == cobject:
						allpoints.append((i, j))
			maxx = minx = allpoints[0][0] 
			maxy = miny = allpoints[0][1]
			
			maxx = max(map(lambda x:x[0], allpoints))
			minx = min(map(lambda x:x[0], allpoints))
			maxy = max(map(lambda x:x[1], allpoints))
			miny = min(map(lambda x:x[1], allpoints))
			
			coords.append((minx, miny, maxx, maxy))
		return coords
			
			
		
		
		
		
