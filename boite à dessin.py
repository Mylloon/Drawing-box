from tkinter import *
from tkinter.messagebox import *
from random import *
import tkinter

pack=1
forme=1
recommencer=False
nolag=0

def draw():
    global forme
    global nolag
    if forme==1:
        if recommencer==True:
            fenetre.after(100, draw)
        if nolag >= 200:
            cleanboard()
            nolag=0
        nolag=nolag+1
        if curselect=="800x600":
            return canvas.create_line((randint(0,800),randint(0,800),randint(0,800),randint(0,800)),fill=couleur())
        elif curselect=="1280x720":
            return canvas.create_line((randint(0,1280),randint(0,1280),randint(0,1280),randint(0,1280)),fill=couleur())
        elif curselect=="1920x1080":
            return canvas.create_line((randint(0,1920),randint(0,1920),randint(0,1920),randint(0,1920)),fill=couleur())
            
    elif forme==2:
        if recommencer==True:
            fenetre.after(100, draw)
        if nolag >= 200:
            cleanboard()
            nolag=0
        nolag=nolag+1
        if curselect=="800x600":
            return canvas.create_polygon(randint(0,800),randint(0,800),randint(0,800),randint(0,800),randint(0,800),randint(0,800),fill=couleur())
        elif curselect=="1280x720":
            return canvas.create_polygon(randint(0,1280),randint(0,1280),randint(0,1280),randint(0,1280),randint(0,1280),randint(0,1280),fill=couleur())
        elif curselect=="1920x1080":
            return canvas.create_polygon(randint(0,1920),randint(0,1920),randint(0,1920),randint(0,1920),randint(0,1920),randint(0,1920),fill=couleur())

def kill():
    return fenetre.destroy()

def couleur():
    global pack
    COULEURS=['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace', 'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff', 'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray', 'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue', 'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue', 'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue', 'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise', 'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green', 'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green', 'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green', 'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow', 'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown', 'indian red', 'saddle brown', 'sandy brown', 'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange', 'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink', 'pale violet red', 'maroon', 'medium violet red', 'violet red', 'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple', 'thistle', 'snow2', 'snow3', 'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3', 'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4', 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3', 'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4', 'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4', 'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2', 'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1', 'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2', 'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1', 'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4', 'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
    COULEURS_FONCES=['gray', 'black', 'blue']
    COULEURS_CLAIRES=['pink', 'red', 'yellow']
    if pack==1:
        return choice(COULEURS)
    elif pack==2:
        return choice(COULEURS_FONCES)
    elif pack==3:
        return choice(COULEURS_CLAIRES)

def cleanboard():
    global canvas
    canvas.delete()
    if curselect=="800x600":
        canvas=Canvas(fenetre,width=780,height=550,bg="#DDDDDD")
    elif curselect=="1280x720":
        canvas=Canvas(fenetre,width=1260,height=670,bg="#DDDDDD")
    elif curselect=="1920x1080":
        canvas=Canvas(fenetre,width=1900,height=1030,bg="#DDDDDD")
    canvas.place(x=8,y=40)

def pack1():
    global pack
    cleanboard()
    pack=1
    showinfo("Changement de pack","Tu as maintenant le pack par defaut !")

def pack2():
    global pack
    cleanboard()
    pack=2
    showinfo("Changement de pack","Tu as maintenant le pack 2 !")

def pack3():
    global pack
    cleanboard()
    pack=3
    showinfo("Changement de pack","Tu as maintenant le pack 3 !")

def nextcolor():
    global pack
    if pack==1:
        pack2()
    elif pack==2:
        pack3()
    elif pack==3:
        pack1()

def forme1():
    global forme
    cleanboard()
    forme=1
    showinfo("Changement de formes","Tu dessines maintenant des lignes !")
    
def forme2():
    global forme
    cleanboard()
    forme=2
    showinfo("Changement de formes","Tu dessines maintenant des figures !")
    
def nextforme():
    global forme
    if forme==1:
        forme2()
    elif forme==2:
        forme1()

def timeron():
	global buttforme
	global buttdraw
	global recommencer
	recommencer=True
	buttforme.destroy()
	buttforme=Button(fenetre, text="Stop auto", command=timeroff, bg="red")
	buttforme.place(x=700,y=5)
	buttdraw.destroy()
	buttdraw=Button(fenetre, text="Accélérer dessins !", command=draw, bg="lawn green")
	buttdraw.place(x=220,y=5)
	draw()

def timeroff():
	global buttforme
	global buttdraw
	global recommencer
	buttforme.destroy()
	buttforme=Button(fenetre, text="Dessin auto", command=timeron)
	buttforme.place(x=700,y=5)
	buttdraw.destroy()
	buttdraw=Button(fenetre, text="Dessiner !", command=draw)
	buttdraw.place(x=220,y=5)
	recommencer=False

def fenetredessin():
    global canvas
    global buttdraw
    global fenetre
    global buttforme    
    accueil.destroy()
    fenetre=Tk()
    fenetre.geometry(curselect)
    if curselect=="1920x1080":
        fenetre.attributes('-fullscreen', 1)
    fenetre.title("Dessin à gogo")
    fenetre.resizable(False,False)

    buttclean=Button(fenetre, text="Nettoyer le board !", command=cleanboard)
    buttclean.place(x=50,y=5)

    buttdraw=Button(fenetre, text="Dessiner !", command=draw)
    buttdraw.place(x=220,y=5)

    buttcolor=Button(fenetre, text="Changer de couleur", command=nextcolor)
    buttcolor.place(x=350,y=5)

    buttforme=Button(fenetre, text="Changer de forme", command=nextforme)
    buttforme.place(x=550,y=5)


    buttforme=Button(fenetre, text="Dessin auto", command=timeron)
    buttforme.place(x=700,y=5)

    if curselect=="800x600":
        canvas=Canvas(fenetre,width=780,height=550,bg="#DDDDDD")
    elif curselect=="1280x720":
        canvas=Canvas(fenetre,width=1260,height=670,bg="#DDDDDD")
    elif curselect=="1920x1080":
        canvas=Canvas(fenetre,width=1900,height=1030,bg="#DDDDDD")
    canvas.place(x=8,y=40)

    menubar=Menu(fenetre)

    menu1=Menu(menubar,tearoff=0)
    menu1.add_command(label="Pack 1 (par defaut)",command=pack1)
    menu1.add_command(label="Pack 2",command=pack2)
    menu1.add_command(label="Pack 3",command=pack3)
    #menu1.add_command(label="Prochaine couleur",command=nextcolor)
    menubar.add_cascade(label="Couleurs",menu=menu1)

    menu2=Menu(menubar,tearoff=0)
    menu2.add_command(label="Nettoyer le board",command=cleanboard)
    menubar.add_cascade(label="Nettoyer le board",menu=menu2)

    menu3=Menu(menubar,tearoff=0)
    menu3.add_command(label="Dessiner des lignes (par defaut)",command=forme1)
    menu3.add_command(label="Dessiner des figures",command=forme2)
    #menu3.add_command(label="Prochaine formes",command=nextforme)
    menubar.add_cascade(label="Formes",menu=menu3)

    menu4=Menu(menubar,tearoff=0)
    menu4.add_command(label="Retour accueil",command=accueilback)
    menu4.add_command(label="Quitter",command=kill)
    menubar.add_cascade(label="Quitter",menu=menu4)

    fenetre.config(menu=menubar)

    fenetre.mainloop()

def accueilback():
    global accueil
    global pack
    global forme
    del(accueil)
    savereglages=askquestion("Sauvegarder paramètres","Voulez vous garder les paramètres sélectionné ?",icon='warning')
    if savereglages=="yes":
        fenetre.destroy()
        debaccueil()
    else:
        fenetre.destroy()
        pack=1
        forme=1
        debaccueil()

def lancement():
    global curselect
    curselect=selectresolution.get(selectresolution.curselection())
    
    if curselect=="S-VGA : 800*600":
        curselect="800x600"
    elif curselect=="HD : 1280*720":
        curselect="1280x720"
    elif curselect=="FS : FullScreen":
        curselect="1920x1080"
        
    fenetredessin()

def debaccueil():
    global selectresolution
    global accueil
    accueil=Tk()
    accueil.geometry("210x105")
    accueil.title("Accueil")
    accueil.resizable(False,False)

    resolution=Label(accueil, text='Résolutions : ')
    resolution.place(x=5,y=5)

    selectresolution=Listbox(accueil,height ='3')
    selectresolution.insert(0, "S-VGA : 800*600")
    selectresolution.insert(1, "HD : 1280*720")
    selectresolution.insert(2, "FS : FullScreen")
    selectresolution.select_set(0)
    selectresolution.place(x=78,y=5)

    start=Button(accueil, text = 'Lancer le programme', command=lancement)
    start.place(x=50,y=67)
     
    accueil.mainloop()

debaccueil()
