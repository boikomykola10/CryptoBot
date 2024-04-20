import telebot

study_button_text = "Навчання 📚"
consultation_button_text = "Консультація 🧑‍💻"
reviews_button_text = "Відгуки 🤝"
buy_study_button_text = "Придбати навчання 💰"

home_keyboard = telebot.types.ReplyKeyboardMarkup(
   row_width=2, resize_keyboard=True
)
study_button = telebot.types.KeyboardButton(study_button_text)
buy_study_button = telebot.types.KeyboardButton(buy_study_button_text)
consultation_button = telebot.types.KeyboardButton(consultation_button_text)
reviews_button = telebot.types.KeyboardButton(reviews_button_text)
home_keyboard.add(buy_study_button)
home_keyboard.add(consultation_button, reviews_button)

study_keyboard = telebot.types.ReplyKeyboardMarkup(
    row_width=2, resize_keyboard=True
)

study_keyboard.add(study_button, consultation_button)
study_keyboard.add(reviews_button)

buy_consultation_button_text = "Придбати консультацію 💰"

consultation_keyboard = telebot.types.ReplyKeyboardMarkup(
    row_width=2, resize_keyboard=True
)
buy_consultation_button = telebot.types.KeyboardButton(
    buy_consultation_button_text
)
consultation_keyboard.add(buy_consultation_button)
consultation_keyboard.add(reviews_button, study_button)

reviews_keyboard = telebot.types.ReplyKeyboardMarkup(
    row_width=2, resize_keyboard=True
)
reviews_keyboard.add(study_button, consultation_button)
