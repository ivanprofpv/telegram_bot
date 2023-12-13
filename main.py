import telebot
import webbrowser

from telebot import types

API_TOKEN = '6981038879:AAH5uTxZvvWxtAFlyrtE2Yg_CxDc_aSRZjg'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://profpv.ru')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    button = types.InlineKeyboardMarkup()
    button.add(types.InlineKeyboardButton('Открыть сайт', url='https://profpv.ru'))
    button2 = types.ReplyKeyboardMarkup()
    button2.add(types.KeyboardButton('Открыть сайт'))
    button2.add(types.KeyboardButton('Показать мои данные'))
    bot.reply_to(message,
                 f'Привет, {message.from_user.first_name}! Что хочешь узнать? Выбери кнопку ниже:', reply_markup=button2)
    bot.register_next_step_handler(message, on_click)

def my_data(message):
    bot.reply_to(message,
                 f'Твой ID: {message.from_user.id}, а логин: {message.from_user.username}')
def on_click(message):
    return start_empty(message)

@bot.message_handler(commands=['help'])
def help_me(message):
    bot.reply_to(message, 'По всем вопросам пишите сюда: <u>@PROBotFPVbot</u>', parse_mode='html')

@bot.message_handler(content_types='photo')


@bot.message_handler()
def start_empty(message):
    if message.text == 'Открыть сайт':
        return site(message)
    elif message.text == 'Показать мои данные':
        return my_data(message)
    else:
        bot.reply_to(message,
                     f'Для выбора команд, нажмите сюда: /start и выберите необходимую кнопку.')

bot.infinity_polling()