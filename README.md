💻 Laptop Price Predictor

An AI-powered Laptop Price Prediction web app built with Machine Learning and Streamlit.
This project predicts the approximate price of a laptop based on its specifications like Brand, Type, RAM, Weight, Screen, Processor, GPU, and Storage.

🔮 The model gives predictions that are very close to actual market prices (verified using Amazon listings).

✨ Features

🧹 Data Cleaning & Preprocessing

📊 Exploratory Data Analysis (EDA) for insights

🤖 Tried multiple ML Algorithms:

Linear Regression

Decision Tree

Random Forest 🌲

Ridge Regression

Lasso

Boosting Algorithms

✅ Best Model: Random Forest Regressor with R² Score = 0.86

🌐 Interactive Web App using Streamlit

💰 Real-world validation: Predictions match closely with Amazon prices

🛠 Tech Stack

Python 🐍

Scikit-learn, Pandas, Numpy (Machine Learning)

Streamlit (Frontend for prediction)

Matplotlib & Seaborn (EDA & Visualization)

📂 Project Structure
Laptop-Price-Predictor/
│── data/                 # Dataset used
│── notebooks/            # EDA and ML experiments
│── app.py                # Streamlit web app
│── model.pkl             # Trained ML model
│── requirements.txt      # Dependencies
│── README.md             # Project Documentation
│── screenshots/          # Screenshots of the app

📈 Algorithm & Model

After testing multiple ML algorithms, Random Forest Regressor was chosen as the final model.

Achieved R² Score: 0.8595 🎯

The model generalizes well and performs better compared to linear models.

🖥 How to Run Locally

Clone the repository:

git clone https://github.com/your-username/Laptop-Price-Predictor.git
cd Laptop-Price-Predictor


Install dependencies:

pip install -r requirements.txt


Run Streamlit app:

streamlit run app.py


Open in browser 🌍

http://localhost:8501/

📸 Screenshots

👉 Keep your screenshots inside a folder named screenshots/ in your repo, and name them like below:

🔹 Web App UI (Prediction Form)

🔹 Predicted Price Output

🔹 Actual Amazon Laptop Price

✔️ Example:

Predicted Price: ₹67,785

Amazon Price: ₹67,990
➡️ Model is giving approx. correct results 🎯

🔮 Future Improvements

Deploy on Streamlit Cloud / AWS / Heroku for public access

Add Deep Learning model for better predictions

Improve UI with more interactive visualizations

👩‍💻 Author

Sumit Raj ✨
📌 Final Year | Computer Science & Engineering
