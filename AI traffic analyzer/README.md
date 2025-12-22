# Network Intrusion Detection Prototype  
### Python · Scapy · Machine Learning

This repository contains a proof-of-concept intrusion detection prototype that combines basic machine learning techniques with real-time network packet interception using Scapy.

The project demonstrates how live network traffic can be captured, processed, and passed to a trained model for classification in a simplified but realistic workflow.

---

## Overview

This prototype integrates the following components:

- Machine Learning classification using **Logistic Regression**
- Live packet interception with **Scapy**
- Simplified feature extraction from network packets
- Real-time packet classification using a trained model

The goal is not to provide a production-ready IDS, but to illustrate the end-to-end logic behind network-based intrusion detection systems.

---

## Dataset Source

The dataset used as a reference for this prototype is **CICIDS2017**, a well-known public intrusion detection dataset available through academic and research repositories.

The dataset was **not created by me** and was obtained from public sources exclusively for **educational purposes**.

---

## Important Notice

Due to the extremely large size of the CICIDS2017 dataset, my personal computer was not capable of fully loading, processing, or training a complete machine learning model using all available features.

As a result, the script included in this repository is intended as a **demonstration prototype**, showing the intended workflow rather than a full-scale implementation.

Conceptual workflow:

- Load dataset (conceptual reference)
- Encode labels
- Train a lightweight machine learning model
- Intercept live packets using Scapy
- Extract simplified packet features
- Send packet features to the model for classification

---

## Features of the Prototype

### Machine Learning Pipeline
- Label encoding  
- Train/test split  
- Logistic Regression classifier  
- Accuracy evaluation  

### Real-Time Packet Sniffing
- Intercepts live network packets using Scapy  

### Feature Extraction
- Converts each packet into a simplified numerical feature vector  

### Packet Classification
- Each intercepted packet is classified by the ML model  
- Example labels include: *Benign, DoS, PortScan*, etc.

---

## Installation

Install the required dependencies:

```bash
pip install scapy
pip install pandas
pip install scikit-learn
