call nssm.exe install wrldc_tmp_hum_monitor "%cd%\run_server.bat"
call nssm.exe set wrldc_tmp_hum_monitor AppStdout "%cd%\logs\wrldc_tmp_hum_monitor.log"
call nssm.exe set wrldc_tmp_hum_monitor AppStderr "%cd%\logs\wrldc_tmp_hum_monitor.log"
call sc start wrldc_tmp_hum_monitor