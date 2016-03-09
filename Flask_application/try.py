import csv
import collections
from collections import Counter
from flask import Flask, render_template, json, request,redirect, url_for
#To connect with mysql install flask-mysql using pip install flask-mysql


app = Flask(__name__)



@app.route('/')
def main():
  return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
  try:
    return render_template('signup.html')
  except Exception as e:
    return json.dumps({'error':str(e)})

@app.route('/signUp',methods=['POST','GET'])
def signUp():
    g = 0
    ch = 0
    
    rules=[]
    d1 = request.form.getlist('chbox')
        

    supp = float(request.form['inputsupport'])
    conf = float(request.form['inputconfi'])
    

        



    cu = 0
    for t in range (len(d1)):
        a1 = d1[t]
        for jk in range (len(d1)):
            if d1[jk] == a1:
                ytyty = 0
            else:
                nor = 0
                count = 0
                a2 = d1[jk]            
                print("\nIf %s -> %s" % (a1,a2))
                g1 =[]
                g2 =[]
                input_file = csv.DictReader(open("TEXAS.csv"))
                for row in input_file:
                    g1.append(row[a1]) 
                    g2.append(row[a2])
            
                a = list(Counter(g1))
                b = list(Counter(g2))
                v = Counter(g1).values()
            
                for i in range (len(a)):
                    r = a[i]
                    dt = float(v[i]) 
                #count = 0
                    for j in range (len(b)):
                        p = b[j]
                        count = 0
                        for k in range (len(g1)):
                            ch = ch +1
                            if r == g1[k]:
                                if p == g2[k]:
                                    count = count + 1
                    
                        if count == 0 :
                            rt = 0
                        else:
                            if (count > 0)and (v[i] > 0):
                                count = float(count)            
                                g = float(count/(len(g1)))
                        #h = float()
                        #l = float(h/len(g2))
                                con = float(count/dt)
        
                            if g >= supp and con >= conf:
                                nor = nor + 1
                                print ("If %s=%s ==> %s=%s " % (a1,r, a2,p))
                                rules.append("If "+a1+"="+r+"==>"+a2+"="+p)
                print rules    
        
                print("Number of Rules = %s" % (nor))
 
    return render_template('view_output.html',r1 = rules)

if __name__ == "__main__":
    app.run(port=5002)