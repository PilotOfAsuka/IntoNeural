# config.py
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

msg_dir = "n_network/saves/messages.txt"

start_msg = ("Этот бот написан на Python. Разработчик @PilotAski\n"
            "Его целью является сбор только текстовой информации для обучения.\n"
            "Это эксперимент разработчика, чтобы научиться создавать нейронные сети.\n"
            "\n"
            "Пожалуйста, обратите внимание, что бот собирает только текстовую информацию и не сохраняет никакие другие данные, такие как изображения, аудио или видео.\n"
            "\n"
            "Если у вас есть какие-либо вопросы или сомнения относительно сбора и использования данных, пожалуйста, не стесняйтесь задать их.")