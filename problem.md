# Practical Data Science Assessment
#### Consider the following problem:

- We have a list of bank transactions characterized by the transaction description and the amount of money involved.
- We want to classify the transactions into different categories (e.g., groceries, salary, rent) based on the transaction description.
- We are given a list of transaction descriptions and their corresponding categories, which we can use as training data.

#### Example data point from this dataset:
|description|amount|balance|date|label|
|-----------|-----------|-----------|-----------|-----------|
|POS Purchase Col Cacchio Bryanston|-858.0|-16380.15|2023-06-05 00:00:00|Restaurants|

#### Limitations on the transaction dataset:

- The dataset is limited in size.
- Unique tokens of a transaction description that give off strong signals may be rare, and thus don't provide enough training
signals for meaningful learning to take place. For example, in the above sample data point, it is clear that `Col Cacchio` is
the defining feature that maps this entry to the label `Restaurants`.

### Problem
Given the above limitation in the dataset, we may want to perform preprocessing such that these rare unique
tokens are replaced with broader class tokens. An example would be: 

|description|amount|balance|date|label|
|-----------|-----------|-----------|-----------|-----------|
|POS Purchase [Restaurants] [Location] |-858.0|-16380.15|2023-06-05 00:00:00|Restaurants|

In this case, `Col Cacchio` was replaced with the class token `[Restaurants]` and `Bryanston` was replaced with `[Location]`.

### Task
Design a solution that preprocesses the transaction descriptions in the dataset to replace rare unique tokens with broader class tokens.

### Deliverables
- A brief write-up explaining your approach, the technology stack and libraries you plan to use.
- A code implementation, showcasing your approach and practical results (if possible). Please avoid using any paid for or proprietary libraries/APIs. Please provide a link to the repository or the code as a zip file.

### Evaluation
We will evaluate the solution based on the following criteria:

- Approach: How well does your approach solve the problem?
- Feasibility: How feasible is your approach? How generaliseable is it to new data?
- Clarity: How clearly is your approach communicated?

### Notes
- You can make any assumptions you like, but please state them explicitly in your write-up.
- If you choose to implement the solution, you can use any programming language you like.
- You can find the dataset in the `data/` directory.







