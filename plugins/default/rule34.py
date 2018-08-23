import untangle
try:
	try:	
		r34text = ' '.join(answ_text)
		r34text = r34text.replace(' ','+')
		blacklist = '-fur+-scat*+-darling_in_the_franxx+-furry+-dragon+-guro+-animal_penis+-animal+-wolf+-fox+-webm+-my_little_pony+-monster*+-3d+-animal*+-ant+-insects+-mammal+-horse+-blotch+-deer+-real*+-shit+-everlasting_summer+-copro*+-wtf+'
		parse = untangle.parse('http://0s.oj2wyzjtgqxhq6dy.cmle.ru/index.php?page=dapi&s=post&q=index&limit=1000&tags='+blacklist+str(r34text))
		randnum = random.randint(0,len(parse.posts.post))
		mess = 'Дрочевня подкатила<br>('+str(randnum)+'/'+str(len(parse.posts.post))+')<br>----------<br>Остальные теги: '+parse.posts.post[randnum]['tags']
		parse = parse.posts.post[randnum]['file_url']
		if parse.find('img.rule34')<0:
			parse = parse.replace('rule34.xxx','0s.oj2wyzjtgqxhq6dy.cmle.ru')
			parse = parse.replace('https','http')
			print(parse)
		else:
			parse = parse.replace('img.rule34.xxx','nfwwo.oj2wyzjtgqxhq6dy.cmle.ru')
			parse = parse.replace('https','http')
		pic = requests.get(parse).content
		open('img/rule34/'+str(userid)+'.jpg','wb').write(pic)
		sendpic('img/rule34/'+str(userid)+'.jpg',mess,toho)
	except UnicodeEncodeError:
		apisay('Ничего не найдено :(',toho)
except AttributeError:
	apisay('Ничего не найдено :(',toho)
