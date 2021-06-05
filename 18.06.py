import play
import pygame
from random import randint
#книга
i=0
a=0
#тюрьма
b=0
f=0
#БАРОН
u=0
m=0

h=0
q=0


BACKGROUND1=play.new_image(image='MakingMap4.png',x=0,y=0,angle=0,size=125)






CHUSE=play.new_image(image='planka.png',x=0,y=0,angle=0,size=325)

CHUSE2=play.new_image(image='planka.png',x=0,y=0,angle=0,size=325)
 

CTRELKA_right=play.new_image(image='mjyutffadfafh.png',x=175,y=100,angle=0,size=225)
CTRELKA_left=play.new_image(image='mgfsteqwefhy.png',x=40,y=100,angle=0,size=225)


text=play.new_text(words = 'Выберите своего персонажа', x= 0, y=-225)
text2=play.new_text(words = '1/2', x= 100, y=100)
text3=play.new_text(words = '2/2', x= 100, y=100)

GG=play.new_image(image='king 4.png',x=-150,y=100,angle=0,size=60)
GG_CHOSE=play.new_image(image='king 4.png',x=-105,y=-25,angle=0,size=100)

GG2=play.new_image(image='king 5.png',x=-150,y=100,angle=0,size=60)
GG2_CHOSE=play.new_image(image='king 5.png',x=100,y=-25,angle=0,size=125)

GG3=play.new_image(image='king 7.png',x=-150,y=100,angle=0,size=40)
GG3_CHOSE=play.new_image(image='king 7.png',x=-105,y=-25,angle=0,size=100)

GG4=play.new_image(image='king 6.png',x=-150,y=100,angle=0,size=90)
GG4_CHOSE=play.new_image(image='king 6.png',x=100,y=-20,angle=0,size=165)


KNOPKA1=play.new_image(image='uifdfg.png',x=-340,y=170,angle=0,size=450)
KNOPKA2=play.new_image(image='adsdvjytfdjhb.png',x=-340,y=100,angle=0,size=425)
KNIGA=play.new_image(image='fidjtyhd.png',x=0,y=0,angle=0,size=325)

STOP1=play.new_image(image='yudmtdumytumdyrttr.png',x=200,y=200,angle=0,size=425)


CTROIT1=play.new_image(image='jhfdu;stelxfgy.png',x=-115,y=-140,angle=0,size=700)
NE_CTROIT1=play.new_image(image='irgygfhfdryj.png',x=100,y=-140,angle=0,size=700)
HORSE1=play.new_image(image='lksshuys.png',x=0,y=100,angle=0,size=235)

CASTLE1=play.new_image(image='lrhgsykytnsrfy.png',x=0,y=25,angle=0,size=235)
HOME1=play.new_image(image='hfrgjhgeyh.png',x=0,y=50,angle=0,size=235)

PLASHA=play.new_image(image='bgyrldbh.png',x=0,y=65,angle=0,size=235)
STRELU=play.new_image(image='hgjuebguhwnujg.png',x=0,y=65,angle=0,size=235)

DOCUMENT=play.new_image(image='mjyfbgrsght.png',x=0,y=25,angle=0,size=550)

VISILICA=play.new_image(image='[]poiuyyt.png',x=-150,y=-25,angle=0,size=525)

SHEA=play.new_image(image='jtfbsaqdgjnbght.png',x=-40,y=-25,angle=0,size=340)

POCADIT=play.new_image(image='gbdyenhl.png',x=60,y=-25,angle=0,size=525)

STOP2=play.new_image(image='yudmtdumytumdyrttr.png',x=220,y=150,angle=0,size=425)

SVOBODA=play.new_image(image='nfbhtudwsvjht.png',x=165,y=-25,angle=0,size=825)

CHURSE=play.new_image(image='kffgjkjtysufu.png',x=20,y=35,angle=0,size=235)

VERA1=play.new_image(image='nbvygfhlhi.png',x=175,y=90,angle=0,size=120)
VERA2=play.new_image(image='kfegnbdtyjdsgjh.png',x=170,y=90,angle=0,size=120)
VERA3=play.new_image(image='jkcfdhifubvrfh.png',x=160,y=90,angle=0,size=120)
VERA4=play.new_image(image='xghgubghfbfj.png',x=175,y=87,angle=0,size=120)


BARON1=play.new_image(image='KATLAS.png',x=90,y=85,angle=0,size=55)
BARON2=play.new_image(image='MITIC.png',x=90,y=90,angle=0,size=60)
BARON3=play.new_image(image='SMELL.png',x=90,y=85,angle=0,size=55)
BARON4=play.new_image(image='KARLOK.png',x=90,y=90,angle=0,size=50)



MEN1=play.new_image(image='men.png',x=-120,y=87,angle=0,size=50)
MEN2=play.new_image(image='men 1.png',x=-120,y=85,angle=0,size=50)
MEN3=play.new_image(image='men 3.png',x=-120,y=85,angle=0,size=45)
MEN6=play.new_image(image='men 6.png',x=-120,y=85,angle=0,size=50)
MEN7=play.new_image(image='men 7.png',x=-120,y=85,angle=0,size=45)
MEN8=play.new_image(image='men 2.png',x=-120,y=85,angle=0,size=45)
MEN9=play.new_image(image='men 4 (2).png',x=-120,y=85,angle=0,size=55)







BARON1.hide()
BARON2.hide()
BARON3.hide()
BARON4.hide()

CTRELKA_left.hide()


MEN1.hide()
MEN2.hide()
MEN3.hide()
MEN6.hide()
MEN7.hide()
MEN8.hide()
MEN9.hide()

text3.hide()
CHUSE2.hide()

GG.hide()
GG2.hide()
GG3.hide()
GG3_CHOSE.hide()
GG4.hide()
GG4_CHOSE.hide()
VERA1.hide()
VERA2.hide()
VERA3.hide()
VERA4.hide()



STOP2.hide()
STRELU.hide()
PLASHA.hide()
HORSE1.hide()
HOME1.hide()



KNOPKA1.hide()
KNOPKA2.hide()

KNIGA.hide()

CASTLE1.hide()
CHURSE.hide()

STOP1.hide()


CTROIT1.hide()
NE_CTROIT1.hide()

DOCUMENT.hide()
VISILICA.hide()
SHEA.hide()
POCADIT.hide()
SVOBODA.hide()

@play.when_program_starts
def start():
    pygame.mixer_music.load('Город-ОрденПорядка (online-audio-converter.com).mp3')
    pygame.mixer_music.play()
    



@KNOPKA1.when_clicked
async def click3():
    
    pygame.mixer_music.load('LICT.mp3')
    pygame.mixer_music.play()
    await play.timer(seconds=1)
    pygame.mixer_music.load('Город-ОрденПорядка (online-audio-converter.com).mp3')
    pygame.mixer_music.play()
    KNIGA.show()
    STOP1.show()
    CTROIT1.show()
    NE_CTROIT1.show()
    a=i+randint(1,6)
    if a==1:
        CASTLE1.show()
    if a==2:
        HOME1.show()
    if a==3:
        HORSE1.show()
    if a==4:
        PLASHA.show()
    if a==5:
        STRELU.show()
    if a==6:
        CHURSE.show()


@STOP1.when_clicked
def click4():
    KNIGA.hide()
    STOP1.hide()
    CTROIT1.hide()
    NE_CTROIT1.hide()
    CASTLE1.hide()
    HOME1.hide()
    HORSE1.hide()
    PLASHA.hide()
    STRELU.hide()
    CHURSE.hide()


@CTROIT1.when_clicked
def click5():
    CTROIT1.hide()
    NE_CTROIT1.hide()
    CASTLE1.hide()
    HOME1.hide()
    HORSE1.hide()
    PLASHA.hide()
    STRELU.hide()
    CHURSE.hide()
    KNIGA.hide()
    STOP1.hide()



@NE_CTROIT1.when_clicked
def ckick6():
    CTROIT1.hide()
    NE_CTROIT1.hide()
    HOME1.hide()
    CASTLE1.hide()
    HORSE1.hide()
    PLASHA.hide()
    STRELU.hide()
    CHURSE.hide()
    KNIGA.hide()
    STOP1.hide()



#тюрьма
@KNOPKA2.when_clicked
def ckick7():
    DOCUMENT.show()
    VISILICA.show()
    STOP2.show()
    SHEA.show()
    POCADIT.show()
    SVOBODA.show()
    b=f+randint(1,4)
    if b==1:
        VERA1.show()
    if b==2:
        VERA2.show()
    if b==3:
        VERA3.show()
    if b==4:
        VERA4.show()
    #баронства
    u=m+randint(1,4)
    if u==1:
        BARON1.show()
    if u==2:
        BARON2.show()
    if u==3:
        BARON3.show()
    if u==4:
        BARON4.show()
    h=q+randint(1,9)
    if h==1:
        MEN1.show()
    if h==2:
        MEN2.show()
    if h==3:
        MEN3.show()
    if h==4:
        MEN6.show()
    if h==5:
        MEN7.show()
    if h==6:
        MEN8.show()
    if h==7:
        MEN9.show()


@STOP2.when_clicked
def ckick8():
    DOCUMENT.hide()
    VISILICA.hide()
    STOP2.hide()
    SHEA.hide()
    POCADIT.hide()
    SVOBODA.hide()
    VERA1.hide()
    VERA2.hide()
    VERA3.hide()
    VERA4.hide()
    BARON1.hide()
    BARON2.hide()
    BARON3.hide()
    BARON4.hide()

@VISILICA.when_clicked
def click9():
    DOCUMENT.hide()
    VISILICA.hide()
    SHEA.hide()
    POCADIT.hide()
    SVOBODA.hide()
    STOP2.hide()
    VERA1.hide()
    VERA2.hide()
    VERA3.hide()
    VERA4.hide()
    BARON1.hide()
    BARON2.hide()
    BARON3.hide()
    BARON4.hide()



@SHEA.when_clicked
def click10():
    DOCUMENT.hide()
    VISILICA.hide()
    SHEA.hide()
    POCADIT.hide()
    SVOBODA.hide()
    STOP2.hide()
    VERA1.hide()
    VERA2.hide()
    VERA3.hide()
    VERA4.hide()
    BARON1.hide()
    BARON2.hide()
    BARON3.hide()
    BARON4.hide()

@POCADIT.when_clicked
def click11():
    DOCUMENT.hide()
    VISILICA.hide()
    SHEA.hide()
    POCADIT.hide()
    SVOBODA.hide()
    STOP2.hide()
    VERA1.hide()
    VERA2.hide()
    VERA3.hide()
    VERA4.hide()
    BARON1.hide()
    BARON2.hide()
    BARON3.hide()
    BARON4.hide()



@SVOBODA.when_clicked
def click12():
    DOCUMENT.hide()
    VISILICA.hide()
    SHEA.hide()
    POCADIT.hide()
    SVOBODA.hide()
    STOP2.hide()
    VERA1.hide()
    VERA2.hide()
    VERA3.hide()
    VERA4.hide()
    BARON1.hide()
    BARON2.hide()
    BARON3.hide()
    BARON4.hide()




@GG_CHOSE.when_clicked
def click13():
    GG.show()
    CHUSE.hide()
    text.hide()
    GG_CHOSE.hide()
    GG2_CHOSE.hide()
    KNOPKA1.show()
    KNOPKA2.show()
    CTRELKA_right.hide()
    CTRELKA_left.hide()
    text2.hide()
    text3.hide()


@GG2_CHOSE.when_clicked
def click14():
    GG2.show()
    CHUSE.hide()
    text.hide()
    GG_CHOSE.hide()
    GG2_CHOSE.hide()
    KNOPKA1.show()
    KNOPKA2.show()
    CTRELKA_right.hide()
    CTRELKA_left.hide()
    text2.hide()
    text3.hide()

@CTRELKA_right.when_clicked
def click15():
    
    CHUSE.hide()
    CHUSE2.show()
    GG_CHOSE.hide()
    GG2_CHOSE.hide()
    text2.hide()
    text3.show()
    CTRELKA_left.show()
    GG3_CHOSE.show()
    GG4_CHOSE.show()

@CTRELKA_left.when_clicked
def click16():
    
    CHUSE.show()
    CHUSE2.hide()
    GG_CHOSE.show()
    GG2_CHOSE.show()
    text2.show()
    text3.hide()
    CTRELKA_left.hide()
    GG3_CHOSE.hide()
    GG4_CHOSE.hide()




@GG3_CHOSE.when_clicked
def click17():
    GG3.show()
    CHUSE.hide()
    CHUSE2.hide()
    GG_CHOSE.hide()
    GG2_CHOSE.hide()
    text.hide()
    text2.hide()
    text3.hide()
    CTRELKA_left.hide()
    GG3_CHOSE.hide()
    CTRELKA_right.hide()
    KNOPKA1.show()
    KNOPKA2.show()
    GG4_CHOSE.hide()

@GG4_CHOSE.when_clicked
def click17():
    
    text.hide()
    GG4.show()
    GG3.hide()
    CHUSE.hide()
    CHUSE2.hide()
    GG_CHOSE.hide()
    GG2_CHOSE.hide()
    text.hide()
    text2.hide()
    text3.hide()
    CTRELKA_left.hide()
    GG3_CHOSE.hide()
    GG4_CHOSE.hide()
    CTRELKA_right.hide()
    KNOPKA1.show()
    KNOPKA2.show()











play.start_program()