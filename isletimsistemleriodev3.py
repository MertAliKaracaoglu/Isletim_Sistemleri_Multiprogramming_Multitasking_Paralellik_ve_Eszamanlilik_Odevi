from multiprocessing import Process
import threading
import time

def kare_hesapla(sayi):
    print(f"Hesaplaniyor (Thread/Process ID: {threading.get_ident()}): {sayi} = {sayi * sayi}")
    time.sleep(1)

def coklu_programlama():
    sayilar = [1,2,3,4,5]
    print ("Coklu programlama başladi (Thread)") 

    threads = []
    
    for sayi in sayilar:
        t = threading.Thread(target = kare_hesapla, args = (sayi, ))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
        print("\nCoklu programlama tamamlandi")    


def coklu_islemci():
    sayilar = [1,2,3,4,5]
    print("\nCoklu islemci basladi (Process)\n" )
    processes = []
    for sayi in sayilar:
        p = Process(target = kare_hesapla, args = (sayi,)) 
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
        print("\nCoklu islemci tamamlandi")

    
if __name__ == "__main__":
    coklu_programlama()
    coklu_islemci()

