import Image
import urllib2
import StringIO
import sys

def makeQRCode(TEXT, filein="in.png", fileout="out.png"):
    # Load Images from source and google's qr code api
    logo = Image.open(filein)
    qrcode = Image.open(
               StringIO.StringIO(
                 urllib2.urlopen("http://chart.googleapis.com/chart?chs=300x300&cht=qr&chl=" + \
            urllib2.quote(TEXT)).read()))

    # Make sure they are both in the correct format
    logo = logo.convert("RGBA")
    qrcode = qrcode.convert("RGBA")

    # Lets get access to both images at the pixel level
    pixsrc = qrcode.load()
    pixdest = logo.load()

    # Copy over only black pixels
    for y in xrange(qrcode.size[1]):
        for x in xrange(qrcode.size[0]):
            if pixsrc[x, y] == (0, 0, 0, 255):
                pixdest[x+215, y+470] = (0, 0, 0, 255)

    logo.save(fileout)

makeQRCode(sys.argv[1], "Large Scale logo.png", "full.png")
makeQRCode(sys.argv[1], "Penguin.png", "part.png")
