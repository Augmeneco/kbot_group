
import psutil
text = '[ Статистика ]<br>Система:<br>&#8195;Процессор:<br>'
for idx, cpu in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
	text += '&#8195;&#8195;Ядро №'+str(idx+1)+': '+str(cpu)+'%<br>'
mem = psutil.virtual_memory()
MB = 1024 * 1024
text += '&#8195;ОЗУ:<br>&#8195;&#8195;Всего: '+str(int(mem.total / MB))+'MB<br>&#8195;&#8195;Использовано: '+str(int((mem.total - mem.available) / MB))+'MB<br>&#8195;&#8195;Свободно: '+str(int(mem.available / MB))+'MB<br>&#8195;&#8195;Использовано ботом: '+str(int(psutil.Process().memory_info().vms / MB))+'MB<br>&#8195;'
end_time = time.monotonic()
text += 'Бот:<br>&#8195;&#8195;Время работы: '+str(datetime.timedelta(seconds=end_time - start_time))
text += '\n&#8195;&#8195;Уровень прав: '+str(usermode)
param = (('v', '5.68'), ('peer_id',toho), ('access_token', token),('message', text))
requests.post('https://api.vk.com/method/messages.send', param)