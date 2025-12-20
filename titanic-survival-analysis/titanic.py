import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report


# ==============================
# 1. Load dataset
# ==============================

data = pd.read_csv("train.csv")


# ==============================
# 2. Basic preprocessing
# ==============================

# Drop columns with little predictive value (or too many missing values)
data = data.drop(columns=["Cabin", "Name", "Ticket"])

# Fill missing values
data["Age"] = data["Age"].fillna(data["Age"].mean())
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

# Convert categorical variables to dummy variables
data = pd.get_dummies(data, columns=["Sex", "Embarked"], drop_first=True)


# ==============================
# 3. Correlation analysis
# ==============================

plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=False, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


# ==============================
# 4. Feature selection
# ==============================

X = data.drop(columns=["Survived"])
y = data["Survived"]


# ==============================
# 5. Train / Test split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ==============================
# 6. Model training
# ==============================

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


# ==============================
# 7. Model evaluation
# ==============================

y_pred = model.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ==============================
# 8.  (optional) Interactive prediction
# ==============================

def predict_survival():
    print("\n--- Passenger Data Input ---")

    pclass = int(input("Pclass (1, 2 or 3): "))
    age = float(input("Age: "))
    sibsp = int(input("Siblings/Spouses aboard: "))
    parch = int(input("Parents/Children aboard: "))
    fare = float(input("Fare: "))
    sex = input("Sex (male/female): ").lower()
    embarked = input("Embarked (C, Q, S): ").upper()

    input_data = {
        "Pclass": pclass,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Sex_male": 1 if sex == "male" else 0,
        "Embarked_Q": 1 if embarked == "Q" else 0,
        "Embarked_S": 1 if embarked == "S" else 0,
    }

    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        print("\nPrediction: Survived")
    else:
        print("\nPrediction: Did not survive")

#Uncomment to enable custom prediction
#predict_survival()