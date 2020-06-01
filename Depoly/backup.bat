:: 產生備份目錄
set Date_folder=%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%
:: 產生備份目錄
md "\\Server\"%Date_folder%
:: 備份Client
xcopy "\\Server\ClientDeploy" "\\server\"%Date_folder% /E /H /C /I /Y

:: 備份Service
xcopy "\\Server\ServicesDeploy" "\\server\"%Date_folder%\Service" /E /H /C /I /Y

:: 更新Client檔案
xcopy "D:\Backup\LeoYang\Desktop\Project\XXX\Client\bin\Debug" "\\Server\ClientDeploy" /E /H /C /I /Y /exclude:D:\Backup\LeoYang\Desktop\Project\XXX\.git\hooks\Exclude.txt

:: 更新服務
xcopy "D:\Backup\LeoYang\Desktop\Project\XXX\Services\bin\Debug" "\\Server\ServicesDeploy" /E /H /C /I /Y /exclude:D:\Backup\LeoYang\Desktop\Project\XXX\.git\hooks\Exclude.txt