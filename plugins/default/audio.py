param = (('v', '5.29'), ('q',' '.join(answ_text)),('count','200'),('sort','2'),('access_token',usertoken))
res = requests.post('https://api.vk.com/method/audio.search', data=param)
res = json.loads(res.text)
if (res['response']['count'] != 0):
	fcount=0
	info = ''
	for k in range(len(res['response']['items'])-1):
		if(fcount == 10):
			break
		info = info+'audio'+str(res['response']['items'][k]['owner_id'])+'_'+str(res['response']['items'][k]['id'])+','
		fcount = fcount+1
	param = (('v', '5.74'), ('peer_id',toho),('access_token',token),('message','Музыка по запросу вашему запросу'),('attachment',info))
	requests.post('https://api.vk.com/method/messages.send', data=param)
else:
	apisay('Музыка по запросу не найдена',toho)