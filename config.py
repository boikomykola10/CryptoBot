import os


class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    HOME_TEXT_FILE = "static/home_text.txt"
    STUDY_TEXT_FILE = "static/study_text.txt"
    BUY_STUDY_TEXT_FILE = "static/buy_study_text.txt"
    CONSULTATION_TEXT_FILE = "static/consultation_text.txt"
    BUY_CONSULTATION_TEXT_FILE = "static/buy_consultation_text.txt"
    REVIEW_IMAGES_PATH = [
        "static/review_1.jpg", "static/review_2.jpg", "static/review_3.jpg"
    ]
