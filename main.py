import telebot
import threading
import time

bot=telebot.TeleBot('6187704258:AAG9qSDOOqLT3cBtCyAmilvA-oVYnF8zCEo')
admin_ids = [1086606083,]
stop_threads = True

def spam_function():
    while True:
        global stop_threads
        if stop_threads:
            break
        bot.send_message(admin_ids[0], "Пришло сообщение!!!")
        time.sleep(2)
        
thread = threading.Thread(target=spam_function)

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id not in admin_ids:
        return
    bot.send_message(message.chat.id, "Привет, я буду оповещать хозяина о входящих уведомлениях")
    
@bot.message_handler(commands=['stop'])
def stop(message):
    if message.from_user.id not in admin_ids:
        return
    global stop_threads
    if stop_threads:
        return
    stop_threads = True
    thread.join()

@bot.message_handler(func=lambda message: True)
def message(message):
    if message.from_user.id in admin_ids:
        return
    global stop_threads
    if not stop_threads:
        return
    stop_threads = False
    thread.start()
    
def main():
    bot.polling(non_stop=True)

if __name__ == "__main__":
    main()
