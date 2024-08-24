# Email Spam Detector

## Project Overview
This project presents a comprehensive Email Spam Detector built using Python. The journey of this project encompasses data exploration, model building, and deployment, creating a robust solution for identifying spam emails.

## Dataset
The dataset used in this project was sourced from Kaggle. It contains a mix of spam and non-spam emails, providing a balanced foundation for training and evaluating the model.

## Exploratory Data Analysis (EDA)
A thorough EDA was performed to gain insights into the dataset, identify patterns, and understand the distribution of spam versus non-spam emails. This step included visualizations, statistical analysis, and data cleaning to ensure a high-quality dataset for model training.

## Data Preprocessing
Data preprocessing involved cleaning the text data, converting it into a format suitable for machine learning models. The TfidfVectorizer was employed to transform the text data into numerical vectors, capturing the importance of each word within the emails.

## Model Building
Multiple machine learning models were tested, including Naive Bayes, Support Vector Machines (SVM), and Random Forest. After extensive evaluation, the Naive Bayes model was selected for its superior performance. The model was trained on the preprocessed data and saved for deployment.

## Model Evaluation
The model's performance was assessed using various metrics such as accuracy, precision, recall, and F1-score. Naive Bayes was chosen as the final model based on its ability to balance precision and recall effectively.

## Frontend Development
A clean and interactive user interface was developed using HTML and CSS. The frontend allows users to input email content and receive immediate feedback on whether the email is spam or not.

## Backend Development
The backend was developed using Flask, a lightweight Python web framework. The `app.py` file manages the Flask application, routing, and integration with the machine learning model. The `util.py` file is responsible for loading the saved model and providing a `predict` function to classify the emails.

## Deployment
The application was successfully deployed, allowing users to access the spam detection functionality through a web interface. The entire workflow, from data analysis to deployment, demonstrates the practical application of machine learning in real-world scenarios.

## Files in the Repository
- `EDA.ipynb`: Notebook containing the Exploratory Data Analysis.
- `model_building.ipynb`: Notebook detailing the model training and evaluation process.
- `app.py`: Flask application script.
- `util.py`: Script for loading the saved model and predicting spam emails.
- `templates/`: Directory containing the HTML files for the frontend.
- `static/`: Directory containing CSS files and other static assets.

## Installation and Usage
1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run `python app.py` to start the Flask application.
4. Access the application in your web browser at `http://127.0.0.1:5000`.

## Future Enhancements
- **Improving Model Accuracy**: Explore deep learning models for even better performance.
- **Feature Engineering**: Incorporate additional features to enhance spam detection accuracy.
- **Deployment**: Deploy the model on a cloud platform for broader accessibility.

## Conclusion
This project exemplifies the complete workflow of building a machine learning application, from data analysis to deployment. The Email Spam Detector is a practical tool for identifying spam emails, with potential for further enhancements and real-world application.
