# Code

## Building the container

```
docker build -f Dockerfile -t "ling-539/final-project-dalcantara7:latest" .
```

## Running the project
To run the run_model.py script which will train a model and print out the F1 score, run the installation line below (to build the docker file) and then run the following command. 

``` 
# executed from within the 'code' directory
docker run ling-539/final-project-dalcantara7 python scripts/run_model.py YOUR_TRAINING_FILE YOUR_TESTING_FILE
``` 

### Removing old docker containers, images, etc.

If you want to save some space on your machine by removing images and containers you're no longer using, [see the instructions here](https://docs.docker.com/config/pruning/).  As always, use caution when deleting things.
