# Data-Sentinel: Behavioral Biometrics Acquisition & Analysis Protocol
### Detección de Anomalías de Movimiento mediante Deep Learning (LSTM)

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

## 📑 Abstract
Data-Sentinel es un sistema de **ciberseguridad basado en biometría conductual**. El proyecto utiliza el entorno de sandbox de *Minecraft* (vía Spigot API) para la recolección de datos vectoriales de movimiento humano (6DOF: X, Y, Z, Pitch, Yaw, Time). El objetivo es entrenar una Red Neuronal Recurrente (LSTM) capaz de distinguir entre patrones de movimiento humano orgánico y scripts automatizados (bots) con alta precisión, proponiendo una alternativa no intrusiva a los CAPTCHAs tradicionales.

## 📐 Arquitectura del Sistema
El proyecto se divide en dos módulos principales:

1.  **Módulo de Ingesta (Java/Spigot):**
    * Captura eventos `PlayerMoveEvent` en tiempo real (PMV.
    * Calcula diferenciales (Deltas) de posición y rotación.
    * Normaliza y exporta vectores de comportamiento a datasets CSV.
2.  **Módulo de Análisis (Python/TensorFlow):**
    * Preprocesamiento de series temporales.
    * Arquitectura LSTM (Long Short-Term Memory) para clasificación secuencial.
    * Detección de anomalías basada en el error de reconstrucción (Autoencoder).

## 📊 Resultados Preliminares (Dataset de Muestra)
Se ha logrado la extracción exitosa de vectores de movimiento, identificando patrones claros en la locomoción humana (ruido en el eje Yaw/Pitch) vs. la linealidad artificial utilizando como base para mi investigacion la ya documentada y explorada API de Spigot.

<img width="1200" height="1000" alt="Code_Generated_Image" src="https://github.com/user-attachments/assets/f70c7edf-db11-4b50-a7d0-f007c9052ec3" />

*(Fig 1. Visualización de los Deltas de movimiento. Nótese la variabilidad orgánica en los ejes de rotación Pitch/Yaw característicos de la interacción con mouse humano).*

## 🚀 Instalación y Uso

### Requisitos
* Java Development Kit (JDK) 17+
* Python 3.9+
* Spigot/Paper Server 1.20+ para recoleccion de data

### Ejecución del Modelo (Python)
```bash
pip install -r requirements.txt
python train_model.py
