def hitung_nilai_akhir(tugas, uts, uas):
    """Menghitung nilai akhir berdasarkan bobot kampus."""
    return (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

def cek_predikat(nilai_akhir):
    """Menentukan huruf mutu dari nilai akhir."""
    if nilai_akhir >= 85:
        return "A (Sangat Baik)"
    elif nilai_akhir >= 70:
        return "B (Baik)"
    elif nilai_akhir >= 55:
        return "C (Cukup)"
    else:
        return "D (Kurang)"