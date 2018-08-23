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
		open('img/kek/'+str(userid)+'.jpg','wb').write(ret)
		image_obj = Image.open('img/kek/'+str(userid)+'.jpg')
		if answ_text[0] == 'лол':
			image2 = image_obj.crop([0,0,int(image_obj.size[0]/2),int(image_obj.size[1])])
			image2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
			image_obj.paste(image2,(int(image_obj.size[0]/2),0))
			image_obj.save('img/kek/'+str(userid)+'.jpg')
			sendpic('img/kek/'+str(userid)+'.jpg','',toho)
		else:
			image2 = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
			image2 = image2.crop([0,0,int(image_obj.size[0]/2),int(image_obj.size[1])])
			image2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
			image_obj = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
			image_obj.paste(image2,(int(image_obj.size[0]/2),0))
			image_obj.save('img/kek/'+str(userid)+'.jpg')
			sendpic('img/kek/'+str(userid)+'.jpg','',toho)
except IndexError:
	apisay('Пикчу то вставь',toho)