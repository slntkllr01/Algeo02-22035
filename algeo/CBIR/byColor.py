import cv2
import numpy as np

def CBIRbyColor(path):
    img = cv2.imread(path)

    resized_img = cv2.resize(img, (60, 60))

    matrix_resized = resized_img

    normalized = matrix_resized / 255.0

    # Mencari Cmax, Cmin, dan delta
    Cmax = np.max(normalized, axis=2)
    Cmin = np.min(normalized, axis=2)
    delta = Cmax - Cmin

    # Inisialisasi H, S, dan V
    H = np.zeros_like(matrix_resized[:,:,0], dtype=float)
    S = np.zeros_like(matrix_resized[:,:,0], dtype=float)
    V = Cmax

    # Menghitung H
    B, G, R = cv2.split(normalized)

    # Menghitung H
    cond = np.logical_and(delta != 0, Cmax == R)
    H[cond] = 60 * (((G - B) / delta % 6))[cond]
    cond = np.logical_and(delta != 0, Cmax == G)
    H[cond] = (60 * ((B - R) / delta + 2))[cond]
    cond = np.logical_and(delta != 0, Cmax == B)
    H[cond] = (60 * ((R - G) / delta + 4))[cond]

    # Mengatasi pembagian oleh nol dengan menetapkan H ke nol ketika delta nol
    H[delta == 0] = 0

    # Menghitung S
    S[Cmax != 0] = delta[Cmax != 0] / Cmax[Cmax != 0]

    # karena sumsi image_height = image_width
    image_height, image_width = H.shape

    # Ukuran blok yang diinginkan (disesuaikan dengan partisi 3x3)
    desired_block_size = image_height // 4  # Ukuran blok yang akan dipartisi

    # Loop untuk membagi gambar menjadi blok 3x3 dan menghitung histogram warna
    histograms = []
    for i in range(4):
        for j in range(4):
            # Tentukan koordinat awal dan akhir untuk blok saat ini
            start_row = i * desired_block_size
            end_row = start_row + desired_block_size
            start_col = j * desired_block_size
            end_col = start_col + desired_block_size

            # Ambil blok dari komponen H, S, dan V
            block_H = H[start_row:end_row, start_col:end_col]
            block_S = S[start_row:end_row, start_col:end_col]
            block_V = V[start_row:end_row, start_col:end_col]

            # Hitung histogram warna untuk masing-masing blok
            hist_H = np.histogram(block_H, bins=8, range=(0, 360))[0]
            hist_S = np.histogram(block_S, bins=3, range=(0, 1))[0]
            hist_V = np.histogram(block_V, bins=3, range=(0, 1))[0]

            # Gabungkan histogram warna dari komponen H, S, dan V
            histogram = np.concatenate((hist_H, hist_S, hist_V))
            # Tambahkan histogram ke daftar histograms
            histograms.append(histogram)

    # Menggabungkan semua elemen histograms menjadi satu array
    concatenated_histograms = np.concatenate(histograms)

    return concatenated_histograms