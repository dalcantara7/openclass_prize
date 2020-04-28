## Layout
Only a couple new files have been added to this repo from the template
1. /test_scores/ <= this folder contains .csv, and corresponding .xlsx files for the tests that I ran to determine the best classifier set up
2. /code/pickle_files <= this folder contains the best scoring model as well as the binarizer and vectorizer used


# Presentation

- [This](https://drive.google.com/file/d/16P1NwQbihpMgJ-XuySzc5nOeo1jSfGjL/view?usp=sharing) is the link to the recorded presentation. You will need a University of Arizona log in to access it.

_NOTE: A PDF of the presentation slides named `presentation-slides.pdf` is in the `presentation-slides` directory._

# Data

The data used for training can be accessed [here](https://github.com/ua-ling-439-spring-2020/final-project-dalcantara7/blob/master/code/openclass_prize.train)

# Code

To run the run_model.py script which will train a model, and print out the F1 score run the installation line below (to build the docker file) and then run the following command. 

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
