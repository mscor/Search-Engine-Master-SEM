import urllib, req, re, sout

def bingsearch(query, start=0):
	sout.write("Exteracting 25% Bing ...        ")
	p = urllib.urlencode({'q' : query, 'first' : start , 'count': '50'})
	s = req.curllib("http://www.bing.com/search", p)

	if s != "Error":
		if '<li class="b_algo"><h2>' in s :
			s = re.findall('<li class="b_algo"><h2><a href="(.*?)" ',s)
			return s
        elif '</span><h2><a href=' in s :
			s = re.findall('<li class="b_algo"><h2><a href="(.*?)" ',s)
			return s
	else:
		sout.write("\033[1;31mError connecting to Bing!	\033[0m")
		return []
