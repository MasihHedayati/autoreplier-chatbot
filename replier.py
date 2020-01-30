import configparser as cfg
import time
from telethon import TelegramClient, events

parser=cfg.ConfigParser()
parser.read('Config.cfg')
phone= str(parser.get('creds','mobile'))
#print(phone)
user_name = parser.get('creds','user_name')
api_hash = parser.get('creds','api_hash')
api_id = int(parser.get('creds','api_id'))
pwd = parser.get('creds','password')
session_file="/home/pmpardeshi/AutoReplier/pmpardeshi.session"
	



if __name__ == '__main__':

	
	message="he is busy right now"
	
	#client = TelegramClient(user_name, api_id, api_hash, sequential_updates=True)
	client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)


	@client.on(events.NewMessage(incoming=True))
	
	async def handle_new_message(event):

		if event.is_private: 
			from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
			
			if not from_.bot: 
				print(time.asctime(), '-', event.message)  # optionally log time and message
				time.sleep(1)  # pause for 1 second to rate-limit automatic replies
				await event.respond(message)


	print(time.asctime(), '-', 'Auto-replying...')
	client.start(phone,pwd)
	client.run_until_disconnected()
	print(time.asctime(), '-', 'Stopped!')	
