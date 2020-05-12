from imageai.Prediction import ImagePrediction
import os

execution_path = os.getcwd()
# Add images to the same folder as cybervision.py

prediction = ImagePrediction()
# Choose model type for processing images:
# - DenseNet (fastest prediction time and moderate accuracy)
# - ResNet by Microsoft Research (fast prediction time and high accuracy)
# - InceptionV3 by Google Brain (slow prediction time and higher accuracy)
# - DenseNet121 by Facebook AI Research (slower prediction time and highest accuracy)
prediction.setModelTypeAsDenseNet()
# 
prediction.setModelPath(os.path.join(execution_path, "DenseNet-BC-121-32.h5"))
prediction.loadModel()

# Specify which picture you want to process
predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "1524514638493.jpeg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)