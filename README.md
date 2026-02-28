# 🎨 AI Image Prompt Generator

Tool Python untuk membuat prompt gambar AI yang detail dan kreatif menggunakan **Anthropic Claude API**.

---

## 📌 Apa Itu Tool Ini?

Tool ini membantu kamu mengubah ide sederhana (seperti "kucing di taman") menjadi prompt gambar AI yang profesional dan detail — siap dipakai di **Midjourney, DALL-E, Stable Diffusion**, dll.

---

## ✅ Fitur

- 🔤 **Single Prompt** — Generate satu prompt dari ide kamu
- 📦 **Batch Mode** — Generate banyak prompt sekaligus
- 🎨 **8 Pilihan Gaya** — Realistic, Anime, Digital Art, Oil Painting, dll
- 💾 **Simpan ke File** — Hasil prompt bisa disimpan ke `.txt`
- 🇮🇩🇺🇸 **Bilingual Output** — Prompt tersedia dalam Bahasa Indonesia & Inggris

---

## 🚀 Cara Instalasi & Penggunaan

### 1. Clone Repository

```bash
git clone https://github.com/USERNAME/ai-image-prompt-generator.git
cd ai-image-prompt-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set API Key Anthropic

Daftar dan dapatkan API key di: https://console.anthropic.com

**Windows (Command Prompt):**
```cmd
set ANTHROPIC_API_KEY=your_api_key_here
```

**Mac / Linux:**
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

### 4. Jalankan Program

```bash
python prompt_generator.py
```

---

## 📖 Contoh Output

**Input:** `kucing persia duduk di taman bunga sakura`  
**Style:** `anime`

```
🇮🇩 PROMPT (Indonesia):
Seekor kucing persia berbulu putih lembut duduk anggun di taman bunga sakura yang bermekaran,
kelopak merah muda beterbangan di udara, pencahayaan sore yang hangat, gaya anime Ghibli,
komposisi medium shot, detail bulu yang halus...

🇺🇸 PROMPT (English):
A fluffy white Persian cat sitting gracefully in a blooming sakura garden, 
pink petals floating in the air, warm golden hour lighting, Studio Ghibli anime style,
medium shot composition, soft detailed fur, dreamy atmosphere...

💡 Tips Penggunaan:
Tambahkan "--ar 16:9" di Midjourney untuk rasio landscape.
```

---

## 📁 Struktur File

```
ai-image-prompt-generator/
├── prompt_generator.py   # File utama program
├── requirements.txt      # Daftar library yang dibutuhkan
├── README.md             # Dokumentasi ini
└── .gitignore            # File yang dikecualikan dari Git
```

---

## 🛠️ Teknologi yang Digunakan

- **Python 3.8+**
- **Anthropic Claude API** (model: claude-sonnet-4-6)

---

## 📝 Lisensi

MIT License - bebas digunakan dan dimodifikasi.
