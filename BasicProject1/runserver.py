"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
#第一個部分是 Flask 的 import 陳述式，此陳述式會建立 Flask 類別的執行個體，該執行個體
#會指派給 app 變數，然後指派 wsgi_app 變數 (這在部署至 Web 主機時相當有用，但目前未使用)：
from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

#第三個部份是些許簡短程式碼，會將函式指派給 URL 路由，這意謂著函式會提供由該 URL 識別的資源。 
#您將使用 Flask 的 @app.route 裝飾項目來定義路由，此裝飾項目的引數是網站根目錄的相對 URL。 
#正如您在程式碼中所看到的，這裡的函式只會傳回文字字串，這已足以供瀏覽器呈現頁面。 
#在接下來的步驟中，您會以 HTML 呈現更豐富的頁面。

@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"


#第二個部分 (位於檔案結尾) 是些許選擇性程式碼，會以取自環境變數的特定主機和連接埠值 (預設為 localhost:5555) 啟動 Flask 開發伺服器：

if __name__ == '__main__':
    import os
    from HelloFlask import app    # Imports the code from HelloFlask/__init__.py

    if __name__ == '__main__':
        HOST = os.environ.get('SERVER_HOST', 'localhost')

        try:
            PORT = int(os.environ.get('SERVER_PORT', '5555'))
        except ValueError:
            PORT = 5555

        app.run(HOST, PORT)