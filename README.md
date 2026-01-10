<div align="center">
  <h1>Data-Sentinel</h1>
  <h3>Behavioral Biometrics Acquisition & Analysis Protocol.</h3>
  <h3>
    
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
    
  </h3>

</div>

### Detección de Anomalías de Movimiento mediante Deep Learning (LSTM)


## 📑 Premisa

Data-Sentinel es un sistema y/o protocolo de recolección de datos que, a su vez, busca ser una propuesta para un futuro proyecto de **ciberseguridad basado en biometría conductual** Open Source. El proyecto utilizaría el entorno de *Minecraft* (vía API de Spigot) para la recolección de datos vectoriales de movimiento humano (6DOF: X, Y, Z, Pitch, Yaw, Time) para análisis, limpieza y estudio posterior. El objetivo es entrenar una **Red Neuronal Recurrente (LSTM)** capaz de distinguir entre patrones de movimiento humano y scripts automatizados (bots) con alta precisión, proponiendo una alternativa no intrusiva a los CAPTCHAs y Anti-Bot tradicionales.

**Nota al margen:** Al momento de escribir esto, evalúo usar **PacketEvents** o **ProtocolLib** para tener acceso más directo al protocolo de red de Minecraft (pero sigo aprendiendo... y soy bastante lento, me tomaré mi tiempo para aprender lo que deba **BIEN**). Por ahora solo estoy prototipando el proyecto en primera instancia, siendo una idea ambiciosa a largo plazo que se enfoca, por ahora, **SOLO** en usar **Análisis Semántico** para los datos provenientes de la API de Spigot y así obtener movimiento consistente de Biometría Conductual con el cual entrenar al modelo en patrones que se puedan aplicar a otros proyectos y sistemas. Es una prueba conceptual en mi tiempo libre que espero escalar y poder contrastar con datos futuros; la finalidad del proyecto es obtener datos limpios para un modelo de IA enfocado en la **eficiencia computacional** para sistemas obsoletos... Evalúo opciones y escucho sugerencias.

## 📐 Arquitectura del Sistema

El proyecto se divide en dos módulos principales:

<img width="429" height="700" alt="Diagrama sin título drawio (6) (2)" src="https://github.com/user-attachments/assets/40a3a87d-a1f1-472f-8e72-fa3c59a3d366" />


1. **Módulo de Ingesta y recolección (Java/Spigot):**
   * Captura eventos `PlayerMoveEvent` en tiempo real.
   * Calcula diferenciales (Deltas) de posición y rotación.
   * Normaliza y exporta vectores de comportamiento a datasets en formato CSV.

2. **Módulo de Análisis (Python/TensorFlow):**
   * Preprocesamiento de series temporales.
   * Arquitectura LSTM (Long Short-Term Memory) para clasificación secuencial.
   * Detección de anomalías basada en el error de reconstrucción (Autoencoder).
   

## 📊 Resultados Preliminares (Dataset de Muestra)

Se ha logrado la extracción exitosa de vectores de movimiento, identificando patrones claros en la locomoción humana (ruido en el eje Yaw/Pitch) vs. la linealidad artificial, utilizando como base para mi investigación la ya documentada y explorada API de Spigot.

<img width="1200" height="1000" alt="Code_Generated_Image" src="https://github.com/user-attachments/assets/f70c7edf-db11-4b50-a7d0-f007c9052ec3" />

*(Fig 1. Visualización de los Deltas de movimiento. Nótese la variabilidad orgánica en los ejes de rotación Pitch/Yaw característicos de la interacción con mouse humano que los sistemas de automatización y bots actuales que usan heurística no están diseñados para replicar; es la firma digital que se necesita estudiar).*

## 🌱 Bases y referencias

1. Estudio y entrenamiento de una red neuronal utilizando como entorno de pruebas **Minecraft** y llevado a cabo por **OpenAI**:
   * **[https://openai.com/index/vpt/](https://openai.com/index/vpt/)**


2. Blog/Post de **Medium** explicando las dificultades actuales para detectar **comportamientos anómalos** donde se habla a detalle sobre la **biometría conductual** o **biometría del comportamiento**:
   * **[https://ayanh.medium.com/utilizing-behavioral-biometrics-to-detect-bots-a-deep-dive-1bb2c52ae7f6](https://ayanh.medium.com/utilizing-behavioral-biometrics-to-detect-bots-a-deep-dive-1bb2c52ae7f6)**


3. Paper que utiliza **Minecraft** como entorno de pruebas usando metodologias similares a las aplicadas pero bajo el algoritmo **Random Forest** y un matiz diferente:
   * **[2110.11080v1.pdf](https://github.com/user-attachments/files/24545430/2110.11080v1.pdf)**



## 🚀 Instalación y Uso

### ⚠️ Advertencia ⚠️

Actualmente esto contiene código **CRUDO** en etapas de conceptualización inicial; para nada se recomienda su uso en servidores en producción.

**DE USARSE, DEBE SER EN UN SERVIDOR CONTROLADO, PREFERIBLEMENTE LOCALHOST.**

### Requisitos

   * Java Development Kit (JDK) 17+
   * Python 3.9+
   * Spigot/Paper Server 1.20+ para recolección de data

### Ejecución del Modelo (Python)

```bash
pip install -r requirements.txt
python train_model.py

```
