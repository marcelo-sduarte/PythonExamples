' loop sempre checando se a janela aparecer a cada meio segundo
' quando a Janela de desconex�o do SAP aparecer, ser� fechada
' no fim do processo do Rob� a Thread ser� fechada

Dim strProcessName
'Dim path
Dim username, strComputer
Dim intLoop, intCPUUsage
Dim inicioExec



Set wshShell = CreateObject("WScript.Shell")
userName = wshShell.ExpandEnvironmentStrings("%UserName%")
path = """C:\Users\" + userName + "\Documents\Automation Anywhere Files\Automation Anywhere\My Tasks\Robo_Materiais\Main.atmx"""
strProcessName = "AAPlayer.exe"
strComputer = "."
inicioExec = Now

Do 
	
	
	'Checar se houve queda no SAP -------------------------------------------
	'Em caso de queda, fechar� o Player do AA e reiniciar o robo atrav�s do Main.atmx
    ret = wshShell.AppActivate("SAP GUI for Windows 750") 
    If ret = True Then 
		'Fechar Mesangem SAP
		wshShell.SendKeys "%{F4}"
		
		'Fechar Player AA
		Call FecharPlayer(strComputer, strProcessName)
		
		'Enviar Email e Iniciar o rob�
		wshShell.Run(path)
    End If
	
	'Checar se o Player do AA ainda continua em execu��o -----------------------------
	'Caso o Player n�o esteja executando, ser� iniciado o rob�
	If Not ProcessoExecutando(strComputer,strProcessName) Then
		wshShell.Run(path) 'Iniciar o rob� 
	End If
	
	'Monitorar Consumo de CPU do Player Automation
	'Caso o Player esteja paralizado (CPU = 0) por 5 minutos, ser� reiniciado o rob�
	For Each Process in GetObject("winmgmts:").ExecQuery("Select * from Win32_Process Where Name like '" & strProcessName & "'")
		intLoop = 0
		
		Do
			intCPUUsage = CPUUSage(Process.Handle)

			If intCPUUsage < 2 And intLoop <= 150 Then
				intLoop = intLoop + 1
				
				If intLoop = 150 Then
					'Fechar Player AA
					Call FecharPlayer(strComputer, strProcessName)
					wshShell.Run(path) 'Iniciar o rob�
					Exit Do 
				End If
			End If
		Loop
		
	Next
	
	'Atualizar Fila de 2 em 2 horas
	If Now >= DateAdd("h",2,inicioExec) Then
		outFile= """C:\Users\" + userName + "\Documents\Automation Anywhere Files\Automation Anywhere\My Tasks\Robo_Materiais\VIM\Controle\AtualizarFila.txt"""
		Set objFile = objFSO.CreateTextFile(outFile,True)
		objFile.Write "Atualizar Fila" & vbCrLf
		objFile.Close
		inicioExec = Now
	End If
	
    WScript.Sleep 500 'Loop a cada 0,5 segundos
	
Loop

'Fun��o para fechar o Player do AA

Function FecharPlayer(strComputer, strProcessName)
	Dim objWMIService, colProcess
	
	Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
	Set colProcess = objWMIService.ExecQuery ("Select * from Win32_Process Where Name like '" & strProcessName & "'")
	For Each p in colProcess
		if strProcessName = p.Name Then
			p.Terminate
			Exit For
		End if
	Next


End Function


'Fun��o para verificar se um processo est� sendo executado atraves do Gerenciador de Tarefas
Function ProcessoExecutando(strComputer, strProcessName)

	Dim objWMIService, strWMIQuery

	strWMIQuery = "Select * from Win32_Process where name like '" & strProcessName & "'"
	
	Set objWMIService = GETOBJECT("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 


	If objWMIService.ExecQuery(strWMIQuery).Count > 0 Then
		ProcessoExecutando = True
	Else
		ProcessoExecutando = False
	End If

End Function

'Fun��o para Monitoramento da CPU
Function CPUUSage( ProcID )
    On Error Resume Next
	
    Set objService = GetObject("Winmgmts:{impersonationlevel=impersonate}!\Root\Cimv2")

    For Each objInstance1 in objService.ExecQuery("Select * from Win32_PerfRawData_PerfProc_Process where IDProcess = '" & ProcID & "'")
        N1 = objInstance1.PercentProcessorTime
        D1 = objInstance1.TimeStamp_Sys100NS
        Exit For
    Next

    WScript.Sleep 2000

	For Each perf_instance2 in objService.ExecQuery("Select * from Win32_PerfRawData_PerfProc_Process where IDProcess = '" & ProcID & "'")
        N2 = perf_instance2.PercentProcessorTime
        D2 = perf_instance2.TimeStamp_Sys100NS
        Exit For
    Next

    ' CounterType - PERF_100NSEC_TIMER_INV
    ' Formula - (1- ((N2 - N1) / (D2 - D1))) x 100
    Nd = (N2 - N1)
    Dd = (D2-D1)
    PercentProcessorTime = ( (Nd/Dd))  * 100
	
	CPUUSage = Round(PercentProcessorTime ,0)
   
End Function

