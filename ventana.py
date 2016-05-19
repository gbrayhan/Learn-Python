import wx

class EjemploMenu(wx.Frame):
    def __init__(self,parent,title):
        super(EjemploMenu,self).__init__(parent,title=title)
        self.InitUI()

    def InitUI(self):
        menubar=wx.MenuBar()
        fileMenu=wx.Menu()

        fileItem=fileMenu.Append(wx.ID_EXIT,'Salir','Salir de la App')
        menubar.Append(fileMenu,'&Archivo')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU,self.OnQuit,fileItem)
        self.Show(True)

    def OnQuit(self,e):
        self.Close()

frame=wx.App()
EjemploMenu(None,'Word')
frame.MainLoop()

    
