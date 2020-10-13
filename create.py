#!C:\Users\choiy\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-Type: text/html")
print()
import cgi, os

# #폴더 안에 있는 파일을 자동으로 업데이트되는 리스트로 만들기
# files = os.listdir(path='data') #'data'라는 폴더 안에 있는 파일들을 리스트로 만들어서 files라는 변수에 저장함
# print(files) #즉, files는 리스트임.
# listStr = '' #listStr이라는 빈 변수를 만들어
# for item in files: #files 안에 있는 element들을 한 개씩 item이라는 변수에 꺼낸다.
#   listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item) #listStr = liStr + item 이었는데 이 item을 바뀌도록 한 것임
# print(listStr)

# #쿼리스트링
# form = cgi.FieldStorage()
# if 'id' in form:
#     pageId = form["id"].value
#     description = open('data/'+pageId, 'r').read()
# else:
#     pageId = 'Welcome'
#     description = 'Hello, web'
# print('''<!doctype html>
# <html>
# <head>
#   <title>WEB1 - Welcome</title>
#   <meta charset="utf-8">
# </head>
# <body>
#   <h1><a href="index.py">WEB</a></h1>
#   {listStr}
#   <a href="create.py">create</a>
#   <form action="process_create.py" method="post"> 
#     <p><input type="text" name="title" placeholder="title"></p>
#     <p><textarea rows="4" name="dexcription" placeholder="description"></textarea></p>
#     <p><input type="submit"></p>
#   </form>
# </body>
# </html>
# '''.format(title=pageId, desc=description, listStr=listStr))

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
 
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="create.py">create</a>
  <form action="process_create.py" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
      <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))