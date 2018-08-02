import cgi,cgitb,json,time


cgitb.enable()
print("Content-Type: text/html")
print()

fs = cgi.FieldStorage()

#数据重组
inputs = {}
for key in fs.keys():
    inputs[key] = fs[key].value

#返回数据
# print(inputs) #返回字典
print(json.dumps(inputs)) #返回json数据