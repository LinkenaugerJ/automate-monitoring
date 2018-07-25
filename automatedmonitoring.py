import webbrowser
>>> url = 'https://app.asana.com/0/626145799413828/board'
>>> chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
>>> webbrowser.get(chrome_path).open(url)

