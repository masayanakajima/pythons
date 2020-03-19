
def matching(string,start):
	result=[]
	l=len(string)
	if(l<=1):
		return []
	elif(l==2):
		if(string[0]==string[1]):
			return [set([(start,start+1)])]
		else:
			return []
	else:
		for i in range(0,l-1):
			for j in range(1,l-i-1):
				if(string[i]==string[l-j]):
					s1=[]
					s2=[]
					if(i==0):
						s1=[set([(start+i,start+l-j)])]
					else:
						s1=cross(matching(string[:i],start),set([(start+i,start+l-j)]))
					
					if(l-j-1<i+1 and j>1):
						s2=matching(string[l-j+1:],start+l-j+1)
					elif(l-j-1>=i+1 and j==1):
						s2=matching(string[i+1:l-j],start+i+1)
					elif(l-j-1>=i+1 and j>1):
						s2=cross2(matching(string[i+1:l-j],start+i+1),matching(string[l-j+1:],start+l-j+1))

					result=result+cross2(s1,s2)
		return remove(result)

def remove(result):
	s=result
	s1=result
	s2=result
	for f1 in s1:
		for f2 in s2:
			if(f1.issuperset(f2) and f1!=f2):
				s.remove(f2)
	return s


def cross(s1,f2):
	s=[]
	if len(s1)==0:
		return [f2]
	for f1 in s1:
		s.append(f1.union(f2))
	return s

def cross2(s1,s2):
	s=[]
	if len(s1)==0:
		return s2
	if len(s2)==0:
		return s1
	for f1 in s1:
		for f2 in s2:
			s.append(f1.union(f2))
	return s

print(matching("ACBABB",0))