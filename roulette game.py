import pygame
import random
import math

pygame.init()
genislik,yukseklik=680,680
pencere=pygame.display.set_mode((genislik,yukseklik))
pygame.display.set_caption("Rulet Oyunu")
saat=pygame.time.Clock()
FPS=60

hesap=500
bahis=0

SARI=(240,240,0)
KIRMIZI=(240,0,0)
SİYAH=(0,0,0)
BEYAZ=(255,255,255)
YEŞİL=(0,240,0)
MAVI=(0,0,100)

buton_genislik, buton_yukseklik=120,30
buton_x, buton_y=(70,560)
buton2_x, buton2_y=(280,560)
buton3_x, buton3_y=(490,560)

buton1_renk=(200,0,0)
buton2_renk=SİYAH
buton3_renk=YEŞİL

buton_font=pygame.font.SysFont("verdana",17)
buton1_metni=buton_font.render("KIRMIZI",True,BEYAZ)
buton2_metni=buton_font.render("SİYAH",True,BEYAZ)
buton3_metni=buton_font.render("YEŞİL",True,BEYAZ)

rakam_font=pygame.font.SysFont("verdana",21)
bitis_font=pygame.font.SysFont("verdana",30)
yazi_font=pygame.font.SysFont("verdana",26)

bahis_renk=None

cark_donuyor=False
donus_acisi=0
donus_hizi=0
kazanan_sayi=-1
kazanan_goster=False


def yazi_yazdir(yazi,font,renk,yuzey,x,y):
    yazi_nesnesi=font.render(yazi,True,renk)
    yazi_koordinat=yazi_nesnesi.get_rect()
    yazi_koordinat.center=(x,y)
    yuzey.blit(yazi_nesnesi,yazi_koordinat)


def cark_ciz(donus_acisi,kazanan_sayi,kazanan_goster):
    pygame.draw.circle(pencere,MAVI, (genislik//2 ,yukseklik//2-100),210)
    pygame.draw.circle(pencere,BEYAZ, (genislik//2, yukseklik//2-100),200)

    pygame.draw.line(pencere, SİYAH, (genislik//2, yukseklik//2-100-100), (genislik//2, yukseklik//2-100+100), 5)  # Dikey çizgi
    pygame.draw.line(pencere, SİYAH, (genislik//2-100, yukseklik//2-100), (genislik//2+100, yukseklik//2-100), 5)  # Yatay çizgi

    #pygame.draw.circle(pencere,SİYAH, (genislik//2, yukseklik//2-100),20)

    for i in range(37):
        aci=math.radians(i* (360/37)+donus_acisi)
        x=genislik//2 + 188*math.cos(aci)
        y=(yukseklik//2-100) + 188*math.sin(aci)
        if i==0:
            renk=YEŞİL
        else:
            renk=KIRMIZI if i%2==0 else SİYAH

        if kazanan_goster and i==kazanan_sayi:
            pygame.draw.circle(pencere,SARI,(int(x),int(y)), 30)  

        pygame.draw.circle(pencere, renk, (int(x),int(y)), 21) 
        yazi_yazdir(str(i), rakam_font, BEYAZ, pencere, int(x),int(y))


durum=True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum=False

        if etkinlik.type==pygame.KEYDOWN:
            if etkinlik.key==pygame.K_SPACE:
                bahis+=100    

        elif etkinlik.type==pygame.MOUSEBUTTONDOWN:
            fare_x, fare_y = etkinlik.pos
            if buton_x <= fare_x <= buton_x + buton_genislik and buton_y <= fare_y <= buton_y + buton_yukseklik and not cark_donuyor:
                cark_donuyor=True
                donus_hizi=10
                kazanan_sayi=random.randint(0,36)
                kazanan_goster=False
                bahis_renk="KIRMIZI"
                

            if buton2_x <= fare_x <= buton2_x + buton_genislik and buton2_y <= fare_y <= buton2_y + buton_yukseklik and not cark_donuyor:
                cark_donuyor=True
                donus_hizi=10
                kazanan_sayi=random.randint(0,36)
                kazanan_goster=False
                bahis_renk="SİYAH"
                

            if buton3_x <= fare_x <= buton3_x + buton_genislik and buton3_y <= fare_y <= buton3_y + buton_yukseklik and not cark_donuyor:
                cark_donuyor=True
                donus_hizi=10
                kazanan_sayi=random.randint(0,36)
                kazanan_goster=False
                bahis_renk="YESİL"
                

    if cark_donuyor:
        donus_acisi+=donus_hizi
        donus_hizi*=0.99
        if donus_hizi<0.8:
            kazanan_goster=True
        if donus_hizi<0.1:
            cark_donuyor=False 
            if bahis_renk:
                if kazanan_sayi==0 and bahis_renk=="YESİL":
                    hesap+=bahis*36
                elif kazanan_sayi%2==0 and bahis_renk=="KIRMIZI":
                    hesap+=bahis
                elif kazanan_sayi%2==1 and bahis_renk=="SİYAH":
                    hesap+=bahis
                else:
                    hesap-=bahis   
            bahis=0            
    
    
    pencere.fill((0,110,0))
    cark_ciz(donus_acisi,kazanan_sayi,kazanan_goster)

    pygame.draw.rect(pencere, buton1_renk, (buton_x, buton_y, buton_genislik, buton_yukseklik))
    pencere.blit(buton1_metni, (buton_x + (buton_genislik - buton1_metni.get_width()) // 2, buton_y + (buton_yukseklik - buton1_metni.get_height()) // 2))
    pygame.draw.rect(pencere, buton2_renk, (buton2_x, buton2_y, buton_genislik, buton_yukseklik))
    pencere.blit(buton2_metni, (buton2_x + (buton_genislik - buton2_metni.get_width()) // 2, buton2_y + (buton_yukseklik - buton2_metni.get_height())//2))
    pygame.draw.rect(pencere, buton3_renk, (buton3_x, buton3_y, buton_genislik, buton_yukseklik))
    pencere.blit(buton3_metni, (buton3_x + (buton_genislik - buton3_metni.get_width()) // 2, buton3_y + (buton_yukseklik - buton3_metni.get_height())//2))

    hesap_yazi=yazi_font.render(f"Hesap: ${hesap}",True, SİYAH)
    bahis_yazi=yazi_font.render(f"Bahis: ${bahis}",True,SİYAH)
    pencere.blit(hesap_yazi,(250,470))
    pencere.blit(bahis_yazi,(250,500))

    if not cark_donuyor and kazanan_sayi!=-1:
        yazi_yazdir(f"Kazanan Sayı: {kazanan_sayi}",bitis_font, BEYAZ, pencere, genislik//2, 625)

    pygame.display.update()
    saat.tick(FPS)

pygame.quit()            