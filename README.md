# suicidalrnot
This is a flask API which takes in a textual data and tells whether the text is suicidal or not.... 
## 😊Hola.... 

Hi! This project was done as a part of my course of ML and NNDL. Me and my friends were looking for some interesting project which is simple to implement and at the same time unique.. and as we browsed through Kaggle for datasets we found the a dataset which was a textual dataset with a label specifying the sentiment of the text.


## 🔗Link to the dataset

The dataset which we used for training the model was from kaggle and the links for the dataset are:
 1. https://www.kaggle.com/datasets/imeshsonu/suicideal-phrases
 2. https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch

## 🤖 Model training..

We knew that our project will be as good as our model is. So, it was really important to use a well defined model. We started looking for model which worked well on text data like LSTM, Bidirectional LSTM but there were already a lot of project done by using those models. So, we though of using **transformer networks** for the training and we found **GPT2** interesting as it is little and can be fine tunned easily for classification problems....

## 💻 Final System

With our model ready, we were left with the part of integrating the model into our website. We fixed upon using a **Flask API** as it was easy to integrate the model😅. So the website send a POST request to the API which will pass the data through the model, predict it, and send back a response which will contain either 1 or 0. 1 for suicidal and 0 for non-suicidal text. This response in our project is then used to separate the person into two csv files. One for suicidal person and another for non suicidal... but, as it is a API. you can use it anywhere and integrate it with anything....

