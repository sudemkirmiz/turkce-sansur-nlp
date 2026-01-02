import spacy
import os
from TurkishStemmer import TurkishStemmer

# Spacy: Kelimeleri ayırmak için (Tokenization)
try:
    nlp = spacy.blank("tr")
except:
    nlp = spacy.blank("xx")

# Stemmer: Kelime kökü bulmak için
stemmer = TurkishStemmer()

# Dosya Yolları
KLASOR = os.path.dirname(os.path.abspath(__file__))
BLACKLIST_PATH = os.path.join(KLASOR, "yasakli_kelimeler.txt")

def load_blacklist(path):
    """Yasaklı kelimeleri dosyadan okur ve bir küme (set) olarak döndürür."""
    words = set()
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip().startswith("#"): continue # Yorum satırlarını atla
                w = line.strip().lower()
                if w:
                    words.add(w)
    else:
        print("UYARI: yasakli_kelimeler.txt bulunamadı!")
    return words

# Listeyi hafızaya yükle
yasaklar = load_blacklist(BLACKLIST_PATH)

def is_toxic(token):
    """Bir kelimenin yasaklı olup olmadığını 3 aşamada kontrol eder."""
    kelime_ham = token.text.lower()
    
    # 1. Aşama: Birebir eşleşme (Hızlı kontrol)
    if kelime_ham in yasaklar:
        return True
    
    # 2. Aşama: Noktalı sansürden kaçma kontrolü
    kelime_noktasiz = kelime_ham.replace(".", "")
    if kelime_noktasiz in yasaklar and len(kelime_noktasiz) > 1:
        return True

    # 3. Aşama: Stemming (Kök bulma)
    kelime_kok = stemmer.stem(kelime_ham)
    if kelime_kok in yasaklar:
        # HATA ÖNLEYİCİ: Kök "normal" gibi masum bir kelimeyle çakışmasın.
        # Örn: "analiz" kelimesinin kökü "anal" çıkabilir (hatalı stemmer durumunda).
        # Kısa kelimelerde (3 harften az) kök kontrolünü sadece belli kelimeler için yap.
        if len(kelime_kok) < 3 and kelime_kok not in ["aq", "oç", "am", "sik"]:
            return False 
        return True

    return False

def censor(metin):
    """Metni alır, yasaklı kelimeleri yıldızlar ve geri döndürür."""
    doc = nlp(metin) #düz split() fonksiyonu sadece boşluktan ayırır. spaCy ise noktalama işaretlerini, virgülleri de ayırır.
    yeni_metin = []
    
    for t in doc:
        if is_toxic(t):
            # Kelime uzunluğu kadar yıldız koy, boşlukları koru
            yeni_metin.append("*" * len(t.text) + t.whitespace_)
        else:
            yeni_metin.append(t.text_with_ws)
            
    return "".join(yeni_metin)

# --- 4. ÇALIŞTIRMA ---
if __name__ == "__main__":
    print("="*50)
    print(f"SANSÜR SİSTEMİ")
    print(f"Veritabanı: {len(yasaklar)} kelime yüklendi")
    print("="*50)
    
    while True:
        try:
            sarki = input("\n🎵 Şarkı sözü gir (Çıkış için 'q'): ")
        except KeyboardInterrupt:
            break

        if sarki.lower() in ["q", "exit", "kapat"]:
            print("Sistem kapatılıyor...")
            break
        
        if not sarki.strip():
            continue
            
        sonuc = censor(sarki)
        print(f" SONUÇ: {sonuc}")