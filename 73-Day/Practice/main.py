from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


df = pd.read_csv('weather_data.csv')

# for x in df.to_dict():
#     print(x['day'])

day = df['day'].to_list()
temp = df['temp'].to_list()
condition = df['condition'].to_list()

# print(df.to_dict())

for val in df.to_dict().values():
    print(val)

@app.route('/')
def home():
    return render_template('index.html', datas=df, day=day, temp=temp, condition=condition)


if __name__ == "__main__":
    app.run(debug=True)
