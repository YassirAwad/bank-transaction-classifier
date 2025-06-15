# Bank Transaction Classifier

This project focuses on improving the classification of bank transactions by preprocessing the transaction descriptions.

In many bank datasets, transaction descriptions often include specific merchant names, locations, or formatting that make generalization difficult. For example, “POS Purchase Col Cacchio Bryanston” is clearly a restaurant transaction, but most models won’t recognize this unless they've seen “Col Cacchio” before — which is unlikely in small datasets.

### 🔍 Problem

These rare and unique tokens reduce the model’s ability to learn useful patterns because they only appear once or twice. The solution is to replace those specific terms with more general class tokens (e.g., `[Restaurant]`, `[Location]`) that preserve the meaning but improve the consistency of the data.

### 🎯 Goal

Build a preprocessing pipeline that replaces rare or domain-specific tokens in transaction descriptions with broader, semantically meaningful class tokens. This makes the data more uniform and easier to classify or analyze.

### 💼 What This Project Includes

- A semantic preprocessing pipeline for replacing specific merchant/location tokens with general class tokens
- A clean and modular Python implementation of the logic
- Power BI dashboards for exploring:
  - Token frequency before and after replacement
  - Distribution of transaction categories
  - Description patterns by label
- A lightweight classifier built using the cleaned descriptions to test learnability
- Minimal unit tests to validate core preprocessing logic
- GitHub Actions for basic CI (runs linting and tests)

