"""Creates a simple HTML page"""


import webbrowser


class HTMLpage():
    
    def __init__(self):
        self.title = ""
        self.text = ""
        self.image = ""
        self.author = ""
        self.path = ""
        
        
    def create(self):
        f = open(self.path, "w")
        content = """
<!DOCTYPE HTML>
        <HTML>
        <HEAD>
           <META charset="UTF-8">
           <META name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
           <LINK rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
           <TITLE>{t}</TITLE>
        </HEAD>
        <BODY>
           <DIV class = "container">
              <DIV class="page-header text-center"><H1>{t}</H1></DIV>
              <DIV class="jumbotron text-center">
                  <P>{b}</P>
                  <P><FOOTER>{a}</FOOTER></P>
                  <P><IMG src={i} class="img-circle" alt=""></P>
              </DIV>              
           </DIV>
        </BODY>
        </HTML>
        """.format(t = self.title, b = self.text, a = self.author, i = self.image)
        f.write(content)
        f.close()
        
        
a = HTMLpage()
a.title = "Kocie motto"
a.text = "Jeśli zobaczysz kogoś, kto odpoczywa, pomóż mu."
a.author = "Każdy kot na świecie"
a.path = "index.html"
a.image = "cat.jpg"
a.create()
webbrowser.open(a.path)
