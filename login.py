from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])    

login_entrar = uic.loadUi("Login.ui")  
citas_entrar = uic.loadUi("Citas.ui")



def login():
    name = login_entrar.txtuser.text()
    password = login_entrar.txtpass.text()
    if len(name)==0 or len(password) ==0 :
        print("ingrese datos")
    elif name == 'luis' and password =='luis':
        citas()
    else:
        print("datos incorrectos")

def citas():
    login_entrar.hide()
    citas_entrar.show()

def volver():
    login_entrar.show()
    citas_entrar.hide()


login()

login_entrar.Btn_login.clicked.connect(login)
citas_entrar.BtnAtras.clicked.connect(volver)



login_entrar.show() 
#citas.show()

app.exec()
