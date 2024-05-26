import telebot
from datetime import datetime
bot = telebot.TeleBot('6570152732:AAHDz6-Fcx4vxTkwKhYqQpR18yKtJyLpMhM')


@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, 'Привет,к какому врачу ты хочешь записаться?', parse_mode='html')


@bot.message_handler(commands=['terapevt'])

def terapevt(message):
    bot.send_message(message.chat.id, 'В нашей больнице терапевт, его зовут Лисицын Вадим Юрьевич.', parse_mode='html')


@bot.message_handler(commands=['lor'])

def lor(message):
    bot.send_message(message.chat.id, 'В нашей больнице только один лор, его зовут Чижов Сергей Юрьевич.', parse_mode='html')


@bot.message_handler(commands=['nevropatolog'])

def nevropotolog(message):
    bot.send_message(message.chat.id, 'В нашей больнице только один неврапотолог, его зовут Федотов Максим Леонидович.', parse_mode='html')


@bot.message_handler(commands=['datatime'])

def datatime(message):
    bot.send_message(message.chat.id,'Выберите время и дату на которое будет назначен приём. Доступное время: 9:15,10:45,13:56. Доступные даты 15.04.24,19.04.24, 25.04.24,28.04.24.Еще введите свое фио. ')

@bot.message_handler()

def datatime1(message):
    if message.text == "9:15,15.04.24":
        bot.send_message(message.chat.id,'вы выбрали время 9:15,вы выбрали дату 15.04.24')
    if message.text == "9:15,19.04.24":
        bot.send_message(message.chat.id, 'вы выбрали время 9:15,вы выбрали дату 19.04.24')
    if message.text == "9:15,25.04.24":
        bot.send_message(message.chat.id, 'вы выбрали время 9:15,вы выбрали дату 25.04.24')
    if message.text == "9:15,28.04.24":
        bot.send_message(message.chat.id,'вы выбрали время 9:15,вы выбрали дату 28.04.24')
    if message.text == "10:45,28.04.24":
        bot.send_message(message.chat.id, 'вы выбрали время 10:45,вы выбрали дату 28.04.24')
    if message.text == "10:45,15.04.24":
        bot.send_message(message.chat.id, 'вы выбрали время 10:45,вы выбрали дату 15.04.24')
    if message.text == "10:45,19.04.24":
        bot.send_message(message.chat.id, 'вы выбрали время 10:45,вы выбрали дату 19.04.24')
    if message.text == "10:45,25.04.24":
        bot.send_message(message.chat.id, 'вы выбрали время 10:45,вы выбрали дату 25.04.24')
    if message.text == "13:56,15.04.24":
        bot.send_message(message.chat.id, 'вы выбрали время 13:56,вы выбрали дату 15.04.24')
    if message.text == "13:56,25.04.24":
        bot.send_message(message.chat.id, 'вы выбрали время 10:45,вы выбрали дату 25.04.24')
    if message.text == "13:56,19.04.24":
        bot.send_message(message.chat.id, 'вы выбрали время 10:45,вы выбрали дату 19.04.24')
    if message.text == "13:56, 28.04.24":
        bot.send_message(message.chat.id, 'вы выбрали время 13:56,вы выбрали дату 28.04.24')
    if message.text == "Наумкин Владислав Сергеевич":
        bot.send_message(message.chat.id,'Ваше Фио : Наумкин Владислав Сергеевич. Вы успешно записаны на приём')

bot.polling(none_stop=True)
