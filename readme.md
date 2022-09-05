# Jinjafy

Template Name: Jinjafy
Template URL:
Version:0.0.1
Author: mr 13 Mehgoss
License: GNU


A program that, with a .html configuration, can:
* Automatically generate jinja2 templates from html files 
* Move files based on their **extensions** . 
* Attending files if they are in main.py > Make > com : ('.html','.css','.map','.js','.woff','.woff2','.txt','.jpg','.png','.php')



## How to use

```
python ./main.py HTML_FOLDER
```

## How to test
### get template

Run the following :
```
python ./get_template.py 

```
Or copy the test template folder from 'Test/' to the current directory 'Jinjafy/'
the output should be a downloaded folder from [Bootstrap_Website](https://bootstrapmade.com) 
let it be called 'HTML_FOLDER'

### run test

then run :

```
python ./main.py HTML_FOLDER

```

test results will be in templates/finals

ideal file structure:
---main
|---assets
    |---css
        |--style.css
    |---js
        |--script.js
    |---img
        |--image.jpg
    |---vendors
    |--style.css
    |--script.js
|---forms
    |--form.php
|---extra_html
    |--file.html
    |--file2.html
files.html



program output:
---main
|---assets
    |---css
        |--style.css
    |---js
        |--script.js
    |---img
        |--image.jpg
    |---vendors
    |--style.css
    |--script.js
|---forms
    |--form.php
|---extra_html
    |--file.html
    |--file2.html
files.html
base.html

