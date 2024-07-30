import os
import os.path
import zipfile
import wget
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama
import time

os.system('cls' if os.name == 'nt' else 'clear')

# Hiển thị menu
print("Auto setup ug")
print("""
Thanks for ticket rep support form ngquocthanh
and W-azure
[1]:Delta
[2]:Fluxus
""")

while True:
    try:
        mode = int(input("Mode: "))
        if 1 <= mode <= 2:
            break
        else:
            print("Wrong value")
    except:
        print("Value not set")

# Tab UI
print("""--------------------
How many tab: """)
while True:
    try:
        tab = int(input("> "))
        if 1 <= tab <= 10:
            break
        else:
            print("Choose 1-10")
    except:
        print("Wrong value")

# Root check
def root():
    try:
        result = os.system('su -c "echo"')
        return result == 0
    except Exception as e:
        print(f"Error checking root status: {e}")
        return False

# Mediafire Download 
internal_urls = set()
external_urls = set()

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def gawl(url):
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.find_all("a"):
        href = a_tag.attrs.get("href", "")
        href = urljoin(url, href)
        if is_valid(href):
            if domain_name in href:
                internal_urls.add(href)
            else:
                external_urls.add(href)      
    for i in external_urls:
        if i[0:16] == "https://download":
            return i

# Unzip
def unzip(a, b, c):
    with zipfile.ZipFile(a, 'r') as zip_ref:
        zip_ref.extract(b, c)

# Unzip all
def unzipall(a, b):
    with zipfile.ZipFile(a, "r") as zObject:
        zObject.extractall(path=b)

# Check file exist
def cfe(file_path):
    return os.path.exists(file_path)

# Zip file test
def testzip(file):
    try:
        with zipfile.ZipFile(file) as zip_ref:
            zip_ref.testzip()
        return True
    except Exception as ex:
        return False

# Func
print("Delete Google Play")
os.system('su -c "pm uninstall -k --user 0 com.android.vending"')

print("Ready to check file")
link = "https://github.com/MinhMeow123/Autosetup/releases/download/database/App.zip"

if not cfe("/sdcard/Download/App.zip"):
    print("Downloading material...")
    wget.download(link, out="/sdcard/Download/App.zip")  
else:
    print("Found App.zip file, ready to unzip...")

print("Unzip File...")
unzipall("/sdcard/Download/App.zip", "/sdcard/Download/")
print("Unzip App.zip done")

if mode == 1:    
    # ---- Roblox Delta
    if tab <= 5 and not cfe("/sdcard/Download/delta.zip"):
        print("Downloading delta.zip")
        wget.download("https://download1979.mediafire.com/n0s1zj6szuqgblrlCVEzJPp1riJPFhlZu6b8N9t1UhMFmw4OmAVOzxfoLfsh3LbBQewHV3JCbVH_v8W-DduF2rDNTQwVNnKxhZH2SDjsV3rgHggTKFf2r_gGh1XFI5c1g8tBVDrIKZ1y1PdgDkpKZSq4SsTJy-F-z2rk2_6llQ/f1imajpk7ghj3gi/delta.zip", out="/sdcard/Download/delta.zip")
    elif tab > 5 and not cfe("/sdcard/Download/deltasvip.zip"):
        print("Downloading delta(large).zip")
        wget.download("https://github.com/MinhMeow123/Autosetup/releases/download/database/delta2.zip", out="/sdcard/Download/deltasvip.zip")

    print("Unzip Delta file...")
    time.sleep(1)

    if cfe("/sdcard/Download/deltasvip.zip"):
        for i in range(1, tab + 1):
            unzip("/sdcard/Download/deltasvip.zip", f"delta{i}.apk", "/sdcard/Download/")
    elif cfe("/sdcard/Download/delta.zip"):
        for i in range(1, tab + 1):
            unzip("/sdcard/Download/delta.zip", f"delta{i}.apk", "/sdcard/Download/")

# Roblox Fluxus
else:
    if tab <= 5 and not cfe("/sdcard/Download/fluxus.zip"):
        print("Downloading fluxus.zip")
        wget.download("https://github.com/MinhMeow123/Autosetup/releases/download/database/fluxus.zip", out="/sdcard/Download/fluxus.zip")
    elif tab > 5 and not cfe("/sdcard/Download/fluxus2.zip"):
        print("Downloading fluxus2.zip")
        wget.download("https://github.com/MinhMeow123/Autosetup/releases/download/database/fluxus2.zip", out="/sdcard/Download/fluxus2.zip")

    print("Unzip Roblox file...")
    if cfe("/sdcard/Download/fluxus2.zip"):
        for i in range(1, tab + 1):
            unzip("/sdcard/Download/fluxus2.zip", f"fluxus{i}.apk", "/sdcard/Download/")
    elif cfe("/sdcard/Download/fluxus.zip"):
        for i in range(1, tab + 1):
            unzip("/sdcard/Download/fluxus.zip", f"fluxus{i}.apk", "/sdcard/Download/")

# Root test
if not root():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Enable Root pls")
    exit()

# APK install
print("Installing APKs...")
if mode == 1:
    for i in range(1, 7):
        print(f"Install {i}.apk")
        os.system(f'su -c "pm install /sdcard/Download/{i}.apk"')

    os.system('su -c "pm uninstall -k --user 0 com.android.vending"')

    for i in range(1, tab + 1):
        print(f"Install delta{i}.apk")
        os.system(f'su -c "pm install /sdcard/Download/delta{i}.apk"')
    os.system('su -c "pm install /sdcard/Download/2.apk"')
else:
    for i in range(1, 7):
        print(f"Install {i}.apk")
        os.system(f'su -c "pm install /sdcard/Download/{i}.apk"')

    os.system('su -c "pm uninstall -k --user 0 com.android.vending"')

    for i in range(1, tab + 1):
        print(f"Install fluxus{i}.apk")
        os.system(f'su -c "pm install /sdcard/Download/fluxus{i}.apk"')
    os.system('su -c "pm install /sdcard/Download/2.apk"')

# Vinh tool
os.system('su -c "cd /sdcard/download && export PATH=$PATH:/data/data/com.termux/files/usr/bin && export TERM=xterm-256color && python ./tool.py"')
