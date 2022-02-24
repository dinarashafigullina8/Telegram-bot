import telebot

bot = telebot.TeleBot('5234828077:AAHPtABuKfSuE_lRey1WT4cV-oHIYEngTlk')

import requests


def get_advice():
    res = requests.get('https://api.adviceslip.com/advice')
    srs = res.json()
    return srs['slip']['advice']


def translate(text):
    res = requests.get(f'https://fasttranslator.herokuapp.com/api/v1/text/to/text?source={text}&lang=en-ru').json()
    if(res['data']):
        return res['data']
    return 'перевод временно недоступен'



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    advice = get_advice()
    text= translate(advice)
    bot.send_message(message.from_user.id, "Готовлю твое предсказание")
    bot.send_message(message.from_user.id, f"{advice}\nПеревод: {text}")


bot.polling()
