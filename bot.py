import telebot

from config import Config
from helpers import (
    study_link, get_text_from_file, file_button_correlation,
    button_keyboard_correlation, additional_text
)
from keyboards import (
    home_keyboard, reviews_button_text, study_button_text,
    consultation_button_text, reviews_keyboard
)

BOT_TOKEN = Config.BOT_TOKEN
bot = telebot.TeleBot(
    BOT_TOKEN, disable_web_page_preview=True, parse_mode="html"
)


@bot.message_handler(commands=["start", "hello", "restart"])
def send_welcome(message):
    """Greets the user and displays the home keyboard."""
    # Construct the greeting message with username
    file_to_read = Config.HOME_TEXT_FILE
    text_from_file = get_text_from_file(file_to_read)

    username = message.from_user.full_name
    reply_message = (
        f"<b>Привіт, {username},</b> {text_from_file}\n\n{study_link}\n\n"
        f"{additional_text}"
    )

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
    username = message.from_user.full_name
    common_text = f"<b>Привіт, {username},</b>"

    if message.text == study_button_text:
        text_from_file = (
            f"{common_text} {text_from_file}\n\n{study_link}\n\n"
            f"{additional_text}"
        )
    elif message.text == consultation_button_text:
        text_from_file = f"{common_text} {text_from_file}"

    bot.send_message(
        message.chat.id,
        text_from_file,
        reply_markup=button_keyboard_correlation[message.text],
        parse_mode="html"
    )


@bot.message_handler(func=lambda message: message.text == reviews_button_text)
def handle_reviews_button(message):
    """Handles the reviews button click."""

    def send_image_group(image_paths, number):
        bot.send_message(message.chat.id, number, timeout=3)

        media = []

        for path in image_paths:
            with open(path, "rb") as image_file:
                media.append(telebot.types.InputMediaPhoto(image_file.read()))

        bot.send_media_group(message.chat.id, media, timeout=3)

    # Send images for each person/category using the helper function
    send_image_group(Config.ANDREW_IMAGES, "1️⃣")
    send_image_group(Config.PASHA_IMAGES,  "2️⃣")
    send_image_group(Config.BOHDAN_IMAGES, "3️⃣")

    bot.send_message(
        message.chat.id,
        "Відгуки 👇"
    )

    for image_path in Config.REVIEW_IMAGES_PATH:
        # Open the image file in binary read mode
        with open(image_path, "rb") as image_file:
            # Send the photo using send_photo
            bot.send_photo(
                message.chat.id, image_file, reply_markup=reviews_keyboard
            )


if __name__ == "__main__":
    bot.infinity_polling()
