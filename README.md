# CyberVision Image Analyzer
-------------
The idea behind this project is to explore AI Computre Vision capabilities to predict objects in a picture using TensorFlow and Keras.
_____________
CyberVision app is based on ImgaeAI project. To process an image, you need to download one of the following models:

- **[SqueezeNet](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/squeezenet_weights_tf_dim_ordering_tf_kernels.h5)** _(Fastest prediction time and moderate accuracy)_
- **[ResNet50](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_weights_tf_dim_ordering_tf_kernels.h5)** by Microsoft Research _(Fast prediction time and high accuracy)_
- **[InceptionV3](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/inception_v3_weights_tf_dim_ordering_tf_kernels.h5)** by Google Brain team _(Slow prediction time and higher accuracy)_
- **[DenseNet121](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/DenseNet-BC-121-32.h5)** by Facebook AI Research _(Slower prediction time and highest accuracy)_