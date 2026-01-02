# 📍 Termux Live Location Tracker

Live GPS location tracking using **Termux + Termux:API**  
Designed for **personal use, research, IoT, and learning purposes**.

> ✅ Legal & consent-based  
> ❌ No spyware / no stealth tracking

---

## ✨ Features

- Live GPS tracking (real-time)
- Adjustable update interval
- Save location logs
- Send location to webhook / server
- Lightweight Bash script
- Android + Termux compatible

---

## 📱 Requirements

- Android device
- Termux
- Termux:API app
- Internet connection (optional, for webhook)

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/termux-live-location-tracker
cd termux-live-location-tracker
chmod +x install.sh tracker.sh
./install.sh

### 1️⃣ Install Termux API
- Install **Termux**
- Install **Termux:API** (F-Droid / Play Store)

### 2️⃣ Install dependencies
```bash
pkg update
pkg install termux-api curl jq python
pip install -r server/requirements.txt

## Kali Linux Support

This project supports Kali Linux as a backend server
for receiving, visualizing, and forwarding GPS data.

GPS acquisition is performed on Android (Termux).
