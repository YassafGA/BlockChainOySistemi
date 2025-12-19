from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from web3 import Web3
import json
import subprocess
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- BİLGİLERİ BURAYA DOLDUR ---
GANACHE_URL = "HTTP://127.0.0.1:7545"
PRIVATE_KEY = "0xbb755070c2db7ecb629a266cc79fe362700a6a4f96127f6cd557ce6e31b2b457" 
MY_ADDRESS = "0xc0b1aCD25a433Cc1C4736458f9C47ccddf6d7bd7"
CONTRACT_ADDRESS = "0x1ef75Ff661B73a662EcAFf22A7453D01aDed2404"
# TC No destekleyen yeni ABI
CONTRACT_ABI = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_isim",
				"type": "string"
			}
		],
		"name": "adayEkle",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_tcNo",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_adayId",
				"type": "uint256"
			}
		],
		"name": "oyVer",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "adaylar",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "isim",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "oySayisi",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "adaySayisi",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "oyKullandiMi",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]# --- GELİŞMİŞ MAC IP BULUCU ---
def get_ip_address():
    try:
        # 1. Yöntem: Mac Wi-Fi (en0)
        ip = subprocess.check_output(["ipconfig", "getifaddr", "en0"]).decode().strip()
        if ip: return ip
    except: pass

    try:
        # 2. Yöntem: Mac Ethernet (en1)
        ip = subprocess.check_output(["ipconfig", "getifaddr", "en1"]).decode().strip()
        if ip: return ip
    except: pass

    try:
        # 3. Yöntem: Google Ping (Evrensel)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1" # Hiçbiri olmazsa

SERVER_IP = get_ip_address()
print("------------------------------------------------")
print(f"📡 SUANKI IP ADRESIN: {SERVER_IP}")
print(f"📱 TELEFON LINKI: http://{SERVER_IP}:8000")
print("------------------------------------------------")

# --- BURASI ÇOK ÖNEMLİ: Frontend'in IP'yi öğrendiği yer ---
@app.get("/sunucu_bilgisi")
def sunucu_bilgisi():
    # Eğer IP boşsa veya localhost ise manuel düzeltme şansı verelim
    return {"ip": SERVER_IP, "port": 8000}

# Bağlantıyı Kur
try:
    w3 = Web3(Web3.HTTPProvider(GANACHE_URL))
    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
    print(f"✅ Blockchain Bağlantısı: {w3.is_connected()}")
except Exception as e:
    print(f"❌ HATA: {e}")

class OyIstegi(BaseModel):
    tc_no: str
    aday_id: int

@app.get("/")
def ana_sayfa():
    return FileResponse("index.html")

# --- MEVCUT KOD ---
@app.get("/")
def ana_sayfa(): 
    return FileResponse("index.html")

# --- YENİ EKLENECEK KOD (Bunu ekle) ---
@app.get("/oy")
def oy_ekrani_sun():
    # Telefonda bu adres açılacak, yine aynı dosyayı gönderiyoruz
    # Ama HTML içindeki React, adrese bakıp ekranı değiştirecek.
    return FileResponse("index.html")

@app.get("/sonuclar")
def sonuclari_getir():
    try:
        toplam = contract.functions.adaySayisi().call()
        liste = []
        for i in range(1, toplam + 1):
            veri = contract.functions.adaylar(i).call()
            liste.append({"id": veri[0], "isim": veri[1], "oy": veri[2]})
        return liste
    except Exception as e:
        print(f"Veri Çekme Hatası: {e}")
        return []

# --- main.py İÇİNDEKİ DEĞİŞİKLİK ---
@app.post("/oy_ver")
def oy_ver(istek: OyIstegi):
    try:
        if len(istek.tc_no) != 11: raise HTTPException(status_code=400, detail="TC No 11 haneli olmalıdır")
        nonce = w3.eth.get_transaction_count(MY_ADDRESS)
        tx = contract.functions.oyVer(istek.tc_no, istek.aday_id).build_transaction({
            'chainId': 1337, 'gas': 3000000, 'gasPrice': w3.to_wei('20', 'gwei'), 'nonce': nonce
        })
        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        w3.eth.wait_for_transaction_receipt(tx_hash)
        
        # DEĞİŞİKLİK BURADA: Sadece "Başarılı" değil, Hash'i de gönderiyoruz (hex formatında)
        return {"durum": "Başarılı", "hash": tx_hash.hex()} 
        
    except Exception as e:
        if "zaten oy kullanildi" in str(e): raise HTTPException(status_code=400, detail="Bu TC ile zaten oy kullanıldı!")
        raise HTTPException(status_code=500, detail=str(e))