import wx

app=wx.App()
frame=wx.Frame(None,-1, "Primer ventana",style= wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX |wx.CLOSE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION ,size=(400,400))

frame.Show()
app.MainLoop()
