## CMPE255 Group Project | Team Name - Precisely Classified

# Bank Marketing Data Set 
The selected dataset is from the UCI Machine Learning Repository. The [Dataset](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing#) is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed. 

#### -- Project Status: [Active]
<!-- *Instructions: Click on the raw button in the upper right hand corner of this box.  Copy and paste the template into the README.md document on your github.  Fill in the titles, information and links where prompted! Feel free to stray a bit to suit your project but try to stick to the format as closely as possible for consistency across DSWG projects.* -->

## Objective
This project will enable the bank to develop a more granular understanding of its customer base, predict customers' response to its telemarketing campaign and establish a target customer profile for future marketing plans.

By analyzing customer features, such as demographics and transaction history, the bank will be able to predict customer saving behaviours and identify which type of customers is more likely to make term deposits. The bank can then focus its marketing efforts on those customers. This will not only allow the bank to secure deposits more effectively but also increase customer satisfaction by reducing undesirable advertisements for certain customers.

### Methods Used
* Machine Learning
* Data Cleaning
* Data Visualization

### Technologies Used 
* Kaggle Notebooks
* Python
* Pandas
* Seaborn
* matplotlib
* flask
* Jupyter Notebook

# Challenges - 
* **Class Imbalance - ** According to the initial data exploration we have found that there is a huge class imbalance in the target label. This is generally because data mining models usually tend to be i nfluenced with the majority class. The class imbalance could consequently lead to  the minority being misclassified and a bad model prediction accuracy.Solving this problem is a major challenge especially in customer related data such churn prediction where the class of interest is the minority and customer response in direct marketing for a product or a service.

<!-- ## Project Description
(Provide more detailed overview of the project.  Talk a bit about your data sources and what questions and hypothesis you are exploring. What specific data analysis/visualization and modelling work are you using to solve the problem? What blockers and challenges are you facing?  Feel free to number or bullet point things here) -->

## Data Description 

Feature | Description
|---------|------------------|
| age | (numeric)|
| job | type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')|
| marital | marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed) |
| education | (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown') |
| default | has credit in default? (categorical: 'no','yes','unknown')  |
|housing | has housing loan? (categorical: 'no','yes','unknown') |
| loan | has personal loan? (categorical: 'no','yes','unknown') |
| contact | contact communication type (categorical: 'cellular','telephone') |
| month | last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec') |
| day_of_week | last contact day of the week (categorical: 'mon','tue','wed','thu','fri') |
| duration | last contact duration, in seconds (numeric)|
| campaign | number of contacts performed during this campaign and for this client (numeric, includes last contact)|
| pdays | number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)|
| previous | number of contacts performed before this campaign and for this client (numeric) |
| poutcome |outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')|

Label | Description
|---------|------------------|
| Target | has the client subscribed a term deposit? (binary: 'yes','no') |
#### Work Schedule:

|Week     |  Tasks Completed | 
|---------|------------------|
|April 11 -  April 18|  Selection of Dataset |
|April 19 - 26 April|  Data Cleaning & Data Exploration  |


## Featured Notebooks/Analysis/Deliverables
* [Data Exploration](https://www.kaggle.com/code/prank939/cmpe255-finalproject-dataexploration)
<!-- * [Notebook/Markdown/Slide DeckTitle](link)
* [Blog Post](link) -->

## Domain Research Reference Papers 

1. [An insight into the effects of class imbalance and sampling on classification accuracy in credit risk assessment](https://www.researchgate.net/publication/329106374_An_insight_into_the_effects_of_class_imbalance_and_sampling_on_classification_accuracy_in_credit_risk_assessment)
2. [Machine Learning Modelsfor Bank Telemarketing Classification and Prediction](http://www.ijaema.com/gallery/119-december-3025.pdf)
3. [Handling Class Imbalance In Direct Marketing Dataset Using A Hybrid Data and Algorithmic Level Solutions](https://research.gold.ac.uk/id/eprint/17248/1/2016_SAI_Computing_IEEE_Class_imbalance.pdf)
## Contributing Team Members
  1. Anupriya
  2. Chetan
  3. Pranika
  4. Rishabh


<!-- |[Full Name](https://github.com/[github handle]) |     @janeDoe    | -->
