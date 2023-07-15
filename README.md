# laughing-enigma

The RESTapi server can be found in rest_server
The helper code to extract the manifest file from apks is present in utils

Code for training the model is present in model_training (initialize.py)

It outputs 2 files,
1. A dump of the decision tree model
2. A dump of the permission names used in the feature vectors in order

These files must be copied into the feat_store folder inside the maldetect_api folder so that it maybe used in realtime

(P. S. Make sure to run the training code with the same python env as the server, or there will be pickling issues. You can activate the virtual environment by sourcing the activate file in the .venv folder of rest_server, which is created after running make install)
