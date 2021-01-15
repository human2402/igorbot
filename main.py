from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

updater = Updater(token='1568990754:AAG4KUMmHSD3DyAqk0lT5QkhjzZ0p-WSlfE')

dispather = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def starting (update, context):
    context.bot.send_message(chat_id=575078092, text='LOG active chat '+str(update.effective_chat))
    #context.bot.send_message(chat_id=458933757, text='кек я могу от сюда писать ыыыы')
    context.bot.send_message(chat_id=update.effective_chat.id, text = 'а здесь пока нет ног, но зато можно позвать /igoring')
def igoring (update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = 'кокой игор')
    context.bot.send_message(chat_id=update.effective_chat.id, text='1.загадочный 2.веселый')
    def choose_mood(update, context):
        if '1' in update.message.text or 'загад' in update.message.text:
            context.bot.send_message(chat_id=update.effective_chat.id, text='о какой')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://sun9-57.userapi.com/impf/c854028/v854028322/242a59/jGjmStpD4RU.jpg?size=745x1080&quality=96&proxy=1&sign=d939513c959218f931e559985340d61f&type=album')
        elif '2' in update.message.text or 'весе' in update.message.text:
            context.bot.send_message(chat_id=update.effective_chat.id, text='joy of life')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://sun9-56.userapi.com/impf/c639628/v639628320/584c5/aJVbF2N6q-Q.jpg?size=720x524&quality=96&proxy=1&sign=44b5d6c7c80ed532592c91110053e500&type=album')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='каво')
            context.bot.send_message(chat_id=update.effective_chat.id, text='1 или 2')

    choose_handler = MessageHandler(Filters.text, choose_mood)
    dispather.add_handler(choose_handler)


starting_handler = CommandHandler('start', starting)
igoring_handler = CommandHandler('igoring', igoring)

dispather.add_handler(igoring_handler)
dispather.add_handler(starting_handler)

updater.start_polling()