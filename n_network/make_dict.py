import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import pickle

epoch = 60

def training_medel():
    try:
        # Загрузим данные для обучения
        with open("n_network/saves/messages.txt", 'r', encoding='utf-8') as file:
            data = file.read()

        # Создадим словарь уникальных символов
        chars = sorted(list(set(data)))
        char_indices = dict((c, i) for i, c in enumerate(chars))
        indices_char = dict((i, c) for i, c in enumerate(chars))

        # Сохраняем char_indices и chars в файл
        with open('n_network/char_indices.pkl', 'wb') as f:
            pickle.dump(char_indices, f)

        with open('n_network/chars.pkl', 'wb') as f:
            pickle.dump(chars, f)

        with open('n_network/indices_char.pkl', 'wb') as f:
            pickle.dump(chars, f)

        # Параметры модели
        maxlen = 40
        step = 3
        sentences = []
        next_chars = []

        # Создадим последовательности входных данных и целевых значений
        for i in range(0, len(data) - maxlen, step):
            sentences.append(data[i:i + maxlen])
            next_chars.append(data[i + maxlen])

        # Преобразуем данные в формат, пригодный для обучения
        x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.int32)
        y = np.zeros((len(sentences), len(chars)), dtype=np.int32)
        for i, sentence in enumerate(sentences):
            for t, char in enumerate(sentence):
                x[i, t, char_indices[char]] = 1
            y[i, char_indices[next_chars[i]]] = 1

        # Создадим модель
        model = Sequential([
            LSTM(128, input_shape=(maxlen, len(chars))),
            Dense(len(chars), activation='softmax')
        ])

        model.compile(loss='categorical_crossentropy', optimizer='adam')

        # Обучим модель
        model.fit(x, y, batch_size=128, epochs=epoch)
        # Сохраним модель
        model.save('n_network/saves/text_generation_model.keras')
        return "Model has saved use /generate to generate text from model"

    except ValueError:
        return "Messages data is empty, check n_network/saves/messages.txt"
