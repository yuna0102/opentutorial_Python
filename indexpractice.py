#!C:\Users\choiy\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
if 'id' in form: #form안에 id값이 있냐?를 물어보는 것
    pageId = form["id"].value #form이라는 변수 안에 id값이라는 데이터가 세팅되어 있음
    description = open('data/'+pageId, 'r').read() #html에서 파일 불러오는 함수 open("workfile", 'w')
else:
    pageId = 'Welcome'
    description = 'Hello, web' #id값이 없을 때 description이라는 변수명이 hello world가 됨

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#Bad Header 오류 뜰 때, 문자를 가져오는 형식이 어떤 지를 선언해줘야함.
print('''<!doctype html>
    <html>
        <head>
            <!-- 웹페이지의 제목 -->
            <title>WEB1 - html</title> 
            <!-- #utf-8이라는 방식으로 저장되어 있다     -->
            <meta charset="utf-8"> 
        </head>
        
        <body>
            <h1><a href="index.py">WEB</a></h1>
            <ol>
                #우리는 id값이 HTML인 웹페이지를 질의합니다. =Query string
                <li><a href="index.py?id=HTML">HTML</a></li>
                <li><a href="index.py?id=CSS">CSS</a></li>
                <li><a href="index.py?id=JavaScript">JavaScript</a></li>
            </ol>
            <ul>
                <li>yuna</li>
                <li>CAU business administration</li>
                <li>@bliiingxa_0102</li>
            </ul>
            
            <h2>{title}</h2>
            <p>{desc}</p>
            <h3><a href="https://opentutorials.org/course/3084/18418" target="_blank" title="html5 specification">HTML</a>이란 무엇인가?</h3>
            <p><h2>Today, I'm going to study html tags.</h2> so I can describe that I want to express my feeling 
                when I learn about it. I learned django web already. But my programming knowledges are unorganized.
                Then, I want to organize things doing this <strong><u>html</u> and markdown</strong>. leggo.</p>
            <p>
                <h3>기본 텍스트 태그</h3>
            1. We learn <strong>strong </strong>tag.<br>
            2. We learn <u>underline</u> tag.<br>
            3. We learn h1 to h6 tag.<br>
            4. We learn new line tag.<br>
            5. We learn paragraph tag.<br>
            </p>
            <p>
                <h3>2대 부모자식 태그</h3>
                6. We learn line tag. 이 태그는 '목차'를 나타낼 때 쓰인다. li 태그는 반드시 부모 태그를 갖고 있다. 어디서부터 어디까지가
                관련된 것인지 알아야 하기 때문.<br>
                7. We learn ul(unordered list) tag. It's a parent tag of li tag<br>
                8. We learn ol(ordered list) tag. It's automatical numbering. 1번 항목 지우면 2번이 자동으로 1번 됨.
            </p>
            <p style="margin-top:40px;">앞에 있는 태그는 '열리는 태그' 뒤에 있는 태그는 '닫히는 태그'<br>
                we already know 8 tags. Usually, one website use 25~30 tags.<br>
                margin tag는 tag와 tag 사이의 여백을 의미한다. 이는 css적인 요소이므로 지금 이해할 필요는 없다.</p>
            <p>
                <h2>고위 태그</h2>
                <ol>
                    <li>head 태그</li>
                    <li>body 태그</li>
                    <li>a 태그 : html의 제왕!<br>>>href는 링크로 이동하는 속성, target="_blank"는 새탭으로 여는 것</li>
                </ol>
            </p>
        </body>
    </html>
'''.format(title=pageId, desc=description))