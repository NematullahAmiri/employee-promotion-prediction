









Employee Promotion Prediction System
An Explainable Machine Learning Solution for Data-Driven Talent Management















By: Nematullah Amiri PMP, MBA, Data Professional





Project Overview
Employee promotion decisions are among the most critical workforce management activities within modern organizations. Identifying high-potential employees requires balancing performance indicators, training outcomes, experience, departmental needs, and organizational objectives. Traditional promotion processes often rely on manual assessments, introducing subjectivity and inconsistencies across departments.
This project develops an end-to-end Machine Learning solution that predicts employee promotion eligibility using historical HR data. By leveraging advanced predictive analytics, explainable AI techniques, and interactive deployment, the system provides a practical decision-support tool that enables Human Resource departments to identify promotion-ready employees with greater accuracy, transparency, and efficiency.
The project follows the complete CRISP-DM (Cross-Industry Standard Process for Data Mining) framework, encompassing Business Understanding, Data Understanding, Data Preparation, Exploratory Data Analysis, Feature Engineering, Model Development, Explainable AI, Model Optimization, and Production Deployment.

Business Objective
The primary objective is to predict whether an employee will be promoted based on organizational, demographic, training, and performance-related attributes.

Business Questions
•	Which employee characteristics most influence promotion decisions?
•	Can promotion outcomes be predicted before formal HR evaluation?
•	What role do performance ratings, training achievements, and awards play in promotion eligibility?
•	How can HR teams identify high-potential employees proactively?
•	Can machine learning improve consistency and objectivity in promotion decisions?

Success Criteria
Develop a predictive model capable of accurately identifying promotion candidates while maintaining interpretability and business relevance for HR stakeholders.

Dataset Overview
The dataset contains employee records from a large organization and includes demographic, educational, performance, and organizational attributes.
Metric	Value
Total Employees	54,808
Original Features	13
Engineered Features	52
Target Variable	is promoted
Promotion Rate	8.52%







Target Variable
Is promoted
•	1 → Employee Promoted
•	0 → Employee Not Promoted
The dataset presents a significant class imbalance, with only 8.5% of employees receiving promotions, making model selection and evaluation particularly challenging.

Exploratory Data Analysis
Exploratory analysis revealed several important promotion drivers.
Performance Ratings
Promotion probability increased consistently with higher annual performance ratings.
Employees receiving the highest rating were more than twice as likely to be promoted compared with average performers.
Awards Recognition
Award-winning employees demonstrated substantially higher promotion rates than employees without formal recognition.
Training Performance: Training outcomes emerged as one of the strongest indicators of promotion potential.
Promoted employees achieved significantly higher average training scores than non-promoted employees.
Departmental Differences
Promotion rates varied considerably across departments.
Technology, Analytics, Procurement, and Operations departments exhibited the highest promotion frequencies, while Legal and HR departments showed comparatively lower promotion activity.
Education Impact
Employees holding Master's degrees or higher demonstrated a greater likelihood of promotion than employees with lower educational attainment.

Feature Engineering
Several preprocessing and transformation techniques were implemented to improve model performance:
Data Quality Treatment
•	Missing Education values imputed using mode.
•	Missing Previous Year Ratings imputed using median.
•	Missing Training Scores imputed using median.

Encoding
Categorical variables transformed using One-Hot Encoding:
•	Department
•	Region
•	Education
•	Gender
•	Recruitment Channel

Final Modeling Dataset
Original Features: 13
Final Engineered Features: 52




Machine Learning Pipeline
Three classification algorithms were evaluated:
Logistic Regression
Used as a baseline interpretable model.
ROC-AUC: 0.797
Random Forest
Implemented to capture nonlinear relationships and feature interactions.
ROC-AUC: 0.779
XGBoost
Gradient boosting framework selected for final model development due to superior predictive performance and robustness.
ROC-AUC: 0.818

Hyper parameter Optimization
Grid Search Cross Validation was performed to optimize XGBoost parameters.
Best Parameters
•	n_estimators = 200
•	max_depth = 3
•	learning_rate = 0.20
•	min_child_weight = 3
•	colsample_bytree = 0.90
•	subsample = 1.00

Optimized Performance
ROC-AUC improved to 0.822.

Threshold Optimization
Given the business importance of identifying promotable employees, classification thresholds were optimized rather than relying on the default 0.50 probability cutoff.

Optimal Threshold
0.2506
Results
Metric	Score
Precision	71%
Recall	42%
F1 Score	53%
ROC-AUC	82.2%
This threshold significantly improved the model's ability to identify employees likely to be promoted.

Explainable AI (SHAP)
To ensure transparency and stakeholder trust, SHAP (SHapley Additive Explanations) was applied to interpret model predictions.
Most Influential Promotion Drivers
1.	Average Training Score
2.	Department (Sales & Marketing)
3.	Previous Year Rating
4.	Department (Operations)
5.	Age
6.	Awards Won
7.	Number of Trainings
8.	Master's Degree
9.	Department (Technology)
10.	Length of Service

Key Insight
Training performance emerged as the most influential predictor of employee promotion, highlighting the strategic value of employee development programs.

Model Validation
Five-fold cross-validation was conducted to evaluate model stability.
Cross-Validation Results
ROC-AUC Scores:
•	0.8155
•	0.8070
•	0.8284
•	0.8357
•	0.8119

Summary
Mean ROC-AUC: 0.820
Standard Deviation: 0.011
The low variance demonstrates strong model stability and consistent predictive performance across multiple validation folds.

Deployment
The final model was deployed using Streamlit as an interactive web application.
Application Features
•	Real-time employee promotion prediction
•	Interactive HR decision-support interface
•	Probability-based promotion scoring
•	Explainable and transparent outputs
•	User-friendly dashboard for non-technical stakeholders

Business Impact
This solution enables organizations to:
Strategic Talent Management
Identify promotion-ready employees proactively.
Workforce Planning
Support succession planning and leadership development initiatives.
Data-Driven HR Decisions
Reduce subjectivity and increase consistency in promotion evaluations.
Employee Development
Understand factors contributing most strongly to career advancement.








Technology Stack
Data Analysis
•	Pandas
•	NumPy
Machine Learning
•	Scikit-Learn
•	XGBoost
Explainable AI
•	SHAP
Visualization
•	Matplotlib
•	Seaborn
Deployment
•	Streamlit
•	Joblib

Project Links
GitHub Repository
https://github.com/NematullahAmiri/employee-promotion-prediction/tree/main

Live Application
https://employee-promotion-prediction-eq4g66rt6fpqn7ximhkrzx.streamlit.app/

Portfolio Website
https://nematullahamiri.github.io/#projects


