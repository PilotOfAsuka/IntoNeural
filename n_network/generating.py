import numpy as np
from tensorflow.keras.models import load_model
import pickle


def generate_from():
    try:
        # Загружаем обученную модель
        model = load_model('n_network/saves/text_generation_model.keras')

        maxlen = 40

        # Путь к вашему файлу с данными
        with open("n_network/saves/messages.txt", 'r', encoding='utf-8') as file:
            data = file.read()

        # Загружаем словарь уникальных символов и индексы символов
        with open('n_network/char_indices.pkl', 'rb') as f:
            char_indices = pickle.load(f)

        with open('n_network/chars.pkl', 'rb') as f:
            chars = pickle.load(f)

        # Восстанавливаем обратный словарь для преобразования индексов в символы
        with open('n_network/indices_char.pkl', 'rb') as f:
            indices_char =pickle.load(f)
        # indices_char = dict((i, c) for c, i in char_indices.items())

        # Задаем начальную последовательность для генерации текста
        start_index = np.random.randint(0, len(data) - maxlen - 1)
        seed_text = data[start_index:start_index + maxlen]

        # Задаем длину генерируемого текста
        generated_text_length = 100

        # Генерируем текст
        generated_text = seed_text
        for i in range(generated_text_length):
            x_pred = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(seed_text):
                x_pred[0, t, char_indices[char]] = 1.

            # Получаем вероятности для следующего символа
            preds = model.predict(x_pred, verbose=0)[0]

            # Выбираем следующий символ на основе вероятностей
            next_index = np.random.choice(len(chars), p=preds)
            next_char = indices_char[next_index]

            # Добавляем следующий символ к сгенерированному тексту
            generated_text += next_char

            # Обновляем seed_text, удаляя первый символ и добавляя новый символ в конец
            seed_text = seed_text[1:] + next_char
        return generated_text
    except OSError as e:
        return str(e)


