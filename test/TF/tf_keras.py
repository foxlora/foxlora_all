import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt


#加载数据
train = pd.read_csv('train_modified.csv')
target='Disbursed' # Disbursed的值就是二元分类的输出
IDcol = 'ID'




x_columns = [x for x in train.columns if x not in [target, IDcol]]
X = train[x_columns]
y = train['Disbursed']



#建立模型
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1,input_shape=(X.shape[1],),activation='sigmoid'))

model.summary()

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['acc'])
history = model.fit(X,y,epochs=10)

plt.plot(history.epoch,history.history.get('acc'))
plt.show()

tf.keras.optimizers.Adam()