;ControlFocus("titile","text","controID") controID = Edit instance
ControlFocus("��","","Edit1")

;Wait 10 seconds for the Upload window to apper
WinWait("#32770","","10")

;Set the File name text on the Edit field
ControlSetText("��","","Edit1","E:\01.jpg")
Sleep(2000)

;Click on the Open button
ControlClick("��","","Button1")