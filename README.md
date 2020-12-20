# Gene Guru 
Gene Guru is a web-based program that enables people to predict the likihood of getting Cancer along with the severity based on certain features. 
The program takes information about 15 gene features and outputs a probability for the person to get cancer based on the data. 

## Background Information
- Every year, Pathologists diagnose 14 million new patients with cancer around the world
- According to the Oslo University Hospital, the accuracy of prognoses is only 60% for pathologists
- A biopsy usually takes a Pathologist 10 days
- If caught early there is a 70% better chance of survival as compared to if caught in later stages
##### 
According to us, a 60% accuracy is not good enough for such a life-threthening disease. This is why we worked to improve the accuracy in the prediction. 
We provide a likihood of getting a severe case of cancer based on just 15 factors. 

## Technologies Used:
- Python
- Machine Learning
- Flask
- Tensorflow
- Sklearn
- HTML
- CSS

## Backend
Our backend mainly is the Machine Learning Model. The ML model is trained on a dataset of cancer patients from Kaggle. 
The data is first preprocessed using some techniques. There are certain issues with the dataset and we performed functions to improve our model.
Originally, we started with 320 features. There were 6300 empty values in the dataset. We got rid of columns that had more than 50% emply values. 
By doing this, we had 298 features remaining and 2773 remaining empty values. We wanted to improve our input data even more and so we continuted preprocessing.
At the end, we redured our 320 features to only 15 most contributing features.
We tried varius methods and at last went when simple imputation with mean values for the remaining empty values.  

Once the data was preprocessed well, we developed several ML models and trained it on our data. We used cross-validation to test our model. The best model we found
is a 4-layer neural network that we created on our own using tensorflow keras. This has an average accuracy of 97%, which is a significant improvement. 

## Frontend
Currently, the frontend is very basic as we focused on the ML model. The frontend has a home page (".../" or ".../home") that is form-like page that takes in 
15 input values for a patient. These fields are pre-checked to make sure that the input type is correct (eg. we cannot enter text where an integer value is 
expected). Once a person enters values the 15 features, they can go ahead and select "predict". This takes to another page (".../predict") where the prediction is 
shown as a percentage and all the entered values can be seen as well. The person can choose to perform a new prediction from here. 

## Future of the Project
- We want to improve on the frontend to make it more user-friendly and useful. 
- Add similar models for different diseases for prediction
- Incorporate a database to store entered data so that it can be useful in hospitals, etc.
- Host on a cloud service to allow global access and low latency

Build from scratch in under 36 hours by:  
Anushree Jana   
Akash Munjial
