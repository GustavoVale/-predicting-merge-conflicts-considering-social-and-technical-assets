import tensorflow as tf
from tensorflow.keras import layers
import keras_metrics

def __get_model(algorithm,
                type_model,
                units,
                num_hidden_layers,
                neuron_dense,
                dropout_rate,
                activation,
                x_train,
                data_index):

    if algorithm == 'DNN':
        inputs = tf.keras.Input(shape=(x_train.shape[1],))
    else:
        inputs = tf.keras.Input(shape=(1, data_index))

    if type_model == 'SEQ':
        x = tf.keras.Sequential()(inputs)
        if algorithm == 'GRU':
            x = layers.GRU(units=units)(x)
    
        elif type_model == 'LSTM':
            x = layers.LSTM(units=units)(x)
    
    # It means MLP
    else:
        if algorithm == 'GRU':
            x = layers.GRU(units=units)(inputs)
        
        elif type_model == 'LSTM':
            x = layers.LSTM(units=units)(inputs)
        
        # It means DNN
        else:
            x = layers.Dropout(dropout_rate)(inputs)

    for _ in range(num_hidden_layers):
        x = layers.Dense(neuron_dense,
                         activation=activation)(x)
        x = layers.Dropout(dropout_rate)(x)

    outputs = layers.Dense(1, activation=activation)(x)

    model = tf.keras.Model(inputs=inputs, outputs=outputs)
    
    return model

def keras_model(algorithm,
                type_model,
                learning_rate,
                dropout_rate,
                units, 
                neuron_dense,
                hidden_layers, 
                epochs,
                batch_size,
                activation,
                x_train,
                y_train,
                data_index):

    keras_model = __get_model(algorithm, type_model, units, hidden_layers, neuron_dense, dropout_rate, activation, x_train, data_index) 
    
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

    # Specify the training configuration.
    keras_model.compile(optimizer=optimizer,
                        loss=tf.keras.losses.BinaryCrossentropy(),
                        metrics=[keras_metrics.recall()])
    keras_model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)
    
    return keras_model
