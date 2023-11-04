import os
import cv2
import numpy as np

# Fungsi untuk menghitung histogram warna
def calculate_histogram(block, bins=30):
    hist = cv2.calcHist([block], [0, 1, 2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])
    return cv2.normalize(hist, hist).flatten()

def cosine_similarity(v1, v2):
    # Hitung dot product
    dot_product = np.dot(v1, v2)
    # Hitung norm
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    # Hitung cosine similarity
    cosine_similarity = dot_product / (norm_v1 * norm_v2)
    return cosine_similarity


import cv2
import numpy as np

def RGBtoHSV(image):
    img = cv2.imread('C:\\Users\\raffa\\OneDrive\\Dokumen\\GitHub\\Algeo02-22035\\lib\\CBIR\\0.jpg')
    # Normalisasi RGB
    normalized = img / 255.0
    # Mencari Cmax, Cmin, dan delta
    Cmax = np.max(normalized, axis=2)
    Cmin = np.min(normalized, axis=2)
    delta = Cmax - Cmin

    # Inisialisasi H, S, dan V
    H = np.zeros_like(image[:,:,0], dtype=float)
    S = np.zeros_like(image[:,:,0], dtype=float)
    V = Cmax


    # Menghitung H
    R, G, B = cv2.split(normalized)

    cond = np.logical_and(delta != 0, Cmax == R)
    H[cond] = 60 * (((G - B) / delta % 6))[cond]
    cond = np.logical_and(delta != 0, Cmax == G)
    H[cond] = (60 * ((B - R) / delta + 2))[cond]
    cond = np.logical_and(delta != 0, Cmax == B)
    H[cond] = (60 * ((R - G) / delta + 4))[cond]

    # Menghitung S
    S[Cmax != 0] = delta[Cmax != 0] / Cmax[Cmax != 0]

    print(H)
    print(S)
    print(V)

RGBtoHSV('C:\\Users\\raffa\\OneDrive\\Dokumen\\GitHub\\Algeo02-22035\\lib\\CBIR\\0.jpg')
# # convert dari RGB ke HSV
# def RGBtoHSV(block):
#     r, g, b = cv2.split(block)
#     maxc = np.max(block, axis=2)
#     minc = np.min(block, axis=2)
#     v = maxc
#     delta = maxc - minc

#     s = np.where(maxc != 0, delta / maxc, 0)
#     rc = np.where(maxc != r, (maxc - r) / delta, 0)
#     gc = np.where(maxc != g, (maxc - g) / delta, 0)
#     bc = np.where(maxc != b, (maxc - b) / delta, 0)

#     h = np.where(maxc == r, bc - gc, 0)
#     h = np.where(maxc == g, 2.0 + rc - bc, h)
#     h = np.where(maxc == b, 4.0 + gc - rc, h)

#     h = (h / 6.0) % 1.0
#     return h * 360, s * 100, v * 100

# Fungsi untuk memproses dataset
def process_dataset(dataset_folder):
    histograms = []
    file_names = []
    for file_name in os.listdir(dataset_folder):
        file_path = os.path.join(dataset_folder, file_name)
        image = cv2.imread(file_path)
        hsv_image = RGBtoHSV(image / 255.0)
        histograms.append(calculate_histogram(hsv_image))
        file_names.append(file_name)
    return histograms, file_names

# Fungsi untuk memproses gambar input
def process_input_image(input_image_path):
    image = cv2.imread(input_image_path)
    hsv_image = RGBtoHSV(image)
    print(hsv_image)
    # return calculate_histogram(hsv_image)

# process_input_image('C:\\Users\\raffa\\OneDrive\\Dokumen\\GitHub\\Algeo02-22035\\lib\\CBIR\\0.jpg')

# Fungsi untuk mencari gambar yang mirip
def find_similar_images(input_hist, dataset_histograms, file_names, threshold=0.6):
    similar_images = []
    for i, hist in enumerate(dataset_histograms):
        similarity = cosine_similarity(input_hist, hist)
        if similarity > threshold:
            similar_images.append((similarity, file_names[i]))
    similar_images.sort(reverse = True)
    return similar_images

# Fungsi utama
def main(input_image_path, dataset_folder):
    # Proses dataset
    dataset_histograms, file_names = process_dataset(dataset_folder)

    # Proses gambar input
    input_hist = process_input_image(input_image_path)

    # Cari gambar yang mirip
    similar_images = find_similar_images(input_hist, dataset_histograms, file_names)

    # Tampilkan hasil
    for similarity, file_name in similar_images:
        print(f'Gambar {file_name} memiliki tingkat kemiripan {similarity*100:.2f}%')

# # Panggil fungsi utama
# main('C:\\Users\\raffa\\OneDrive\\Dokumen\\GitHub\\Algeo02-22035\\lib\\CBIR\\0.jpg', 'C:\\Users\\raffa\\OneDrive\\Dokumen\\GitHub\\Algeo02-22035\\lib\\CBIR\\dataset')

