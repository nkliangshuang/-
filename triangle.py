#!/usr/bin/env python
# coding: utf-8
import wx
#########################ifTriangle()####################################
def ifTriangle(a,b,c):
	if(a+b>c):
		if(a==b==c):
			return "%d\t\t%d\t\t%d\t\t%s" % (a,b,c,"等边三角形")
		elif(a==b or a==c or b==c):
			return "%d\t\t%d\t\t%d\t\t%s" % (a,b,c,"等腰三角形")
		else:
			return "%d\t\t%d\t\t%d\t\t%s" % (a,b,c,"一般三角形")
	else:
			return "%d\t\t%d\t\t%d\t\t%s" % (a,b,c,"不是三角形")
#######################b1()######################################
def b1(event):
	try:
		aMin=int(a_min.GetValue())
		aMax=int(a_max.GetValue())
		bMin=int(b_min.GetValue())
		bMax=int(b_max.GetValue())
		cMin=int(c_min.GetValue())
		cMax=int(c_max.GetValue())	
			
		flag=(aMin<aMax)and(bMin<bMax)and(cMin<cMax)and(aMin>0)and(aMax>0)and(bMin>0)and(bMax>0)and(bMin>0)and(bMax>0)		
		if(flag):
			a=[aMin,aMin+1,(aMin+aMax)/2,aMax-1,aMax]
			b=[bMin,bMin+1,(bMin+bMax)/2,bMax-1,bMax]
			c=[cMin,cMin+1,(cMin+cMax)/2,cMax-1,cMax]
			Str=''
			for i in range(0,5):
				Str+=ifTriangle(a[2],b[2],c[i])
				Str+='\n'
			for i in range(0,5):
				Str+=ifTriangle(a[2],b[i],c[2])
				Str+='\n'
			for i in range(0,5):
				Str+=ifTriangle(a[i],b[2],c[2])
				Str+='\n'
			contents.SetValue(Str)
		else:
			contents.SetValue("输入错误，请重新输入")
	except ValueError:
		contents.SetValue("输入错误，请重新输入.")
	#	raise
#############################b2()###############################################
def b2(event):
	try:
		aMin=int(a_min.GetValue())
		aMax=int(a_max.GetValue())
		bMin=int(b_min.GetValue())
		bMax=int(b_max.GetValue())
		cMin=int(c_min.GetValue())
		cMax=int(c_max.GetValue())
			
		flag=(aMin<aMax)and(bMin<bMax)and(cMin<cMax)and(aMin>0)and(aMax>0)and(bMin>0)and(bMax>0)and(bMin>0)and(bMax>0)		
		if(flag):
			a=[aMin-1,aMin,aMin+1,(aMin+aMax)/2,aMax-1,aMax,aMax+1]
			b=[bMin-1,bMin,bMin+1,(bMin+bMax)/2,bMax-1,bMax,bMax+1]
			c=[cMin-1,cMin,cMin+1,(cMin+cMax)/2,cMax-1,cMax,cMax+1]
			Str=''
			for i in range(0,7):
				if(c[i]<=0):
					Str+="%d\t\t%d\t\t%d\t\t%s"  % (a[3],b[3],c[i],"边长不能<=0")
					Str+='\n'		
				else:
					Str+=ifTriangle(a[3],b[3],c[i])
					Str+='\n'
			for i in range(0,7):
				if(b[i]<=0):
					Str+="%d\t\t%d\t\t%d\t\t%s" % (a[3],b[i],c[3],"边长不能<=0")
					Str+='\n'		
				else:
					Str+=ifTriangle(a[3],b[i],c[3])
					Str+='\n'
			for i in range(0,7):
				if(a[i]<=0):
					Str+="%d\t\t%d\t\t%d\t\t%s" % (a[i],b[3],c[3],"边长不能<=0")
					Str+='\n'		
				else:
					Str+=ifTriangle(a[i],b[3],c[3])
					Str+='\n'
			contents.SetValue(Str)
		else:
			contents.SetValue("输入错误，请重新输入")
	except ValueError:
		contents.SetValue("输入错误，请重新输入")
###########################b3()############################################
def b3(event):
	try:
		aMin=int(a_min.GetValue())
		aMax=int(a_max.GetValue())
		bMin=int(b_min.GetValue())
		bMax=int(b_max.GetValue())
		cMin=int(c_min.GetValue())
		cMax=int(c_max.GetValue())
			
		flag=(aMin<aMax)and(bMin<bMax)and(cMin<cMax)and(aMin>0)and(aMax>0)and(bMin>0)and(bMax>0)and(bMin>0)and(bMax>0)		
		if(flag):
			a=[aMin,aMin+1,(aMin+aMax)/2,aMax-1,aMax]
			b=[bMin,bMin+1,(bMin+bMax)/2,bMax-1,bMax]
			c=[cMin,cMin+1,(cMin+cMax)/2,cMax-1,cMax]
			Str=''
			for i in range(0,5):
				for j in range(0,5):
					for k in range(0,5):
						Str+=ifTriangle(a[i],b[j],c[k])
						Str+='\n'
			contents.SetValue(Str)
		else:
			contents.SetValue("输入错误，请重新输入")
	except ValueError:
		contents.SetValue("输入错误，请重新输入")
##########################b4()########################################
def b4(event):
	try:
		aMin=int(a_min.GetValue())
		aMax=int(a_max.GetValue())
		bMin=int(b_min.GetValue())
		bMax=int(b_max.GetValue())
		cMin=int(c_min.GetValue())
		cMax=int(c_max.GetValue())
			
		flag=(aMin<aMax)and(bMin<bMax)and(cMin<cMax)and(aMin>0)and(aMax>0)and(bMin>0)and(bMax>0)and(bMin>0)and(bMax>0)		
		if(flag):
			a=[aMin-1,aMin,aMin+1,(aMin+aMax)/2,aMax-1,aMax,aMax+1]
			b=[bMin-1,bMin,bMin+1,(bMin+bMax)/2,bMax-1,bMax,bMax+1]
			c=[cMin-1,cMin,cMin+1,(cMin+cMax)/2,cMax-1,cMax,cMax+1]
			Str=''
			zeroFlag=1
			for i in range(0,7):
				for j in range(0,7):
					for k in range(0,7):
						if(a[i]<=0 or b[j]<=0 or c[k]<=0):
							Str+="%d\t\t%d\t\t%d\t\t%s" % (a[i],b[j],c[k],"边长不能<=0")
							Str+='\n'
						else:
							Str+=ifTriangle(a[i],b[j],c[k])
							Str+='\n'
			contents.SetValue(Str)
		else:
			contents.SetValue("输入错误，请重新输入")
	except ValueError:
		contents.SetValue("输入错误，请重新输入")
#############################save()###################################
def save(event):
	try:	
		file=open(filename.GetValue(),'w')
		file.write(contents.GetValue().encode('utf-8'))
		file.close()
	except:
		contents.SetValue("出错了，请检查您的文件路径是否合法有效")
		raise
################################main######################################
app=wx.App()
win=wx.Frame(None,title='triangle',size=(410,450))
bkg=wx.Panel(win)

a_static=wx.StaticText(bkg,-1,'请输入边长a的范围:  ')
b_static=wx.StaticText(bkg,-1,'请输入边长b的范围:  ')
c_static=wx.StaticText(bkg,-1,'请输入边长c的范围:  ')

a_min=wx.TextCtrl(bkg,-1,'1')
a_max=wx.TextCtrl(bkg,-1,'100')
b_min=wx.TextCtrl(bkg,-1,'1')
b_max=wx.TextCtrl(bkg,-1,'100')
c_min=wx.TextCtrl(bkg,-1,'1')
c_max=wx.TextCtrl(bkg,-1,'100')

button1=wx.Button(bkg,label='测试1')
button1.Bind(wx.EVT_BUTTON,b1)
button2=wx.Button(bkg,label='测试2')
button2.Bind(wx.EVT_BUTTON,b2)
button3=wx.Button(bkg,label='测试3')
button3.Bind(wx.EVT_BUTTON,b3)
button4=wx.Button(bkg,label='测试4')
button4.Bind(wx.EVT_BUTTON,b4)

filename=wx.TextCtrl(bkg,-1,'triangle.txt')
save_button=wx.Button(bkg,label="保存")
save_button.Bind(wx.EVT_BUTTON,save)

contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)


hboxA=wx.BoxSizer()
hboxA.Add(a_static,proportion=2,flag=wx.LEFT,border=5)
hboxA.Add(a_min,proportion=1,flag=wx.LEFT,border=5)
hboxA.Add(a_max,proportion=1,flag=wx.LEFT,border=5)

hboxB=wx.BoxSizer()
hboxB.Add(b_static,proportion=2,flag=wx.LEFT,border=5)
hboxB.Add(b_min,proportion=1,flag=wx.LEFT,border=5)
hboxB.Add(b_max,proportion=1,flag=wx.LEFT,border=5)

hboxC=wx.BoxSizer()
hboxC.Add(c_static,proportion=2,flag=wx.LEFT,border=5)
hboxC.Add(c_min,proportion=1,flag=wx.LEFT,border=5)
hboxC.Add(c_max,proportion=1,flag=wx.LEFT,border=5)

hboxSave=wx.BoxSizer()
hboxSave.Add(filename,proportion=2,flag=wx.LEFT,border=5)
hboxSave.Add(save_button,proportion=1,flag=wx.LEFT,border=5)

hbox2=wx.BoxSizer()
hbox2.Add(button1,proportion=1,flag=wx.LEFT,border=5)
hbox2.Add(button2,proportion=1,flag=wx.LEFT,border=5)
hbox2.Add(button3,proportion=1,flag=wx.LEFT,border=5)
hbox2.Add(button4,proportion=1,flag=wx.LEFT,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hboxA,proportion=0,flag=wx.EXPAND,border=5)
vbox.Add(hboxB,proportion=0,flag=wx.EXPAND,border=5)
vbox.Add(hboxC,proportion=0,flag=wx.EXPAND,border=5)
vbox.Add(hboxSave,proportion=0,flag=wx.EXPAND,border=5)
vbox.Add(hbox2,proportion=0,flag=wx.EXPAND,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,border=5)



bkg.SetSizer(vbox)
win.Show()
app.MainLoop()



