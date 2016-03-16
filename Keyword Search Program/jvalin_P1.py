# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 15:42:53 2015

@author: Jvalin
"""

# -*- coding: utf-8 -*-
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
import math
from collections import Counter
from operator import itemgetter
#from nltk.stem.porter import PorterStemmer
j = 0 
i = 0

cont = 1
f = 0
pl = 0
dn = 0
kr = 0
vm = 0
o = 0
e = 0
we = 0
eq = 0
gh = 0
v =[]
b =[]
ch = []
jk = []
ck = []
bk = []
wt = []
q = []
tf =[]
z = []
li=[]
a =[]
fx= []
cx = []
visited =[]
#import ntpath
import os
import glob


os.chdir('stateoftheunionaddresses')
for fil in glob.glob("*.txt"):
    v.append(fil)



corpus_root = ('stateoftheunionaddresses')
for stateoftheunionaddresses in os.listdir(corpus_root):
    file = open(os.path.join(corpus_root, stateoftheunionaddresses), "r")
    doc = file.read()
    b = sorted((stopwords.words('english')))   
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    tokens = tokenizer.tokenize(doc)
    
    tokens = [w for w in tokens if not w.lower() in b]
    
    #print(v[f])

    for p in range (len(tokens)):
        stemmer = PorterStemmer()
        tokens[p] = stemmer.stem(tokens[p])

    for j in range (len(tokens)):
        fx.append(tokens[j])

    jk.append(len(tokens))
    
    count = Counter(tokens)
    
    
    wt = list(count.keys())
    
    for i in range (len(wt)):
        q.append(wt[i])
    
    cx.append(len(q))
    bk.append(len(wt))
    
    a = list(count.values())

    ck.append(len(a))
    
    for i in range (len(a)):
        z.append(a[i])
    #print (len(count))
        
    
    f = f + 1
    file.close()

print(len(cx))

for i in range (len(fx)):
    if fx[i] not in visited:
        visited.append(fx[i])
      

    
vm =[]
x =[]
for i in range (len(visited)):
    vm.append(0)

for i in range (len(q)):
    x.append(0)
    
kl = 0
fq = 0

#idf for files
corpus_root = ('stateoftheunionaddresses')
for stateoftheunionaddresses in os.listdir(corpus_root):
    file = open(os.path.join(corpus_root, stateoftheunionaddresses), "r")
    doc = file.read()
    b = sorted((stopwords.words('english')))   
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    tokens = tokenizer.tokenize(doc)
    tokens = [w for w in tokens if not w.lower() in b]
    kl= kl + 1        
    for p in range (len(tokens)):
        stemmer = PorterStemmer()
        tokens[p] = stemmer.stem(tokens[p])
    
    count = Counter(tokens)
    
    
    wt = list(count.keys())
    
    for i in range (len(q)):
        wrd = q[i]
        flag = 8
        if wrd in wt:
            flag = 1
        if flag == 1:
            x[i] = x[i] + 1

    for j in range (len(visited)):
        cw = visited[j]
        fg = 3
        if cw in wt:
            fg = 9
        if fg == 9:
            vm[j] = vm[j] + 1
            
    file.close()
#x contains idf of all unique words per document
# z contains tf of all unique words per document
for i in range (len(vm)):
    evm = math.log10(f/vm[i])
    vm[i] = evm


for i in range (len(x)):
    eq = math.log10(f/x[i])
    x[i] = eq
    
for j in range (len(z)):
    we = 1 + math.log10(z[j])
    z[j] = we

for r in range (len(z)):
    td = x[r] * z[r]
    tf.append(td)
    
#vectorization of tf idf of all words
s = 0
ad = 0
cv = 0
cdv =[]
for i in range (f):
    for j in range(s,(cx[i]-1)):
        s = s + 1
        cv = cv + math.pow(tf[j],2)
    for j in range (ad,(cx[i]-1)):
        ad = ad + 1
        cf = tf[j]/math.sqrt(cv)
        cdv.append(cf)
        
        


qt =[]
qd = []
etq= []
qdv = []
et=[]
et1 =[]
eb = []
cq =[]
tq =[]

qstring = input('Enter Query String: ')
    
def query(qstring):
    
    #print("string Calculation")
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    tokens = tokenizer.tokenize(qstring)
    
    ch = sorted((stopwords.words('english')))
        
    tokens = [w for w in tokens if not w.lower() in ch] 
     
    for p in range (len(tokens)):
        stemmer = PorterStemmer()
        tokens[p] = stemmer.stem(tokens[p])
        
    can = Counter(tokens)
    
    qt = list(can.keys())

        
    for i in range (len(qt)):
        et.append(qt[i])
        
    for i in range (len(et)):   
        et1.append(0)
        
    qd = list(can.values())
    
    for i in range (len(qd)):
         eb.append(qd[i])   
    #idf of particular word
    for l in range (len(visited)):
        for j in range ((len(et))):
            if et[j] ==  visited[l]:
                et1[j] = vm[l]
    
    #tf idf product
    for i in range (len(qd)):
        sq = et1[i] * (1 + math.log10(eb[i]) )
        etq.append(sq) 
    
    qv = 0
    #vector normalization of query
    for j in range (len(eb)):
        qv = qv + math.pow(etq[j],2)
    for j in range (len(eb)):
        cq = etq[j]/math.sqrt(qv)
        qdv.append(cq)

    
    #sum of tf idf of query
    fk = cosq(qstring)
    return(v[fk])

#function
vec = []
    
def gettfidfvec(filename):
    filen = filename
    for i in range (len(v)):
        if filen == v[i]:
            y = i


    rt = ck[y-1]
    ru = ck[y]
    for i in range (rt,ru-1):
        print(cdv[i])
        print(q[i])
    
            


def getidf(token):
            
        stemmer = PorterStemmer()
        t = stemmer.stem(token) 
        
        if t in visited:
            for i in range (len(visited)):
                if t == visited[i]:
                    gtfid = vm[i]
                    
        else:
            return(0)
      
        print(gtfid)      
        tokid = math.log10(f/gtfid)
        return(tokid)      
              
        
ax = []       
        
def cosq(qstring):
    pk = 0
    ol = 0 
    for i in range (f):
        n = []
        xyz = []
        cs = 0
        for k in range (ol,(cx[i]-1)):
            xyz.append(q[k])
            ol = ol + 1
        for pol in range (len(et)):
            g = et[pol]
            if g in xyz:
                for y in range (pk,(cx[i]-1)):
                    if g == q[y]:
                        n.append(qdv[pol]*cdv[y])
                    pk = pk + 1
            else:
                n.append(0.0) 
        
        for pr in range (len(n)):
            so = n.pop()
            cs = cs + so
        ax.append(cs)   
                         
    gf = max(enumerate(ax), key=itemgetter(1))[0]
    return(gf)                    


def docdocsim(filename1,filename2):
    fl1 = filename1
    tot  = 0
    fl2 = filename2
    dds = []
    ddt = []
    ddu = []
    ddv = []
    rx = []
    
    if fl1 in v:
        for i in range (len(v)):
            if fl1== v[i]:
                g1 = i
                
        
        rt = ck[g1-1]
        ru = ck[g1]
        
        for i in range (rt,ru-1):
            dds.append(q[i])
            ddt.append(cdv[i])
        
    if fl2 in v:
        for j in range (len(v)):
            if fl2  == v[j]:
                g2 = j
                
    
        rg = ck[g2-1]
        rh = ck[g2]
        
        for j in range (rg,rh-1):
            ddu.append(q[j])
            ddv.append(cdv[j])
            
    for i in range (len(ddu)):
        chq = ddu[i]
        for j in range (len(dds)):
            if chq == dds[j]:
                r = ddt[i]*ddv[j]
                rx.append(r)
            else:
                rx.append(0)

    for i in range (len(rx)):
        t = rx.pop()
        tot = tot + t
    
    
    return(tot)            




def querydocsim(query, filename):
    
    qt =[]
    ch =[]
    ft =[]
    fv =[]
    qd =[]
    etq =[]
    qdv =[]
    et =[]
    et1 =[]
    eb =[]
    qdv =[]
    
    qry = query
    
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    tokns = tokenizer.tokenize(qry)
    
    ch = sorted((stopwords.words('english')))
        
    tokns = [w for w in tokns if not w.lower() in ch] 
     
    for p in range (len(tokns)):
        stemmer = PorterStemmer()
        tokns[p] = stemmer.stem(tokns[p])
        
    cin = Counter(tokns)
    
    qt = list(cin.keys())

        
    for i in range (len(qt)):
        et.append(qt[i])
        
    for i in range (len(et)):   
        et1.append(0)
        
    qd = list(cin.values())
    
    for i in range (len(qd)):
         eb.append(qd[i])   
    #idf of particular word
    for l in range (len(visited)):
        for j in range ((len(et))):
            if et[j] ==  visited[l]:
                et1[j] = vm[l]
    
    #tf idf product
    for i in range (len(qd)):
        sq = et1[i] * (1 + math.log10(eb[i]) )
        etq.append(sq) 
    
    qv = 0
    #vector normalization of query
    for j in range (len(eb)):
        qv = qv + math.pow(etq[j],2)
    for j in range (len(eb)):
        cq = etq[j]/math.sqrt(qv)
        qdv.append(cq)        
        
    fl = filename
        
    if fl in v:
        for j in range (len(v)):
            if fl == v[j]:
                h = j
    else:
        return(0)
         
    rc =[]     
    rt = cx[h-1]          
    ru = cx[h]
                        
    for i in range (rt,ru-1):
        ft.append(q[i])
        fv.append(cdv[i])
        
    for i in range (len(et)):
        fry = et[i]
        if fry in ft:
            for j in range (len(ft)):
                if fry == ft[j]:
                    rc.append(qdv[i]*fv[j])
                    
        else:
            rc.append(0)
    
    so = 0
    cs = 0
    for pr in range (len(rc)):
            so = rc.pop()
            cs = cs + so

    return(cs)        
            

print(query(qstring))
print (getidf("health"))
#print(docdocsim("Barack ObamaJanuary 20, 2015.txt", "Barack ObamaJanuary 28, 2014.txt"))
print (gettfidfvec("Barack ObamaJanuary 20, 2015.txt"))
print(querydocsim("health insurance wall street", "Barack ObamaJanuary 28, 2014.txt"))
