from PIL import Image
longpoll[userid]=result
try:
	if 'photo' in longpoll[userid]['object']['attachments'][0]:
		ret = longpoll[userid]['object']['attachments'][0]['photo']['sizes']
		num = 0
		for size in ret:
			if size['width'] > num:
				num = size['width']
				url = size['url']
		ret = requests.get(url).content
		open('img/vietnam/'+str(userid)+'.png','wb').write(ret)
		pic1 = Image.open('img/vietnam/vietnam.png')
		pic2 = Image.open('img/vietnam/'+str(userid)+'.png')
		pic1 = pic1.resize(pic2.size)
		pic2 = pic2.convert('RGBA')
		pic3 = Image.alpha_composite(pic2,pic1)
		pic3.save('img/vietnam/'+str(userid)+'.png')
		sendpic('img/vietnam/'+str(userid)+'.png','',toho)
except IndexError:
	apisay('Пикчу то вставь',toho)