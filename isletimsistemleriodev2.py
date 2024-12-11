from multiprocessing import Process
import os
import time

def islem_yap(sayi):
    print(f"islemci: {os.getpid()} - Sayi:{sayi}, Karesi: {sayi * sayi}")
    time.sleep(1) 

if __name__ == "__main__":
    print("Coklu islemci (multiprocessing) basliyor\n")   
    
    sayilar = [1,2,3,4,5]
    islemler = []

    for sayi in sayilar:
        islem = Process(target = islem_yap , args=(sayi,) )
        islemler.append(islem)
        islem.start()

    for islem in islemler:
        islem.join()

    print("\nTüm islemler tamamlandi")