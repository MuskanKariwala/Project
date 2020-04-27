from flask import Flask, request, render_template
#from sklearn.metrics import accuracy_score
#from sklearn.preprocessing import MinMaxScaler
import pandas as pd
#import os
#UPLOAD_FOLDER = 'C:/Users/Muskan/Desktop/uploads'

#AFTER_CLEAN_PATH = 'C:/Users/Muskan/Desktop/uploads/mammogram.csv'


app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['AFTER_CLEAN_PATH'] = AFTER_CLEAN_PATH


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

	#if request.method=='POST':

      file = request.files['file']
      df = pd.read_csv(file)
      print(type(df))
      #file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
      #file.open(os.path.join(app.config['UPLOAD_FOLDER'], "hello"))
      df.to_csv("C:/Users/Muskan/Desktop/uploads/mammographic_masses.data.txt", index = False)

      #return render_template("index.html", message="File uploaded successfully")
      return render_template('index.html', data = df.head(15).to_html(), title= 'The Mammogram Dataset', shape = ' Number of rows and columns available in the dataset: {}'.format(df.shape))
      
    #return render_template("index.html", message="Upload")

@app.route('/fillmissing', methods=['POST'])
def fillmissing():
	df1 = pd.read_csv(r'C:/Users/Muskan/Desktop/miniproject/mammographic_masses.data.txt', na_values='?')
	df1['AGE']=df1['AGE'].fillna(method="ffill")
	df1['SHAPE']=df1['SHAPE'].fillna(method="ffill")
	df1['MARGIN']=df1['MARGIN'].fillna(method="ffill")
	df1['DENSITY']=df1['DENSITY'].fillna(method="ffill")
	df1.to_csv("C:/Users/Muskan/Desktop/uploads/mammogram.csv", index = False)
	after_change_csv = pd.read_csv(r'C:/Users/Muskan/Desktop/uploads/mammogram.csv')
	return render_template('index.html', data1 = after_change_csv.head(15).to_html())


@app.route('/convertfloat', methods=['POST'])
def convertfloat():
	df = pd.read_csv(r'C:/Users/Muskan/Desktop/uploads/mammogram.csv')
	df['BI_RAIDS']=pd.to_numeric(df['BI_RAIDS'], downcast='integer')
	df['AGE']=pd.to_numeric(df['AGE'], downcast='integer')
	df['SHAPE']=pd.to_numeric(df['SHAPE'], downcast='integer')
	df['MARGIN']=pd.to_numeric(df['MARGIN'], downcast='integer')
	df['DENSITY']=pd.to_numeric(df['DENSITY'], downcast='integer')
	df.to_csv("C:/Users/Muskan/Desktop/uploads/mammogram1.csv", index = False)
	after_change_csv = pd.read_csv(r'C:/Users/Muskan/Desktop/uploads/mammogram1.csv')
	return render_template('index.html', data2 = after_change_csv.head(15).to_html())

# @app.route('/normalise', methods=['POST'])
# def normalise():
# 	df = pd.read_csv(r'C:/Users/Muskan/Desktop/uploads/mammogram1.csv')
# 	f=df[['AGE']].values
# 	from sklearn.metrics import accuracy_score
# 	from sklearn.preprocessing import MinMaxScaler
# 	scaler=MinMaxScaler(feature_range=(0,10))
# 	df['AGE_SCALED']=scaler.fit_transform(f)
# 	print("Scaled features:")
# 	df.to_csv("C:/Users/Muskan/Desktop/uploads/mammogram2.csv", index = False)
# 	after_change_csv = pd.read_csv(r'C:/Users/Muskan/Desktop/uploads/mammogram2.csv')
# 	features_scaled=df[['AGE_SCALED','SHAPE','MARGIN','DENSITY']].values
# 	features_scaled
# 	return render_template('index.html', data3 = after_change_csv.head(15).to_html())


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)