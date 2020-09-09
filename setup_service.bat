call nssm.exe install wrldc_tmp_hum_monitor "%cd%\run_server.bat"
call nssm.exe set wrldc_tmp_hum_monitor AppStdout "%cd%\logs\mis_rpc_gen_hrs.log"
call nssm.exe set wrldc_tmp_hum_monitor AppStderr "%cd%\logs\mis_rpc_gen_hrs.log"
call sc start wrldc_tmp_hum_monitor