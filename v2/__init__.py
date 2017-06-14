from learning import *
from predict import *

print "cat"

def learning():
    train()

def predict():
    args = init_arguments()
    char = recognize_image(args.image)
    print(char)

