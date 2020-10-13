#!C:\Users\choiy\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-Type: text/html")
print()

import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

opened_file = open('data/'+title, 'w', encoding='utf-8') 
opened_file.write(description) #description에 해당하는 값이 data 폴더에 있는 title이라는 파일명을 갖고 만들어진다.
opened_file.close()

#Redirection
#Redirection
print("Location: index.py?id="+title)
print()

print(title)
print(description)
