import pyxel


global x
global y
x,y=45,31

def sol():
    for  i in range(16):
        pyxel.blt(16*i,55,0,0,64,16,32,0)
        
        
        
        
def cloud():
    for i in range(16):
            pyxel.blt(16*i,1,0,0,128,49,128,128)
            
def realcloud():
    for i in range(16):
            pyxel.blt(16*i,1,0,0,33,113,128,128)



    

class App:
    def __init__(self):
        #initialisation de la fenetre : dimensions 160*80 et titre
        pyxel.init(160, 80, title="Mon premeir jeu Pyxel")
        #chargement des medias (dessins ,musiques ,sons)
        pyxel.load("media.pyxres")
        #les methodes update() et draw() sont executees en boucle
        #30 fois par secondes
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            #on quitte si la touche Q (Qwerty) est pressee
            pyxel.quit()
        global x,y
        if pyxel.btn(pyxel.KEY_RIGHT):
            x=x+2
        elif pyxel.btn(pyxel.KEY_LEFT):
            x=x-2

        elif pyxel.btn(pyxel.KEY_DOWN) and pyxel.pget(x+8,y+24)!=11:
            y=y+2
    
    def draw(self):
        pyxel.cls(0)
        #affiche le texte avec la couleur 2 au point (55,41)
        #affiche le texte avec la couleur 2 au point (55,41)
        realcloud()
        cloud()
        sol()
        pyxel.blt(x,y,0,0,29,32,26,7)
    
    
       
App()

