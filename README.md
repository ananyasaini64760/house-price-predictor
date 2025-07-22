# 🏡 House Price Prediction App

A web application built using Streamlit to predict the **selling price of a house** based on features like area, number of bathrooms, garage capacity, and overall quality. The model is trained on the [Kaggle House Prices Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques).

---

## 🚀 Live Demo
🧪 This app can be deployed locally or on [Streamlit Cloud](https://share.streamlit.io).

---

## 📌 Features

- 📊 Input fields for:
  - Overall Quality
  - Living Area (sq ft)
  - Garage Capacity
  - Basement Area (sq ft)
  - Number of Bathrooms
- 🤖 Trained with `LinearRegression`
- 📈 Real-time price prediction
- 💻 Deployable with one click using Streamlit

---

## 📁 Project Structure

```
house-price-predictor/
│
├── app.py               # Streamlit web app
├── train_model.py       # Script to train & export model.pkl
├── model.pkl            # Trained ML model (generated)
├── requirements.txt     # Required Python libraries
└── README.md            # Project overview and instructions
```

---

## 🧠 How It Works

The model uses the following features to predict house prices:

- `OverallQual` – Overall material and finish quality
- `GrLivArea` – Above-ground living area (sq ft)
- `GarageCars` – Capacity of garage (cars)
- `TotalBsmtSF` – Basement area (sq ft)
- `FullBath` – Number of full bathrooms

Trained using `LinearRegression` from scikit-learn.

---

## 📷 Screenshot

> Add a screenshot of your Streamlit app here:
> ```
> ![Screenshot](screenshot.png)
> ```

---


## 📜 License

MIT 

---

## 🤝 Acknowledgements

- [Kaggle: House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
- Streamlit.io for UI framework
