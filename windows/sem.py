import sys, os, re, args, only, time
if sys.platform == 'linux' or sys.platform == 'linux2':
	inc = "/inc/"
else:
	inc = "\\inc\\"

sys.path.append(os.path.dirname(os.path.realpath(__file__))+inc)
import mainsearch, sout


argments = args.argsload()

results = []
query = argments["dork"]
pages = argments["p"]
webappdir = argments["wp"]
outputfile = argments["o"]
donly = argments['do']
honly = argments['ho']
norepeat = argments['nor']


print("\033[92m " +  args.bannerx())
print("\033[92m[+]:\033[0m\033[0m Dork : \033[32m" + query + "\033[0m")

#time.sleep(10)

for startnum in range(int(pages[0]),int(pages[1])):
	try:
		results = results + list( set( mainsearch.search( query, startnum, int(pages[1])-1 ) ) )
	except (KeyboardInterrupt, SystemExit):
		print("\r\n\033[31mExited... bye!")
		exit()


if donly:
	results = only.d(results,webappdir)
elif honly:
	results = only.h(results,webappdir)

results = sout.sort_and_deduplicate(results)

if len(results) == 0:
	sout.done("\033[31m[!]: \033[91mNo Internet Connection...!\n")
	exit()
else:
	print("\r\033[92m[+]:\033[0m Urls: \033[92m%s\033[0m" %len(results) )

if outputfile:
	path = outputfile.split("/")
	try:
		path.pop()
	except:
		0
	if os.access("/".join(path), os.R_OK):
		
		if os.path.isfile(outputfile) == False :
			try:
				open(outputfile, 'w').write("[+]===================[SEMaster]===================[+]\r\n")
			except:
				0
		try:
			f = open( outputfile, 'a')
			f.write("\r\n".join(results)+"\r\n")
			f.close()
		except:
			0
		print("\r\033[92m[[+]:\033[0m Outfile : "+"["+outputfile+"\033[0m")
	else:
		print("\033[31m"+"[+]:"+"\033[0m"+" Outfile : "+"\033[31m"+"Error"+"\033[0m")

print("................................")
print("\n".join(results))
