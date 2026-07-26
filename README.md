# 🏠 House Price Prediction using Linear Regression

## 📌 Project Overview

This project focuses on predicting house prices using a **Linear Regression Machine Learning model**. The model uses various housing features such as average area income, house age, number of rooms, number of bedrooms, and area population to estimate the selling price of a house.

The project covers the complete Machine Learning workflow including data preprocessing, Exploratory Data Analysis (EDA), feature engineering, model training, evaluation, and deployment using Streamlit.

---

## 🌐 Live Demo

Try the deployed application here:

**https://house-price-prediction-aiml-project.streamlit.app/**

# 🎯 Problem Statement

To build a machine learning model that can predict house prices based on different housing characteristics.

---

# 💼 Business Objective

The objective of this project is to develop a predictive model that helps estimate property prices using historical housing data.

Such a model can assist:

- 🏡 Home buyers in estimating property values
- 🏢 Real estate businesses in price analysis
- 📊 Sellers in making informed pricing decisions

---

# 📂 Dataset Information

The dataset used in this project is **USA Housing Dataset**.

The dataset contains the following features:

| Feature | Description |
|---------|-------------|
| Avg. Area Income | Average income of the area |
| Avg. Area House Age | Average age of houses in the area |
| Avg. Area Number of Rooms | Average number of rooms |
| Avg. Area Number of Bedrooms | Average number of bedrooms |
| Area Population | Population of the area |
| Address | House address |
| Price | Target variable |

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Streamlit
- Joblib

---

# 📋 Project Workflow

The project follows these steps:

1. Loaded the dataset using Pandas.
2. Performed data inspection and understanding.
3. Checked missing values and duplicate records.
4. Removed unnecessary columns.
5. Renamed columns for better readability.
6. Performed Exploratory Data Analysis (EDA).
7. Created new features using feature engineering.
8. Split data into training and testing sets.
9. Trained a Linear Regression model.
10. Evaluated model performance using multiple metrics.
11. Built a Streamlit web application for prediction.

---

# 🧹 Data Cleaning

The following preprocessing steps were performed:

- Removed the **Address** column because it is a text-based feature and not suitable for Linear Regression.
- Checked for missing values.
- Verified duplicate records.
- Checked numerical features for invalid values.
- Renamed columns for easier handling.

---

# 📊 Exploratory Data Analysis (EDA)

The following visualizations were created:

- Price Distribution Plot
- Feature Histograms
- Correlation Heatmap
- Feature vs Price Scatter Plots
- Residual Distribution Plot
- Predicted vs Actual Price Plot

## Key Findings

- House prices follow an approximately normal distribution.
- Average Area Income has the strongest positive relationship with house prices.
- Number of Rooms also shows a strong relationship with price.
- Number of Bedrooms showed a weaker relationship compared to other features.
- No significant outliers were observed.

---

# ⚙️ Feature Engineering

## 1. Rooms per Bedroom Ratio

A new feature was created:
rooms_per_bedroom = Number of Rooms / Number of Bedrooms

This represents the average number of rooms available per bedroom.

---

## 2. Population Category

Area Population was divided into three categories using `pd.qcut()`:

- Low Population
- Medium Population
- High Population

This was used to analyze model performance across different population groups.

---

# 🤖 Model Building

### Algorithm Used:

**Linear Regression**

### Training Configuration:

- Train-Test Split: 80% Training / 20% Testing
- Random State: 42

The model was trained on the training dataset and used to predict house prices on unseen test data.

---

# 📈 Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score


## Model Performance

| Metric | Value |
|--------|-------:|
| MAE | 80,881.07 |
| MSE | 10,089,898,690.08 |
| RMSE | 100,448.49 |
| R² Score | 0.9180 |


The model achieved an **R² score of 0.918**, meaning it explains approximately **91.8% of the variation in house prices**.

---

# 📊 Population Category Performance Analysis

Mean Absolute Error was calculated for different population groups.

| Population Category | Mean Absolute Error |
|--------------------|--------------------:|
| Low | 80,626.65 |
| Medium | 80,982.43 |
| High | 81,022.41 |

### Observation:

The error values are very similar across all categories, showing that the model performs consistently and does not show significant bias toward any population group.

---

# 🌐 Streamlit Web Application

A user-friendly web application was developed using Streamlit.

The application allows users to enter:

- Average Area Income
- House Age
- Number of Rooms
- Number of Bedrooms
- Area Population

and predicts the estimated house price using the trained Linear Regression model.

## Run Application

Install dependencies:
pip install -r requirements.txt


Run Streamlit app:


streamlit run app.py


---

# 📁 Project Structure

HOUSE-PRICE-PREDICTION/

│
├── Dataset/
│ └── USA_Housing.csv
│
├── Model/
│ └── house_price_model.pkl
│
├── Notebook/
│ └── House_Price_Prediction.ipynb
│
├── Images/
│ ├── Actual_Vs_Predicted.png
│ ├── Heatmap.png
│ ├── Scatter_plots.png
│ ├── Box_plot.png
│ ├── Column_price_hist.png
│ └── Error_by_population_category.png
  |__ Distribution_of_house_price_hist.png
│
├── app.py
│
├── requirements.txt
│
└── README.md


---

# 🚀 Future Improvements

Possible improvements:

- Try advanced regression algorithms:
  - Random Forest Regressor
  - XGBoost
  - Gradient Boosting

- Perform hyperparameter tuning.
- Apply feature selection techniques.
- Add more real estate related features.
- Improve the Streamlit interface.

---

# ✅ Conclusion

A Linear Regression model was successfully developed to predict house prices using housing-related features.

The model achieved an **R² score of 0.918**, demonstrating strong predictive performance.

Feature engineering was performed by creating a rooms-per-bedroom ratio and population categories. The analysis showed that the model provides consistent predictions across different population levels.

The trained model was deployed using Streamlit, making it accessible through a simple web application.

---

# 👩‍💻 Author

**Nivedita Rani**

B.Tech CSE | ITS Engineering College

GitHub: Add your GitHub profile link here
