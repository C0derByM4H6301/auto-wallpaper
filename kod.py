import ctypes
import time

# Fotoğrafların yolunu ve dosya adlarını diziye alın
photos = ["Fotos/1.jpg"]

# Sonsuz bir döngü kurun
while True:
  # Fotoğrafları dizi içinde döngü kurarak her bir fotoğraf için aşağıdaki işlemleri gerçekleştirin
  for photo in photos:
    # Fotoğraf dosyasını duvar kağıdı olarak ayarlayın
    ctypes.windll.user32.SystemParametersInfoW(20, 0, photo, 0)
    
    # 1 dakika bekleyin
    time.sleep(5)
