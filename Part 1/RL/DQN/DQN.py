from tensorflow.keras import Sequential
from keras.layers.core import Dense, Dropout, Conv2D, Maxpooling2D, Activation, Flatten


from keras.callbacks import TensorBoard

class DQNAgent:
    def create_model(self):
        model = Seqential()
        model.add(Conv2D(256, (3, 3), input_shape=env.OBSERVATION_SPACE_VALUES))
        