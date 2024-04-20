import telebot

from config import Config
from helpers import (
    study_link, get_text_from_file, file_button_correlation,
    button_keyboard_correlation
)
from keyboards import (
    home_keyboard, reviews_button_text, reviews_keyboard, study_button_text,
    consultation_button_text
)

BOT_TOKEN = Config.BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "hello", "restart"])
def send_welcome(message):
    """Greets the user and displays the home keyboard."""
    # Construct the greeting message with username
    file_to_read = Config.HOME_TEXT_FILE
    text_from_file = get_text_from_file(file_to_read)

    username = message.from_user.username
    reply_message = f"Привіт, {username}, {text_from_file}\n\n{study_link}"

    bot.send_message(
        message.chat.id,
        reply_message,
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
    username = message.from_user.username

    if message.text == study_button_text:
        text_from_file = f"Привіт, {username}, {text_from_file}\n\n{study_link}"
    elif message.text == consultation_button_text:
        text_from_file = f"Привіт, {username}, {text_from_file}"

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
        "ㅤ",
        reply_markup=reviews_keyboard
    )

    def send_image_group(image_paths):
        media = []
        for path in image_paths:
            with open(path, "rb") as image_file:
                media.append(telebot.types.InputMediaPhoto(image_file.read()))

        bot.send_media_group(message.chat.id, media)

    # Send images for each person/category using the helper function
    send_image_group(Config.ANDREW_IMAGES)
    send_image_group(Config.PASHA_IMAGES)
    send_image_group(Config.BOHDAN_IMAGES)
    send_image_group(Config.REVIEW_IMAGES_PATH)


if __name__ == "__main__":
    bot.infinity_polling()
