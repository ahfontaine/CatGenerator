Hi.
This is the CatGenerator3000.
This was coded in Python 3.6.8 and PyQT 5.11.
If you want to change the text and the original creator is non-existent, simply do the following steps:
- Download Visual Studio Code.
- Download Python 3.6.8 (you can use 3.6.9)
- Download QT, Open-Source edition.
The previous 3 steps are completely free.

After this, you need to do the following in either Python bash, or in a command-line (If you don't know what a command line is, Press Start and type Cmd.exe)
Type in the following :
pip install PyQt5
pip install Pyinstaller

The text is in the Main.py file.

If you want to build it afterwards, here's the command line you need to put (go in the CatGenerator code folder, hold Shift on your keyboard and rightclick on a file. You will see a "open in Powershell" option)
type in or copy the following :

pyinstaller .\Main.py --onefile --icon=cat.ico --name=CatGenerator3000

That's it!