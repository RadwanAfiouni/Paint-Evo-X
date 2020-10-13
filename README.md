


# Paint Evolution X

```
                        Welcome to the
                    Paint Evolution X V2.0
                         ReadMe File
	                       May 18, 2020
__________        .__        __    ___________             ____  ___ 
\______   \_____  |__| _____/  |_  \_   _____/__  ______   \   \/  / 
 |     ___/\__  \ |  |/    \   __\  |    __)_\  \/ /  _ \   \     /  
 |    |     / __ \|  |   |  \  |    |        \\   (  <_> )  /     \  
 |____|    (____  /__|___|  /__|   /_______  / \_/ \____/  /___/\  \ 
                \/        \/               \/                    \_/ 


```
 
 
## 0. Contents 
1. Installing Required Libraries
2. User Guide
3. Known Issues
4. Future Additions
5. Changelog

## 1. Installing Required Libraries

Use the package manager [pip](https://pip.pypa.io/en/stable/) 


WINDOWS : Press windows + R. Type in cmd and press enter
MAC OS  : Press command (⌘) + Space Bar to open Spotlight search. Type in Terminal and press enter.

Use the next set of commands to install NumPy and Pillow using the following instructions
```
python -m pip install numpy
python -m pip install pillow
python -m pip install matplotlib
```


## 2. User Guide

To run just double click on the 'Launcher' file

Loading images : File -> Open, then select any JPG image OR (if applicable) File -> Recents 
Creating a blank image : File -> New

The menubar menus now become usable; check out the attached video for a demo !


NB: The following features are not featured in the video (available upon request): 
 
 - You can place a grid for precision drawing in the 'View' menu
 - You can get the image's color intensities by selecting Get Histogram in the Image Menu
 - You can deselect your drawing tool by double clicking the right mouse button


## 3. Known Issues

- When drawing with a small thicknes, moving your mouse too fast may cause the drawed line to appear inconsistent, this is caused by Tkinter's mainloop refresh rate
 - The image may rarely go out of bounds, if that happens, try the Zoom Auto command (Ctrl+A)
 - Support is limited for PNG and ICO files, use at your own risk ! (JPEG fully supported)

## 4. Future Additions
 - Full support for all image files
 - Rework of the editing tools to be fully independent from pillow's ImageEnhance and ImageFilter modules
 
## 5. Changelog
 - All menus are fully working
 - Code refactored to be more efficient and readable
 - Drawing tools implemented


## License
[MIT](https://choosealicense.com/licenses/mit/)
