"""
AI Image Prompt Generator
=========================
Tool ini membantu kamu membuat prompt gambar yang detail dan kreatif
menggunakan LiteLLM API (custom endpoint).

Author: Generated with Claude AI
"""

import os       # Untuk mengakses environment variables (API key)
import requests # Untuk HTTP request ke LiteLLM endpoint


# ============================================================
# KONFIGURASI API
# ============================================================

# Base URL endpoint LiteLLM kamu
API_BASE_URL = "https://litellm.koboi2026.biz.id/v1"

# Endpoint untuk chat completions (standar OpenAI-compatible)
CHAT_ENDPOINT = f"{API_BASE_URL}/chat/completions"

# Model yang digunakan (bisa diganti sesuai model yang tersedia di LiteLLM)
MODEL_NAME = "gpt-4o"  # Ganti jika model berbeda, contoh: "claude-3-5-sonnet", dll


def get_api_key() -> str:
    """
    Ambil API key dari environment variable.
    Jika tidak ada, tampilkan pesan error yang jelas.
    """
    api_key = os.environ.get("LITELLM_API_KEY")
    if not api_key:
        print("\n❌ ERROR: LITELLM_API_KEY tidak ditemukan!")
        print("   Set dulu dengan perintah:")
        print("   Windows : set LITELLM_API_KEY=your_api_key_here")
        print("   Mac/Linux: export LITELLM_API_KEY=your_api_key_here")
        exit(1)
    return api_key


# ============================================================
# FUNGSI UTAMA: Generate Image Prompt
# ============================================================

def generate_image_prompt(user_idea: str, style: str = "realistic") -> str:
    """
    Fungsi ini menerima ide sederhana dari user, lalu menggunakan
    AI (via LiteLLM) untuk mengubahnya menjadi prompt gambar yang detail.

    Parameter:
    - user_idea : Ide dasar dari user (contoh: "kucing di taman")
    - style     : Gaya gambar yang diinginkan (default: "realistic")

    Return:
    - String berisi prompt gambar yang sudah diperkaya
    """

    api_key = get_api_key()

    # System prompt: instruksi untuk AI tentang tugasnya
    system_prompt = """Kamu adalah ahli dalam membuat prompt untuk AI image generator 
seperti Midjourney, DALL-E, dan Stable Diffusion. 

Tugasmu adalah mengubah ide sederhana dari user menjadi prompt gambar yang:
1. Detail dan deskriptif
2. Mencakup: subjek utama, latar belakang, pencahayaan, suasana, komposisi
3. Menggunakan kata kunci teknis yang cocok untuk AI image generator
4. Tersedia dalam 2 versi: Bahasa Indonesia dan English

Format output kamu:
---
🇮🇩 PROMPT (Indonesia):
[prompt dalam bahasa Indonesia]

🇺🇸 PROMPT (English):
[prompt dalam bahasa Inggris - ini yang paling optimal untuk AI generator]

💡 Tips Penggunaan:
[saran singkat cara menggunakan prompt ini]
---"""

    # Pesan yang dikirim ke AI
    user_message = f"""
Buatkan prompt gambar AI dari ide berikut:
Ide: {user_idea}
Gaya/Style: {style}
    """

    # Header HTTP request (autentikasi + format data)
    headers = {
        "Authorization": f"Bearer {api_key}",  # API key dikirim di header
        "Content-Type": "application/json"      # Format data JSON
    }

    # Body request (format standar OpenAI-compatible yang juga dipakai LiteLLM)
    payload = {
        "model": MODEL_NAME,
        "max_tokens": 1024,
        "messages": [
            {"role": "system", "content": system_prompt},   # Instruksi sistem
            {"role": "user",   "content": user_message}     # Pesan user
        ]
    }

    # Kirim request ke LiteLLM endpoint
    response = requests.post(CHAT_ENDPOINT, headers=headers, json=payload, timeout=60)

    # Cek apakah request berhasil (status 200)
    if response.status_code != 200:
        raise Exception(f"API Error {response.status_code}: {response.text}")

    # Parse JSON response dan ambil teks jawaban
    data = response.json()
    return data["choices"][0]["message"]["content"]


# ============================================================
# FUNGSI: Tampilkan menu gaya gambar
# ============================================================

def show_style_menu():
    """
    Menampilkan pilihan gaya gambar yang tersedia.
    """
    styles = {
        "1": "realistic",           # Foto-realistis
        "2": "anime",               # Gaya anime/manga Jepang
        "3": "digital art",         # Seni digital modern
        "4": "oil painting",        # Lukisan cat minyak
        "5": "watercolor",          # Lukisan cat air
        "6": "3D render",           # Render 3D
        "7": "sketch",              # Sketsa pensil
        "8": "fantasy art",         # Seni fantasi
    }

    print("\n🎨 Pilih Gaya Gambar:")
    print("-" * 30)
    for key, value in styles.items():
        print(f"  {key}. {value}")
    print("-" * 30)

    return styles


# ============================================================
# FUNGSI: Simpan hasil ke file
# ============================================================

def save_prompt_to_file(idea: str, style: str, result: str):
    """
    Menyimpan hasil prompt ke file .txt agar bisa digunakan nanti.

    Parameter:
    - idea   : Ide awal dari user
    - style  : Gaya gambar yang dipilih
    - result : Hasil prompt dari Claude
    """
    # Buat nama file berdasarkan ide (hapus karakter spesial)
    safe_name = "".join(c if c.isalnum() or c == " " else "_" for c in idea)
    safe_name = safe_name.replace(" ", "_")[:30]  # Batasi 30 karakter
    filename = f"prompt_{safe_name}.txt"

    # Tulis ke file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"IDE AWAL: {idea}\n")
        f.write(f"GAYA: {style}\n")
        f.write("=" * 50 + "\n\n")
        f.write(result)

    print(f"\n✅ Prompt tersimpan di file: {filename}")


# ============================================================
# FUNGSI: Mode Batch - generate banyak prompt sekaligus
# ============================================================

def batch_generate(ideas_list: list, style: str = "realistic") -> list:
    """
    Membuat banyak prompt sekaligus dari daftar ide.

    Parameter:
    - ideas_list : List berisi beberapa ide
    - style      : Gaya gambar yang sama untuk semua

    Return:
    - List berisi semua hasil prompt
    """
    results = []
    print(f"\n🔄 Memproses {len(ideas_list)} ide...")

    for i, idea in enumerate(ideas_list, 1):
        print(f"  [{i}/{len(ideas_list)}] Generating: {idea}...")
        result = generate_image_prompt(idea, style)
        results.append({"idea": idea, "style": style, "prompt": result})
        print(f"  ✅ Selesai!")

    return results


# ============================================================
# PROGRAM UTAMA (Main)
# ============================================================

def main():
    """
    Fungsi utama yang menjalankan program secara interaktif.
    User bisa memasukkan ide dan memilih gaya gambar.
    """

    print("=" * 60)
    print("🎨 AI IMAGE PROMPT GENERATOR")
    print("   Powered by Anthropic Claude")
    print("=" * 60)

    # Cek apakah API key sudah di-set
    if not os.environ.get("LITELLM_API_KEY"):
        print("\n❌ ERROR: LITELLM_API_KEY tidak ditemukan!")
        print("   Silakan set API key dulu:")
        print("   Windows : set LITELLM_API_KEY=your_api_key_here")
        print("   Mac/Linux: export LITELLM_API_KEY=your_api_key_here")
        return

    while True:  # Loop utama program
        print("\n📋 MENU UTAMA:")
        print("  1. Generate satu prompt")
        print("  2. Generate banyak prompt sekaligus (batch)")
        print("  3. Keluar")
        print("-" * 30)

        choice = input("Pilihan kamu (1/2/3): ").strip()

        # ---- PILIHAN 1: Single Prompt ----
        if choice == "1":
            idea = input("\n💭 Masukkan ide gambarmu: ").strip()

            if not idea:
                print("❌ Ide tidak boleh kosong!")
                continue

            # Tampilkan menu style
            styles = show_style_menu()
            style_choice = input("Pilih nomor gaya (atau ketik sendiri): ").strip()

            # Ambil gaya dari pilihan atau gunakan input langsung
            style = styles.get(style_choice, style_choice if style_choice else "realistic")

            print(f"\n⏳ Sedang generate prompt untuk: '{idea}' dengan gaya '{style}'...")
            print("   (Mohon tunggu beberapa detik...)\n")

            # Generate prompt
            result = generate_image_prompt(idea, style)

            # Tampilkan hasil
            print("\n" + "=" * 60)
            print("✨ HASIL PROMPT:")
            print("=" * 60)
            print(result)
            print("=" * 60)

            # Tanya mau disimpan atau tidak
            save = input("\n💾 Simpan ke file? (y/n): ").strip().lower()
            if save == "y":
                save_prompt_to_file(idea, style, result)

        # ---- PILIHAN 2: Batch Generate ----
        elif choice == "2":
            print("\n📝 Mode Batch - Masukkan beberapa ide (ketik 'selesai' untuk berhenti):")

            ideas = []
            while True:
                ide = input(f"  Ide {len(ideas) + 1}: ").strip()
                if ide.lower() == "selesai":
                    break
                if ide:
                    ideas.append(ide)

            if not ideas:
                print("❌ Tidak ada ide yang dimasukkan!")
                continue

            # Pilih satu gaya untuk semua
            styles = show_style_menu()
            style_choice = input("Pilih nomor gaya untuk semua: ").strip()
            style = styles.get(style_choice, "realistic")

            # Generate semua
            results = batch_generate(ideas, style)

            # Simpan semua ke satu file
            with open("batch_prompts.txt", "w", encoding="utf-8") as f:
                for i, item in enumerate(results, 1):
                    f.write(f"\n{'=' * 60}\n")
                    f.write(f"#{i} - IDE: {item['idea']}\n")
                    f.write(f"GAYA: {item['style']}\n")
                    f.write(f"{'=' * 60}\n")
                    f.write(item['prompt'])
                    f.write("\n")

            print(f"\n✅ Semua prompt tersimpan di: batch_prompts.txt")

        # ---- PILIHAN 3: Keluar ----
        elif choice == "3":
            print("\n👋 Terima kasih sudah menggunakan AI Image Prompt Generator!")
            print("   Selamat berkreasi! 🎨\n")
            break

        else:
            print("❌ Pilihan tidak valid, coba lagi!")


# Entry point - kode ini dijalankan saat file di-eksekusi langsung
if __name__ == "__main__":
    main()
