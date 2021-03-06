# Mental-Health-Assessment
<a href="https://colab.research.google.com/drive/17sgdF6EZ6wWmrprG9jAwcpvGIu0iwk8J#scrollTo=F0IwAO4mas2V">Colab notebook</a>

## Introduction
This project provides a method for the military to assess the mental health of soldiers and take responsible actions for them if they in a dark place.<br>
According to recent studies, PTSD is the most common mental health problem faced by returning troops. The symptoms include difficulty concentrating, lack of interest/apathy, feelings of detachment, loss of appetite, hypervigilance, exaggerated startle response, and sleep disturbances.

## Dataset
The dataset used in this project is obtained by combining 3 seperate datasets.

**1.** <a href="https://huggingface.co/datasets/emotion">emotions</a> dataset from hugging face.<br>
**2.** text_emotion dataset from kaggle.<br>
**3.** <a href="https://www.kaggle.com/nikhileswarkomati/suicide-watch">Suicide_Detection</a> dataset from kaggle.<br>

**Note: The final dataset is not uploaded here, but it can be generated by downloading each dataset from the given links and running the scripts**

The final dataset contains about 16 emotions which are condensed into 3 for better performance.<br><br>
<img src="multi_emotions.png" alt="multiple emotions" width="400" height="250">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="condensed_emotions.png" alt="condensed emotions" width="400" height="250">

## Model
Linear SVM is used in this project for emotion detection as it gave the highest accuracy( 92.7% )

### How is the mental health report generated?
The person is asked a series of questions and their responses are tokenized into sentences.<br>
The sentences are passed into the model to identify the emotions in each and a percentage composition is calculated for each emotion.<br>
The generate_report function creates a report according to the percentage values.<br><br>
Here is a sample response and the report generated.<br><br>
<img src="sample_response.png" alt="response" width="500" height="600">
