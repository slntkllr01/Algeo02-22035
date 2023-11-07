# Reference: https://yunusmuhammad007.medium.com/feature-extraction-gray-level-co-occurrence-matrix-glcm-10c45b6d46a1
# Reference: https://www.sciencedirect.com/science/article/pii/S0895717710005352#s000030
# Reference: https://ojs.uma.ac.id/index.php/jite/article/view/3885/2785

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
        vektorQuantized.append(vektorGrayscale[i]//8)
        # if vektorGrayscale[i] < 8:
        #     vektorQuantized.append(0)
        # elif vektorGrayscale[i] < 16:
        #     vektorQuantized.append(1)
        # elif vektorGrayscale[i] < 24:
        #     vektorQuantized.append(2)
        # elif vektorGrayscale[i] < 32:
        #     vektorQuantized.append(3)
        # elif vektorGrayscale[i] < 40:
        #     vektorQuantized.append(4)
        # elif vektorGrayscale[i] < 48:
        #     vektorQuantized.append(5)
        # elif vektorGrayscale[i] < 56:
        #     vektorQuantized.append(6)
        # elif vektorGrayscale[i] < 64:
        #     vektorQuantized.append(7)
        # elif vektorGrayscale[i] < 72:
        #     vektorQuantized.append(8)
        # elif vektorGrayscale[i] < 80:
        #     vektorQuantized.append(9)
        # elif vektorGrayscale[i] < 88:
        #     vektorQuantized.append(10)
        # elif vektorGrayscale[i] < 96:
        #     vektorQuantized.append(11)
        # elif vektorGrayscale[i] < 104:
        #     vektorQuantized.append(12)
        # elif vektorGrayscale[i] < 112:
        #     vektorQuantized.append(13)
        # elif vektorGrayscale[i] < 120:
        #     vektorQuantized.append(14)
        # elif vektorGrayscale[i] < 128:
        #     vektorQuantized.append(15)
        # elif vektorGrayscale[i] < 136:
        #     vektorQuantized.append(16)
        # elif vektorGrayscale[i] < 144:
        #     vektorQuantized.append(17)
        # elif vektorGrayscale[i] < 152:
        #     vektorQuantized.append(18)
        # elif vektorGrayscale[i] < 160:
        #     vektorQuantized.append(19)
        # elif vektorGrayscale[i] < 168:
        #     vektorQuantized.append(20)
        # elif vektorGrayscale[i] < 176:
        #     vektorQuantized.append(21)
        # elif vektorGrayscale[i] < 184:
        #     vektorQuantized.append(22)
        # elif vektorGrayscale[i] < 192:
        #     vektorQuantized.append(23)
        # elif vektorGrayscale[i] < 200:
        #     vektorQuantized.append(24)
        # elif vektorGrayscale[i] < 208:
        #     vektorQuantized.append(25)
        # elif vektorGrayscale[i] < 216:
        #     vektorQuantized.append(26)
        # elif vektorGrayscale[i] < 224:
        #     vektorQuantized.append(27)
        # elif vektorGrayscale[i] < 232:
        #     vektorQuantized.append(28)
        # elif vektorGrayscale[i] < 240:
        #     vektorQuantized.append(29)
        # elif vektorGrayscale[i] < 248:
        #     vektorQuantized.append(30)
        # elif vektorGrayscale[i] < 256:
        #     vektorQuantized.append(31)
    return vektorQuantized

def buildCoOccurenceMatrixA(vektorQuantized):
    """" Membangun matriks co-occurence matriks vektor grayscale dengan jarak 1 skala 0 derajat"""
    CoOccurenceMatrix = [[0 for i in range(32)] for j in range(32)]
    for i in range(512):
        for j in range(511):
            CoOccurenceMatrix[vektorQuantized[i][j]][vektorQuantized[i][j+1]] += 1
    return CoOccurenceMatrix

def buildCoOccurenceMatrixB(vektorQuantized):
    """" Membangun matriks co-occurence matriks vektor grayscale dengan jarak 1 skala 90 derajat"""
    CoOccurenceMatrix = [[0 for i in range(32)] for j in range(32)]
    for i in range(511):
        for j in range(512):
            CoOccurenceMatrix[vektorQuantized[i][j]][vektorQuantized[i+1][j]] += 1
    return CoOccurenceMatrix

def buildCoOccurenceMatrixC(vektorQuantized):
    """" Membangun matriks co-occurence matriks vektor grayscale dengan jarak 1 skala 45 derajat"""
    CoOccurenceMatrix = [[0 for i in range(32)] for j in range(32)]
    for i in range(1, 512):
        for j in range(511):
            CoOccurenceMatrix[vektorQuantized[i][j]][vektorQuantized[i-1][j+1]] += 1
    return CoOccurenceMatrix

def buildCoOccurenceMatrixD(vektorQuantized):
    """" Membangun matriks co-occurence matriks vektor grayscale dengan jarak 1 skala 135 derajat"""
    CoOccurenceMatrix = [[0 for i in range(32)] for j in range(32)]
    for i in range(1, 512):
        for j in range(1, 512):
            CoOccurenceMatrix[vektorQuantized[i][j]][vektorQuantized[i-1][j-1]] += 1
    return CoOccurenceMatrix
    
def transpose(matrix):
    """ Transpose matrix """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def getSymmetryMatrix(matrix1, matrix2):
    """ Sum two matrix """
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1))] for i in range(len(matrix1[0]))]

def normalizeMatrix(matrix):
    """ Normalize matrix """
    sum = 0
    matrix1 = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            sum += matrix[i][j]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix1[i][j] = matrix[i][j]/sum
    return matrix1

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
            homogeneity += GLCM[i][j]/(1 + (i-j)**2)
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

def getEntropy(GLCM):
    """Menghitung nilai entropy dari matriks GLCM"""
    entropy = 0
    for i in range(0, len(GLCM)):
        for j in range(0, len(GLCM)):
            if GLCM[i][j] != 0:
                entropy += GLCM[i][j] * math.log(GLCM[i][j])
    return -entropy

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

def getTextureFeatures(ImageMatrix):
    """Menyimpan nilai contrast, dissimilarity, homogeneity, ASM, energy, dan colleration dari matriks GLCM dalam suatu vektor"""
    GLCM1A = buildCoOccurenceMatrixA(quantifyGrayscale(rgbToGrayscale(ImageMatrix)))
    GLCM1B = buildCoOccurenceMatrixB(quantifyGrayscale(rgbToGrayscale(ImageMatrix)))
    GLCM1C = buildCoOccurenceMatrixC(quantifyGrayscale(rgbToGrayscale(ImageMatrix)))
    GLCM1D = buildCoOccurenceMatrixD(quantifyGrayscale(rgbToGrayscale(ImageMatrix)))
    GLCM1A = normalizeMatrix(getSymmetryMatrix(GLCM1A, transpose(GLCM1A)))
    GLCM1B = normalizeMatrix(getSymmetryMatrix(GLCM1B, transpose(GLCM1B)))
    GLCM1C = normalizeMatrix(getSymmetryMatrix(GLCM1C, transpose(GLCM1C)))
    GLCM1D = normalizeMatrix(getSymmetryMatrix(GLCM1D, transpose(GLCM1D)))

    contrastData = [getContrast(GLCM1A), getContrast(GLCM1B), getContrast(GLCM1C), getContrast(GLCM1D)]
    dissimilarityData = [getDissimalirity(GLCM1A), getDissimalirity(GLCM1B), getDissimalirity(GLCM1C), getDissimalirity(GLCM1D)]
    homogeneityData = [getHomogeneity(GLCM1A), getHomogeneity(GLCM1B), getHomogeneity(GLCM1C), getHomogeneity(GLCM1D)]
    ASMData = [getASM(GLCM1A), getASM(GLCM1B), getASM(GLCM1C), getASM(GLCM1D)]
    energyData = [getEnergy(GLCM1A), getEnergy(GLCM1B), getEnergy(GLCM1C), getEnergy(GLCM1D)]
    entropyData = [getEntropy(GLCM1A), getEntropy(GLCM1B), getEntropy(GLCM1C), getEntropy(GLCM1D)]
    collerationData = [getColleration(GLCM1A), getColleration(GLCM1B), getColleration(GLCM1C), getColleration(GLCM1D)]
    
    return [contrast, dissimilarity, homogeneity, ASM, energy, entropy, colleration]


def compareByTexture(Texture1, Texture2):
    cosineSimilarity = 0
    for i in range (len(Texture1)):
        dot_product += Texture1[i] * Texture2[i]
        normA += Texture1[i]**2
        normB += Texture2[i]**2
    cosineSimilarity = dot_product / (math.sqrt(normA) * math.sqrt(normB))
    # lakukan cosine similarity
    return cosineSimilarity



def decimalToPercentage(decimal):
    """Mengubah nilai desimal menjadi persentase dua angka di belakang koma"""
    return round(decimal*100, 2)
