import untangle
try:
	try:
		r34text = ' '.join(answ_text)
		r34text = r34text.replace(' ','+')
		parse = untangle.parse('http://safebooru.org/index.php?page=dapi&s=post&q=index&limit=1000&tags='+str(r34text))
		randnum = random.randint(0,len(parse.posts.post))
		mess = 'Бурятские артики по запросу<br>('+str(randnum)+'/'+str(len(parse.posts.post))+')<br>----------<br>Остальные теги: '+parse.posts.post[randnum]['tags']
		parse = parse.posts.post[randnum]['file_url']
		parse = parse.replace('//','http://')
		pic = requests.get(parse).content
		open('img/booru/'+str(userid)+'.jpg','wb').write(pic)
		sendpic('img/booru/'+str(userid)+'.jpg',mess,toho)
	except UnicodeEncodeError:
		apisay('Ничего не найдено :(',toho)
except AttributeError:
	apisay('Ничего не найдено :(',toho)
