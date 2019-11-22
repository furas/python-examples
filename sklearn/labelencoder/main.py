from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.DataFrame({
        'first_browser': ['Firefox', 'Chrome', 'Opera'],
        'gender': ['Male', 'Female', 'Male'],
     })

cols = ['first_browser', 'gender'] # strings with column's names for encoding

all_labelencoders = {} # dictionary for encoders

# create encoders

for name in cols:
    # create encoder and keep it in dictionary
    
    labelencoder = LabelEncoder()
    all_labelencoders[name] = labelencoder

    # use encoder to encode original column to new column
    labelencoder.fit( df[name] )   
    df['encoded_' + name] = labelencoder.transform( df[name] )

    # the same in one line
    #df['encoded_' + name] = labelencoder.fit_transform( df[name] )

# check encoders

for name in cols:
    print(name, '=', all_labelencoders[name])

print(df)

# ... calculations ...

# inverse data

for name in cols:
    encoder = all_labelencoders[name]
    data = encoder.inverse_transform(df['encoded_' + name])
    print(name, '=', data)
