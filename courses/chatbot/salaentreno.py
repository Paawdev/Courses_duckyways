import numpy as np
import json
import nltk
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ReduceLROnPlateau
from nltk.stem import WordNetLemmatizer
import pickle

# Cargar datos y recursos de NLTK
nltk.download('punkt')
nltk.download('wordnet')

# Cargar intents
with open('intents.json') as file:
    intents = json.load(file)

lemmatizer = WordNetLemmatizer()

# Preprocesar datos
training_sentences = []
training_labels = []
classes = []
responses = {}

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern.lower())
        training_sentences.append(' '.join([lemmatizer.lemmatize(word) for word in word_list]))
        training_labels.append(intent['tag'])

    if intent['tag'] not in classes:
        classes.append(intent['tag'])

    responses[intent['tag']] = intent['responses']

# Tokenizar y normalizar
tokenizer = Tokenizer()
tokenizer.fit_on_texts(training_sentences)
X_train = tokenizer.texts_to_sequences(training_sentences)
max_len = max(len(seq) for seq in X_train)  # Máximo número de tokens
X_train = pad_sequences(X_train, padding='post', maxlen=max_len)
X_train = np.expand_dims(X_train, -1)

# Etiquetas
label_encoder = LabelEncoder()
y_train = label_encoder.fit_transform(training_labels)

# Guardar tokenizer y label encoder
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle)

with open('label_encoder.pickle', 'wb') as handle:
    pickle.dump(label_encoder, handle)

# Crear modelo
model = Sequential()
model.add(LSTM(256, input_shape=(X_train.shape[1], X_train.shape[2]), activation='relu', return_sequences=True))
model.add(LSTM(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))  # Dropout ajustado
model.add(Dense(len(classes), activation='softmax'))

# Compilar
optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Callback de aprendizaje
lr_scheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=10, min_lr=0.00001)

# Entrenamiento
model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=300,
    batch_size=16,
    callbacks=[lr_scheduler]
)

# Guardar modelo
model.save('chatbot_model.keras')

print("Entrenamiento completado y modelo guardado.")
