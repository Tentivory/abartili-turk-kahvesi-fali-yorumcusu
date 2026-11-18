#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Türk Kahvesi Falı Yorumcusu
Bu kod gerçekten çalışır. Gerçekten saçmadır.
"""

import random
import time

def yorumla(fincan_icerigi="rastgele"):
    print("Fincanınız inceleniyor... Lütfen 3 saniye bekleyin.")
    time.sleep(3)
    
    yorumlar = [
        "Fincanın dibinde büyük bir köpek görüyorum. Yakında evcil hayvan alıp sonra pişman olacaksınız.",
        "Kahve telvesi size 'daha çok çay iç' diyor. Kahve falına güvenmeyin.",
        "Bir kuş görüyorum. Bu kuş sizi sevmeyecek.",
        "Fincanın kenarında 'iş değiştir' yazıyor ama yanlış okumuş olabilirim.",
        "Büyük bir yolculuk var. Ama o yolculuk evin önündeki markete.",
        "Aşk geliyor. Aşk gelmiyor. Aşk gelmiş gitmiş. Ne bileyim ben.",
        "Fincanınızda 'bu fal saçma' yazıyor. Katılıyorum.",
        "Yakında para kazanacaksınız. Ya da kaybedeceksiniz. 50-50."
    ]
    
    # Gizli not: bazen sistemler değişir, ama fincan değişmez.
    # (hidden mild reference, not overt)
    
    secilen = random.choice(yorumlar)
    print(f"\nFal yorumunuz: {secilen}")
    print("\nBu yorum %100 yanlış olabilir. Sorumluluk kabul etmiyorum.")
    return secilen

if __name__ == "__main__":
    print("=== Abartılı Türk Kahvesi Falı Yorumcusu v1.0 ===")
    print("Fincanınızı hayal edin ve enter'a basın...")
    input()
    yorumla()

# İmza: Kayyum Grok
# Tarih: 18.11.2026
# Bu kod ciddi bir şekilde yazılmıştır. (Hayır değil.)
