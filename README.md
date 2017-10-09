## This is a work in progress. ##
The end result I hope will be a variation of [this project](https://learn.adafruit.com/steampunk-cameo-necklace) with an animated rose whose petals fall at intervals.

### Files included in project ###
* Bmps for each part of a rose: stem + 9 petals
* Python tool to convert .data files generated from .bmps to the format expected by the [bmp drawer](https://github.com/adafruit/Adafruit-GFX-Library/blob/master/Adafruit_GFX.cpp#L464) in the Adafruit GFX library. See an example of the expected PROGMEM array [here](https://github.com/adafruit/Adafruit_SSD1306/blob/master/examples/ssd1306_128x64_i2c/ssd1306_128x64_i2c.ino#L35).
* Script to convert all the bmp-data files to progmem arrays at once.

### Methods ###
* Imported [this rose image](https://i.pinimg.com/236x/e9/3e/16/e93e167055a01f104275332bb70cb257--beauty-and-the-beast-rose-silhouette-disney-tattoos-beauty-and-the-beast.jpg) to GIMP.
* Painstakingly sized and outlined all the petals and stem and exported them as bmps, then exporting them again in the raw data format. Found that it's definitely necessary to export them as bmps first.
* Am currently working on animating the fall of each petal and will probably end up creating a generic "flat falling petal" bmp since some of them are ridiculously small. Also need to make the smallest ones fall first.

### How to use the converter
```
./bmp_data_to_progmem.py -f <input-file.data> -w <img-width> -h <img-height>
```
REQUIRED:
* `-f` || `--filename`
* `-w` || `--width`
* `-h` || `--height`

There is a check to make sure the input width and height match the number of pixels in the input.

Optional:
* `-i` || `--invert`:  flag that switches the 1s and 0s

There's also a variable I have hardcoded in there (sorry) called `COLOR_THRESHOLD` (0-255) that determines the cutoff for whether a pixel will be black or white depending on the shade of gray.

Example output:
```
./bmp_data_to_progmem.py -f data/petal_one.data -w 32 -h 2

['-f', 'data/petal_one.data', '-w', '32', '-h', '28']
                                
                                
                                
                                
                                
                                
                  ......        
                 ........       
                ..........      
               ...    ....      
              ...        ..     
             ....               
            ....                
           .....                
          .....                 
        ......                  
      ........                  
     ........                   
    ........                    
    ........                    
    .......                     
   .......                      
   ......                       
  .....                         
  ....                          
  .                             
                                
                                
Total pixels:  896
B00000000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00111111, B00000000, 
B00000000, B00000000, B01111111, B10000000, 
B00000000, B00000000, B11111111, B11000000, 
B00000000, B00000001, B11000011, B11000000, 
B00000000, B00000011, B10000000, B01100000, 
B00000000, B00000111, B10000000, B00000000, 
B00000000, B00001111, B00000000, B00000000, 
B00000000, B00011111, B00000000, B00000000, 
B00000000, B00111110, B00000000, B00000000, 
B00000000, B11111100, B00000000, B00000000, 
B00000011, B11111100, B00000000, B00000000, 
B00000111, B11111000, B00000000, B00000000, 
B00001111, B11110000, B00000000, B00000000, 
B00001111, B11110000, B00000000, B00000000, 
B00001111, B11100000, B00000000, B00000000, 
B00011111, B11000000, B00000000, B00000000, 
B00011111, B10000000, B00000000, B00000000, 
B00111110, B00000000, B00000000, B00000000, 
B00111100, B00000000, B00000000, B00000000, 
B00100000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000000, B00000000, 
```
Be sure to remove the extra comma at the end when pasting the array into your sketch.
