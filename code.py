import wx
class MyFrame(wx.Frame):
    def _init_(self):
        wx.Frame._init(self,None,
                       pos=wx.DefaultPosition,size=wx.size(450,100),
                       style=wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.CAPTION |
                       wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                       title="VIRTUAL BOX")
        panel-wx.panel(self)
        my_sizer=wx.BoxSizer(panel,
                             label="Hey  i m pyda, your assistant. how can i help you....")
        my_sizer.Add(lbl,0,wx,ALL,5)
        self.txt=wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEnter)
        my_sizer.Add(self.txt,0,wx.ALL,5)
        panel.SetSizer(my_sizer)
        self.how()
    def OnEnter(self,event):
        input=self.txt.GetValue()
        my_input=input.lower()
        print("It Worked")
if __name__=="__main__":
    app=wx.App(True)
    frame=MyFrame()
    app.MainLoop()
