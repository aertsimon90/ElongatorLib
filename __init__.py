import random

class Elongator:
	def __init__(self):
		pass
	def middlemid_elongation(self, i, length):
		li = len(i)
		while li < length:
			diff = length-li
			if diff%2 == 0:
				leftdiff = diff/2
				rightdiff = leftdiff
			else:
				leftdiff = int(diff/2)
				rightdiff = leftdiff+1
			mid = li//2
			left = i[:mid]
			right = i[mid:]
			newleft = []
			for h in left[::-1]:
				if leftdiff:
					newleft.append(h)
					leftdiff -= 1
				newleft.append(h)
			newright = []
			for h in right:
				if rightdiff:
					newright.append(h)
					rightdiff -= 1
				newright.append(h)
			i = newleft[::-1]+newright
			li = len(i)
		return i
	def sidesmid_elongation(self, i, length):
		li = len(i)
		while li < length:
			diff = length-li
			if diff%2 == 0:
				leftdiff = diff/2
				rightdiff = leftdiff
			else:
				leftdiff = int(diff/2)
				rightdiff = leftdiff+1
			mid = li//2
			left = i[:mid]
			right = i[mid:]
			newleft = []
			for h in left:
				if leftdiff:
					newleft.append(h)
					leftdiff -= 1
				newleft.append(h)
			newright = []
			for h in right[::-1]:
				if rightdiff:
					newright.append(h)
					rightdiff -= 1
				newright.append(h)
			i = newleft+(newright[::-1])
			li = len(i)
		return i
	def left_elongation(self, i, length):
		li = len(i)
		while li < length:
			diff = length-li
			new = []
			for h in i:
				if diff:
					new.append(h)
					diff -= 1
				new.append(h)
			i = new
			li = len(i)
		return i
	def right_elongation(self, i, length):
		return self.left_elongation(i[::-1], length)[::-1]
	def left_messy_elongation(self, i, length):
		li = len(i)
		m = [1]*li
		diff = length-li
		while diff:
			nm = []
			for h in m:
				if diff and random.random()>0.5:
					h = h+1
					diff -= 1
				nm.append(h)
			m = nm
		ni = []
		for ii, h in enumerate(i):
			ni += [h]*m[ii]
		return ni
	def right_messy_elongation(self, i, length):
		return self.left_messy_elongation(i[::-1], length)[::-1]
	def middlemid_messy_elongation(self, i, length):
		li = len(i)
		mid = li//2
		if length == 1:
			return [i[mid]]
		left = i[:mid]
		right = i[mid:]
		diff = length-li
		if diff%2 == 0:
			leftdiff = diff/2
			rightdiff = leftdiff
		else:
			leftdiff = int(diff/2)
			rightdiff = leftdiff+1
		return self.left_messy_elongation(left, len(left)+leftdiff)+self.right_messy_elongation(right, len(right)+rightdiff)
	def sidesmid_messy_elongation(self, i, length):
		li = len(i)
		mid = li//2
		if length == 1:
			return [i[mid]]
		left = i[:mid]
		right = i[mid:]
		diff = length-li
		if diff%2 == 0:
			leftdiff = diff/2
			rightdiff = leftdiff
		else:
			leftdiff = int(diff/2)
			rightdiff = leftdiff+1
		return self.right_messy_elongation(left, len(left)+leftdiff)+self.left_messy_elongation(right, len(right)+rightdiff)
	def elongation(self, i, length, type="middlemid"):
		li = len(i)
		if li == 0:
			return []
		if li == 1:
			return i*length
		if type == "middlemid":
			return self.middlemid_elongation(i, length)
		elif type == "sidesmid":
			return self.sidesmid_elongation(i, length)
		elif type == "left":
			return self.left_elongation(i, length)
		elif type == "right":
			return self.right_elongation(i, length)
		elif type == "left_messy":
			return self.left_messy_elongation(i, length)
		elif type == "right_messy":
			return self.right_messy_elongation(i, length)
		elif type == "middlemid_messy":
			return self.middlemid_messy_elongation(i, length)
		elif type == "sidesmid_messy":
			return self.sidesmid_messy_elongation(i, length)
		else:
			raise ValueError("Invalid type of list elongation function.")
	def left_compaction(self, i, length):
		li = len(i)
		while li > length:
			diff = li-length
			new = []
			for ii, h in enumerate(i):
				if diff and (ii-1)%2 == 0:
					diff -= 1
				else:
					new.append(h)
			i = new
			li = len(i)
		return i
	def right_compaction(self, i, length):
		return self.left_compaction(i[::-1], length)[::-1]
	def middlemid_compaction(self, i, length):
		if length == 1:
			return [i[0]]
		li = len(i)
		mid = li//2
		left = i[:mid]
		right = i[mid:]
		diff = li-length
		if diff%2 == 0:
			leftdiff = diff/2
			rightdiff = leftdiff
		else:
			leftdiff = int(diff/2)
			rightdiff = leftdiff+1
		return self.left_compaction(left, len(left)-leftdiff)+self.right_compaction(right, len(right)-rightdiff)
	def sidesmid_compaction(self, i, length):
		if length == 1:
			return [i[0]]
		li = len(i)
		mid = li//2
		left = i[:mid]
		right = i[mid:]
		diff = li-length
		if diff%2 == 0:
			leftdiff = diff/2
			rightdiff = leftdiff
		else:
			leftdiff = int(diff/2)
			rightdiff = leftdiff+1
		return self.right_compaction(left, len(left)-leftdiff)+self.left_compaction(right, len(right)-rightdiff)
	def left_messy_compaction(self, i, length):
		li = len(i)
		while li > length:
			diff = li-length
			new = []
			for ii, h in enumerate(i):
				if diff and random.random()>0.5:
					diff -= 1
				else:
					new.append(h)
			i = new
			li = len(i)
		return i
	def right_messy_compaction(self, i, length):
		return self.left_messy_compaction(i[::-1], length)[::-1]
	def middlemid_messy_compaction(self, i, length):
		if length == 1:
			return [i[0]]
		li = len(i)
		mid = li//2
		left = i[:mid]
		right = i[mid:]
		diff = li-length
		if diff%2 == 0:
			leftdiff = diff/2
			rightdiff = leftdiff
		else:
			leftdiff = int(diff/2)
			rightdiff = leftdiff+1
		return self.left_messy_compaction(left, len(left)-leftdiff)+self.right_messy_compaction(right, len(right)-rightdiff)
	def sidesmid_messy_compaction(self, i, length):
		if length == 1:
			return [i[0]]
		li = len(i)
		mid = li//2
		left = i[:mid]
		right = i[mid:]
		diff = li-length
		if diff%2 == 0:
			leftdiff = diff/2
			rightdiff = leftdiff
		else:
			leftdiff = int(diff/2)
			rightdiff = leftdiff+1
		return self.right_messy_compaction(left, len(left)-leftdiff)+self.left_messy_compaction(right, len(right)-rightdiff)
	def compaction(self, i, length, type="middlemid"):
		li = len(i)
		if li == 0:
			return []
		if li == 1 or length == 1:
			return [i[li//2]]
		if type == "middlemid":
			return self.middlemid_compaction(i, length)
		elif type == "sidesmid":
			return self.sidesmid_compaction(i, length)
		elif type == "left":
			return self.left_compaction(i, length)
		elif type == "right":
			return self.right_compaction(i, length)
		elif type == "left_messy":
			return self.left_messy_compaction(i, length)
		elif type == "right_messy":
			return self.right_messy_compaction(i, length)
		elif type == "middlemid_messy":
			return self.middlemid_messy_compaction(i, length)
		elif type == "sidesmid_messy":
			return self.sidesmid_messy_compaction(i, length)
		else:
			raise ValueError("Invalid type of list compaction function.")
	def seq(self, a, b, valuediff=True):
		la = len(a)
		if not valuediff:
			return sum([1 if h==h2 else 0 for h, h2 in zip(a, b)])/la
		md = max(a+b)-min(a+b)
		return 1-(sum([abs(h-h2)/md for h, h2 in zip(a, b)])/la)
