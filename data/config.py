
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
BOT_TOKEN = config["settings"]["token"]
admin_for_logs = config["settings"]["admin_id"]
admins = config["settings"]["admin_id"]
api_id = config["settings"]["api_id"]
api_hash = config["settings"]["api_hash"]
if "," in admins:
    admins = admins.split(",")
else:
    if len(admins) >= 1:
        admins = [admins]
    else:
        admins = []
        print("***** Вы не указали админ ID *****")

bot_version = "1.4"
bot_description = f"<b>▫️Разработчик: @ZyzSoon</b>\n" \
                  f"<b>▫️Версия:</b> <code>{bot_version}</code>\n" \
                  f"<b>▫️Новости и обновления:</b> <a href='https://t.me/joinchat/Og6GW1rTmMYyZTEy'><b>перейти</b></a>\n"
