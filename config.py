import os


class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    HOME_TEXT_FILE = "static/home_text.txt"
    BUY_STUDY_TEXT_FILE = "static/buy_study_text.txt"
    CONSULTATION_TEXT_FILE = "static/consultation_text.txt"
    BUY_CONSULTATION_TEXT_FILE = "static/buy_consultation_text.txt"
    ANDREW_IMAGES = [
        "static/andrew_1.jpg", "static/andrew_2.jpg", "static/andrew_3.jpg",
        "static/andrew_4.jpg", "static/andrew_5.jpg"
    ]
    PASHA_IMAGES = [
        "static/pasha_1.jpg", "static/pasha_2.jpg", "static/pasha_3.jpg",
        "static/pasha_4.jpg", "static/pasha_5.jpg"
    ]
    BOHDAN_IMAGES = [
        "static/bohdan_1.jpg", "static/bohdan_2.jpg", "static/bohdan_3.jpg",
        "static/bohdan_4.jpg", "static/bohdan_5.jpg"
    ]
    REVIEW_IMAGES_PATH = [
        "static/review_1.jpg", "static/review_2.jpg", "static/review_3.jpg"
    ]
