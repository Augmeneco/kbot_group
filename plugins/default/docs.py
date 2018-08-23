param = (('v', '5.68'), ('q',' '.join(answ_text)),('count','100'),('access_token',token))
res = requests.post('https://api.vk.com/method/docs.search', data=param)
res = json.loads(res.text)
if (res['response']['count'] != 0):
	fcount=0
	info = ''
	for k in range(len(res['response']['items'])-1):
		if(fcount == 10):
			break
		info = info+'doc'+str(res['response']['items'][k]['owner_id'])+'_'+str(res['response']['items'][k]['id'])+','
		fcount = fcount+1
	param = (('v', '5.68'), ('peer_id',toho),('access_token',token),('message','Документы по вашему запросу'),('attachment',info))
	requests.post('https://api.vk.com/method/messages.send', data=param)
else:
	apisay('Документы по запросу не найдены',toho)