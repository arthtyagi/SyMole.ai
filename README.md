# SyMole.ai
NOTE :  We recommend our users to read this particular documentation to be able to use our services more efficiently.
## Presented By:
* **Arth Tyagi** ( Team Leader, CEO And ML Engineer [@arthtyagi](https://github.com/arthtyagi) )
* **Pranav Dhawan** ( Sternographer [@pranavdhawan](https://github.com/pranavdhawan))
* **Siddharth Nikhil** ( UI Designer [Deviant Art Profile](https://www.deviantart.com/siddkid) ) [@siddnikh](https://github.com/siddnikh)
## Description 
This is a suite of __two__ Health Services. A **Heart Disease Predictor, CardioNosis** and an **AI Therapist, Nikola**. We believe that health and well-being are primarily the most important components of life. 
Cardiovascular Diseases account to about 24.8% of deaths per year in India. The Heart Disease Predictor would provide such information which,if predicted well in advance, can provide important insights to doctors who can then adapt their diagnosis and treatment per patient basis.
The AI Therapist is designed for people suffering with mental health disorders like clinical depression, stress, anxiety, etc. These Mental Health disorders account to about 3% of total deaths per year in India and is increasing at a staggering rate lately. Currently there is no official government organisation providing suicide prevention helpline in India and what there exists are a number of NGO Helplines which in most cases prove to be dysfunctional and lack proper monetary funds for a proper working. The open-source AI Therapist is designed in a way that people can encounter a friendly interaction with Artificial Intelligence. This would be a small step towards the advancement in human-AI relationship and hopefully would also help people who are going through these miserable conditions.

## What does SyMole.ai do?
SyMole.ai consists of two applications.

### Nikola
Nikola is going to provide counselling to people :
* In Anxiety,
* In Narcissist Personality Disorder,
* In Depression,
  
with bad communication skills but possessing a  will  to  improve them if provided with general emotional support and consolation.
   

### CardioNosis 
The heart disease predictor which will provide patient analysis and results of a health condition test for cardiovascular diseases through the patient's Health Data. This will be in the format of a Python Executable File. This Machine Learning Model will accept patient reports like Age, Sex, Max. Blood Pressure, etc.
The Heart Disease Predictor is in a IPython Notebook format and will be using Machine Learning Algorithms to make predictions on whether a person is suffering from Heart Disease or not. The ML Model will receive information of the patient like Age, Sex, Max. Heart Rate, Serum Cholesterol, and various other attributes(given below) and analyze the data to conclude results via RandomForestClassifier, one of the most sophisticated Machine Learning algorithms.


#### Attribute Information for Heart Disease Predictor
* Age : displays the age of the individual.
* Sex : displays the gender of the individual using the following format : 1 = male 0 = female.
* Chest-pain type : displays the type of chest-pain experienced by the individual using the following format : 1 = typical angina 2 = atypical angina 3 = non - anginal pain 4 = asymptotic
* Resting Blood Pressure : displays the resting blood pressure value of an individual in mmHg (unit)
* Serum Cholestrol : displays the serum cholestrol in mg/dl (unit)
* Fasting Blood Sugar : compares the fasting blood sugar value of an individual with 120mg/dl. If fasting blood sugar > 120mg/dl then : 1 (true) else : 0 (false)
* Resting ECG : 0 = normal 1 = having ST-T wave abnormality 2 = left ventricular hyperthrophy
* Max heart rate achieved : displays the max heart rate achieved by an individual.
* Exercise induced angina : 1 = yes 0 = no
* ST depression induced by exercise relative to rest : displays the value which is integer or float.
* Peak exercise ST segment : 1 = upsloping 2 = flat 3 = downsloping
* Number of major vessels (0-3) colored by flourosopy : displays the value as integer or float.
* Thal : displays the thalassemia : 3 = normal 6 = fixed defect 7 = reversable defect
* Diagnosis of heart disease : Displays whether the individual is suffering from heart disease or not : __0 = absence 1,2,3,4 = present.__
## Prerequisites
There are absolutely no prerequisites for the Nikola AI service.
As for the CardioNosis, the user requires to know how to use Python executable files. Basic knowledge of Python would be highly useful though. A good start for learning python is [learnpython.org](https://www.learnpython.org/)
## Installation
### Setting up our two services :computer: :
* #### For Heart Disease Predictor ( SyMole.ai CardioNosis :heart: ) :-
 `git clone github.com/pranavdhawan/SyMole.ai`
 
 Open the CardioNosis folder and head over to the Python file.
  You can watch the video tutorial to use our Python executable file.
  ##### YouTube link : [Learn to use CardioNosis' Python file ](https://www.youtube.com/watch?v=9v-Rx-xiN70&t=11s)
  
* #### For AI Therapist ( Symole.ai Nikola :zap: ) :-
Clone the repository to your local  machine using the command: 
 `
 git clone github.com/pranavdhawan/SyMole.ai`

Once you have cloned our repository, head over to **index.html**.

Run it in your web browser, it's a locally hosted model.

## Dependencies
* https://www.kaggle.com/ronitf/heart-disease-uci
* ELIZA Framework

## License
* [Open MIT](https://opensource.org/licenses/mit-license.php)




