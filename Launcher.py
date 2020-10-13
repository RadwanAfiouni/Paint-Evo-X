print('importing libraries')
import numpy as np
from tkinter import*
from tkinter import ttk, filedialog, colorchooser, messagebox
from PIL import ImageTk,Image
import os
from Main import *
import matplotlib.pyplot as plt
import operator
#import time



class Application:

    def __init__(self, window):



        self.window = window
        self.menubar = Menu(self.window)

        ############################################## MAIN CANVAS

        self.root_canvas = Canvas(self.window, bg = '#d0d0d0')
        self.root_canvas.grid(row = 0, column = 0, sticky = (N,S,E,W))

        self.root_canvas.rowconfigure(0,weight = 1)
        self.root_canvas.columnconfigure(0,weight = 1)


        ############################################## IMAGE FRAME

        self.img_frame = Frame(self.root_canvas, bg = '#d0d0d0')
        self.img_frame.grid(sticky = (N,S,E,W))


        self.img_frame.rowconfigure(0,weight = 1)
        self.img_frame.columnconfigure(0,weight = 1)
        
        self.img_canvas = self.root_canvas.create_window((self.root_canvas.winfo_width()/2, self.root_canvas.winfo_height()/2),anchor = 'center', window = self.img_frame)
        

        ############################################## SECONDARY CANVAS 

        self.canvas = Canvas(self.img_frame, bg = 'white', width = 0, height = 0, highlightthickness=0.5, highlightbackground="black", cursor = 'cross')
        self.canvas.grid(row = 0, column = 0)

        #self.canvas.create_image(0,0,image = ImageTk.PhotoImage(Image.fromarray(np.zeros([500,700,3]).astype(np.uint8))), anchor = NW)

        ############################################## SCROLLBARS

        self.x_scrl = ttk.Scrollbar(self.window, orient = HORIZONTAL, command = self.root_canvas.xview)
        self.x_scrl.grid(row = 2, column = 0, sticky = (E,W))

        self.y_scrl = ttk.Scrollbar(self.window, orient = VERTICAL, command = self.root_canvas.yview)
        self.y_scrl.grid(sticky = (N,S), row = 0, column = 1)

        self.root_canvas.configure(yscrollcommand = self.y_scrl.set, xscrollcommand = self.x_scrl.set)
        #self.root_canvas.configure(scrollregion = self.canvas.bbox("all"))

        ############################################## INFO FRAME


        self.info_name = StringVar()
        self.info_res  = StringVar()
        self.info_pos  = StringVar()

        self.img7 = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\resolution.png').resize((24,24)))
        self.img8 = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\target.png').resize((24,24)))
        self.img9 = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\folder.png').resize((24,24)))


        self.info_name.set(os.getcwd())
        self.info_res.set('700x500')

        self.info_frame = ttk.Frame(window, height = 20)
        self.info_frame.grid(row = 1000, sticky = (S,E,W))

        self.info_frame.columnconfigure(0,weight = 2)
        self.info_frame.columnconfigure(3,weight = 100)
        self.info_frame.columnconfigure(6,weight = 2)
        self.info_frame.columnconfigure(9,weight = 2)

        self.info_label_name_1 = ttk.Label(self.info_frame, image = self.img9)
        self.info_label_name_2 = ttk.Label(self.info_frame, textvariable = self.info_name)


        self.info_label_res_1 = ttk.Label(self.info_frame, image = self.img7)
        self.info_label_res_2 = ttk.Label(self.info_frame, textvariable = self.info_res)

        self.info_label_pos_1 = ttk.Label(self.info_frame, image = self.img8)
        self.info_label_pos_2 = ttk.Label(self.info_frame, textvariable = self.info_pos)

        self.info_label_name_1.grid(row = 0,column = 1, sticky = W)
        self.info_label_name_2.grid(row = 0,column = 2, sticky = W)

        self.info_label_pos_1.grid(row = 0, column = 4)
        self.info_label_pos_2.grid(row = 0, column = 5)

        self.info_label_res_1.grid(row = 0, column = 7, sticky = E) 
        self.info_label_res_2.grid(row = 0, column = 8, sticky = E)

        ############################################ DRAWING FRAME

        self.color = (0,'black')

        self.drawing_frame = Frame(self.window, bg = '#d0d0d0',height = 150, width = 75)
        self.drawing_frame.grid(row = 0, column = 0, sticky = (W))

        self.img1 = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\brush.png').resize((32,32)))
        self.img2 = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\marker.png').resize((32,32)))
        self.img3 = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\check.png').resize((32,32)))
        self.img4 = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\palette.png').resize((32,32)))
        self.img5 = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\eraser.png').resize((32,32)))
        self.img6 = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\thickness.png').resize((32,32)))
        self.img12 = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\brush2.png').resize((32,32)))
        self.img13 = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\marker2.png').resize((32,32)))



        self.BTN1 = ttk.Button(self.drawing_frame, image = self.img1, command = lambda:[self.canvas.bind('<B1-Motion>', self.brush),self.canvas.bind('<Button-1>', self.brush),self.BTN1.configure(image = self.img12),self.BTN2.configure(image=self.img2)])
        self.BTN2 = ttk.Button(self.drawing_frame, image = self.img2, command = lambda:[self.canvas.bind('<B1-Motion>', self.marker),self.canvas.bind('<Button-1>', self.marker), self.BTN2.configure(image=self.img13),self.BTN1.configure(image=self.img1)])
        self.BTN6 = ttk.Button(self.drawing_frame, image = self.img3, command = self.flatten)
        self.BTN4 = ttk.Button(self.drawing_frame, image = self.img4, command = self.getColor)
        self.BTN5 = ttk.Button(self.drawing_frame, image = self.img5, command = self.erase)
        self.BTN3 = ttk.Button(self.drawing_frame, image = self.img6, command = self.getThickness)

        self.color_label = Button(self.drawing_frame, bg = self.color[1], width = 10, height  = 1, borderwidth = 2, relief = 'sunken',command = self.getColor)
         
        self.BTN1.grid(row = 0, column = 0)
        self.BTN2.grid(row = 0, column = 1)
        self.BTN3.grid(row = 1, column = 0)
        self.BTN4.grid(row = 1, column = 1)
        self.BTN5.grid(row = 2, column = 0)
        self.BTN6.grid(row = 2, column = 1)

        self.color_label.grid(row = 3, column = 0, columnspan = 2, pady = 4)


        
        self.t = IntVar()
        self.t.set(3)

        self.window.bind('<Double-Button-3>', self.right)

        
        ############################################ MENUBARS

        self.window['menu']=self.menubar

        self.menu_file=Menu(self.menubar, tearoff = 0) #Menu file
        self.menubar.add_cascade(menu=self.menu_file,label='File')

        self.menu_file.add_command(label='New',command=self.new)
        self.menu_file.add_command(label='Open',command=self.load)
        self.menu_recent=Menu(self.menu_file, tearoff = 0)
        self.menu_file.add_cascade(menu=self.menu_recent,label='Recent')

        
        self.menu_file.add_command(label='Save',command=self.save)
        self.menu_file.add_command(label='Save As...',command=self.saveAs)
        self.menu_share=Menu(self.menu_file, tearoff = 0)
##        self.menu_file.add_cascade(menu=self.menu_share,label='Share',command=self.share) 
##        self.menu_share.add_command(label='Instagram',command=self.instagram)
##        self.menu_share.add_command(label='Facebook',command=self.facebook)
##        self.menu_share.add_command(label='Twitter',command=self.twitter)
        self.menu_file.add_separator()
        self.menu_file.add_command(label='Exit',command=self.on_close)

        self.menu_file.entryconfig(2, state = 'disabled')
        self.menu_file.entryconfig(3, state = 'disabled')
        self.menu_file.entryconfig(4, state = 'disabled')
        #self.menu_file.entryconfig(5, state = 'disabled')





        self.menu_edit=Menu(self.menubar, tearoff = 0) #Menu edit
        self.menubar.add_cascade(menu=self.menu_edit,label='Edit')

        self.menu_edit.add_command(label='Undo',command=self.undo)
        self.menu_edit.add_command(label='Redo',command=self.redo)

        self.menu_edit.entryconfig(0, state = 'disabled')
        self.menu_edit.entryconfig(1, state = 'disabled')



        self.menu_view=Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(menu=self.menu_view,label='View')

        self.menu_view.add_command(label='Zoom In',command=self.zoomIn)
        self.menu_view.add_command(label='Zoom Out',command=self.zoomOut)
        self.menu_view.add_command(label='Zoom Auto',command=self.zoomAuto)
        self.menu_view.add_separator()
        self.menu_view.add_command(label='Grid',command=self.grid)
        #self.menu_view.add_command(label='Ruler',command=self.ruler)


        self.menu_image=Menu(self.menubar, tearoff = 0) #Menu image
        self.menubar.add_cascade(menu=self.menu_image,label='Image')

        self.menu_image.add_command(label='Get Histogram',command=self.histo)
        self.menu_image.add_separator()
        self.menu_image.add_command(label='Crop',command=self.crop)
        self.menu_image.add_command(label='Resize...',command=self.resize)
        self.menu_image.add_separator()
        self.menu_image.add_command(label='Flip Horizontal',command=self.flipH)
        self.menu_image.add_command(label='Flip Vertical',command=self.flipV)
        self.menu_image.add_separator()
        self.menu_image.add_command(label='Rotate Clockwise',command=self.rotateClockwise)
        self.menu_image.add_command(label='Rotate Counter Clockwise',command=self.rotateCounterClockwise)


        self.menu_adjustments=Menu(self.menubar, tearoff = 0) #Menu adjusments
        self.menubar.add_cascade(menu=self.menu_adjustments,label='Adjustments')

        self.menu_adjustments.add_command(label='Sharpness / Saturation',command=self.sharpnessSaturation)
        self.menu_adjustments.add_command(label='Black and White',command=self.blackWhite)
        self.menu_adjustments.add_command(label='Brightness / Contrast',command=self.brightnessContrast)
        self.menu_adjustments.add_command(label='Color Levels',command=self.colorLevels)
        self.menu_adjustments.add_command(label='Invert Colors',command=self.invertColors)


        self.menu_effects=Menu(self.menubar, tearoff = 0) #Menu effects
        self.menubar.add_cascade(menu=self.menu_effects,label='Effects')

        self.menu_effects.add_command(label='Emboss',command=self.emboss)
        self.menu_effects.add_command(label='Soften',command=self.soften)
        self.menu_effects.add_command(label='Edges',command=self.edges)
        self.menu_effects.add_command(label='Add Noise',command=self.addNoise)
        self.menu_blur=Menu(self.menu_effects, tearoff = 0)
        self.menu_effects.add_cascade(label='Blurs',menu=self.menu_blur)
        self.menu_blur.add_command(label='Gaussian Blur',command=self.gaussian)
        self.menu_blur.add_command(label='Box Blur',command=self.box)

        self.menubar.bind("<<MenuSelect>>", self.select_test)

        self.info_pos.set(self.canvas.bind('<Motion>', self.pos_update))
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        self.window.bind('<Configure>',self.configure)

        self.menubar.entryconfig(2, state=DISABLED)
        self.menubar.entryconfig(3, state=DISABLED)
        self.menubar.entryconfig(4, state=DISABLED)
        self.menubar.entryconfig(5, state=DISABLED)
        self.menubar.entryconfig(6, state=DISABLED)

        self.x , self.y = 0, 0
        self.info_pos.set('{}, {}'.format(self.x, self.y))


        self.coef = 1

        self.flag = True
        self.saved = True
        self.named = False
        self.start = True
        self.configure(self)
        #self.geom = (701,501)

        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        
        self.window.bind("<Control-z>", self.undo)
        self.window.bind("<Control-y>", self.redo)
##        self.window.bind("<Control-Key-+>", self.zoomIn)
##        self.window.bind("<Control-Key-->", self.zoomOut)
        self.window.bind("<Control-a>", self.zoomAuto)



        

        self.new()
        self.recent()
        self.tmp_canvas = Canvas(self.window, bg = '#d0d0d0')
        
        self.tmp_canvas.grid(row = 0, column = 0,rowspan = 1001, columnspan = 100, sticky = (N,S,E,W))

    

    ###################################### TOOLS

    def _on_mousewheel(self, event):
        self.root_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def on_close(self):

        if self.saved == False or self.flag == False:

            bl = messagebox.askyesnocancel("Quit", "Do you want to save before quitting ?\nUnsaved changes will be lost forever (a really long time !)")
         
            if bl  == True:

                self.flatten()

                if self.named:

                    self.save()

                else :

                    try:
                        self.saveAs()
                    except FileNotFoundError:
                        return
                    except AttributeError:
                        return

                self.window.destroy()

            elif bl == False:

                self.window.destroy()

        else:

            if messagebox.askokcancel("Quit", "Do you really want to quit ?"):

                self.window.destroy()


    def select_test(self, event):

        if self.flag != True:

            messagebox.showwarning('Warning',"You must flatten the image before proceeding!\n               (hint: it's the check button)")
            
 

    def pos_update(self, event):
        
        
        
        self.x, self.y = int(self.coef * event.x), int(self.coef * event.y)
        self.info_pos.set('{}, {}'.format(self.x, self.y))
        
        return self.info_pos.get()

    def configure(self,event):

        #self.geom = (2 * self.root_canvas.winfo_width() - self.canvas.winfo_width(),2* self.root_canvas.winfo_height()- self.canvas.winfo_height())
        self.geom = (self.canvas.winfo_width(),self.canvas.winfo_height())
        #print(self.geom)
        #self.root_canvas.coords(self.img_canvas,(self.geom[0]/2, self.geom[1]/2))


    def img_update(self, r = False):

        self.canvas.delete('im')

        self.image = self.main.temp
        self.info_res.set(self.main.res)

        if not r: self.saved = False
        
        self.image = ImageTk.PhotoImage(self.image.resize((self.width, self.height), Image.ANTIALIAS))
        self.canvas.create_image(0,0,image = self.image, anchor = NW, tags = 'im')
        self.canvas.configure(width = self.width-1, height = self.height-1)
        

        if self.canvas.find_withtag('grid') != ():

            self.canvas.delete('grid')
            self.grid()

        if len(self.main.undolist) == 1:

            self.menu_edit.entryconfig(0, state = 'disabled')

        else:

            self.menu_edit.entryconfig(0, state = 'normal')

        if self.main.redolist == []:
            
            self.menu_edit.entryconfig(1, state = 'disabled')

        else:

            self.menu_edit.entryconfig(1, state = 'normal')


        
        self.root_canvas.configure(scrollregion = (-self.geom[0],-self.geom[1]) + (self.geom[0],self.geom[1]))
        #print((-self.geom[0],-self.geom[1]) + (self.geom[0],self.geom[1]))
        
        #self.root_canvas.configure(scrollregion = (-self.geom[0]/2,-self.geom[1]/2) + (self.geom[0]*2,self.geom[1]*2))

        #self.root_canvas.coords(self.img_canvas,(self.root_canvas.winfo_width()/2, self.root_canvas.winfo_height()/2))
     


        #print(self.x_scrl.get())
        #print(self.y_scrl.get())

        
        
    

    ###################################### DRAWING TOOLS

    def brush(self,event):

        self.BTN2.configure(image = self.img2)

        self.flag = False

        x1, y1 = (event.x - self.t.get()), (event.y - self.t.get())
        x2, y2 = (event.x + self.t.get()), (event.y + self.t.get())
        self.canvas.create_oval(x1, y1, x2, y2, fill = self.color[1], width = 0, tags = 'drawings')

        self.main.brush(x1*self.coef,y1*self.coef,x2*self.coef,y2*self.coef,self.color[1])
        self.pos_update(event)

        

    def marker(self,event):

        self.BTN1.configure(image = self.img1)
    
        self.flag = False
        
        x1, y1 = (event.x - self.t.get()), (event.y - self.t.get())
        x2, y2 = (event.x + self.t.get()), (event.y + self.t.get())
        self.canvas.create_rectangle(x1, y1, x2, y2, fill = self.color[1], width = 0, tags = 'drawings')
    

        self.main.marker(x1*self.coef,y1*self.coef,x2*self.coef,y2*self.coef,self.color[1])
        self.pos_update(event)


    def flatten(self):

        self.main.flatten()
        self.canvas.delete('drawings')

        self.flag = True
        self.img_update()

        self.right(self)        

    def getColor(self):

        self.color = colorchooser.askcolor()
        self.color_label.configure(bg = self.color[1])

    def erase(self):

        self.canvas.delete('drawings')
        self.main.revert()
        self.flag = True
        self.img_update()


        self.right(self)

    def getThickness(self):
        
        self.slider = Toplevel(self.window)
        self.slider.grab_set()
        self.slider.title('Thickness')
        dico = {'slider1' : ['Thickness : ', 1, 100, self.t]}
        commands = {'cancel' : lambda:[self.slider.grab_release()]}
        Slider(self.slider, dico, None)

    def right(self,event):

        self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<Button-1>')
        self.canvas.unbind('<ButtonRelease-1>')
        self.BTN1.configure(image = self.img1)
        self.BTN2.configure(image = self.img2)
        


    ###################################### FILE MENU

    def new(self):

        
        if self.saved == False:

            bl = messagebox.askyesnocancel("Unsaved Changes", "Do you want to save ?\nUnsaved changes will be lost forever (a really long time !)")

         
            if bl  == True:

                self.flatten()

                if self.named:

                    self.save()
                    self.saved = True

                else :

                    self.saveAs()
                    self.saved = True
                    if self.path == '':
                        self.saved = False
                        return

            if bl == None:
                return

        
         
        self.canvas.delete("all")
        self.info_name.set(os.getcwd())
        self.main = Picture(os.getcwd()+'\\files\\sample.jpg')
        self.extension = '.jpg'
        self.height = 500
        self.width  = 700
        self.canvas.configure(height = self.height-1, width = self.width-1)
        self.info_res.set(self.main.res)
        self.coef = 1
        self.img_update()   
        self.zoomAuto()
        self.saved = True
        self.named = False

        

        if self.start == False:

            #self.menu_file.entryconfig(2, state = 'normal')
            self.menu_file.entryconfig(3, state = 'normal')
            self.menu_file.entryconfig(4, state = 'normal')
            #self.menu_file.entryconfig(5, state = 'normal')


            self.menubar.entryconfig(2, state='normal')
            self.menubar.entryconfig(3, state='normal')
            self.menubar.entryconfig(4, state='normal')
            self.menubar.entryconfig(5, state='normal')
            self.menubar.entryconfig(6, state='normal')
            

        self.start = False

        try:
            self.tmp_canvas.destroy()
        except:
            pass

        self.root_canvas.yview_moveto('0.23')
        self.root_canvas.xview_moveto('0.142')
        self.zoomAuto()
               
        
        

    def load(self):
        
        if self.saved == False:

            bl = messagebox.askyesnocancel("Unsaved Changes", "Do you want to save ?\nUnsaved changes will be lost forever (a really long time !)")
            #print(bl)
         
            if bl  == True:

                self.flatten()

                if self.named:

                    self.save()
                    self.saved = True

                else :

                    self.saveAs()
                    self.saved = True

            elif bl == None:
                return

        

        self.saved = True
            
        self.coef = 1
        self.path = filedialog.askopenfilename(title ='Open',filetypes = [('All Image Files','.jpg .jpeg .jpe .jfif .png .ico'),('JPEG', '.jpg .jpeg .jpe .jfif'),('PNG', '.png'),('ICO','.ico'),("All files", "*.*")])
        self.extension = os.path.splitext(self.path)[1]
        #print(self.extension)

        if not self.path: return

       
        with open(os.getcwd()+'\\files\\recent.txt','a') as f:

            f.write(self.path)
            f.write('\n')

        with open(os.getcwd()+'\\files\\recent.txt','r') as f:

            self.recents = f.readlines()

        with open(os.getcwd()+'\\files\\recent.txt','w') as f:
            
            while len(self.recents) > 6:
                
                del(self.recents[0])
            f.writelines(self.recents)

        i = len(self.recents)

        '''try:

            while i > 0:
                i -= 1
                self.menu_recent.delete(i)
        except:
            pass

        

        self.recent()'''
                
 

            
        self.new()

        self.canvas.delete("all")

        self.main = Picture(self.path) #OBJECT OF Picture CLASS
        self.info_name.set(self.path)

        self.info_res.set(self.main.res)

        self.height = self.main.height
        self.width  = self.main.width

        self.named = True

        self.zoomAuto()
  
    


        
        
    def save(self):
        

        if self.named == False:
            
            try:
                self.saveAs()
            except FileNotFoundError:
                return
            except AttributeError:
                return
            except ValueError:
                return

        self.extension = os.path.splitext(self.path)[1]


        if self.extension in ['.jpg','.jpeg','.jpe','.jfif']:

            self.extension = 'JPEG'

        if self.extension == '.png':

            self.extension = 'PNG'

        if self.extension == '.ico':

            self.extension = 'ICO'

        if self.extension == '':

            return



        
        try:
            self.main.image.save(self.path, self.extension)
        except FileNotFoundError:
            return
        except AttributeError:
            return
        self.saved = True
        
    def saveAs(self):
        
        self.path = filedialog.asksaveasfilename(title ='Save As',defaultextension="*.*",filetypes = [('JPEG', '.jpg'),('PNG', '.png'),('ICO','.ico')])      
        if not self.path: return

        with open(os.getcwd()+'\\files\\recent.txt','a') as f:

            f.write(self.path)
            f.write('\n')

        with open(os.getcwd()+'\\files\\recent.txt','r') as f:

            self.recents = f.readlines()

        with open(os.getcwd()+'\\files\\recent.txt','w') as f:
            
            while len(self.recents) > 6:
                
                del(self.recents[0])
            f.writelines(self.recents)

        i = len(self.recents)

        try:

            while i > 0:
                i -= 1
                self.menu_recent.delete(i)
                self.recent()
        except:
            pass 


       
                

        self.extension = os.path.splitext(self.path)[1]
        self.named = True
        self.save()
        
        

    def share(self):
        pass
    def recent(self):

        self.recents = []

        with open(os.getcwd()+'\\files\\recent.txt','r') as f:

            self.recents = f.readlines()

        i = len(self.recents)

        
            

        while i > 0:
            i -= 1
            name = self.recents[i]
            self.menu_recent.add_command(label=str(len(self.recents) - i) + ' ' + self.recents[i],command=self.recent_callback(name))
            self.menu_file.entryconfig(2, state = 'normal')

    

    def recent_callback(self, name):

       

        def fun():

            self.path = name.strip('\n')
            #print(self.path)

            
            self.new()

            

            try:
                self.main = Picture(self.path) #OBJECT OF Picture CLASS
            except FileNotFoundError:
                messagebox.showerror(title='Error', message='The selected image has been moved or deleted')
                self.new()
                return
            except:
                messagebox.showerror(title='Error', message='The selected image is corrupted or of unsupported type')
                self.new()
                return


            self.canvas.delete("all")

            self.info_name.set(self.path)

            self.info_res.set(self.main.res)

            self.height = self.main.height
            self.width  = self.main.width

            self.named = True

            self.zoomAuto()

        return fun

        
            
            
        



    ###################################### EDIT MENU

    def undo(self, event = None):

        if self.flag == False:

            return
        
        self.main.undo()
        self.update_shape(self.main.matrix.shape[1],self.main.matrix.shape[0])
        self.img_update()
        self.zoomAuto()

    def redo(self, event = None):
        if self.flag == False:

            return

        self.main.redo() 
        self.update_shape(self.main.matrix.shape[1],self.main.matrix.shape[0])
        self.img_update()
        self.zoomAuto()

    ###################################### VIEW MENU

    def zoomIn(self, event = None):
        if self.flag == False:

            return

        try:

            self.height = int(self.height * 1.2)
            self.width  = int(self.width * 1.2)
            self.coef /= 1.2

            self.image = self.main.temp.resize((self.width, self.height), Image.ANTIALIAS)
            
            self.canvas.configure(height = self.height-1, width = self.width-1)
            self.img_update(True)

        except:
            zoomAuto()


    def zoomOut(self, event = None):
        if self.flag == False:

            return

        try:

            self.height = int(self.height / 1.2)
            self.width  = int(self.width / 1.2)
            self.coef *= 1.2

            self.image = self.main.temp.resize((self.width, self.height), Image.ANTIALIAS)
            self.canvas.configure(height = self.height-1, width = self.width-1)
            
            self.img_update(True)
        except ValueError:
            zoomAuto()

    def zoomAuto(self, event = None):

        if self.flag == False:

            return
    
        if self.height > 800 or self.width > 800:
        
            while self.height > 800 or self.width > 800:

                self.height = int(self.height / 1.2)
                self.width  = int(self.width / 1.2)
                self.coef *= 1.2
                
        elif self.height < 500 or self.width < 500:


            while self.height < 500 or self.width < 500:

                self.height = int(self.height * 1.2)
                self.width  = int(self.width * 1.2)
                self.coef /= 1.2

        self.image = self.main.temp.resize((self.width, self.height), Image.ANTIALIAS)
        self.canvas.configure(height = self.height-1, width = self.width-1)

        self.img_update(True)

    def grid(self):

        if self.canvas.find_withtag('grid') != ():

            self.canvas.delete('grid')
            return
        
        x, y = (self.width), (self.height)
        
        i=7
        while 7<=i<=self.width :
            
            self.canvas.create_line(i,y,i,0, fill='grey', width=0.25, tags = 'grid')
            i=i+7
            
        s=7
        while 7<=s<=self.height :
            
            self.canvas.create_line(x,s,0,s, fill='grey', width=0.25, tags = 'grid')
            s=s+7

        self.canvas.create_line(x/3, y, x/3, 0, width=2,tags = 'grid')
        self.canvas.create_line(2*x/3, y, 2*x/3, 0, width=2,tags = 'grid')
        self.canvas.create_line(x, y/3, 0, y/3, width=2,tags = 'grid')
        self.canvas.create_line(x, 2*y/3, 0, 2*y/3, width=2,tags = 'grid')

    def ruler(self):
        pass

    ###################################### IMAGE MENU

    def histo(self):
        
        histogram = self.main.temp.histogram()
        
        def Red(i): return '#%02x%02x%02x'%(i,0,0)
        def Green(i): return '#%02x%02x%02x'%(0,i,0)
        def Blue(i):return '#%02x%02x%02x'%(0,0,i)
        
        R = histogram[0:256]
        G = histogram[256:512]
        B = histogram[512:768]

        plt.figure(0)             # plots a figure to display RED Histogram
        for i in range(0, 256):
            plt.bar(i, R[i], color = Red(i),alpha=0.3)
        plt.figure(1)             # plots a figure to display GREEN Histogram
        for i in range(0, 256):
            plt.bar(i, G[i], color = Green(i),alpha=0.3)
        plt.figure(2)             # plots a figure to display BLUE Histogram
        for i in range(0, 256):
            plt.bar(i, B[i], color = Blue(i),alpha=0.3)
        plt.show()



    def crop(self):

        self.canvas.bind("<Button-1>", self.press)
        self.canvas.bind("<B1-Motion>", self.move)
        self.canvas.bind("<ButtonRelease-1>", self.release)

        self.area = None
        self.init_x = None
        self.init_y = None

    def press(self, event):
    
        self.init_x = event.x
        self.init_y = event.y

        self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, tags = 'area')

    def move(self, event):
        curX, curY = (event.x, event.y)

        if curX >= self.width:
            curX = self.width

        if curY >= self.height:
            curY = self.height
        
        self.canvas.coords(self.rect, self.init_x, self.init_y, curX, curY)
        self.pos_update(event)



    def release(self, event):

        self.area =  self.canvas.coords(self.rect)
        self.area = [self.area[0] * self.coef, self.area[1] * self.coef,self.area[2] * self.coef,self.area[3] * self.coef,]

        #print(self.area)
        self.main.crop(tuple(self.area))
        self.canvas.delete('area')
        self.right(event)
        self.width = self.main.width
        self.height = self.main.height
        self.img_update()

        
    def resize(self):
        
        self.spin = Toplevel(self.window)
        self.spin.title('Resize')
        self.hori = IntVar()
        self.vert = IntVar()
        self.maintain = IntVar()
        self.maintain.set(1)
        self.hori.set(self.main.width)
        self.vert.set(self.main.height)
        shape = [self.hori, self.vert, self.maintain]
        orig = self.main.image
        orig_shape = [self.hori.get(), self.vert.get()]
        commands = lambda:[self.main.resize(shape[0],shape[1]),self.img_update(),self.update_shape(shape[0].get(),shape[1].get()),self.main.confirm()]
        unresize = lambda:[self.main.unresize(orig,orig_shape),self.spin.withdraw(),self.update_shape(orig_shape[0],orig_shape[1]),self.img_update()]
        Size(self.spin, shape,commands,unresize)

    def update_shape(self,width,height):

        self.width = width
        self.height = height
        self.coef = 1
        self.img_update()
        self.zoomAuto()
            
        

    def flipH(self):

        self.main.flipH()
        
        self.image = self.main.temp
        self.img_update()

    def flipV(self):

        self.main.flipV()
        
        self.image = self.main.temp
        self.img_update()

    def rotateClockwise(self):
    
        self.height, self.width = self.width, self.height
        self.canvas.configure(height = self.height-1, width = self.width-1)
        self.main.rotateClockwise()

        self.image = self.main.temp
        self.img_update()

    def rotateCounterClockwise(self):
    
        self.height, self.width = self.width, self.height
        self.canvas.configure(height = self.height-1, width = self.width-1)
        self.main.rotateCounterClockwise()

        self.image = self.main.temp
        self.img_update()

    ###################################### ADJUSTMENTS MENU

    def sharpnessSaturation(self):

        self.slider = Toplevel(self.window)
        self.slider.title('Sharpness / Saturation')
        self.slider.grab_set()
        
        dico = {'slider1' : ['Sharpness : ', -100, 100, self.main.sp_var], 'slider2' : ['Saturation : ', -100, 100, self.main.st_var]}
        commands = {'apply' : lambda:[self.main.sharpnessSaturation(),self.img_update()], 'cancel' : lambda:[self.main.revert(), self.img_update(),self.slider.grab_release(), self.slider.withdraw()], 'save' : lambda:[self.main.confirm(),self.slider.grab_release(), self.slider.withdraw(),self.menu_edit.entryconfig(0, state = 'normal')]}
        Slider(self.slider, dico, commands)

    def blackWhite(self):

        self.main.blackWhite()
        self.img_update()


    def brightnessContrast(self):

        self.slider = Toplevel(self.window)
        self.slider.title('Brightness / Contrast')
        self.slider.grab_set()
        
        dico = {'slider1' : ['Brightness : ', -100, 100, self.main.b_var], 'slider2' : ['Contrast : ', -100, 100, self.main.c_var]}
        commands = {'apply' : lambda:[self.main.brightnessContrast(),self.img_update()], 'cancel' : lambda:[self.main.revert(),self.slider.grab_release(), self.img_update(), self.slider.withdraw()], 'save' : lambda:[self.main.confirm(), self.slider.withdraw(),self.slider.grab_release(),self.menu_edit.entryconfig(0, state = 'normal')]}
        Slider(self.slider, dico, commands)

    def colorLevels(self):

        self.slider = Toplevel(self.window)
        self.slider.title('Color Levels')
        self.slider.grab_set()

        dico = {'slider1' : ['Red : ', 0, 100, self.main.r_var], 'slider2' : ['Green : ', 0, 100, self.main.g_var], 'slider3' : ['Blue : ', 0, 100, self.main.b_var]}
        commands = {'apply' : lambda:[self.main.colorLevels(),self.img_update()], 'cancel' : lambda:[self.main.revert(), self.img_update(),self.slider.grab_release(), self.slider.withdraw()], 'save' : lambda:[self.main.confirm(),self.slider.grab_release(), self.slider.withdraw(),self.menu_edit.entryconfig(0, state = 'normal')]}
        Slider(self.slider, dico, commands)

    def invertColors(self):

        self.main.invertColors()
        self.img_update()

    ###################################### EFFECTS MENU

    def emboss(self):

        self.main.emboss()
        self.img_update()
        
    def soften(self):

        self.main.soften()
        self.img_update()
        
    def edges(self):

        self.main.edges()
        self.img_update()

    def addNoise(self):

        self.main.addNoise()
        self.img_update()

    def gaussian(self):
        
        self.slider = Toplevel(self.window)
        self.slider.title('Gaussian Blur')
        self.slider.grab_set()

        dico = {'slider1' : ['Radius : ', 0, 200, self.main.gb_var]}
        commands = {'apply' : lambda:[self.main.gaussian(),self.img_update()], 'cancel' : lambda:[self.main.revert(),self.slider.grab_release(), self.img_update(), self.slider.withdraw()], 'save' : lambda:[self.main.confirm(),self.slider.grab_release(), self.slider.withdraw(),self.menu_edit.entryconfig(0, state = 'normal')]}
        Slider(self.slider, dico, commands)

    def box(self):

        self.slider = Toplevel(self.window)
        self.slider.title('Box Blur')
        self.slider.grab_set()

        dico = {'slider1' : ['Radius : ', 0, 200, self.main.bb_var]}
        commands = {'apply' : lambda:[self.main.box(),self.img_update()], 'cancel' : lambda:[self.main.revert(), self.img_update(),self.slider.grab_release(), self.slider.withdraw()], 'save' : lambda:[self.main.confirm(),self.slider.grab_release(), self.slider.withdraw(),self.menu_edit.entryconfig(0, state = 'normal')]}
        Slider(self.slider, dico, commands)

        
    
    ###################################### SHARE MENU

    def instagram(self): 
        pass
    def facebook(self):
        pass
    def twitter(self):
        pass

class Slider:

    def __init__(self, slider, dico, commands):

        self.slider = slider
        self.slider.resizable(False, False)
        self.dico = dico
        self.commands = commands
        

        try:
            self.slider.protocol("WM_DELETE_WINDOW", self.commands['cancel'])
        except:
            pass

       
        if self.commands == []:
            self.ok()

        self.create()

    def create(self):

        try:

            FRM11 = LabelFrame(self.slider, text = self.dico['slider1'][0], foreground = 'black')
            FRM11.grid(row = 0,column = 0,columnspan = 3,padx = 10)

            #LBL11 = ttk.Label(FRM11 ,text = self.dico['slider1'][0])
            SCL11 = ttk.Scale(FRM11, from_=self.dico['slider1'][1], to=self.dico['slider1'][2], orient=HORIZONTAL, variable = self.dico['slider1'][3], length = 200)
            LBL12 = ttk.Spinbox(FRM11, textvariable = self.dico['slider1'][3], width = 8,from_=self.dico['slider1'][1], to=self.dico['slider1'][2])
            
            #LBL11.grid(row = 0, column = 0,padx = 10)
            SCL11.grid(row = 0, column = 0, columnspan = 2,padx = 10,pady = 10)
            LBL12.grid(row = 0, column = 2, padx = 10)

            if len(self.dico) >= 2:

                FRM21 = LabelFrame(self.slider, text = self.dico['slider2'][0], foreground = 'black')
                FRM21.grid(row = 1,column = 0,columnspan = 3,padx = 10)

                #LBL21 = ttk.Label(self.slider ,text = self.dico['slider2'][0])
                SCL21 = ttk.Scale(FRM21, from_=self.dico['slider2'][1], to=self.dico['slider2'][2], orient=HORIZONTAL, variable = self.dico['slider2'][3], length = 200)
                LBL22 = ttk.Spinbox(FRM21, textvariable = self.dico['slider2'][3], width = 8,from_=self.dico['slider2'][1], to=self.dico['slider2'][2])
                
                #LBL21.grid(row = 1, column = 0)
                SCL21.grid(row = 1, column = 0, columnspan = 2,padx = 10,pady = 10)
                LBL22.grid(row = 1, column = 2, padx = 10)

            if len(self.dico) == 3:

                FRM31 = LabelFrame(self.slider, text = self.dico['slider3'][0], foreground = 'black')
                FRM31.grid(row = 2,column = 0,columnspan = 3,padx = 10)

                #LBL31 = ttk.Label(self.slider ,text = self.dico['slider3'][0])
                SCL31 = ttk.Scale(FRM31, from_=self.dico['slider3'][1], to=self.dico['slider3'][2], orient=HORIZONTAL, variable = self.dico['slider3'][3], length = 200)
                LBL32 = ttk.Spinbox(FRM31, textvariable = self.dico['slider3'][3], width = 8,from_=self.dico['slider3'][1], to=self.dico['slider3'][2])
                
                #LBL31.grid(row = 2, column = 0)
                SCL31.grid(row = 2, column = 0, columnspan = 2,padx = 10,pady = 10)
                LBL32.grid(row = 2, column = 2, padx = 10)
                

            apply = ttk.Button(self.slider, text = 'Apply', command = self.commands['apply'])
            cancel = ttk.Button(self.slider, text = 'Cancel', command = self.commands['cancel'] )
            save = ttk.Button(self.slider, text = 'Save', command = self.commands['save'])

            #self.slider.columnconfigure(0,weight =2)

            #ttk.Label(self.slider, text = '    ').grid(column = 0)

            apply.grid(column = 0, row = 10)
            cancel.grid(column = 1, row = 10,padx =10,pady = 5)
            save.grid(column = 2,row = 10)

        except TypeError:

             pass


class Size:

    def __init__(self, spin, shape, commands, unresize):

        self.spin = spin
        self.spin.resizable(False, False)

        self.shape = shape
        self.commands = commands
        self.unresize = unresize

        self.original = shape

        self.h = self.shape[0].trace('w',self.get_ratio_h)
        self.v = self.shape[1].trace('w',self.get_ratio_v)



        self.ratio = self.shape[0].get() / self.shape[1].get()
     
        self.FRM = LabelFrame(self.spin, text = 'Resize :', foreground = 'black')
        self.FRM.grid(padx = 10, pady = 10, row = 0, column = 0, columnspan = 3)

        
        self.IMG1 = ttk.Label(self.FRM, image = img10)
        self.IMG2 = ttk.Label(self.FRM, image = img11)

        self.LBL1 = ttk.Label(self.FRM, text = 'Horizontal:')
        self.LBL2 = ttk.Label(self.FRM, text = 'Vertical:')

        self.ENT1 = ttk.Entry(self.FRM, width = 10, textvariable = self.shape[0])
        self.ENT2 = ttk.Entry(self.FRM, width = 10, textvariable = self.shape[1])

        self.CHK1 = ttk.Checkbutton(self.FRM, text = 'Maintain aspect ratio', variable = self.shape[2], onvalue = 1, offvalue = 0)

        self.BTN1 = ttk.Button(self.spin, text = 'OK', command = self.commands)
        self.BTN2 = ttk.Button(self.spin, text = 'Cancel', command = self.unresize)

        self.IMG1.grid(row = 0, column = 0)
        self.IMG2.grid(row = 1, column = 0)

        self.LBL1.grid(row = 0, column = 1, padx = 10, sticky = W)
        self.LBL2.grid(row = 1, column = 1, padx = 10, sticky = W)

        self.ENT1.grid(row = 0, column = 2, padx = 10)
        self.ENT2.grid(row = 1, column = 2, padx = 10)

        self.CHK1.grid(row = 2, column = 0, columnspan = 2)

        self.BTN1.grid(row = 1,column = 0,pady = 5)
        self.BTN2.grid(row = 1,column = 2)
        


    def get_ratio_h(self,a,b,c):

        try:

            self.shape[1].trace_vdelete('w',self.v)

            if self.shape[2].get() == 1:        
                self.shape[1].set(int((1/self.ratio) * self.shape[0].get()))

            self.v = self.shape[1].trace('w',self.get_ratio_v)

        except:

            self.shape[0].set(0)
            self.shape[1].set(0)
            self.v = self.shape[1].trace('w',self.get_ratio_v)

            
            


    def get_ratio_v(self,a,b,c):

        try:

            self.shape[0].trace_vdelete('w',self.h)

            if self.shape[2].get() == 1:
                self.shape[0].set(int(self.ratio * self.shape[1].get()))

            self.h = self.shape[0].trace('w',self.get_ratio_h)

        except:
            
            self.shape[0].set(0)
            self.shape[1].set(0)
            self.h = self.shape[0].trace('w',self.get_ratio_h)





        

        

        


        
        
        

        

        

window = Tk()

img10 = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\horizontal.png').resize((64,64)))
img11 = ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\vertical.png').resize((64,64)))

window.title('Paint Evolution X')

window.geometry("1024x576")
window.rowconfigure(0,weight = 1)
window.columnconfigure(0,weight = 1)
window.iconphoto(True, ImageTk.PhotoImage(Image.open(os.getcwd()+'\\files\\icon.png')))
app = Application(window)

window.mainloop()
