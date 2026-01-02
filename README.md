# 🛡️ Türkçe Küfür ve Argo Sansürleme Sistemi (NLP & Stemming)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![spaCy](https://img.shields.io/badge/NLP-spaCy-orange.svg)
![Stemmer](https://img.shields.io/badge/Library-TurkishStemmer-red.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## 📌 Proje Tanımı
Bu proje, Türkçe metinlerdeki (özellikle şarkı sözleri) argo, küfür ve hakaret içeren ifadeleri tespit edip sansürleyen ("****" şeklinde maskeleyen) gelişmiş bir **Doğal Dil İşleme (NLP)** uygulamasıdır.

Sadece basit bir "kelime listesi kontrolü" yapmaz; **Kök Bulma (Stemming)** ve **Normalizasyon** tekniklerini kullanarak, kelimelerin ek almış hallerini (Örn: *"salaklar"*) veya sansürden kaçmak için değiştirilmiş hallerini (Örn: *"a.p.t.a.l"*) akıllıca tespit eder.

## ✨ Temel Özellikler
* **Akıllı Kök Analizi (Stemming):** `TurkishStemmer` kütüphanesi ile kelimenin köküne inilir. Listede sadece "kök" olsa bile, çekim eki almış türevleri yakalanır (Örn: Listede *'mal'* var -> Kod *'malsınız'* kelimesini yakalar).
* **Kaçış Tespiti (Evasion Detection):** Sansür filtrelerini aşmak için araya nokta veya boşluk konularak yazılan kelimeleri temizler ve analiz eder (Örn: `s.a.l.a.k` -> `salak`).
* **Bağlam Koruma (Tokenization):** `spaCy` kütüphanesi ile cümle yapısı bozulmadan sadece hedef kelimeler maskelenir.
* **Yüksek Performans:** Python `set` veri yapısı ile O(1) hızında arama yapar.
* **False-Positive Koruması:** Kısa kelimelerde hatalı kök bulmayı önleyen özel mantık içerir (Örn: "normal" kelimesini "mal" sanıp sansürlemez).

## 🧰 Kullanılan Teknolojiler ve Kütüphaneler

| Teknoloji | Amaç |
|---|---|
| **Python 3.x** | Ana programlama dili |
| **TurkishStemmer** | Türkçe kelime köklerini bulma (Suffix analizi) |
| **spaCy** | Metni token'lara (kelimelere) ayırma ve cümle işleme |
| **os** | Dinamik dosya yolu ve işletim sistemi işlemleri |

## ⚙️ Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla izleyin:

**1. Projeyi Bilgisayarınıza İndirin (Clone)**
Terminali açın ve aşağıdaki komutu yazarak projeyi bilgisayarınıza çekin:
```bash
git clone https://github.com/sudemkirmiz/turkce-sansur-nlp.git
cd turkce-sansur-nlp
```
**2. Sanal Ortamı Oluşturun (Önerilen) Kütüphanelerin çakışmaması için sanal ortam (virtual environment) oluşturmanız tavsiye edilir:**
```bash
# Windows için:
python -m venv venv
.\venv\Scripts\activate
```
```bash
# Mac/Linux için:
python3 -m venv venv
source venv/bin/activate
```
**3. Gerekli Kütüphaneleri Yükleyin Projenin çalışması için gereken spaCy ve TurkishStemmer paketlerini yükleyin:**
```bash
pip install -r requirements.txt
```
**4. Uygulamayı Çalıştırın Kurulum tamamlandıktan sonra projeyi başlatın:**
```bash
python sansur.py
```

## 📂 Klasör Yapısı

```text
turkce-sansur-nlp/
├── sansur.py                 # Ana uygulama dosyası
├── yasakli_kelimeler.txt     # Sansürlenecek kelimeler (kara liste)
├── requirements.txt          # Gerekli Python kütüphaneleri
├── .gitignore                # Git tarafından izlenmeyecek dosyalar
└── README.md                 # Proje dokümantasyonu
```
>Geliştirici: Sudem Kırmız. Bu proje NLP öğrenim sürecimin bir parçası olarak geliştirilmiştir
