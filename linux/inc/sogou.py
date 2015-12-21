import urllib, req, re, sout, time

def sogousearch(query, start=1):
	sout.write("Exteracting 32% Bing ...        ")
	p = urllib.urlencode({ 'keyword':query, 'p':start, 'pg':'webSearchList', 'type':'1' })
	s = req.curllib("http://wap.sogou.com/web/searchList.jsp", p)

	if s != "Error":
		s = re.findall('&amp;url=(.*?)&amp;',s)
		for x in range(0, len( list( s ) ) ):
			s[x] = urllib.unquote(s[x]).decode('utf8') 
		return list( s )
	else:
		sout.write("\033[1;31mError connecting to Bing!	\033[0m")
		return []
