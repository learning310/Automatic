import requests
url = "https://app.xaut.edu.cn/ncov/wap/default/save"
# 请求头
headers = {
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Connection': 'keep-alive',
	'Content-Length': '2223',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Cookie': 'eai-sess=3j4ulav4050bvtpf376mg8urb6; UUkey=178e86dfa13bba2f261f839a4e399eec', #################################################
	'Host': 'app.xaut.edu.cn',
	'Origin': 'https://app.xaut.edu.cn',
	'Referer': 'https://app.xaut.edu.cn/ncov/wap/default/index',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-origin',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
	'X-Requested-With': 'XMLHttpRequest'
}
# 请求体
data = {
    "zgfxdq":"0",
    "mjry":"0",
    "csmjry":"0",
    "tw":"2",# 体温，选第二项
    "sfcxtz":"0",
    "sfjcbh":"0",
    "sfcxzysx":"0",
    "qksm":"",
    "sfyyjc":"0",
    "jcjgqr":"0",
    "remark":"",
    "address": "陕西省西安市碑林区东关南街街道咸宁西路11号西安理工大学金花校区",
	"geo_api_info": "{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"dEa\":\"jsonp_952503_\",\"position\":{\"Q\":34.25172,\"R\":108.99192,\"lng\":108.99192,\"lat\":34.25172},\"message\":\"Get+ipLocation+success.Get+address+success.\",\"location_type\":\"ip\",\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{\"citycode\":\"029\",\"adcode\":\"610103\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"咸宁西路\",\"streetNumber\":\"11号\",\"country\":\"中国\",\"province\":\"陕西省\",\"city\":\"西安市\",\"district\":\"碑林区\",\"township\":\"东关南街街道\"},\"formattedAddress\":\"陕西省西安市碑林区东关南街街道咸宁西路11号西安理工大学金花校区\",\"roads\":[],\"crosses\":[],\"pois\":[]}",
	"area": "陕西省+西安市+碑林区",
	"province": "陕西省",
	"city": "西安市",
	"sfzx": "1",
    "sfjcwhry":"0",
    "sfjchbry":"0",
    "sfcyglq":"0",#是否处于隔离期
    "gllx":"",
    "glksrq":"",
    "jcbhlx":"",
    "jcbhrq":"",
    "bztcyy":"1",
    "sftjhb":"0",
    "sftjwh":"0",
    "jcjg":"",
    "date":str(datetime.date.today() - datetime.timedelta(days=1)).replace("-", ""),
    "uid":"61784",       #################################################
    "created":str(int(time.time())),
    "jcqzrq":"",
    "sfjcqz":"",
    "szsqsfybl":"0",
    "sfsqhzjkk":"0",
    "sqhzjkkys":"",
    "sfygtjzzfj":"0",
    "gtjzzfjsj":"",
    "fxyy":"上课", #返校原因
    "id":"20941180",        #################################################
    "gwszdd":"",
    "sfyqjzgc":"",
    "jrsfqzys":"",
    "jrsfqzfy":"",
    "ismoved":"0"
}

print(eval(requests.post(url=url, data=data, headers=headers).text)['m'])
