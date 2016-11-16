import requests
import json

login_url = "https://api.zoomeye.org/user/login"
user_info_url = "https://api.zoomeye.org/resources-info"
host_search_url = "https://api.zoomeye.org/host/search"
web_search_url = "https://api.zoomeye.org/web/search"

user = "jackfredzk@gmail.com"
password = "1a2a3a4a5a"

######################
# get access_token
######################

payload = "{\r\n\"username\":\"%s\",\r\n\"password\":\"%s\"\r\n}" % (user, password)
headers = {
	'content-type': "application/json",
	'cache-control': "no-cache"
	}
access_token_response = requests.request("POST", login_url, data=payload, headers=headers)

######################
# get access_token
######################
access_token = json.loads(access_token_response.text)["access_token"]
print "login success!"


######################
# get user info
######################

authorization = "JWT %s" % (access_token)
headers = {
    'authorization': authorization,
    'cache-control': "no-cache"
    }
get_user_info_response = requests.request("GET", user_info_url, headers=headers)

######################
# get user info
######################
user_info_response_obj = json.loads(get_user_info_response.text)
host_search_num = user_info_response_obj["resources"]["host-search"]
web_search_num = user_info_response_obj["resources"]["web-search"]
print "host search limit:%s , web search limit:%s" % (host_search_num, web_search_num)


######################
# search host or web 
######################

choice = raw_input("choice host or web search:")
if choice == "host":
	print "change to host search"
	querystring = {
		"query":"",
		"page":"",
		"facets":"",
		"app":"",
		"device":"",
		"service":"",
		"os":"",
		"port":"",
		"country":"",
		"city":""
	}
else:
	print "change to web search"
	querystring = {
		"query":"",
		"page":"",
		"facets":"",
		"webapp":"",
		"component":"",
		"framework":"",
		"frontend":"",
		"server":"",
		"waf":"",
		"os":"",
		"country":"",
		"city":""
	}

true_query = {}
for item in querystring:
	s_tips = "query %s:" % (item)
	get_input_value = raw_input(s_tips)
	if get_input_value:
		true_query[item] = get_input_value

if choice == "host":
	search_response = requests.request("GET", host_search_url, headers=headers, params=true_query)
else:
	search_response = requests.request("GET", web_search_url, headers=headers, params=true_query)

search_list = json.loads(search_response.text)["matches"]
print len(search_list)
print search_list[0]
