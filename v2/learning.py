from keras import backend
from keras.callbacks import TensorBoard

import image_generator as imggen
import network

import os




img_w = img_h = 64
nb_epoch = 1
iterations = 25
TRAINING_SET_SIZE = 50000
TEST_SET_SIZE = 10000

backend.set_learning_phase(1)
if backend.image_data_format() == 'channels_first':
    input_shape = (1, img_w, img_h)
else:
    input_shape = (img_w, img_h, 1)


def train(path):
    print (os.path.join(path,"results/data"))
    model = network.init_model(imggen.LABEL_SIZE, input_shape)
    model.compile(loss='categorical_crossentropy',
                  optimizer='adadelta', metrics=['accuracy'])
    tensorboard = TensorBoard(log_dir=os.path.join(path,'logs'),
                              histogram_freq=0,
                              write_graph=True, write_images=True)

    for epoch in range(0, iterations):
        (x_train, y_train) = imggen.next_batch(TRAINING_SET_SIZE,
                                               rotate=True, ud=True,
                                               multi_fonts=True,
                                               multi_sizes=True, blur=True)

        model.fit(x_train, y_train, batch_size=32,
                  epochs=epoch + 1, verbose=1,
                  validation_split=0.1, callbacks=[tensorboard],
                  initial_epoch=epoch)
    if not os.path.exists(os.path.join(path,'results/data')):
        os.makedirs(os.path.join(join,'results/data'))
    model.save_weights(os.path.join(path,'results/data/model%d.h5' )% (epoch))

    (x_test, y_test) = imggen.next_batch(TEST_SET_SIZE)
    score = model.evaluate(x_test, y_test)
    print "\n"
    print 'Test score: {0:.4g}'.format(score[0])
    print 'Test accur: {0:.4g}'.format(score[1])


if __name__ == '__main__':
    train()
