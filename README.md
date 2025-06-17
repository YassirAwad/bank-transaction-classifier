
# Semantic Tokenization & Classification of Bank Transactions

This project demonstrates how to improve transaction classification by preprocessing text-based descriptions using rule-based token replacement. Rare or noisy vendor/location tokens are replaced with general class tokens such as `[restaurant]`, `[location]`, and `[date]` to enhance model generalization.

---

## Project Overview

**Objective:**
Transform transaction descriptions into standardized formats using semantic tokens to reduce vocabulary noise and improve classification accuracy.

---

## Project Structure

```
bank-transaction-classifier/
├── data/                         # Data files
│   ├── transactions.csv          # Raw dataset
│   └── transactions_tokenized.csv  # Preprocessed dataset with tokenized descriptions
│
├── notebooks/                    # Development and analysis notebooks
│   ├── 01_eda.ipynb              # Initial data exploration
│   ├── 02_token_replacement.ipynb # Token development and pattern testing
│   ├── 03_apply_tokenizer.ipynb # Applying preprocessing to full dataset
│   └── 04_model_comparison.ipynb # Model performance: raw vs tokenized
│
├── report/
│   └── writeup.md                # Findings, assumptions, and detailed explanation
│
├── src/                          # Core preprocessing code
│   ├── preprocess.py             # Token replacement logic
│   └── utils.py                  # (Optional) helper functions
│
├── tests/
│   └── test_preprocess.py        # Unit tests for preprocessing logic
│
├── README.md                     # Project overview and instructions
├── problem.md                    # Provided project prompt
├── requirements.txt              # Python dependencies
├── .gitignore
├── LICENSE
```

---

##  How It Works

###  Description Normalization

* Lowercased all text
* Removed or replaced inline date patterns like `* 14 Oct` → `[date]`

###  Token Replacement Strategy

| Token          | Replaces Examples             | Purpose                      |
| -------------- | ----------------------------- | ---------------------------- |
| `[grocers]`    | Woolworths, Checkers, PnP     | Reduces vendor name noise    |
| `[restaurant]` | KFC, Uber Eats, Marble Pantry | Generalizes fast food/dining |
| `[garage]`     | Engen, Sasol, Shell           | Unifies fuel vendors         |
| `[location]`   | Bryanston, Arcadia, Craighall | Removes branch/region noise  |
| `[date]`       | `* 12 Oct`, `* 15 Sep`        | Removes date-specific tokens |

###  Location & Type Inference

* Inserted `[location]` between `[restaurant]`/`[garage]` and `[date]`
* Inferred `[restaurant]` when missing for known `Eating Out` transactions

---

## 📊 Model Performance (Raw vs Tokenized)

| Metric            | Raw Description | Tokenized | Improvement |
| ----------------- | --------------- | --------- | ----------- |
| Accuracy          | 0.75            | 0.84      |  +0.09     |
| Macro F1-Score    | 0.52            | 0.60      |  +0.08     |
| Weighted F1-Score | 0.69            | 0.79      |  +0.10     |

Tokenization notably improved performance for:

* `Eating Out`: F1 ↑ from 0.69 → 1.00
* `Groceries`: F1 ↑ from 0.71 → 0.91
* `Fuel`: F1 ↑ from 0.00 → 1.00
* `General Purchases`: F1 ↑ from 0.40 → 0.67

---

##  Testing

Run unit tests for the preprocessing logic:

```bash
pytest tests/test_preprocess.py
```

Covers:

* Grocer name substitution
* Inferred `[restaurant]` token
* Location detection for Fuel/Eating Out

---

##  Running the Tokenizer

```python
from src.preprocess import replace_tokens

df['description'] = df.apply(lambda row: replace_tokens(row['description'], row['label']), axis=1)
df.to_csv("data/transactions_tokenized.csv", index=False)
```

---

##  Writeup

For a complete explanation of:

* Design decisions
* Assumptions
* Implementation breakdown
* Model insights

➡️ See `report/writeup.md`

---

## 👤 Author

Developed by **Yassir Ali**
As part of a Data Science test assessment.

> “Tokenizing noise into meaning.”

