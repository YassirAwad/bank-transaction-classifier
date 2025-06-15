# Bank Transaction Classifier

This project tackles the challenge of improving the classification of bank transactions by preprocessing transaction descriptions.

Bank transactions often contain specific merchant or location names (e.g., "Col Cacchio Bryanston") that appear only once or a few times in a dataset. These rare tokens can prevent machine learning models from generalizing well.

### 🎯 Objective

The main goal is to **replace rare or unique tokens in transaction descriptions with broader class tokens** such as `[Restaurant]`, `[Retailer]`, or `[Location]`. This improves the consistency and quality of the input data for classification tasks or downstream analysis.

### 📦 Key Features

- Clean and analyze raw transaction descriptions
- Identify and replace rare tokens using semantic or pattern-based logic
- Generalize descriptions using class tokens (e.g., `[Restaurants]`)
- Train a simple classifier to predict transaction categories
- Create Power BI visualizations to explore token frequencies and category distributions
- Includes minimal testing and GitHub Actions CI for professional project hygiene

### 📁 Project Structure

bank-transaction-classifier/
│
├── data/ # Raw dataset (CSV)
├── notebooks/ # Jupyter notebooks for exploration and development
├── src/ # Preprocessing scripts
├── tests/ # Unit tests
├── .github/workflows/ # CI pipeline (lint + test)
├── reports/ # Final report/write-up
├── README.md
├── requirements.txt
└── .gitignore
