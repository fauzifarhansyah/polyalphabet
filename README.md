# polyalphabet
file polyalphabet ini guna memenuhi prasyarat tugas kripto
buatlah source code (saya disini menggunakan bahasa pemograman python) bahsa pemograman python

# Hasil Program
![Logo GitHub](https://github.com/fauzifarhansyah/polyalphabet/blob/717885582ac78f2bdaf5e03197a662a3a2e915c1/ss%20polyalphabet/polyalphabet.png)

#Penjelasan Mengenai poly Alphabet Zig - Zag
Fungsi `polyalphabetic_zigzag` ini adalah untuk melakukan enkripsi teks menggunakan metode polyalphabetic substitution cipher dengan teknik zigzag. Berikut penjelasan setiap bagian dari kode:

1. **polyalphabetic_zigzag Function:**
   - `polyalphabetic_zigzag(text, key)`: Fungsi ini mengambil dua parameter, yaitu `text` (teks yang akan dienkripsi) dan `key` (kunci enkripsi).

   - `encrypted_text = ""`: Membuat string kosong untuk menyimpan teks terenkripsi.

   - `key_length = len(key)`: Menghitung panjang kunci untuk digunakan dalam pengulangan.

   - `for i in range(len(text)):`: Iterasi melalui setiap karakter dalam teks input.

     - `char = text[i]`: Mengambil karakter saat ini dalam iterasi.

     - `if char.isalpha():`: Memeriksa apakah karakter adalah huruf alfabet.

       - `shift = ord(key[i % key_length].lower()) - ord('a')`: Menghitung nilai shift berdasarkan karakter kunci pada posisi tertentu. Fungsi `ord` digunakan untuk mendapatkan nilai ASCII karakter, dan `lower()` digunakan untuk memastikan kunci dianggap huruf kecil.

       - `if char.isupper():`: Memeriksa apakah karakter dalam teks adalah huruf kapital.

         - `encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))`: Mengenkripsi karakter kapital dengan metode polyalphabetic substitution cipher dan teknik zigzag. `ord` digunakan untuk mendapatkan nilai ASCII, dan `chr` digunakan untuk mengonversi kembali ke karakter. Formula ini memastikan bahwa enkripsi tetap dalam rentang huruf kapital.

       - `else:`: Dijalankan jika karakter dalam teks adalah huruf kecil.

         - `encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))`: Mengenkripsi karakter kecil dengan metode yang sama seperti karakter kapital, memastikan enkripsi tetap dalam rentang huruf kecil.

       - `encrypted_text += encrypted_char`: Menambahkan karakter terenkripsi ke dalam string `encrypted_text`.

     - `else:`: Dijalankan jika karakter dalam teks bukan huruf alfabet.

       - `encrypted_text += char`: Menambahkan karakter non-alfabet ke dalam string `encrypted_text` tanpa melakukan enkripsi.

   - `return encrypted_text`: Mengembalikan teks yang telah dienkripsi.

2. **main Function:**
   - `main()`: Fungsi utama yang akan dijalankan jika skrip ini dijalankan sebagai program utama.

   - `plaintext = input("Masukkan teks yang ingin dienkripsi: ")`: Menerima input dari pengguna berupa teks yang akan dienkripsi.

   - `key = input("Masukkan kunci enkripsi: ")`: Menerima input kunci enkripsi dari pengguna.

   - `encrypted_text = polyalphabetic_zigzag(plaintext, key)`: Memanggil fungsi `polyalphabetic_zigzag` untuk melakukan enkripsi menggunakan teks dan kunci yang telah diinput.

   - `print("Teks terenkripsi:", encrypted_text)`: Menampilkan teks terenkripsi ke layar.

   - `if __name__ == "__main__":`: Memastikan bahwa fungsi `main()` hanya dijalankan jika skrip ini dijalankan sebagai program utama, bukan diimpor sebagai modul dalam skrip lain.
