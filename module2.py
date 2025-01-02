import module1 as m1
urunler=m1.urunler

def urunEkle(a,b):
    urunler.append((a,b))
    
def urunGuncelle(c,d,e):
    urunler[c]=(d,e)
    
def urunleriGetir():
    for x in urunler:
        print(x)
        

