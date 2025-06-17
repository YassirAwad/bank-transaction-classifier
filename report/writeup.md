
---

# 📝 Project Write-Up: Transaction Description Tokenization & Classification

##  Problem Statement

In this project, I was tasked with preprocessing a dataset of bank transaction descriptions. Many of these descriptions contained rare or vendor-specific tokens (e.g., “Col Cacchio”, “Mitchell Park”) that made it difficult for machine learning models to generalize, especially with the dataset’s limited size.

To address this, I needed to design a rule-based preprocessing system that could replace these rare terms with broader semantic class tokens (like `[restaurant]`, `[location]`, `[date]`). The ultimate goal was to normalize the descriptions in a way that would enhance the performance of downstream classification models.

---

##  My Approach

I followed an iterative, example-driven strategy that combined exploratory data analysis with rule-based pattern design. My approach had three main phases:

### 1. **Normalization**

* I lowercased all `description` entries and removed any leading or trailing whitespace.
* I identified common patterns like embedded date stamps (e.g., `* 23 Sep`) and replaced them with the `[date]` token.

### 2. **Semantic Token Replacement**

I manually analyzed class-label relationships to identify patterns in vendor names. I then curated token lists for three key classes:

* `[restaurant]` — e.g., Uber Eats, KFC, Marble Pantry
* `[grocers]` — e.g., Woolworths, Pick n Pay, Checkers
* `[garage]` — e.g., Engen, Sasol, Shell

Using regex with whole-word boundaries, I replaced matching words in the descriptions with their corresponding semantic tokens.

### 3. **Contextual Inference**

For certain classes like `Eating Out` and `Fuel`, I noticed consistent placement of location names between vendors and date tokens. So I:

* Inferred `[restaurant]` if the label was `Eating Out` and no vendor match was found
* Inserted `[location]` between `[restaurant]`/`[garage]` and `[date]` to normalize the sequence structure

---

##  Evaluation

To test the value of my preprocessing, I trained a Logistic Regression classifier using both the raw and tokenized descriptions. The results clearly showed that the semantic abstraction improved classification performance.

| Metric            | Raw Description | Tokenized | Improvement |
| ----------------- | --------------- | --------- | ----------- |
| Accuracy          | 0.75            | 0.84      |  +0.09     |
| Macro F1-Score    | 0.52            | 0.60      |  +0.08     |
| Weighted F1-Score | 0.69            | 0.79      |  +0.10     |

In particular, I saw dramatic improvements in:

* **Eating Out** (F1 score increased from 0.69 to 1.00)
* **Fuel** (F1 score increased from 0.00 to 1.00)
* **Groceries** (F1 score increased from 0.71 to 0.91)
* **General Purchases** (F1 score increased from 0.40 to 0.67)

These results validated that my tokenization approach helped the model focus on meaning rather than rare string tokens.

---

## Technology Stack

I used the following tools and libraries:

| Purpose         | Tool / Library                                       |
| --------------- | ---------------------------------------------------- |
| Language        | Python 3.13                                          |
| Data Handling   | `pandas`                                             |
| Text Processing | `re` (Python regex)                                  |
| Modeling        | `scikit-learn` (LogisticRegression, CountVectorizer) |
| Testing         | `pytest`, `flake8`                                   |
| Development     | Jupyter Notebooks                                    |
| Version Control | Git and GitHub                                       |

---

## ✅ Deliverables

Here’s what I completed and included in the repository:

* ✅ Token replacement logic (`src/preprocess.py`)
* ✅ Tokenized dataset output (`data/transactions_tokenized.csv`)
* ✅ Evaluation notebook comparing raw vs tokenized (`04_model_comparison.ipynb`)
* ✅ Supporting development notebooks (`02_token_replacement.ipynb`, `03_apply_tokenizer.ipynb`)
* ✅ Unit tests for replacement logic (`tests/test_preprocess.py`)
* ✅ README for project usage
* ✅ This write-up

---

This project not only improved classification performance but also demonstrated how structured preprocessing of textual descriptions can add real value to machine learning pipelines.

