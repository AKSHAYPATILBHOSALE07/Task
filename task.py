import requests
from bs4 import BeautifulSoup
import pickle
import json
url = "https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml') # If this line causes an error, run 'pip install html5lib' or install html5lib
#print(soup.prettify())



######################## Price ###############

#for value in soup.find_all(class_='price'):
#    print(value.text)

######################## Title ####################

#heading = soup.find(class_='catalog-item-name')
#print(heading.text)
#for heading in soup.find_all( class_='catalog-item-name'):
#    print(heading.text)
    
###################### Stock Status ####################
"""
status = soup.find(class_='status')
#print(status.text)


for stat in soup.find_all(class_='status'):
    #print(stat.text)
    var = stat.text
    print(type(var))
    if var == "Out of Stock":
        print("False")
    else:
        print("True")  
print("The end") """
         
##################  Manufacturer ##########
"""
manufacturer = soup.find(class_='catalog-item-brand')
#print(manufacturer.text)

for man in soup.find_all(class_='catalog-item-brand'):
    print(man.text)  """

######################## Main ###########################
z = {}
result = []  
a =str("price")

for value in soup.find_all(class_='price'):
    #print(value.text)
    price_v = value.text
    result.append(price_v)
 
z[a] = result
res = pickle.dumps(z)
b = pickle.loads(res)
#print(b)  
#print('\n')   

#print(result)    

y = {}
c =str("title")
result1 = []    
for heading in soup.find_all(class_='catalog-item-name'):
    #print(heading.text)
    title = heading.text
    result1.append(title)
#print(result1)   

y[c] = result1
res1 = pickle.dumps(y)
d = pickle.loads(res1)
#print(d)   
#print('\n')  


 
x = {}
e =str("stock") 
  
result2 =[]    
for stat in soup.find_all(class_='status'):
    #print(stat.text)
    var = stat.text
    #print(type(var))
    if var == "Out of Stock":
        #print("False")
        var = False
        result2.append(var)
        
        x[e] = result2
        res2 = pickle.dumps(x)
        f = pickle.loads(res2)
        #print(f)   

        
    if var ==  "In Stock":
        #print("True")  
        var = True
        result2.append(var)
        
        x[e] = result2
        res2 = pickle.dumps(x)
        f = pickle.loads(res2)
            
#print(result2)
#print(f) 
#print('\n')    
        
 
w = {}
g = str("maftr") 
result3 =[]       
for man in soup.find_all(class_='catalog-item-brand'):
    #print(man.text)   
    manufacturer = man.text  
    
    result3.append(manufacturer)
#print(result3)

w[g] = result3
res3 = pickle.dumps(w)
h = pickle.loads(res3)

#print(h)


F_list = [ b, d, f, h]   #list of dict
#print(F_list)  

jsonStr = json.dumps(F_list) #json
print(jsonStr)

#print(type(price_v))
#print(type(title))
#print(type(var))
#print(type(manufacturer))    
        
