import telebot

from config import Config
from helpers import (
    study_link, get_text_from_file, file_button_correlation,
    button_keyboard_correlation
)
from keyboards import (
    home_keyboard, study_button_text, reviews_button_text, reviews_keyboard
)

BOT_TOKEN = Config.BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "hello", "restart"])
def send_welcome(message):
    """Greets the user and displays the home keyboard."""
    # Construct the greeting message with username
    username = message.from_user.username
    greeting_message = (
        f"Привіт, {username}, дякую що слідкуєш за моїм контентом 🤝"
    )

    bot.send_message(
        message.chat.id,
        greeting_message,
        reply_markup=home_keyboard,
        parse_mode="html"
    )


@bot.message_handler(
    func=lambda message: message.text in file_button_correlation.keys()
)
def handle_main_buttons(message):
    """Handles the study button click."""
    message_file_path = file_button_correlation[message.text]
    text_from_file = get_text_from_file(message_file_path)

    if message.text == study_button_text:
        text_from_file = f"{text_from_file}\n\n{study_link}"

    bot.send_message(
        message.chat.id,
        text_from_file,
        reply_markup=button_keyboard_correlation[message.text],
        parse_mode="html"
    )


@bot.message_handler(func=lambda message: message.text == reviews_button_text)
def handle_reviews_button(message):
    """Handles the reviews button click."""

    bot.send_message(
        message.chat.id,
        "Ось декілька відгуків",
        reply_markup=reviews_keyboard
    )

    # Create a list of media objects
    media = []

    for path in Config.REVIEW_IMAGES_PATH:
        with open(path, "rb") as image_file:
            media.append(telebot.types.InputMediaPhoto(image_file.read()))

    bot.send_media_group(message.chat.id, media)


bot.infinity_polling()
