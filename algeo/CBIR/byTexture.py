# Reference: https://yunusmuhammad007.medium.com/feature-extraction-gray-level-co-occurrence-matrix-glcm-10c45b6d46a1
# Reference: https://www.sciencedirect.com/science/article/pii/S0895717710005352#s000030
# Reference: https://ojs.uma.ac.id/index.php/jite/article/view/3885/2785

import math
import numpy as np

def rgbToGrayscale(vektorRGB):
    """Mengubah nilai vektor RGB menjadi Grayscale """
    arrayRGB = np.array(vektorRGB)
    r = arrayRGB[:, :, 0]
    g = arrayRGB[:, :, 1]
    b = arrayRGB[:, :, 2]
    vektorGrayscale = np.round(0.29*r + 0.587*g + 0.114*b).astype(int)
    return vektorGrayscale

def quantifyGrayscale(vektorGrayscale):
    """[optional] for faster processing, quantize grayscale value.
    The idea is like the following, but the quantization number lets discuss"""
    length = len(vektorGrayscale)
    vektorQuantized = [[0 for i in range(length)] for j in range (length)]
    for i in range(0, length):
        for j in range (0, length):
            vektorQuantized[i][j]=vektorGrayscale[i][j]//8
    return vektorQuantized


def buildCoOccurrenceMatrix(vektorQuantized):
    """Membangun matriks co-occurence matriks vektor grayscale dengan jarak 1 skala 0 derajat"""
    vektorQuantized = np.array(vektorQuantized)
    length = len(vektorQuantized)
    # Using NumPy to calculate the co-occurrence matrix
    CoOccurrenceMatrix = np.zeros((length, length), dtype=int)
    for i in range(len(vektorQuantized)):
        CoOccurrenceMatrix[vektorQuantized[i, :-1], vektorQuantized[i, 1:]] += 1
    return CoOccurrenceMatrix

def transpose(matrix):
    """ Transpose matrix """
    return np.transpose(matrix)

def getSymmetryMatrix(matrix1, matrix2):
    """ Sum two matrix """
    return np.add(matrix1, matrix2)

def normalizeMatrix(matrix):
    """ Normalize matrix """
    total_sum = np.sum(matrix)
    return matrix / total_sum

def getContrast(GLCM):
    """Menghitung nilai contrast dari matriks GLCM"""
    i, j = np.indices(GLCM.shape)
    return np.sum((i - j) ** 2 * GLCM)

def getDissimilarity(GLCM):
    """Menghitung nilai dissimilarity dari matriks GLCM"""
    i, j = np.indices(GLCM.shape)
    return np.sum(np.abs(i - j) * GLCM)

def getHomogeneity(GLCM):
    """Menghitung nilai homogeneity dari matriks GLCM"""
    i, j = np.indices(GLCM.shape)
    return np.sum(GLCM / (1 + (i - j) ** 2))

def getASM(GLCM):
    """Menghitung nilai ASM dari matriks GLCM"""
    return np.sum(GLCM**2)

def getEnergy(GLCM):
    """Menghitung nilai energy dari matriks GLCM"""
    return math.sqrt(getASM(GLCM))

def getEntropy(GLCM):
    """Menghitung nilai entropy dari matriks GLCM"""
    non_zero_elements = GLCM[GLCM != 0]
    entropy = -np.sum(non_zero_elements * np.log(non_zero_elements))
    return entropy


def getColleration(GLCM):
    """Menghitung nilai colleration dari matriks GLCM"""
    levels = len(GLCM)
    sum_row_x = np.sum(GLCM, axis=1)
    sum_row_y = np.sum(GLCM, axis=0)
    
    meanX = np.sum(np.arange(levels) * sum_row_x)
    meanY = np.sum(np.arange(levels) * sum_row_y)
    
    stdX = np.sqrt(np.sum((np.arange(levels) - meanX)**2 * sum_row_x))
    stdY = np.sqrt(np.sum((np.arange(levels) - meanY)**2 * sum_row_y))
    if stdX == 0 or stdY == 0:
        correlation = np.sum(((np.arange(levels) - meanX) * (np.arange(levels) - meanY) * GLCM))
    else:
        correlation = np.sum(((np.arange(levels) - meanX) * (np.arange(levels) - meanY) * GLCM) / (stdX * stdY))
    
    return correlation

def getTextureFeatures(ImageMatrix):
    """Menyimpan nilai contrast, dissimilarity, homogeneity, ASM, energy, dan colleration dari matriks GLCM dalam suatu vektor"""
    GLCM = buildCoOccurrenceMatrix(quantifyGrayscale(rgbToGrayscale(ImageMatrix)))
    GLCM = normalizeMatrix(getSymmetryMatrix(GLCM, transpose(GLCM)))
    featuresTemp = [getContrast(GLCM), getDissimilarity(GLCM), getHomogeneity(GLCM), getASM(GLCM), getEnergy(GLCM), getEntropy(GLCM), getColleration(GLCM)]
    return featuresTemp

def CosineSimilarity(Texture1, Texture2):
    cosineSimilarity = 0
    dot_product = 0
    normA = 0
    normB = 0
    for i in range (len(Texture1)):
        dot_product += Texture1[i] * Texture2[i]
        normA += Texture1[i]**2
        normB += Texture2[i]**2
    cosineSimilarity = dot_product / (math.sqrt(normA) * math.sqrt(normB))
    return cosineSimilarity

def decimalToPercentage(decimal):
    """Mengubah nilai desimal menjadi persentase dua angka di belakang koma"""
    return round(decimal*100, 2)
