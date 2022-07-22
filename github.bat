@echo off

if "%~1"=="" CALL :welcome
if "%~1"=="-h" CALL :welcome
if "%~1"=="--help" CALL :welcome

if "%~1"=="-L" CALL :login 
if "%~1"=="--login" CALL :login 

if "%~1"=="-O" CALL :logout
if "%~1"=="--logout" CALL :logout 

if "%~1"=="-c" (if not "%~2"=="" (CALL :create %~2 %~3) else (echo SyntaxtError: github -c [REPO_NAME] [0-1]))
if "%~1"=="--create" (if not "%~2"=="" (CALL :create %~2 %~3) else (echo SyntaxtError: github --creat [REPO_NAME] [0-1]))

if "%~1"=="-u" (if not "%~2"=="" (if not "%~3"=="" (
    for /f "tokens=2,* delims= " %%a in ("%*") do set x=%%b
    CALL :upload %~2 "%x%") else (echo SyntextError: github -u [REPO_NAME] [FILE_PATH, ...])) else (echo SyntextError: github -u [REPO_NAME] [FILE_PATH, ...])) 
if "%~1"=="--upoload" (if not "%~2"=="" (if not "%~3"=="" (
    for /f "tokens=2,* delims= " %%a in ("%*") do set x=%%b
    CALL :upload %~2 "%x%") else (echo SyntextError: github -u [REPO_NAME] [FILE_PATH, ...])) else (echo SyntextError: github -u [REPO_NAME] [FILE_PATH, ...])) 

if "%~1"=="-l" CALL :list
if "%~1"=="--list" CALL :list 

if "%~1"=="-r" (if not "%~2"=="" (CALL :readme %~2) else (echo SyntaxtError: github -r [REPO_NAME]))  
if "%~1"=="--redme" (if not "%~2"=="" (CALL :readme %~2) else (echo SyntaxtError: github -readme [REPO_NAME])) 

if "%~1"=="-s" (if not "%~2"=="" (CALL :status %~2) else (echo SyntaxtError: github -s [REPO_NAME])) 
if "%~1"=="--status" (if not "%~2"=="" (CALL :status %~2) else (echo SyntaxtError: github -status [REPO_NAME]))  

if "%~1"=="-i" (if not "%~2"=="" (CALL :issues %~2) else (echo SyntaxtError: github -i [REPO_NAME])) 
if "%~1"=="--issues" (if not "%~2"=="" (CALL :issues %~2) else (echo SyntaxtError: github -issues [REPO_NAME])) 

if "%~1"=="-p" (if not "%~2"=="" (CALL :pullrequests %~2) else (echo SyntaxtError: github -p [REPO_NAME])) 
if "%~1"=="--pullrequests" (if not "%~2"=="" (CALL :pullrequests %~2) else (echo SyntaxtError: github -pullrequests [REPO_NAME])) 

if "%~1"=="-f" (if not "%~2"=="" (CALL :fork %~2) else (echo SyntaxtError: github -f [URL]))  
if "%~1"=="--fork" (if not "%~2"=="" (CALL :fork %~2) else (echo SyntaxtError: github --fork [URL])) 

if %ERRORLEVEL% EQU 0 echo InvalidOption: Use github -h, --help for details

exit /b 0


:welcome
echo "    _____ _____ _______ _    _ _    _ ____    
echo "   / ____|_   _|__   __| |  | | |  | |  _ \   
echo "  | |  __  | |    | |  | |__| | |  | | |_) | 
echo "  | | |_ | | |    | |  |  __  | |  | |  _ <  
echo "  | |__| |_| |_   | |  | |  | | |__| | |_) | 
echo "   \_____|_____|  |_|  |_|  |_|\____/|____/  
echo "
echo =================================================
echo.
echo Perform basic github operation on cmd (usign python and selenium)
echo Syntaxt:
echo        github [OPTION] [repository NAME] 
echo Options:
echo        -c, --create [REPO_NAME] [0-1]          create new repository (0 - public, 1 - private)
echo        -f, --fork [URL]                        fork repository
echo        -h, --help                              show details
echo        -i, --issues [REPO_NAME]                show all issues
echo        -l, --list                              show all repository  
echo        -L, --login                             login to github
echo        -O, --logout                            logout to github
echo        -p, --pullrequests [REPO_NAME]          show all pull requests
echo        -r, --readme [REPO_NAME]                show readme file                        
echo        -s, --status [REPO_NAME]                show status(stars, watching, forks) of repository  
echo        -u, --upload [FILE_PATH, ...]           upload file(s)                                                                                                                                   

exit /b 1

:login
python -c "import sys; sys.path.insert(0, r'C:\Users\lazzy\Documents\GitHub'); from github import *; git = GitHub(); git.login();"
exit /b 1

:logout
python -c "import sys; sys.path.insert(0, r'C:\Users\lazzy\Documents\GitHub'); from github import *; git = GitHub(); git.logout(); git.close()"
exit /b 1

:create
python -c "import sys; sys.path.insert(0, r'C:\Users\lazzy\Documents\GitHub'); from github import *; git = GitHub(); git.create(""%~1"", ""%~2""); git.close()"
exit /b 1

:upload
python -c "import sys; sys.path.insert(0, r'C:\Users\lazzy\Documents\GitHub'); from github import *; git = GitHub(); git.upload(""%~1"", r""%~2""); git.close()"
exit /b 1

:list
python -c "import sys; sys.path.insert(0, r'C:\Users\lazzy\Documents\GitHub'); from github import *; git = GitHub(); git.list(); git.close()"
exit /b 1

:readme
python -c "import sys; sys.path.insert(0, r'C:\Users\lazzy\Documents\GitHub'); from github import *; git = GitHub(); git.readme(""%~1""); git.close()"
exit /b 1

:status
python -c "import sys; sys.path.insert(0, r'C:\Users\lazzy\Desktop\GitHub'); from github import *; git = GitHub(); git.status(""%~1""); git.close()"
exit /b 1

:issues
python -c "import sys; sys.path.insert(0, r'C:\Users\lazzy\Documents\GitHub'); from github import *; git = GitHub(); git.issues(""%~1""); git.close()"
exit /b 1

:pullrequests
python -c "import sys; sys.path.insert(0, r'C:\Users\lazzy\Documents\GitHub'); from github import *; git = GitHub(); git.pullrequests(""%~1""); git.close()"
exit /b 1

:fork
python -c "import sys; sys.path.insert(0, r'C:\Users\lazzy\Documents\GitHub'); from github import *; git = GitHub(); git.fork(""%~1""); git.close()"
exit /b 1



