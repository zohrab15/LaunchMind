import numpy as np
from sklearn.linear_model import LinearRegression

# Məşq (training) üçün sadə data nümunələri
X = [
    [10000, 3, 4, 2, 1, 1],   # capital, experience, potential, competition, has_team, has_customers
    [20000, 5, 5, 1, 1, 1],
    [5000, 1, 2, 4, 0, 0],
    [15000, 2, 3, 3, 1, 0],
    [7000, 0, 1, 5, 0, 0],
]
y = [65, 90, 30, 55, 20]  # Uğur ehtimalı (faizlə)

# Modeli məşq etdir
model = LinearRegression()
model.fit(X, y)

# Yeni istifadəçi dəyərləri ilə proqnozlaşdır
def predict_success(capital, experience, potential, competition, has_team, has_customers):
    input_data = np.array([[capital, experience, potential, competition, has_team, has_customers]])
    prediction = model.predict(input_data)
    return round(prediction[0], 2)

# Test üçün:
if __name__ == "__main__":
    print(predict_success(12000, 3, 4, 2, 1, 1))  # Məsələn nəticə: 70.34
