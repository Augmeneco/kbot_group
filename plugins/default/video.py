param = (('v', '5.68'), ('q',' '.join(answ_text)),('count','10'),('access_token',usertoken),('adult','1'))
res = requests.post('https://api.vk.com/method/video.search', data=param)
res = json.loads(res.text)
info = ''
if (res['response']['count'] != 0):
	for k in range(len(res['response']['items'])-1):
		info = info+'video'+str(res['response']['items'][k]['owner_id'])+'_'+str(res['response']['items'][k]['id'])+','
	param = (('v', '5.68'), ('peer_id',toho),('access_token',token),('message','Видео по вашему запросу'),('attachment',info))
	requests.post('https://api.vk.com/method/messages.send', data=param)
else:
	apisay('Видео по запросу не найдены.',toho)
