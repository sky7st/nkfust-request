#coding=utf-8
import requests,re,urllib2,cookielib,os


home_url = "http://aais15.nkfust.edu.tw/crs_quest/fill_out.jsp?lang=C&crsno="
login_check_url = "http://aais15.nkfust.edu.tw/crs_quest/logincheck.jsp"
std_qst_url = "http://aais15.nkfust.edu.tw/crs_quest/stud_qst.jsp"
save_data_url = "http://aais15.nkfust.edu.tw/crs_quest/save_data.jsp"
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
opener.open(login_check_url)

cookie_compile_jsessionid = re.compile(r'JSESSIONID=(.*?) for')
cookie_compile_TS019720c7 = re.compile(r'TS019720c7=(.*?) for')
jsessionid = cookie_compile_jsessionid.findall(str(cookie))
TS019720c7 = cookie_compile_TS019720c7.findall(str(cookie))


res = requests.session()
login_check_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                       "Host":"aais15.nkfust.edu.tw",
                       "Origin":"http://aais15.nkfust.edu.tw",
                       "Referer":"http://aais15.nkfust.edu.tw/crs_quest/note.html",
                       "cookie":"JSESSIONID=%s; TS019720c7=%s"%(jsessionid[0],TS019720c7[0])}
CTID=""
STUID=""
PASSWD=""

CTID = raw_input("Input CTID:")
STUID = raw_input("Input STID:")

PASSWD= raw_input("Input PassWord:")

login_param = {"CTID":CTID,"STUID":STUID,"PASSWD":PASSWD}

qus_header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                       "Host":"aais15.nkfust.edu.tw",
                       "Origin":"http://aais15.nkfust.edu.tw",
                       "Referer":"http://aais15.nkfust.edu.tw/crs_quest/stud_qst.jsp",
                       "cookie":"JSESSIONID=%s; TS019720c7=%s"%(jsessionid[0],TS019720c7[0])}




menu = res.post(login_check_url,headers = login_check_headers, params = login_param)


std = res.get(std_qst_url,headers = login_check_headers)

re1 = re.compile(r'<a href="(.*?)">')
patt1 = re1.findall(std.text)


del patt1[len(patt1)-1]
crsno = 0
crsno2 = 1
use_lang = 0
qus_url = ""
if len(patt1)!=0:
    i = 1
    for url in patt1:
        if "lang=C" in url:
            use_lang_com = re.compile(r'&use_lang=(\d?)')
            crs_com = re.compile(r'crsno=(.*?)&')
            crs2_com = re.compile(r'crsno2=(.*?)&')

            crs = crs_com.findall(url)
            crs2 = crs2_com.findall(url)
            use_lang = use_lang_com.findall(url)
            qus_url = home_url +  crs[0] + "&crsno2=" + crs2[0] + "&use_lang=" + use_lang[0]
            save_data_header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                                   "Host":"aais15.nkfust.edu.tw",
                                   "Origin":"http://aais15.nkfust.edu.tw",
                                   "Referer":qus_url,
                                   "cookie":"JSESSIONID=%s; TS019720c7=%s"%(jsessionid[0],TS019720c7[0])}
            answer = "5"
            save_data_param = {"use_lang":"%s"%use_lang[0],
            "lang":"C",
            "card_type":"1",
            "crsno":"%s"%crs[0],
            "crsno2":"%s"%crs2[0],
            "qa01":answer,
            "qa02":answer,
            "qa03":answer,
            "qa04":answer,
            "qa05":answer,
            "qb01":answer,
            "qb02":answer,
            "qb03":answer,
            "qb04":answer,
            "qb05":answer,
            "qb06":answer,
            "qb07":answer,
            "qb08":answer,
            "qb09":answer,
            "qb10":answer,
            "qb11":answer,
            "qb12":answer,
            "qb13":answer,
            "qb14":answer,
            "qb15":answer,
            "qb16":answer,
            "qb17":answer,
            "qb18":answer,
            "qb19":answer,
            "qc01":"",
            "qc02":"",
            "qc03":"",
            "qc04":"",
            "qc05":""}
            qus = res.get(qus_url,headers = qus_header)
            
            save = res.post(save_data_url, headers = save_data_header, params = save_data_param)
        print "the %d questionnairesis finished!"%i
        i+=1
    print "all questionnairesis"
    os.system('pause')
else:
    print "no questionnaires!"
    os.system('pause')
