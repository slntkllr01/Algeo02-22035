# Reference: https://yunusmuhammad007.medium.com/feature-extraction-gray-level-co-occurrence-matrix-glcm-10c45b6d46a1
# Reference: https://www.sciencedirect.com/science/article/pii/S0895717710005352#s000030
# Reference: https://ojs.uma.ac.id/index.php/jite/article/view/3885/2785

import math
import numpy as np

def rgbToGrayscale(vektorRGB):
    """Mengubah nilai vektor RGB menjadi Grayscale """
    vektorGrayscale = [[0 for i in range(len(vektorRGB))] for j in range (len(vektorRGB))]
    for i in range(0, len(vektorRGB)):
        for j in range (0, len(vektorRGB)):
            r = vektorRGB[i][j][0]
            g = vektorRGB[i][j][1]
            b = vektorRGB[i][j][2]
            vektorGrayscale[i][j]=round(0.29*r + 0.587*g + 0.114*b)
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

def buildCoOccurenceMatrixA(vektorQuantized):
    """" Membangun matriks co-occurence matriks vektor grayscale dengan jarak 1 skala 0 derajat"""
    CoOccurenceMatrix = [[0 for i in range(128)] for j in range(128)]
    length = len(vektorQuantized)
    for i in range(length):
        for j in range(length-1):
            CoOccurenceMatrix[vektorQuantized[i][j]][vektorQuantized[i][j+1]] += 1
    return CoOccurenceMatrix

def buildCoOccurenceMatrixB(vektorQuantized):
    """" Membangun matriks co-occurence matriks vektor grayscale dengan jarak 1 skala 90 derajat"""
    CoOccurenceMatrix = [[0 for i in range(128)] for j in range(128)]
    length = len(vektorQuantized)
    for i in range(length-1):
        for j in range(length):
            CoOccurenceMatrix[vektorQuantized[i][j]][vektorQuantized[i+1][j]] += 1
    return CoOccurenceMatrix

def buildCoOccurenceMatrixC(vektorQuantized):
    """" Membangun matriks co-occurence matriks vektor grayscale dengan jarak 1 skala 45 derajat"""
    CoOccurenceMatrix = [[0 for i in range(128)] for j in range(128)]
    length = len(vektorQuantized)
    for i in range(1, length):
        for j in range(length-1):
            CoOccurenceMatrix[vektorQuantized[i][j]][vektorQuantized[i-1][j+1]] += 1
    return CoOccurenceMatrix

def buildCoOccurenceMatrixD(vektorQuantized):
    """" Membangun matriks co-occurence matriks vektor grayscale dengan jarak 1 skala 135 derajat"""
    CoOccurenceMatrix = [[0 for i in range(128)] for j in range(128)]
    length = len(vektorQuantized)
    for i in range(1, length):
        for j in range(1, length):
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

    # contrast = sum(contrastData)/len(contrastData)
    # dissimilarity = sum(dissimilarityData)/len(dissimilarityData)
    # homogeneity = sum(homogeneityData)/len(homogeneityData)
    # ASM = sum(ASMData)/len(ASMData)
    # energy = sum(energyData)/len(energyData)
    # entropy = sum(entropyData)/len(entropyData)
    # colleration = sum(collerationData)/len(collerationData)

    # n = 4
    # squared_differences = [(x - contrast) ** 2 for x in contrastData]
    # contrastStandardDeviation = (sum(squared_differences) / n) ** 0.5
    # squared_differences = [(x - dissimilarity) ** 2 for x in dissimilarityData]
    # dissimilarityStandardDeviation = (sum(squared_differences) / n) ** 0.5
    # squared_differences = [(x - homogeneity) ** 2 for x in homogeneityData]
    # homogeneityStandardDeviation = (sum(squared_differences) / n) ** 0.5
    # squared_differences = [(x - ASM) ** 2 for x in ASMData]
    # ASMStandardDeviation = (sum(squared_differences) / n) ** 0.5
    # squared_differences = [(x - energy) ** 2 for x in energyData]
    # energyStandardDeviation = (sum(squared_differences) / n) ** 0.5
    # squared_differences = [(x - entropy) ** 2 for x in entropyData]
    # entropyStandardDeviation = (sum(squared_differences) / n) ** 0.5
    # squared_differences = [(x - colleration) ** 2 for x in collerationData]
    # collerationStandardDeviation = (sum(squared_differences) / n) ** 0.5

    # featuresTemp = [contrast, contrastStandardDeviation, dissimilarity, dissimilarityStandardDeviation, homogeneity, homogeneityStandardDeviation, ASM, ASMStandardDeviation, energy, energyStandardDeviation, entropy, entropyStandardDeviation, colleration, collerationStandardDeviation]
    # internal normalization gaussian distribution from array featuresTemp

    featuresTemp = contrastData + dissimilarityData + homogeneityData + ASMData + energyData + entropyData + collerationData
    # textureFeature = []
    # for i in range(len(featuresTemp)):
    #     mean = sum(featuresTemp) / len(featuresTemp)
    #     stdev = math.sqrt(sum([(x - mean) ** 2 for x in featuresTemp]) / len(featuresTemp))
    #     textureFeature.append((featuresTemp[i] - mean) / stdev)
    return featuresTemp

def compareByTexture(Texture1, Texture2):
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
