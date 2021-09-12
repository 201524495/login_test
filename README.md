# login_test


## with Chromedriver

  ![withChromedriver](https://github.com/201524495/login_test/blob/main/image/withChromedriver.JPG)
  
  there is not path Chromedriver. so we need to add chromedriver to binary
  
  
## Input Values with Xpath

  ![input](https://github.com/201524495/login_test/blob/main/image/input.JPG)
  
  
  
## Click Button with Xpath

  ![clickWithXpath](https://github.com/201524495/login_test/blob/main/image/clickXpath.JPG)
  
  Click Button using Xpath
  
  
## Select Option value with Xpath

  ![](https://github.com/201524495/login_test/blob/main/image/SelectandValue.JPG)
  
  Click Select Option with value and Xpath
  
  
## make UI file to PY file

  ![UItoPY](https://github.com/201524495/login_test/blob/main/image/UItoPY.JPG)
  
    pyuic5 -x ui/register_form.ui -o modules/UI.py

## make EXE file with Chromedriver

  ![makeEXEwithChromedriver.JPG](https://github.com/201524495/login_test/blob/main/image/makeEXEwithChromedriver.JPG)
  
    pyinstaller -w -F --add-binary "chromedriver.exe";"." Run.py
  
  don't want to see cmd console ==> using "--noconsole" or "-w"
  
  make only one file ==> "--onefile" or "-F" 
  
  <h1>some issue in pyinstaller</h1>
  
  original code : pyinstaller -w -F --add-binary "chromedriver.exe";"." Run.py
  
  new code : pyinstaller -w -F --add-binary "chromedriver.exe;." Run.py
  
## Result

 ![result](https://github.com/201524495/login_test/blob/main/image/result.JPG)
 
 my execution file's reservation time is under 10sec 

![myResult](https://github.com/201524495/login_test/blob/main/image/myResult.PNG)
![otherResult](https://github.com/201524495/login_test/blob/main/image/otherResult.PNG)
