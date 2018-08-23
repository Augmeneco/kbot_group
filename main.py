# -*- coding: utf-8 -*-
import requests, json, threading, sys, random, os, time, datetime
from termcolor import colored
sys.path.append('system')
import augdb
kb_name = ['158856938','кв','хуй']
cmds = json.loads(open('system/cmds.json','r').read())['path']
usertoken = 'токен юзера' #нужен для команд в которых токен группы не работает, к примеру поиск видео
token = 'токен группы'
###важные переменные
balance = {}
longpoll = {}
###
def do_cmd(cmd,answ_text,toho,userid):
	exec(open('plugins/'+cmd,'r').read())
def apisay(text,toho):
	return requests.post('https://api.vk.com/method/messages.send',data={'access_token':token,'v':'5.80','peer_id':toho,'message':text})
def sendpic(pic,mess,toho):
	ret = requests.get('https://api.vk.com/method/photos.getMessagesUploadServer?access_token={access_token}&v=5.68'.format(access_token=token)).json()
	with open(pic, 'rb') as f:
		ret = requests.post(ret['response']['upload_url'],files={'file1': f}).text
	ret = json.loads(ret)
	ret = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto?v=5.68&album_id=-3&server='+str(ret['server'])+'&photo='+ret['photo']+'&hash='+str(ret['hash'])+'&access_token='+token).text
	ret = json.loads(ret)
	requests.get('https://api.vk.com/method/messages.send?attachment=photo'+str(ret['response'][0]['owner_id'])+'_'+str(ret['response'][0]['id'])+'&message='+mess+'&v=5.68&peer_id='+str(toho)+'&access_token='+str(token))
lpb = requests.post('https://api.vk.com/method/groups.getLongPollServer',data={'access_token':token,'v':'5.80','group_id':'158856938'}).text
lpb = json.loads(lpb)['response']
print(lpb)
print('['+colored('*','green')+'] Инициализация Longpoll завершена')
ts = lpb['ts']
start_time = time.monotonic()
while True:
	try:
		#print('Жив')
		response = requests.post(lpb['server']+'?act=a_check&key='+lpb['key']+'&ts='+str(ts)+'&wait=25').text
		response = json.loads(response)
		for result in response['updates']:
			ts = response['ts']
			text = result['object']['text']
			toho = result['object']['peer_id']
			userid = result['object']['from_id']
			if '[club' in text:
				text = text.replace('[club','')
				text = text.split('|')
				text = text[0]+text[1].split(']')[1]
			text = text.split(' ')
			if text[0].lower() in kb_name and len(text) > 1:
				print('['+colored('*','green')+'] Упоминание кб в '+str(toho))
				text.remove(text[0])
				answ_text = ' '.join(text).split(' ')
				if len(text) > 1:
					answ_text.remove(text[0])
				else:
					answ_text = ['']
				if text[0].lower() in cmds:
					usermode = 0
					if len(augdb.read('system/users.db','vip','id='+str(userid))) > 0:
						usermode = 1
					if len(augdb.read('system/users.db','admin','id='+str(userid))) > 0:
						usermode = 2
					cmdmode = cmds[text[0]][0]
					if cmds[text[0]][0]=='default':
						threading.Thread(target=do_cmd,args=('default/'+cmds[text[0]][1],answ_text,toho,userid)).start()
					if cmds[text[0]][0]=='vip' and usermode > 0:
						threading.Thread(target=do_cmd,args=('vip/'+cmds[text[0]][1],answ_text,toho,userid)).start()
					if cmds[text[0]][0]=='admin' and usermode == 2:
						threading.Thread(target=do_cmd,args=('admin/'+cmds[text[0]][1],answ_text,toho,userid)).start()
					if cmds[text[0]][0]=='admin' and usermode < 2:
						apisay('Ну и хули ты забыл в админке?', toho)
					if cmds[text[0]][0]=='vip' and usermode == 1:
						apisay('А випки то у тебя нет, лол',toho)
				else:
					param = (('q',' '.join(answ_text)),('adminname','кекер'))
					cmdl = requests.post('https://isinkin-bot-api.herokuapp.com/1/talk',data=param).json()
					print(cmds)
					if 'text' in cmdl:
						apisay(cmdl['text'],toho)
					else:
						apisay('Команда не найдена :(', toho)
	except KeyError:
		print('['+colored('*','red')+'] Ошибка обработки Longpoll')
		lpb = requests.post('https://api.vk.com/method/groups.getLongPollServer',data={'access_token':token,'v':'5.80','group_id':'158856938'}).text
		lpb = json.loads(lpb)['response']
		print(lpb)
		ts = lpb['ts']
		continue	