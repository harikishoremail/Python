#!usr/bin/python3.4
import pymysql
import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/html\n\n")

str_word="what is the phone number and fax number of google"
arr=str_word.split(" ")
#eliminating stop words
f = open( "stopwords.txt", "r" )
a = []
stopw=[]
for line in f:
    a+=[line]
f.close()
length_query = len(arr)
length_stop = len(a)
check =False
i=0
while( i <length_query):
	j=0
	while(j < length_stop):
		temp=a[j]
		l = len(temp)-2
		t = temp[1:l]
		if arr[i] == t:
			del arr[i]
			i-=1
			length_query -= 1
			#check=True
			break
		j+=1
	i+=1
			#stopw+=[t]


finance = ['sno', 'fin_ticker', 'marketcap', 'e_value', 'ret_on_assets', 'tot_cash', 'op_cash', 'lev_free_cf', 'tot_debt', 'curr_ratio', 'gross_profit', 'prof_margin', 'last_trade', 'trade_time', 'prev_close'];
management= ['serialno', 'mgt_ticker', 'high_paid_emp', 'high_pay', 'key_exe_list'];

profiles= ['ticker', 'name', 'Address', 'phonenum', 'faxnum', 'website', 'Index_mem', 'sector', 'industry', 'full_time', 'news', 'bus_summ'];
column=[]
#keyword finding
f = open( "keywords.txt", "r" )
keywords=[]
kw=[]
for line in f:
    keywords=line.split(" ")
    aa=0
    while(aa < len(arr)):
	a=0
	while(a < len(keywords)):
		#print(keywords)
		if(keywords[a]== arr[aa] ):
			kw.append(keywords[0]);
			arr = [w.replace(arr[aa], keywords[0]) for w in arr]
			print(kw)
		a+=1
	aa+=1
f.close()
#replacing the correct word in data base ..arrr
#query creating	
k=0
while(k < len(arr)):
	if arr[k] in finance:
		column+=["finance."+arr[k]]
	elif arr[k] in management:
		column+=["management."+arr[k]]
	elif arr[k] in profiles:
		column+=["profiles."+arr[k]]
	k+=1

#print (len(arr))
arr1=[i.split('.')[0] for i in column]
query = "select "+ column[0]+" from "+arr1[0];
print(query)

conn = pymysql.connect(host='localhost', user='root', passwd='', db='companydb')
cur = conn.cursor()
cur.execute(query)

result = " "

for r in cur:
    result = result + " " + str(r)
cur.close()
conn.close()


htmlFormat = """
<html>
    <Title>Python - NLIDB </Title>
      <body>
		<br><br><br><br><br><br><br><br>
	        <h3 style="color:blue" align="center">The RESULT IS : {result} </h3>
      </body>
</html> """

print(htmlFormat.format(**locals()))
