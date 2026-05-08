import telebot
from telebot import types

TOKEN = "8776485449:AAEzbSfMxD9TsUnFWQzoiwMNg3uz48cK9yA"
bot = telebot.TeleBot(TOKEN)

# ==================== ЗДЕСЬ ВСТАВЛЯЙ СВОИ ССЫЛКИ ====================
links = {
    "квартиры": "https://ostrovok.tpm.lv/6B497trq",           # ← замени
    "отели": "https://yandex.tpm.lv/dfMdXHpN",
    "машины": "https://economybookings.tpm.lv/lvBDSAQc",
    "яхты": "https://searadar.tpm.lv/sjVhIFv3",           # ← уже твоя ссылка
    "круизы": "https://lavoyage.tpm.lv/UgAnQ6k2",
    "мото": "https://bikesbooking.tpm.lv/q5B9iUJM",
    "сим": "https://airalo.tpm.lv/O38Y7r4a"
}
# =================================================================

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("🏠 Квартиры", "🏨 Отели")
    markup.add("🚗 Машины", "⛴ Яхты")
    markup.add("🛳 Круизы", "🏍 Мото")
    markup.add("📱 Сим-карты")
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Выберите категорию:", reply_markup=main_menu())

@bot.message_handler(func=lambda m: True)
def handle_buttons(message):
    text = message.text
    cat_map = {
        "🏠 Квартиры": "квартиры",
        "🏨 Отели": "отели",
        "🚗 Машины": "машины",
        "⛴ Яхты": "яхты",
        "🛳 Круизы": "круизы",
        "🏍 Мото": "мото",
        "📱 Сим-карты": "сим"
    }

    if text in cat_map:
        key = cat_map[text]
        if links.get(key):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("👉 Перейти на сайт", url=links[key]))
            bot.send_message(message.chat.id, f"✅ {text}", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, f"🔴 Для {text} пока нет ссылки")
    else:
        bot.send_message(message.chat.id, "Выберите категорию из меню 👇", reply_markup=main_menu())

print("🤖 Бот запущен!")
bot.infinity_polling()