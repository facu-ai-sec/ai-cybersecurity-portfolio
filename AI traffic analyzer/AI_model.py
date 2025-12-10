import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from scapy.all import sniff, IP, TCP, UDP, Raw

# -----------------------------
# 1) Load dataset
# -----------------------------
datos = pd.read_csv('CICIDS2017_unificado.csv')

# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(datos[' Label'])

# Drop label column
datos = datos.drop([' Label'], axis=1)

# Define X and y
X = datos

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
modelo = LogisticRegression(max_iter=2000)
modelo.fit(X_train, y_train)

print("Training accuracy:", modelo.score(X_train, y_train))
print("Testing accuracy:", modelo.score(X_test, y_test))

# -------------------------------------------------------
# 2) Real-time packet interception with Scapy
# -------------------------------------------------------

# Convert a Scapy packet to a feature vector
# (Simplified — must match CICIDS feature structure for real use)

def extract_features(pkt):
    features = {}

    # Basic IP features
    if IP in pkt:
        features['src_bytes'] = len(pkt[IP].src)
        features['dst_bytes'] = len(pkt[IP].dst)
        features['pkt_size'] = len(pkt)
    else:
        features['src_bytes'] = 0
        features['dst_bytes'] = 0
        features['pkt_size'] = len(pkt)

    # Protocol flags
    features['is_TCP'] = 1 if TCP in pkt else 0
    features['is_UDP'] = 1 if UDP in pkt else 0

    # Payload length
    if Raw in pkt:
        features['payload_len'] = len(pkt[Raw].load)
    else:
        features['payload_len'] = 0

    return features

# Predict class of captured packet

def classify_packet(pkt):
    feats = extract_features(pkt)
    df = pd.DataFrame([feats])

    # Ensure missing columns match training structure
    for col in X.columns:
        if col not in df:
            df[col] = 0

    df = df[X.columns]

    pred = modelo.predict(df)[0]
    label = encoder.inverse_transform([pred])[0]

    print(f"Packet captured → Predicted label: {label}")

# Start sniffing

def start_sniffing():
    print("Sniffing network packets... (Ctrl + C to stop)")
    sniff(prn=classify_packet, store=0)


start_sniffing()