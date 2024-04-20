from config import Config
from keyboards import study_button_text, buy_study_button_text, \
    consultation_button_text, buy_consultation_button_text, study_keyboard, \
    home_keyboard, consultation_keyboard

link_text = "📋Повна структура навчання"
link_url = "https://teletype.in/@taras_tseya/xpOIWvtkCZ0"
study_link = f"<a href=\"{link_url}\">{link_text}</a>"


def get_text_from_file(file_path: str) -> str:
    """Reads the text from the file and returns it."""
    with open(file_path, "r", encoding="utf-8") as message_file:
        message_text = message_file.read().strip()

    return message_text


file_button_correlation = {
    study_button_text: Config.STUDY_TEXT_FILE,
    buy_study_button_text: Config.BUY_STUDY_TEXT_FILE,
    consultation_button_text: Config.CONSULTATION_TEXT_FILE,
    buy_consultation_button_text: Config.BUY_CONSULTATION_TEXT_FILE
}

button_keyboard_correlation = {
    study_button_text: home_keyboard,
    buy_study_button_text: study_keyboard,
    consultation_button_text: consultation_keyboard,
    buy_consultation_button_text: study_keyboard
}
