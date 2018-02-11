# CAN'T BE USED; HAS TO RUN ON AWS

# import tflearn
# from tflearn.data_utils import to_categorical, pad_sequences
# from tflearn.datasets import imdb

# # imdb movie database
# #n_words number of words
# #valid_portion: portion of data used for validation instead of training
# # --> 9000 words for training, 1000 words for validation
# train, test, _ = imdb.load_data(path='imdb.pkl', n_words=10000, valid_portion=0.1)
# trainX, trainY = train
# textX, testY = test

# # Data preprocessing
# # Sequence padding --> convert words into labels
# trainX = pad_sequences(trainX, maxlen=100, value=0.)
# textX = pad_sequences(testX, maxlen=100, value=0.)

# # convert labels to vectors
# trainY = to_categorical(trainY, nb_classes=2)
# textY = to_categorical(testY, nb_classes=2)

# # Build up the network
# netBaseLayer = tflearn.input_data([None, 100]) #100 because maxlength is 100
# netHiddenLayer = tflearn.embedding(netBaseLayer, input_dim=10000, output_dim=128) #input=10000 because of 10000 words
# #create long short term memory
# netLstmLayer = tflearn.lstm(netHiddenLayer, 128, dropout=0.8) #dropout prevents overfitting by randomly dropping
# netFullyConnectedLayer = tflearn.fully_connected(netLstmLayer, 2, activation='softmax') #turns vectors to outcome probabilities
# netRegressionLayer = tflearn.regression(netFullyConnectedLayer, ptimizer='adam', learning_rate=0.0001, loss='categorcial_rossentropy')

# model = tflearn.DNN(netRegressionLayer, tensorboard_verbose=0)
# model.fit(trainX, trainY, validation_set(testX, testY), show_metric=True, batch_size=32)
