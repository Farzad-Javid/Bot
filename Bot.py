# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Bot:@I_Raisi_Bot
Created on May 2021

@authors: Javid and Farzad

A Simple robot to advertise a presidential candidate.

"""
import datetime as dt
import time
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters , CallbackQueryHandler
from telegram import Chat,Bot,InlineKeyboardButton, InlineKeyboardMarkup

class Chats:
    id = 0
    counter=0

mem = []
bot = Bot("Token")

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#Private Sector
def echo(update, context):
    chat = update.message.chat 
    if chat.type == "private":
        if update.message.text=="/start":
            update.message.reply_text('این ربات، جهت حمایت از آیت الله ابراهیم رئیسی در انتخابات سال ۱۴۰۰ ایجاد شده است\n\n با ارسال دستورات زیر می توانید اطلاعات بیشتری کسب نمایید.\n /history - تاریخچه ای از زندگی نامزد انتخاباتی \n /link - آدرس کانال تبلیغاتی \n /help - دستورات کمکی ربات ')
        elif update.message.text == "/history":
               update.message.reply_text('سید ابراهیم رئیس‌الساداتی (زادهٔ ۲۳ آذر ۱۳۳۹) سیاستمدار اصول‌گرا، روحانی مسلمان و نایب‌رئیس اول مجلس خبرگان رهبری و رئیس قوه قضائیه ایران است که در ۱۶ اسفند ۱۳۹۷ توسط سید علی خامنه‌ای، رهبر ایران، منصوب شده‌است.')
        elif update.message.text == "/link":
                update.message.reply_text('برای حمایت از آیت الله ابراهیم رئیسی در انتخابات به بزرگترین کمپین حمایتی ایشان ملحق شوید:\n\nhttps://t.me/raeessii1400')

        elif update.message.text == "/help":
                update.message.reply_text('/history - تاریخچه ای از زندگی نامزد انتخاباتی \n /link - آدرس کانال تبلیغاتی \n /help - دستورات کمکی ربات')
        else:
                update.message.reply_text('جز دستورات ربات نیست.')
#Public Sector
def send_link(update, context):
    chat = update.message.chat
    if chat.type == "group" or chat.type == "supergroup":
        index = -1
        for i in range(0,len(mem)):
            if chat.id == mem[i]:
                index = i
                break

        if index == -1:
            mem.append(chat.id)


def error(update, context):
    print(f'Update {update} caused error {context.error}')

# the main part of the code
def main():
    """Start the bot."""
    updater = Updater("Token", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.command, echo))
    dp.add_handler(MessageHandler(Filters.text, send_link, pass_chat_data=True))

    # log all errors
    dp.add_error_handler(error)
   
    updater.start_polling()
# Send a message to the group every 1800s
    msg = "برای حمایت از آیت الله ابراهیم رئیسی در انتخابات به بزرگترین کمپین حمایتی ایشان ملحق شوید:\n\nhttps://t.me/raeessii1400";
    while(dt.datetime.today().hour>=8 and dt.datetime.today().hour<=24 ):
        for i in range(0, len(mem)):
            bot.send_message(mem[i], text=msg)
        time.sleep(1800)

    updater.idle()


if __name__ == '__main__':
    main()
