import wx

class EjemploMenu(wx.Frame):
    def __init__(self,parent,title):
        super(EjemploMenu,self).__init__(parent,title=title)
        self.InitUI()

    def InitUI(self):
        menubar=wx.MenuBar()
        
        archivo=wx.Menu()
        archivo.Append(wx.ID_FILE,'&Archivo')
        archivo.Append(wx.ID_EDIT,'&Editar')
        archivo.Append(wx.ID_SAVE,'&Guardar')
        archivo.Append(wx.ID_HELP,'&Ayuda')
        archivo.AppendSeparator()

        edit=wx.Menu()
        edit.Append(wx.ID_ANY,'&Personal')
        edit.Append(wx.ID_ANY,'&Datos')
        edit.Append(wx.ID_ANY,'&Color')

        archivo.AppendMenu(wx.ID_ANY,'&Editar',edit)

        opcion=wx.MenuItem(archivo,wx.ID_ANY,'&Salir')
        archivo.AppendItem(opcion)

        self.Bind(wx.EVT_MENU,self.OnQuit,opcion)
        menubar.Append(archivo,'&Archivo')
        self.SetMenuBar(menubar)
        
        self.Show(True)

        
        

    def OnQuit(self,e):
        self.Close()

frame=wx.App()
EjemploMenu(None,'Word')
frame.MainLoop()
