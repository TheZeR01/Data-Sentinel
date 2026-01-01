import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN ---
# Nombre de tu archivo CSV (Cámbialo si generas uno nuevo)
CSV_FILE = "dataset/tu_archivo_aqui.csv" 
SEQUENCE_LENGTH = 50  # La IA mirará los últimos 50 ticks (2.5 segundos) para decidir

print(">>> 1. Cargando el Dataset de Comportamiento Humano...")
# Cargar datos (Sin encabezados, asignamos nombres manualmente)
try:
    df = pd.read_csv(CSV_FILE, header=None)
    df.columns = ['Timestamp', 'DeltaX', 'DeltaY', 'DeltaZ', 'DeltaPitch', 'DeltaYaw']
except FileNotFoundError:
    print(f"ERROR: No encuentro el archivo {CSV_FILE}. Asegúrate de poner el nombre correcto.")
    exit()

# Solo nos interesan los datos de movimiento, no el Timestamp para el entrenamiento
data = df[['DeltaX', 'DeltaY', 'DeltaZ', 'DeltaPitch', 'DeltaYaw']].values

print(f">>> Datos cargados: {data.shape[0]} muestras de movimiento.")

# --- PREPROCESAMIENTO ---
print(">>> 2. Normalizando datos (Escala 0 a 1)...")
# Las redes neuronales funcionan mejor con números pequeños
scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data)

# Crear secuencias (X) y etiquetas (y)
# Como es un prototipo "Autoencoder" (Detección de Anomalías), intentamos predecir el siguiente movimiento
X = []
y = []

for i in range(SEQUENCE_LENGTH, len(data_scaled)):
    X.append(data_scaled[i-SEQUENCE_LENGTH:i]) # Los 50 pasos anteriores
    y.append(data_scaled[i])                 # El paso actual (lo que intentamos predecir)

X, y = np.array(X), np.array(y)
print(f">>> Secuencias generadas para LSTM: {X.shape}")

# --- ARQUITECTURA DEL MODELO (LA PARTE CIENTÍFICA) ---
print(">>> 3. Construyendo Red Neuronal LSTM...")

model = Sequential()

# Capa 1: LSTM (Memoria a Corto Plazo)
model.add(LSTM(units=64, return_sequences=True, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))

# Capa 2: LSTM
model.add(LSTM(units=32, return_sequences=False))
model.add(Dropout(0.2))

# Capa de Salida
model.add(Dense(units=5))

# Compilación: Optimizador Adam (el estándar de oro)
model.compile(optimizer='adam', loss='mean_squared_error')

model.summary()

# --- ENTRENAMIENTO (SIMULACIÓN) ---
print(">>> 4. Iniciando entrenamiento neuronal...")
history = model.fit(X, y, epochs=5, batch_size=32, validation_split=0.1)

print(">>> ¡MODELO ENTRENADO!")
print(">>> Guardando modelo en 'sentinel_model.h5'...")
model.save("sentinel_model.h5")

# --- VISUALIZACIÓN DEL ERROR (Pérdida) ---
plt.plot(history.history['loss'], label='Error de Entrenamiento')
plt.plot(history.history['val_loss'], label='Error de Validación')
plt.title('Convergencia del Modelo LSTM')
plt.xlabel('Épocas')
plt.ylabel('Error (Loss)')
plt.legend()
plt.show()