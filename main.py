from PIL import Image

group1 = [
    r'C:/FilePath/square/green.png',
    r'C:/FilePath/square/purple.png',
    r'C:/FilePath/square/red.png'
]

group2 = [
    r'C:/FilePath/circle/orange.png',
    r'C:/FilePath/circle/pink.png',
    r'C:/FilePath/circle/yellow.png'
]

group3 = [
    r'C:/FilePath/triangle/black.png',
    r'C:/FilePath/grey.png',
    r'C:/FilePath/white.png'
]

counter = 0


def createImage(a, b, c, counter):
    image01 = Image.open(group1[a]).convert("RGBA")
    image02 = Image.open(group2[b]).convert("RGBA")
    image03 = Image.open(group3[c]).convert("RGBA")

    intermediate = Image.alpha_composite(image01, image02)
    intermediate2 = Image.alpha_composite(intermediate, image03)
    name = "C:/Users/Jared/Documents/ProfessionalDevelopment/Web3_Bootcamp/NFTs/Done" + str(counter) + ".png"
    intermediate2.save(name)


for x in range(3):
    for y in range(3):
        for z in range(3):

            createImage(x, y, z, counter)
            counter += 1