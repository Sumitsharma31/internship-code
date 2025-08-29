# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Dataset
data = pd.read_csv("Crop_recommendation.csv")  # download from Kaggle

# 2. Check data
print("First 5 rows:\n", data.head())
print("\nDataset Info:\n")
print(data.info())
print("\nClass labels (crops):\n", data['label'].unique())

# 3. Basic Analysis
plt.figure(figsize=(8,5))
sns.countplot(x="label", data=data)
plt.xticks(rotation=90)
plt.title("Crop Distribution in Dataset")
plt.show()

# 4. Prepare Data
X = data.drop("label", axis=1)   # features (N, P, K, temp, humidity, ph, rainfall)
y = data["label"]                # target (crop type)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Predictions
y_pred = model.predict(X_test)

# 7. Accuracy
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 8. Test with Custom Input
sample = [[90, 40, 40, 20, 80, 6.5, 200]]  # [N,P,K,temp,humidity,pH,rainfall]
prediction = model.predict(sample)
print("\nRecommended Crop:", prediction[0])
