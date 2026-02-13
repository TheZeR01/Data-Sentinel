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

### Motion Anomaly Detection using Deep Learning (LSTM)

## 📑 Premise

Data-Sentinel is a data collection system and/or protocol that aims to be a proposal for a future **open-source behavioral biometrics-based cybersecurity** project. The project would use the **Minecraft environment** (With the Spigot API) to collect vector data of human movement (6DOF: X, Y, Z, Pitch, Yaw, Time) for analysis, cleaning, and further study. The goal is to train a **Recurrent Neural Network (LSTM)** capable of distinguishing between human movement patterns and automated scripts (bots) with high accuracy, proposing a non-intrusive alternative to traditional CAPTCHAs and anti-bots.

**Side note:** As I write this, I'm considering using **PacketEvents** or **ProtocolLib** for more direct access to Minecraft's network protocol (but I'm still learning... and I'm quite slow, so I'll take my time to learn what I need to **PROPERLY**). For now, I'm just prototyping the project. It's an ambitious long-term idea that, for the moment, focuses **ONLY** on using **Semantic Analysis** on data from the Spigot API to obtain consistent Behavioral Biometrics movement patterns. This will allow me to train the model on patterns that can be applied to other projects and systems. It's a proof of concept in my spare time that I hope to scale and compare with future data. The project's goal is to obtain clean data for an AI model focused on **computational efficiency** for obsolete systems. I'm evaluating options and open to suggestions.


## 📐 System Architecture

The project is divided into two main modules:

<img width="429" height="700" alt="Untitled diagram drawio (6) (2)" src="https://github.com/user-attachments/assets/40a3a87d-a1f1-472f-8e72-fa3c59a3d366" />

1. **Ingestion and Collection Module (Java/Spigot):**
   * Captures `PlayerMoveEvent` events in real time.
   * Calculates differentials (Deltas) of position and rotation.
   * Normalizes and exports behavior vectors to datasets in CSV format.

2. **Analysis Module (Python/TensorFlow):**
   * Preprocessing of time series.
   * LSTM (Long Short-Term Memory) architecture for sequential classification.
   * Anomaly detection based on reconstruction error (Autoencoder).

## 📊 Preliminary Results (Sample Dataset)

Successful extraction of motion vectors has been achieved, identifying clear patterns in human locomotion (noise on the Yaw/Pitch axis) versus artificial linearity, using the already documented and explored Spigot API as the basis for my research.

<img width="1200" height="1000" alt="Code_Generated_Image" src="https://github.com/user-attachments/assets/f70c7edf-db11-4b50-a7d0-f007c9052ec3" />

*(Fig. 1. Visualization of movement deltas. Note the organic variability in the pitch/yaw rotation axes characteristic of human mouse interaction, which current automation systems and bots using heuristics are not designed to replicate; this is the digital signature that needs to be studied.)*

## 🌱 Foundations and References

1. Study and training of a neural network using Minecraft as a testing environment, carried out by OpenAI:

   * **[https://openai.com/index/vpt/](https://openai.com/index/vpt/)**

2. Blog/Post by A Medium article explaining the current difficulties in detecting anomalous behaviors, discussing behavioral biometrics in detail:

   * **[https://ayanh.medium.com/utilizing-behavioral-biometrics-to-detect-bots-a-deep-dive-1bb2c52ae7f6](https://ayanh.medium.com/utilizing-behavioral-biometrics-to-detect-bots-a-deep-dive-1bb2c52ae7f6)**

3. A paper using Minecraft as a testing environment with similar methodologies, but under the Random Forest algorithm and a different approach:

   * **[2110.11080v1.pdf](https://github.com/user-attachments/files/24545430/2110.11080v1.pdf)**

## 🚀 Installation and Use

### ⚠️ Warning ⚠️

This currently contains **RAW** code in the initial conceptualization stages; its use on production servers is strongly discouraged.

**IF USED, IT MUST BE ON A CONTROLLED SERVER, PREFERABLY LOCALHOST.**

### Requirements

   * Java Development Kit (JDK) 17+
   * Python 3.9+
   * Spigot/Paper Server 1.20+ for data collection

### Model Execution (Python)

```bash
pip install -r requirements.txt
python train_model.py

```
