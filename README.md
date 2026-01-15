# 🗳️ Blockchain Tabanlı Güvenli e-Seçim Sistemi

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Backend-Python%20%7C%20FastAPI-green)
![React](https://img.shields.io/badge/Frontend-React.js-blue)
![Ethereum](https://img.shields.io/badge/Blockchain-Ethereum%20%7C%20Solidity-gray)

Bu proje, geleneksel seçim sistemlerindeki güvenlik açıklarını, hatalı sayımları ve güven sorunlarını ortadan kaldırmak amacıyla geliştirilmiş **merkeziyetsiz, şeffaf ve değiştirilemez** bir elektronik oylama sistemidir.

Proje, **Ethereum Sanal Makinesi (EVM)** altyapısını kullanarak oyları kriptografik olarak şifreler ve blok zincirine yazar.

---

## 🚀 Özellikler

- **🔒 Değiştirilemez Kayıtlar:** Verilen her oy, Blockchain üzerinde bir blok olarak saklanır ve geriye dönük değiştirilemez.
- **📱 Mobil Entegrasyon (QR Kod):** Masaüstü ekranındaki QR kod taranarak telefon üzerinden güvenli oy kullanılabilir.
- **🚫 Mükerrer Oy Engeli:** Akıllı Kontratlar (Smart Contracts), aynı TC Kimlik numarasıyla ikinci kez oy kullanılmasını matematiksel olarak engeller.
- **🧾 Kanıtlanabilirlik (Oy Fişi):** Oy veren kullanıcıya, oyunun zincire işlendiğini kanıtlayan benzersiz bir **Transaction Hash (İşlem Kodu)** verilir.
- **📊 Canlı Takip:** Sonuçlar anlık olarak grafiklere yansır ve herkes tarafından izlenebilir.
- **🔍 Şeffaf Doğrulama:** Kullanıcılar, kendilerine verilen Hash kodu ile oylarının sistemde kayıtlı olduğunu doğrulayabilirler.

---

## 🛠️ Kullanılan Teknolojiler

### ⛓️ Blockchain Katmanı
- **Solidity:** Akıllı Sözleşmelerin (Smart Contract) yazılması.
- **Ganache:** Yerel Ethereum blok zinciri simülasyonu.
- **Web3.py:** Python ile Blockchain arasındaki köprü.

### 🔙 Backend (Sunucu)
- **Python 3.x:** Ana programlama dili.
- **FastAPI:** Yüksek performanslı web sunucusu ve API yönetimi.

### 🎨 Frontend (Arayüz)
- **React.js:** Kullanıcı arayüzü (CDN üzerinden).
- **TailwindCSS:** Modern ve responsive tasarım.
- **HTML5/JS:** Tek sayfa uygulaması (SPA) yapısı.

---

## ⚙️ Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### Ön Hazırlıklar
1. **Python** yüklü olmalı.
2. **Ganache** (GUI veya CLI) yüklü ve çalışıyor olmalı.

### Adım 1: Projeyi Klonlayın

git clone [https://github.com/kullaniciadin/blockchain-secim-sistemi.git](https://github.com/kullaniciadin/blockchain-secim-sistemi.git)
cd blockchain-secim-sistemi

Adım 2: Gerekli Kütüphaneleri Yükleyin

pip install fastapi uvicorn web3

Adım 3: Yapılandırma

main.py dosyasını açın ve Ganache bilgilerinizi güncelleyin:

Python
GANACHE_URL = "HTTP://127.0.0.1:7545"
PRIVATE_KEY = "SİZİN_GANACHE_PRIVATE_KEYİNİZ"
MY_ADDRESS = "SİZİN_CÜZDAN_ADRESİNİZ"
CONTRACT_ADDRESS = "DEPLOY_EDİLEN_KONTRAT_ADRESİ"
Adım 4: Uygulamayı Başlatın

Terminalden şu komutu çalıştırın:

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

### 🖥️ Kullanım Senaryosu

1. Seçim Paneli (Masaüstü)

Tarayıcınızda http://localhost:8000 adresine gidin.

Burada Canlı Sonuç Grafikleri ve mobil giriş için QR Kod bulunur.

Ayrıca sağ altta Oy Doğrulama Kutusu yer alır.

2. Oy Verme (Mobil)

QR kodu telefonunuzla okutun veya http://IP_ADRESINIZ:8000/oy adresine gidin.

TC Kimlik Numaranızı girin.

Adayınızı seçin.

Sonuç: Ekrana "Oy Makbuzu" ve "Hash Kodu" gelecektir.

3. Doğrulama

Telefondaki Hash kodunu kopyalayın, masaüstündeki arama kutusuna yapıştırın. Sistemin oyu Blockchain üzerinde bulup doğruladığını göreceksiniz.

### 🏗️ Mimari ve Güvenlik
Sistem "Proof of Authority" (Otorite Kanıtı) benzeri bir yapı ile çalışır.

Kullanıcı isteği gönderir.

Backend, isteği yetkili cüzdan ile imzalar.

Akıllı Kontrat oyKullandiMi kontrolü yapar.

İşlem onaylanırsa Blok Zincire eklenir ve Hash üretilir.

Not: Bu proje Ganache üzerinde test ortamında çalışmaktadır. Gerçek bir senaryoda Ethereum Mainnet veya Private Chain üzerine deploy edilebilir.

📄 Lisans
Bu proje MIT lisansı ile lisanslanmıştır.
