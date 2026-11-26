**HITUNG_KAMPUS**

**hitung_kampus** adalah pustaka pihak ketiga (*third-party library*) sederhana berbasis Python yang digunakan untuk menghitung nilai akhir mahasiswa berdasarkan bobot komponen penilaian serta menentukan predikat kelulusan.

Pustaka ini dibuat sebagai bagian dari tugas kuliah Pemrograman untuk memahami proses pembuatan, pengemasan, instalasi, dan penggunaan pustaka Python.

**STRUKTUR_PROYEK**

```text
ryan_tugas/
├── pyproject.toml
└── hitung_kampus/
    ├── inibos.py
    └── nilai.py
```

**Fitur Utama**

Pustaka ini menyediakan dua fungsi utama:

### 1. `hitung_nilai_akhir(tugas, uts, uas)`

Menghitung nilai akhir mahasiswa berdasarkan komposisi bobot berikut:

| Komponen Penilaian | Bobot |
|---|---:|
| Tugas | 30% |
| UTS | 30% |
| UAS | 40% |
| **Total** | **100%** |

Rumus perhitungan:

```text
Nilai Akhir = (Tugas × 30%) + (UTS × 30%) + (UAS × 40%)
```

### 2. `cek_predikat(nilai_akhir)`

Menentukan huruf mutu dan predikat berdasarkan nilai akhir mahasiswa.

| Rentang Nilai | Huruf Mutu | Predikat |
|---|---|---|
| 80–100 | A | Sangat Baik |
| 70–79 | B | Baik |
| 60–69 | C | Cukup |
| 0–59 | D | Kurang |

**Persyaratan**

- Python versi 3.8 atau lebih baru.
- pip
