# Reference: https://yunusmuhammad007.medium.com/feature-extraction-gray-level-co-occurrence-matrix-glcm-10c45b6d46a1
# Reference: https://www.sciencedirect.com/science/article/pii/S0895717710005352#s000030

from extract import *

def rgbToGrayscale(vektorRGB):
    """Mengubah nilai vektor RGB menjadi Grayscale """
    vektorGrayscale = []
    for i in range(0, len(vektorRGB)):
        r = vektorRGB[i][0]
        g = vektorRGB[i][1]
        b = vektorRGB[i][2]
        vektorGrayscale.append(round(0.29*r + 0.587*g + 0.114*b))
    return vektorGrayscale

def quantifyGrayscale(vektorGrayscale):
    """[optional] for faster processing, quantize grayscale value.
    The idea is like the following, but the quantization number lets discuss"""
    vektorQuantized = []
    for i in range(0, len(vektorGrayscale)):
        if vektorGrayscale[i] < 64:
            vektorQuantized.append(0)
        elif vektorGrayscale[i] < 128:
            vektorQuantized.append(1)
        elif vektorGrayscale[i] < 192:
            vektorQuantized.append(2)
        else:
            vektorQuantized.append(3)
    return vektorQuantized

def buildCoOccurenceMatrix(distances, angles):
    """" Membangun matriks co-occurence matriks vektor grayscale.
    Ini susah, banyak banget referensi bingung mau yangmana."""
    CoOccurenceMatrix = []
    return CoOccurenceMatrix

def transpose(matrix):
    """ Transpose matrix """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def getSymmetryMatrix(matrix1, matrix2):
    """ Sum two matrix """
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1))] for i in range(len(matrix1[0]))]

def normalizeMatrix(matrix):
    """ Normalize matrix """
    return [[matrix[i][j]/sum(matrix[i]) for j in range(len(matrix))] for i in range(len(matrix[0]))]

def getContrast(GLCM):
    """Menghitung nilai contrast dari matriks GLCM"""
    contrast = 0
    for i in range(0, len(GLCM)):
        for j in range(0, len(GLCM)):
            contrast += (i-j)**2 * GLCM[i][j]
    return contrast

def getDissimalirity(GLCM):
    """Menghitung nilai dissimilarity dari matriks GLCM"""
    dissimilarity = 0
    for i in range(0, len(GLCM)):
        for j in range(0, len(GLCM)):
            dissimilarity += abs(i-j) * GLCM[i][j]
    return dissimilarity

def getHomogeneity(GLCM):
    """Menghitung nilai homogeneity dari matriks GLCM"""
    homogeneity = 0
    for i in range(0, len(GLCM)):
        for j in range(0, len(GLCM)):
            homogeneity += GLCM[i][j]/(1 + abs(i-j))
    return homogeneity

def getASM(GLCM):
    """Menghitung nilai ASM dari matriks GLCM"""
    ASM = 0
    for i in range(0, len(GLCM)):
        for j in range(0, len(GLCM)):
            ASM += GLCM[i][j]**2
    return ASM

def getEnergy(GLCM):
    """Menghitung nilai energy dari matriks GLCM"""
    return math.sqrt(getASM(GLCM))

def getColleration(GLCM):
    """Menghitung nilai colleration dari matriks GLCM"""
    meanX = 0
    meanY = 0
    stdX = 0
    stdY = 0
    for i in range(0, len(GLCM)):
        for j in range(0, len(GLCM)):
            meanX += i * GLCM[i][j]
            meanY += j * GLCM[i][j]
    for i in range(0, len(GLCM)):
        for j in range(0, len(GLCM)):
            stdX += (i - meanX)**2 * GLCM[i][j]
            stdY += (j - meanY)**2 * GLCM[i][j]
    stdX = math.sqrt(stdX)
    stdY = math.sqrt(stdY)
    colleration = 0
    for i in range(0, len(GLCM)):
        for j in range(0, len(GLCM)):
            colleration += ((i - meanX) * (j - meanY) * GLCM[i][j])/(stdX * stdY)
    return colleration

def getTextureFeatures(GLCM):
    """Menyimpan nilai contrast, dissimilarity, homogeneity, ASM, energy, dan colleration dari matriks GLCM dalam suatu vektor"""
    contrast = getContrast(GLCM)
    dissimilarity = getDissimalirity(GLCM)
    homogeneity = getHomogeneity(GLCM)
    ASM = getASM(GLCM)
    energy = getEnergy(GLCM)
    colleration = getColleration(GLCM)
    return [contrast, dissimilarity, homogeneity, ASM, energy, colleration]


def compareByTexture(GLCM1, GLCM2):
    cosineSimilarity = 0
    textureFeature1 = getTextureFeatures(GLCM1)
    textureFeature1 = getTextureFeatures(GLCM2)
    # lakukan cosine similarity
    return cosineSimilarity
