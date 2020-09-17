# Open Class Prize

## Goal
The goal of this project is to tag question/answer samples strucutured in a tab/line separated text file as any of many topics (this implementation involves ~325 unique topics)

## Methods
The best solution ended up involving using a unique logistic regression classifier for each class along with a TFID-vectorized input. Given the small data size the choice of __seed__ for tbe train-test split also proved to be an important factor in development.  

The data was highly unbalanced. Many labels appeared only once in the training data making it impossible to train on in some instances.  

![dist of labels before removal](https://github.com/dalcantara7/openclass_prize/blob/master/images/before%20removal.png)

It was a trade-off between never being able to pick the given class and trying to get the model to incorporate the one-off case. Removing such labels from training enabled better results. 

![dist of labels after removal](https://github.com/dalcantara7/openclass_prize/blob/master/images/after%20removal.png)

Several methods were of exploration were used to determine the right set of hyper-parameters (i.e. class-weight, train-test split seed, number of labels to keep, what part of question/answer to use, etc.). A full detailed explanation of my process is available in the presentation [video](https://drive.google.com/file/d/16P1NwQbihpMgJ-XuySzc5nOeo1jSfGjL/view?usp=sharing)


## Results
My algorithm ended up acheiving a __0.54 F2 score__. I'm quite proud of this result given the small training data size. This was also higher than the algorithm developed by the creator of OpenClass

_NOTE: the presentation states that my highest F2 score was only __0.52__. I had made the presentation before my last "hail-mary" submission to the competition using the entire training set for training (as opposed to setting aside a dev set)__

# BELOW HERE WAS PROVIDED BY SCHOOL AND FILLED IN BY ME

# Layout
Only a couple new files have been added to this repo from the template
1. /test_scores/ <= this folder contains .csv, and corresponding .xlsx files for the tests that I ran to determine the best classifier set up
2. /code/pickle_files <= this folder contains the best scoring model as well as the binarizer and vectorizer used


# Presentation

- [This](https://drive.google.com/file/d/16P1NwQbihpMgJ-XuySzc5nOeo1jSfGjL/view?usp=sharing) is the link to the recorded presentation.

_NOTE: The video gives the most comprehensive overview of my methodology, but a PDF of the presentation slides named `presentation-slides.pdf` is in the `presentation-slides` directory._

# Data

The data used for training can be accessed [here](https://github.com/ua-ling-439-spring-2020/final-project-dalcantara7/blob/master/code/openclass_prize.train)

# Leaderboard Identification

On the OpenClass leaderboard the team name I used was __"I guess this'll work"__

# Code

To run the run_model.py script which will train a model and print out the F1 score, run the installation line below (to build the docker file) and then run the following command. 

``` 
# executed from within the 'code' directory
docker run ling-539/final-project-dalcantara7 python scripts/run_model.py YOUR_TRAINING_FILE YOUR_TESTING_FILE
``` 

## Installation

Dependencies are within the requirements.txt and the docker file is set up to install them

``` 
# executed from within the `code` directory:
docker build -f Dockerfile -t "ling-539/final-project:latest" .
```
