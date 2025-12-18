  Network Intrusion Detection Prototype (Python + Scapy + Machine Learning)

This repository contains a proof-of-concept intrusion detection script that combines:

- Basic Machine Learning classification (Logistic Regression)

- Packet interception using Scapy

- A simplified feature extractor for live network packets

The project demonstrates how real-time traffic can be captured and passed to a trained model for classification.

  Dataset Source  

The dataset used as reference for this prototype is CICIDS2017, a well-known public intrusion detection dataset available on the internet through various research archives and repositories.
The dataset was not created by me, it was downloaded from public sources exclusively for educational purposes.

  Important Notice

Due to the extremely large size of the CICIDS2017 dataset, my personal computer was not capable of fully loading, processing, or training a complete machine learning model with all available features.
Therefore, the script included in this repository is meant as a demonstration prototype, showing the intended workflow:

- Load dataset (conceptually)

- Encode labels

- Train a lightweight model

- Build a Scapy packet interceptor

- Extract simplified features

- Send packet features to the model for classification

  Features of the Prototype
- Machine Learning Pipeline

  - Label encoding

  - Train/test split

  - Logistic Regression classifier

  - Accuracy printout

- Real-Time Packet Sniffing

  - Uses Scapy to intercept live packets from the network.

- Feature Extraction

  - Converts each packet into a simplified feature vector. 

- Packet Classification

  - Each intercepted packet is sent to the ML model, which predicts a label (e.g., Benign, DoS, PortScan, etc.).
Installation

----------------------------------------------------------------------------------

  Install required dependencies:

  - pip install scapy
  - pip install pandas
  - pip install scikit-learn

(Scapy may require administrator or root permissions depending on the operating system).

  Usage

- Run the script:

  - python script.py

----------------------------------------------------------------------------------


Disclaimer

This project is intended strictly for educational and research purposes.
Do not use it for unauthorized network monitoring.
Always ensure you have permission before capturing or inspecting traffic.


