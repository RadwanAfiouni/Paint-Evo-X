import numpy as np
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image, ImageEnhance, ImageFilter, ImageDraw
import random


class Picture:

    def __init__(self, path):

        self.path = path

       
        self.matrix = np.asarray(Image.open(self.path))



        self.height = self.matrix.shape[0]
        self.width  = self.matrix.shape[1]
        
        self.res = (str(self.width) + 'x' + str(self.height))
    
        self.image = Image.open(self.path)
        self.temp  = Image.open(self.path)
        self.temp2 = self.image.copy()

        self.st_var = IntVar() #saturation factor
        self.sp_var = IntVar() #sharpness factor

        self.b_var = IntVar()  #brightness factor
        self.c_var = IntVar()  #contrastfactor

        self.r_var = IntVar()  #red multiplier
        self.g_var = IntVar()  #green multiplier
        self.b_var = IntVar()  #blue multiplier

        self.gb_var = IntVar() #gaussian blur radius
        self.bb_var = IntVar() #box blur raidus

        self.undolist = []
        self.redolist = []
        self.undolist.append(self.image)

    ###################################### TOOLS

    def revert(self):

        self.temp = self.image
        self.matrix = np.asarray(self.image)
        self.temp2 = self.image.copy()

    def confirm(self):

        self.image = self.temp
        self.matrix = np.asarray(self.temp)
        self.temp2 = self.image.copy()


        self.st_var.set(0)
        self.sp_var.set(0)
        
        self.b_var.set(0)
        self.c_var.set(0) 

        self.r_var.set(0)
        self.g_var.set(0)
        self.b_var.set(0)

        self.gb_var.set(0)
        self.bb_var.set(0)

        self.undolist.append(self.image)

    def brush(self,x1,y1,x2,y2,color):

               
        draw = ImageDraw.Draw(self.temp2)
        draw.ellipse([x1, y1, x2, y2],color,width = 0)
        


    def marker(self,x1,y1,x2,y2,color):

        draw = ImageDraw.Draw(self.temp2)
        draw.rectangle([x1+0.7, y1+0.7, x2-0.7, y2-0.7],color,width = 0)

    def flatten(self):
        self.temp = self.temp2.copy()
        self.image = self.temp
        self.matrix = np.asarray(self.temp)
        self.undolist.append(self.image)


    ###################################### EDIT MENU

    def undo(self):

        #print(len(self.undolist))
        
        if len(self.undolist) == 1:
            
            pass

        
        else:
            
            self.redolist.append(self.undolist[-1])
            del(self.undolist[-1])
            self.temp=self.undolist[-1]
            self.image = self.temp
            self.matrix = np.asarray(self.temp)
            self.height = self.matrix.shape[0]
            self.width  = self.matrix.shape[1]
            self.res = (str(self.width) + 'x' + str(self.height))
            self.temp2 = self.image.copy()




            

    def redo(self):

        #print(len(self.undolist))

        if self.redolist==[]:
            #print('max redo')
         #self.redo.configure(state='!active')
            pass
  
        else:
             self.temp=self.redolist[-1]
    
             self.undolist.append(self.redolist[-1])
             del(self.redolist[-1])
             self.image = self.temp
             self.matrix = np.asarray(self.temp)
             self.height = self.matrix.shape[0]
             self.width  = self.matrix.shape[1]
             self.res = (str(self.width) + 'x' + str(self.height))
             self.temp2 = self.image.copy()



 



    ###################################### IMAGE MENU

    def resize(self, width, height):
        
        self.width = width.get()
        self.height = height.get()
        self.temp = self.image.resize((self.width,self.height),Image.ANTIALIAS)
        self.res = (str(self.width) + 'x' + str(self.height))
        
        self.undolist.append(self.image)

    def unresize(self,orig,orig_shape):

        self.temp = orig
        self.width = orig_shape[0]
        self.height = orig_shape[1]
        self.res = (str(self.width) + 'x' + str(self.height))
        self.confirm()
        

    def crop(self, area):
        
        self.temp = self.temp.crop(area)
        self.image = self.temp
        self.matrix = np.asarray(self.temp)
        self.height = self.matrix.shape[0]
        self.width  = self.matrix.shape[1]
        self.temp2 = self.image.copy()

        
        self.undolist.append(self.image)


    def flipH(self):

        self.matrix = self.matrix[:, ::-1]
        self.temp = Image.fromarray(self.matrix)
        self.image = self.temp
        self.temp2 = self.image.copy()

        
        self.undolist.append(self.image)

    def flipV(self):

        self.matrix = self.matrix[::-1,:]
        self.temp = Image.fromarray(self.matrix)
        self.image = self.temp
        self.temp2 = self.image.copy()

        
        self.undolist.append(self.image)


    def rotateClockwise(self):

        self.matrix = np.rot90(self.matrix, 3)
        self.temp = Image.fromarray(self.matrix)
        self.image = self.temp
        self.temp2 = self.image.copy()
        self.undolist.append(self.image)

    def rotateCounterClockwise(self):

        self.matrix = np.rot90(self.matrix)
        self.temp = Image.fromarray(self.matrix)
        self.image = self.temp
        self.temp2 = self.image.copy()
        self.undolist.append(self.image)

    ###################################### ADJUSTMENTS MENU

    def sharpnessSaturation(self):

        self.temp = self.image
        
        self.factor_sp = 1 + self.sp_var.get() / 100
        self.factor_st = 1 + self.st_var.get() / 100

        self.temp = ImageEnhance.Sharpness(self.temp).enhance(self.factor_sp)
        self.temp = ImageEnhance.Color(self.temp).enhance(self.factor_st)

    def blackWhite(self):

        self.matrix = np.asarray(self.image)
        self.matrix = np.copy(self.matrix)
       
        r = 0.2990 * self.matrix[:,:,0] #This splits the rgb channels of the image matrix
        g = 0.5870 * self.matrix[:,:,1]
        b = 0.1140 * self.matrix[:,:,2]

        rgb = r + g + b #this creates a 2D array of the rgb channels
        
        for i in range(3): #transforming the 2D array into a 3D array

            self.matrix[:,:,i] = rgb

        self.temp = Image.fromarray(self.matrix)
        self.image = self.temp
        self.temp2 = self.image.copy()
        
        self.undolist.append(self.image)
    

    def brightnessContrast(self):

        self.temp = self.image

        self.factor_b = 1 + self.b_var.get() / 100
        self.factor_c = 1 + self.c_var.get() / 100        

        self.temp = ImageEnhance.Brightness(self.temp).enhance(self.factor_b)
        self.temp = ImageEnhance.Contrast(self.temp).enhance(self.factor_c)

    def colorLevels(self):

        self.matrix = np.asarray(self.image)
        self.matrix = np.copy(self.matrix)

        r = (self.r_var.get() /100) * self.matrix[:,:,0] #This splits the rgb channels of the image matrix
        g = (self.g_var.get() /100) * self.matrix[:,:,1]
        b = (self.b_var.get() /100) * self.matrix[:,:,2]

        rgb = [r,g,b]

        for i in range(3): #transforming the 2D array into a 3D array

            self.matrix[:,:,i] = rgb[i]

        self.temp = Image.fromarray(self.matrix)

    def invertColors(self):

        self.matrix = np.asarray(self.image)


        self.matrix = np.copy(self.matrix)
        self.matrix = 255 - self.matrix

        self.temp = Image.fromarray(self.matrix)
        self.image = self.temp
        self.temp2 = self.image.copy()
        
        self.undolist.append(self.image)
       
    ###################################### EFFECTS MENU

    def emboss(self): 

        self.temp = self.image.filter(ImageFilter.EMBOSS)
        self.image = self.temp
        self.temp2 = self.image.copy()
        
        self.undolist.append(self.image)

    def addNoise(self):

        self.matrix = np.asarray(self.image)
        self.matrix = np.copy(self.matrix)

        r,g,b = random.randint(0, 255) , random.randint(0, 255), random.randint(0, 255)

        matrix = np.random.random((self.matrix.shape[0],self.matrix.shape[1])) #this create a matrix with random floats between 0 and 1
        
        for x in range(matrix.shape[0]): #the following lines go over each element of the matrix

            for y in range(matrix.shape[1]):

                if matrix[x,y] <= 0.01: #if an element is below the selected probability, the pixel is whitened

                    self.matrix[x,y] = np.array([r,g,b]) #this noisens the pixel

        self.temp = Image.fromarray(self.matrix)
        self.image = self.temp
        self.temp2 = self.image.copy()
        
        self.undolist.append(self.image)

    def gaussian(self):

        self.radius = self.gb_var.get()/100
        
        self.temp = (self.image).filter(ImageFilter.GaussianBlur(self.radius))

    def box(self):

        self.radius = self.bb_var.get()/100
        
        self.temp = (self.image).filter(ImageFilter.BoxBlur(self.radius))


    def soften(self):

        self.temp = self.image.filter(ImageFilter.SMOOTH)
        self.image = self.temp
        self.temp2 = self.image.copy()
        self.undolist.append(self.image)

    def edges(self):

        self.temp = self.image.filter(ImageFilter.FIND_EDGES)
        self.image = self.temp
        self.temp2 = self.image.copy()
        self.undolist.append(self.image)

        

  
