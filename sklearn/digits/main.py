#!/usr/bin/env python3

# http://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html

from sklearn.datasets import load_digits
from sklearn import svm, metrics
import matplotlib.pyplot as plt

# laod digits as object with images, data (X), target (y), target names
digits = load_digits()

#print(digits.data[0].shape)   # (64,) # every digit as row with 64 number
#print(digits.images[0].shape) # (8,8) # every digit as matrix 8x8 (like in image)
#print(len(digits.data))       # 1797  # number of examples in dataset

#print(digits.target[:15])       # few targets as numbers
#print(digits.target_names[:15]) # few targets as names

#plt.gray()                       # turn on gray scale 
#for image in digits.images[:2]:  # get few images
#    plt.matshow(image)           # display image
#    plt.show()                   # show window with image

size = len(digits.data) * 1 // 2 
#print(size)  # 898 # number of examples to learn (rest will be used for test)

# create model
classifier = svm.SVC(gamma=0.01)

# learn using X,y
classifier.fit(digits.data[:size], digits.target[:size])

# predict
predicted = classifier.predict(digits.data[size:])

# expected results for prediction
expected = digits.target[size:]

print(' the same:', sum(predicted == expected))
print('different:', sum(predicted != expected))
print('      all:', len(predicted))
    
# compare results expected and predicted    
print(metrics.confusion_matrix(expected, predicted))
print(metrics.classification_report(expected, predicted))
