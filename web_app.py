import pandas as pd
from flask import * 
 
app = Flask(__name__)  
#path = input()

#modify the path to the original location of scraped data csv file 
df = pd.read_csv(r'shopclues (1).csv')
df2 = pd.DataFrame(df['Product_name'])
df2["Discount"] = pd.DataFrame(df['Discount'].str.extract('(\d+)').astype(int))
df2['Price'] = pd.DataFrame(df[' Price '].str.extract('(\d+)').astype(int))
df2["Image_url"] = df["Image_url"]
df2["Image_url"]= df2["Image_url"].str.slice(4,-1, 1)



    
#dictionary1 = {}
#for key,value in df.iteritems():
  #dictionary1[key] = list(value)  
@app.route('/', methods=("POST", "GET"))  
def message():
      return render_template('message.html',  tables=[df2.to_html(classes='data')], titles=df2.columns.values)

@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form
      df2['Product_name'] = df2['Product_name'].str.lower()
      df1 = df2[df2['Product_name'].str.contains(result['name'].lower())]
      return render_template('result_data.html',  tables=[df1.to_html(classes='data')], titles=df1.columns.values)
if __name__ == '__main__':  
   app.run(debug = True)     
   
 
 

  
