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

# Key check
def check_key():
    key = input("Please enter the key to continue: ")
    return key == 'quanexe'

if not check_key():
    print("Invalid key. Exiting...")
    exit()

# Executor
print("Auto setup ug")
print("""
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
print("--------------------\nHow many tab: ")
while True:
    try:
        tab = int(input("> "))
        if 1 <= tab <= 10:
            break
        else:
            print("Chose 1-10")
    except:
        print("Wrong value")

# Rootcheck
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

# Function
print("Delete Google Play")
os.system('su -c "pm uninstall -k --user 0 com.android.vending"')
print("Ready to check file")
link = gawl("https://www.mediafire.com/file/88smx13m9ot4nts/App.zip/file")
if not cfe("/sdcard/Download/App.zip"):
    print("Download material...")
    wget.download(link, out="/sdcard/Download/App.zip")
else:
    print("Found App.zip file, ready to unzip...")
print("Unzip File....")
unzipall("/sdcard/Download/App.zip", "/sdcard/Download/")
print("Unzip App.zip done")
print("Wait 5s cooldown")
time.sleep(5)
print("Done")

if mode == 1:
    #----Roblox Delta
    if tab <= 5 and not cfe("/sdcard/Download/delta.zip"):
        print("Download delta.zip")
        delta = gawl("https://www.mediafire.com/file/f1imajpk7ghj3gi/delta.zip/file")
        wget.download(delta, out="/sdcard/Download/delta.zip")
    elif tab > 5 and not cfe("/sdcard/Download/deltasvip.zip"):
        print("Download delta(large).zip")
        delta2 = gawl("https://www.mediafire.com/file/lfxn5c2i8bupfnh/deltasvip.zip/file")
        wget.download(delta2, out="/sdcard/Download/deltasvip.zip")
    print("Unzip Delta file...")
    #----Unzip
    if cfe("/sdcard/Download/deltasvip.zip"):
        for i in range(1, tab + 1):
            unzip("/sdcard/Download/deltasvip.zip", f"delta{i}.apk", "/sdcard/Download/")
    elif cfe("/sdcard/Download/delta.zip"):
        for i in range(1, tab + 1):
            unzip("/sdcard/Download/delta.zip", f"delta{i}.apk", "/sdcard/Download/")
else:
    if tab <= 5 and not cfe("/sdcard/Download/fluxus.zip"):
        print("Download fluxus.zip")
        fluxus = gawl("https://www.mediafire.com/file/ftijj6omvmcaztn/fluxus.zip/file")
        wget.download(fluxus, out="/sdcard/Download/fluxus.zip")
    elif tab > 5 and not cfe("/sdcard/Download/fluxus2.zip"):
        print("Download fluxus2.zip")
        fluxus2 = gawl("https://www.mediafire.com/file/fpv1r4hv7b3a548/fluxus2.zip/file")
        wget.download(fluxus2, out="/sdcard/Download/fluxus2.zip")
    print("Unzip Roblox file...")
    #----Unzip
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

# APK Install
if mode == 1:
    print("Install apk....")
    for i in range(1, 7):
        print(f"Install {i}.apk")
        os.system(f'su -c "pm install /sdcard/Download/{i}.apk"')     
    os.system('su -c "pm uninstall -k --user 0 com.android.vending"')  
    for i in range(1, tab + 1):
        print(f"Install delta{i}.apk")
        os.system(f'su -c "pm install /sdcard/Download/delta{i}.apk"')
    os.system('su -c "pm install /sdcard/Download/2.apk"')
else:
    print("Install apk....")
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
