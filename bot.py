from requests import get
from re import findall
from rubika.client import Bot
import time
import random

bot = Bot("AUTH")
target = input('GROUP ID: ')
answered = [bot.getGroupAdmins]
retries = {}
sleeped = False
group = bot.getGroupInfo(target)["data"]["group"]["group_title"]
print("                         Powered by Diego Gram")
print("---------------------------------------------------------------------")
print("Source name: diegogram")
print("This feature will be added soon Rock Paper Scissors")
#rock paper sissors
print("This feature will be added soon Number of panels")
#number panels
#number numberpanel Manage chat from the panel
#Education https://rubika.ir/joinc/BDDFBEGB0RMIJBJHJIWTKSROSPOGLNMV
#Manufacturer @web_dev
#Go to the chat panel admin panel: 
print("@web_dev3")
print(f"  Go to the chat panel admin panel: { group } ")
print("Version 1 source")
print("-----------------------------------")


Manufacturer = '@web_dev3'



plus= True

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue
		
		open("id.db","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if msg.get("text") == "." and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "✓", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!add") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "User successfully added!", message_id=msg.get("message_id"))

					elif msg.get("text") == "!help":
						bot.sendMessage(target, "!lock: Close the pawn\n !open: Open group \n !on: Turn on \n !off: Turn off the bot \n number: Random number \n !font matn: instead of matn Give your name \n !ping \n !user ID: Instead of an ID id Bad user \n !trans: Translator \n \n Version 1 of Diego Gram")
					elif msg.get("text").startswith("!cal"):
						msd = msg.get("text")
						if plus == True:
							try:
								call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
								if call[1] == "+":
									am = float(call[0]) + float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
									plus = False
							
								elif call[1] == "-":
									am = float(call[0]) - float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "*":
									am = float(call[0]) * float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "/":
									am = float(call[0]) / float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							except IndexError:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌" ,message_id=msg.get("message_id"))
						plus= True
					elif msg.get("text").startswith("!send") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "Message sent successfully✓", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "سلام":
						bot.sendMessage(target, "سلام عزیز من گل من عخش من", message_id=msg.get("message_id"))
						
						bot.sendMessage(target, "سلام عشقم چطوری ؟ ❤😍", message_id=msg.get("message_id"))
#دیگو گرام
					elif msg.get("text") == "بات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "انلاینم✓", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "اره" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "😐مبارکه", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "نه" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "اهمیت ندادم", message_id=msg.get("message_id"))

					elif msg.get("text") == "خوبی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "ممنون به خوبیت تو خوبی؟", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "number" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, random.randint(1, 999), message_id=msg.get("message_id"))
						#diegogram
					elif msg.get("text") == "numberpanel" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "This feature will be added soon", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "Rock Paper Scissors" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "This feature will be added soon", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ایول" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بنازم به ایول گفتنت😍", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "😡" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "چیز اضافی خودم😐💔", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "سلامتی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "اله", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "!help2" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "New features: \n 🔢 number \n 🔢💡numberpanel \n The rest of the features are not in this list! ", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چقدر منو دوست داری" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خیلی دوست دارم انقد که گفتنی نیست😊❤️", message_id=msg.get("message_id"))
						#دیکو گرام
					elif msg.get("text") == "استقلال" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "قسم به تیم استقلال ، قسم به سیمای خوبان ، قسم به ناصر حجازی ، ندای ما استقلال 💙", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "💙" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "قسم به تیم استقلال ، قسم به سیمای خوبان ، قسم به ناصر حجازی ، ندای ما استقلال 💙", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "پرسپولیس" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "پرسپولیس عشق آسیایی پرسپولیس خالق یک جامی گل بزن امشبو به یاد پروین و علی دایی ❤", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "❤" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "پرسپولیس عشق آسیایی پرسپولیس خالق یک جامی گل بزن امشبو به یاد پروین و علی دایی ❤", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "😎" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "هر کی با ما در افتاد ور افتاد 😎", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "😂" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خنده خنده می اورد", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "😐" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بخورش", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "😂😂" and msg.get("author_object_guid") :
						#دیگو گرام
						bot.sendMessage(target, "حون اوا", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "هعپ" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "آبی روشن عین من سیتی برف میاد سریع ترکیم هووو(خلسه اید یا هم نیاید)", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "امیر" and msg.get("author_object_guid") :
						#دیگو گرام
						bot.sendMessage(target, "عشق منه رئیس منه(امیر ارشادی)", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "نام" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, f"نام گروه: { group }", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "لینک" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "https://rubika.ir/Diegogram", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "گوه نخور" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "شب میرینم صبح بخور", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "ربات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "انلاینم✓", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "bot" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "انلاینم✓", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "خودتو معرفی کن" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "من ربات هستم که با هوش مصنوعی میتونم اینجا رو مدیریت کنم و باهاتون مثل یک انسان واقعی چت کنم", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "ممنون" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خواهش میکنم گلم💋😌", message_id=msg.get("message_id"))
						#دیگو کرام
					elif msg.get("text") == "بای" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "کجا میری بودی حالا 😕", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "چه خبر" and msg.get("author_object_guid") :
						#دیگو گرام
						bot.sendMessage(target, "سلامتی خوبم میگذرونم دیگه", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "عشق" and msg.get("author_object_guid") :
						#دیگو گرام
						bot.sendMessage(target, "😊❤️", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "منم خوبم" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خدا رو شکر 😘", message_id=msg.get("message_id"))
#دیگو گرام
					elif msg.get("text") == "فدات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خدا نکنه قربونت 😁❤️", message_id=msg.get("message_id"))
						#دیگو کرام
					elif msg.get("text") == "بی تر ادب" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "اره دا تو همینم نیستی 😏", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "هعی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "زر نزن باو", message_id=msg.get("message_id"))
						#دیگو کرام
					elif msg.get("text") == "مرسی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "😍", message_id=msg.get("message_id"))
						#دیگو گرام
						
					elif msg.get("text") == "https:// " and msg.get("author_object_guid"):
						print("One link da")
						#dellink
					elif msg.get("text") == "!start" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "سلام به ابر سرویس دیگو گرام خوش امدید💸 \n لطفا کلمه !help را ارسال کنید! \n و کلمه !help2 ارسال کنید!", message_id=msg.get("message_id"))
						

					if  msg.get("text").startswith('!user @'):
						try:
							user_info = bot.getInfoByUsername( msg.get("text")[7:])
							if user_info['data']['exist'] == True:
								if user_info['data']['type'] == 'User':
									bot.sendMessage(target, 'Name User:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nBio User:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
									print('sended response')
								else:
									bot.sendMessage(target, 'Is a channel' ,  msg.get('message_id'))
									print('sended response')
							else:
								bot.sendMessage(target, "There is no user" ,  msg.get('message_id'))
								print('sended response')
						except:
							print('server bug6')
							bot.sendMessage(target, "error" ,message_id=msg.get("message_id"))
							

					elif msg.get("text") == "!off" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "The robot was successfully disabled", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!ping"):
						
						try:
							responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
							bot.sendMessage(target, responser,message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "error", message_id=msg["message_id"])
							
					elif msg.get("text") == "name g" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, f"the name of the group: { group }", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!trans"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "Results sent to your pew", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "error", message_id=msg["message_id"])

					elif msg.get("text").startswith("!font"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							bot.sendMessage(target, "Results sent to your pew", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "error", message_id=msg["message_id"])
							
							
					elif msg.get("text").startswith("!air"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/weather/?city={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:])).text
							bot.sendMessage(target, "Results sent to your pew", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "error", message_id=msg["message_id"])
							
							
					elif msg.get("text").startswith("!name"):
						
						try:
							response = get("https://api.codebazan.ir/name/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "error", message_id=msg["message_id"])
							
							
					elif msg.get("text").startswith("!number"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/num/?num={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:])).text
							bot.sendMessage(target, "Results sent to your pew", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "error", message_id=msg["message_id"])

#دیگو گرام

					elif msg.get("text").startswith("!jok"):
						
						try:
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "error", message_id=msg["message_id"])

					elif msg.get("text") == "!time":
						bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))

					elif msg.get("text") == "":
						bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))

					elif msg.get("text") == "!del" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "Done", message_id=msg.get("message_id"))

					# elif msg.get("text").split(" ")[0] in  delmess:
					# 	bot.deleteMessages(target, [msg.get("message_id")])
					# 	bot.sendMessage(target, "یک پیام مستهجن پاک شد ✅", message_id=msg.get("message_id"))

#دیگو گرام
					elif msg.get("text") == "!lock" and msg.get("author_object_guid") in admins :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "Chat closed", message_id=msg.get("message_id"))

					elif msg.get("text") == "!open" and msg.get("author_object_guid") in admins :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "Chat opened", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!ban") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, f"User successfully removed", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, f"error", message_id=msg.get("message_id"))
								
						except IndexError:
							a = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
							if a in admins:
								bot.sendMessage(target, f"error", message_id=msg.get("message_id"))
							else:
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								bot.sendMessage(target, f"User successfully removed", message_id=msg.get("message_id"))

				else:
					if msg.get("text") == "!on" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "The robot was successfully activated", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"The user was removed from the group due to non-compliance with the rules", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"Hello user {user} To the group {name} Welcome😍", message_id=msg["message_id"])
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"Goodbye", message_id=msg["message_id"])
					
				elif msg.get("text") == "number" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, random.randint(1, 100), message_id=msg.get("message_id"))
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
				bot.sendMessage(target, f"Hello user {user} To the group {name} Welcome😍", message_id=msg["message_id"])
				
			else:
				if "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("message_id")])
						guid = msg.get("author_object_guid")
						user = bot.getUserInfo(guid)["data"]["user"]["username"]
						bot.deleteMessages(target, [msg.get("message_id")])
						alert(guid,user,True)
						
						continue

			answered.append(msg.get("message_id"))
			print("(" + msg.get("message_id")+ ") user >>> " + msg.get("text") + "\n ----------------------------")
			print(f"start panel: { target }")
			print("Source name: diegogram")
			print("Version 1 source")

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue

#دیگو گرام