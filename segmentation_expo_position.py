import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import pandas as pd
import matplotlib as mpl
import traceback

mpl.rcParams['legend.fontsize'] = 10

pd.set_option('display.expand_frame_repr', False)
fn = 0
path = '/result'

# Taking any image from the sample images
# #image saved from canvas.py # #
img = cv.imread('painted_image.jpg')


# In[findFeaturPoints]
def findCapPoints(img):
    cpoints = []
    dpoints = []
    for i in range(img.shape[1]):
        col = img[:, i:i + 1]
        k = col.shape[0]
        while k > 0:
            if col[k - 1] == 255:
                dpoints.append((i, k))
                break
            k -= 1

        for j in range(col.shape[0]):
            if col[j] == 255:
                cpoints.append((i, j))
                break
    return cpoints, dpoints

# In[equwrite]
#****************************************************************************#
#To find type of equation
#If polynomial then get the index where expo is present
def equwrite(l):
    exp=[]
    if len(l)==1:
        print("LINEAR EQUATION")
    else:
        for i in range(1,len(l[0])):
            p=-1
            min=9999999999
            for j in range(len(l[1])):
                if min>=abs(l[0][i]-l[1][j]):
                    min=abs(l[0][i]-l[1][j])
                    p=j
            if p>=0:
                exp.append(p)
        print("________________________")
        print("EXPOTENTS AT INDEX:",exp)
        print("________________________")

# In[wordSegment]
# *****************************************************************************#
def wordSegment(textLines):
    wordImgList = []
    counter = 0
    cl = 0
    lcount=[]
    for txtLine in textLines:
        gray = cv.cvtColor(txtLine, cv.COLOR_BGR2GRAY)
        th, threshed = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        final_thr = cv.dilate(threshed, None, iterations=20)

        #plt.imshow(final_thr)
        #plt.show()

        contours, hierarchy = cv.findContours(final_thr, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        boundingBoxes = [cv.boundingRect(c) for c in contours]
        (contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes), key=lambda b: b[1][0], reverse=False))
        print("cl_outer:",cl)
        lcon=[]
        for cnt in contours:
            area = cv.contourArea(cnt)
            print("cl_mid:", cl)
            print("area:",area)
            #  print area
            if area > 10000:
                print('Area= ', area)
                x, y, w, h = cv.boundingRect(cnt)
                print("rectangle(((",x, y, w, h,")))")
                if cl==0:
                    lcon.append(x)
                else:
                    lcon.append(x+w)
                letterBgr = txtLine[0:txtLine.shape[1], x:x + w]
                wordImgList.append(letterBgr)
                print("cl_inner:",cl)
                cv.imwrite("segl"+str(cl)+"w" + str(counter) + ".jpg", letterBgr)
                counter = counter + 1
        lcount.append(lcon)
        cl = cl + 1
    print(lcount)
    equwrite(lcount)
    return wordImgList


# *****************************************************************************#

# In[fitToSize]
# *****************************************************************************#
def fitToSize(thresh1):
    mask = thresh1 > 0
    coords = np.argwhere(mask)

    x0, y0 = coords.min(axis=0)
    x1, y1 = coords.max(axis=0) + 1  # slices are exclusive at the top
    cropped = thresh1[x0:x1, y0:y1]
    return cropped


# *****************************************************************************#

# In[lineSegment]
# *****************************************************************************#
def lineSegment(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    th, threshed = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

    upper = []
    lower = []
    flag = True
    for i in range(threshed.shape[0]):

        col = threshed[i:i + 1, :]
        cnt = 0
        if flag:
            cnt = np.count_nonzero(col == 255)
            if cnt > 0:
                upper.append(i)
                flag = False
        else:
            cnt = np.count_nonzero(col == 255)
            if cnt < 2:
                lower.append(i)
                flag = True
    textLines = []
    if len(upper) != len(lower): lower.append(threshed.shape[0])
    #    print upper
    #    print lower
    for i in range(len(upper)):
        timg = img[upper[i]:lower[i], 0:]

        if timg.shape[0] > 5:
            #            plt.imshow(timg)
            #            plt.show()
            timg = cv.resize(timg, ((timg.shape[1] * 5, timg.shape[0] * 8)))
            textLines.append(timg)

    return textLines


# *****************************************************************************#



# In[segmentCharacters]
def segmentCharacters(seg, lettergray):
    s = 0
    wordImgList = []
    global fn
    for i in range(len(seg)):
        if i == 0:
            s = seg[i]
            if s > 15:
                wordImg = lettergray[0:, 0:s]
                cntx = np.count_nonzero(wordImg == 255)
                print('count', cntx)
                plt.imshow(wordImg)
                plt.show()
                fn = fn + 1
            else:
                continue
        elif (i != (len(seg) - 1)):
            if seg[i] - s > 15:
                wordImg = lettergray[0:, s:seg[i]]
                cntx = np.count_nonzero(wordImg == 255)
                print('count', cntx)
                plt.imshow(wordImg)
                plt.show()
                fn = fn + 1
                s = seg[i]
            else:
                continue
        else:
            wordImg = lettergray[0:, seg[len(seg) - 1]:]
            cntx = np.count_nonzero(wordImg == 255)
            print('count', cntx)
            #plt.imshow(wordImg)
            #plt.show()
            fn = fn + 1
        wordImgList.append(wordImg)

    return wordImgList


# *****************************************************************************#
# In[Main]:
try:
    textLines = lineSegment(img)
    print('No. of Lines', len(textLines))
    imgList = wordSegment(textLines)
    print('No. of Words', len(imgList))

    ###---------------------------------------------------------------------------#####

    print('Original Image')
    plt.imshow(img)
    plt.show()

except Exception as e:
    print('Error Message ', e)
    cv.destroyAllWindows()
    traceback.print_exc()
    pass

traceback.print_exc()