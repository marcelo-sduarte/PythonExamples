' loop sempre checando se a janela aparecer a cada meio segundo
' quando a Janela de desconex�o do SAP aparecer, ser� fechada
' no fim do processo do Rob� a Thread ser� fechada

Dim objWMIService, colProcess
Dim strProcessName
'Dim path
Dim username, strComputer

 Set wshShell = CreateObject("WScript.Shell")
 userName = wshShell.ExpandEnvironmentStrings("%UserName%")
'path = """C:\Users\" + userName + "\Documents\Automation Anywhere Files\Automation Anywhere\My Tasks\AutoPay_II\MainTask_AUTOPAY.atmx"""
 strProcessName = "AAPlayer.exe"
 strComputer = "."



Do 
    ret = wshShell.AppActivate("SAP GUI for Windows 750") 
    If ret = True Then 
        
	'Fechar Mesangem SAP
	wshShell.SendKeys "%{F4}"
	
	'Fechar Player AA
	Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
	Set colProcess = objWMIService.ExecQuery ("Select * from Win32_Process Where Name like '" & strProcessName & "'")
	For Each p in colProcess
		if strProcessName = p.Name Then
			p.Terminate
			Exit For
		End if
	Next

	'Executar o rob� 
	'wshShell.Run(path)
    End If 
    WScript.Sleep 500 
Loop 