# -*- coding: utf-8 -*- 
# MIT license
#
# Copyright (C) 2018 by XESS Corporation / Hildo G Jr
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Libraries.
import wx # wxWidgets for Python.
import os # To access OS commands.
import platform # To check the system platform when open the XLS file.
import re # Regular expression parser.
from . import __version__ # Version control by @xesscorp.
from .kicost import distributors, eda_tools # List of the distributos and EDA supported.

__all__ = ['kicost_gui']


# Author information.
__author__ = 'Hildo Guillardi Junior'
__webpage__ = 'https://github.com/hildogjr/'
__company__ = 'University of Campinas - Brazil'


FILE_HIST_QTY = 10
WILDCARD = "BoM compatible formats (*.xml,*.csv)|*.xml;*.csv|"\
			"KiCad/Altium BoM file (*.xml)|*.xml|" \
			"Proteus/Generic BoM file (*.csv)|*.csv"

class MyForm ( wx.Frame ):
	
	def __init__( self, parent ):
		#### **  Begin of the guide code generated by wxFormBulilder software, avaliable in <https://github.com/wxFormBuilder/wxFormBuilder/>  ** ####
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"KiCost", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Files" ), wx.HORIZONTAL )
		
		m_comboBox_filesChoices = []
		self.m_comboBox_files = wx.ComboBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Files", wx.DefaultPosition, wx.DefaultSize, m_comboBox_filesChoices, 0 )
		self.m_comboBox_files.SetToolTip( u"BoM file(s) to scrape." )
		
		sbSizer2.Add( self.m_comboBox_files, 1, wx.ALL, 5 )
		
		self.m_button_openfile = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Chooose BoM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_openfile.SetToolTip( u"Open a BoM file." )
		
		sbSizer2.Add( self.m_button_openfile, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( sbSizer2, 0, wx.EXPAND|wx.TOP, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Distributors to scrape" ), wx.VERTICAL )
		
		m_checkList_distChoices = [wx.EmptyString]
		self.m_checkList_dist = wx.CheckListBox( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList_distChoices, 0 )
		self.m_checkList_dist.SetToolTip( u"Web distributor (or local) to scrape the prices." )
		
		sbSizer3.Add( self.m_checkList_dist, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer4.Add( sbSizer3, 1, wx.EXPAND|wx.LEFT, 5 )
		
		wSizer1 = wx.WrapSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_radioBox_edatoolChoices = [ wx.EmptyString ]
		self.m_radioBox_edatool = wx.RadioBox( self.m_panel1, wx.ID_ANY, u"EDA tool", wx.DefaultPosition, wx.DefaultSize, m_radioBox_edatoolChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_edatool.SetSelection( 0 )
		self.m_radioBox_edatool.SetToolTip( u"Choose EDA tool from which the XML BOM file originated, or use csv for .CSV files." )
		
		bSizer6.Add( self.m_radioBox_edatool, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button_run = wx.Button( self.m_panel1, wx.ID_ANY, u"KiCost it!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_run.SetToolTip( u"Rum KiCost." )
		
		bSizer7.Add( self.m_button_run, 0, wx.ALL, 5 )
		
		self.m_checkBox_openXLS = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Open spreadsheet", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_openXLS.SetToolTip( u"Open the spreadsheet after finish the KiCost process." )
		
		bSizer7.Add( self.m_checkBox_openXLS, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		wSizer1.Add( bSizer6, 1, wx.EXPAND|wx.RIGHT, 5 )
		
		
		bSizer4.Add( wSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"BoM", True )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		wSizer2 = wx.WrapSizer( wx.HORIZONTAL )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Parallel process", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer9.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_spinCtrl_np = wx.SpinCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 30, 0 )
		self.m_spinCtrl_np.SetToolTip( u"Set the number of parallel processes used for web scraping part data." )
		
		bSizer9.Add( self.m_spinCtrl_np, 0, wx.ALL, 5 )
		
		self.m_checkBox_overwrite = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"--overwrite", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_overwrite.SetValue(True) 
		self.m_checkBox_overwrite.SetToolTip( u"Allow overwriting of an existing spreadsheet." )
		
		bSizer9.Add( self.m_checkBox_overwrite, 0, wx.ALL, 5 )
		
		
		wSizer2.Add( bSizer9, 1, wx.TOP|wx.LEFT, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Scrap retries", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer11.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_spinCtrl_retries = wx.SpinCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 4, 200, 0 )
		self.m_spinCtrl_retries.SetToolTip( u"Specify the number of attempts to retrieve part data from a website." )
		
		bSizer11.Add( self.m_spinCtrl_retries, 0, wx.ALL, 5 )
		
		self.m_checkBox_quite = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"--quite", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_quite.SetValue(True) 
		self.m_checkBox_quite.SetToolTip( u"Enable quiet mode with no warnings." )
		
		bSizer11.Add( self.m_checkBox_quite, 0, wx.ALL, 5 )
		
		
		wSizer2.Add( bSizer11, 1, wx.TOP|wx.RIGHT, 5 )
		
		
		bSizer8.Add( wSizer2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Extra commands", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer8.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrlextracmd = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlextracmd.SetToolTip( u" Here use the kicost extra commands. In the terminal/command type`kicost --help` to check the list." )
		
		bSizer8.Add( self.m_textCtrlextracmd, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer8 )
		self.m_panel2.Layout()
		bSizer8.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"KiCost config", False )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText_credits = wx.StaticText( self.m_panel3, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_credits.Wrap( -1 )
		bSizer2.Add( self.m_staticText_credits, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( bSizer2 )
		self.m_panel3.Layout()
		bSizer2.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"About", False )
		
		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.app_close )
		self.m_button_openfile.Bind( wx.EVT_BUTTON, self.button_openfile )
		self.m_button_run.Bind( wx.EVT_BUTTON, self.button_run )
		#### **  End of the guide code generated by wxFormBulilder software, avaliable in <https://github.com/wxFormBuilder/wxFormBuilder/>  ** ####
		self.restore_properties()
	
	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	
	def app_close( self, event ):
		self.save_properties()
		event.Skip()
	
	def button_openfile( self, event ):
		""" Create and show the Open FileDialog """
		actualDir = (os.getcwd() if self.m_comboBox_files.GetValue() else \
			os.path.dirname(os.path.abspath( self.m_comboBox_files.GetValue() )) )
		
		print(actualDir)
		
		dlg = wx.FileDialog(
			self, message="Select BoMs",
			defaultDir=actualDir, 
			defaultFile="",
			wildcard=WILDCARD,
			style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
			)
		if dlg.ShowModal() == wx.ID_OK:
			paths = dlg.GetPaths()
			print("You chose the following file(s):")
			for path in paths:
				print(path)
			fileBOM = ' '.join(['"' + file + '"' for file in paths])
			if self.m_comboBox_files.FindString(fileBOM)==wx.NOT_FOUND:
				self.m_comboBox_files.Insert( fileBOM, 0 )
			self.m_comboBox_files.SetValue( fileBOM )
			try:
				self.m_comboBox_files.Delete(FILE_HIST_QTY-1) # Keep 10 files on history.
			except:
				pass
		dlg.Destroy()
		
		event.Skip()
	
	def button_run( self, event ):
		''' Run KiCost '''
		
		self.save_properties() # Save the current graphical configuration before call the KiCost motor.
		
		# Get the current distributors to scrape.
		choisen_dist = list(self.m_checkList_dist.GetCheckedItems())
		if choisen_dist:
			choisen_dist = [self.distributors_list[idx] for idx in choisen_dist]
			choisen_dist = ' --include ' + ' '.join(choisen_dist)
		else:
			choisen_dist = ''
		
		command = ("kicost"
			+ " -i " + self.m_comboBox_files.GetValue()
			+ " -eda " * (not self.m_radioBox_edatool.IsEmpty()) + self.m_radioBox_edatool.GetStringSelection()
			+ " -np " + str(self.m_spinCtrl_np.GetValue()) # Parallels process scrapping.
			+ " -rt " + str(self.m_spinCtrl_retries.GetValue()) # Retry time in the scraps
			+ " -w" * self.m_checkBox_overwrite.GetValue()
			+ " -q" * self.m_checkBox_quite.GetValue()
			+ choisen_dist
			+ self.m_textCtrlextracmd.GetValue()
			)
		print("Running: ", command)
		os.system(command + '&') # Could call directly the `kicost.py`, which is better? Missing put the process bar here!
		
		if self.m_checkBox_openXLS.GetValue():
			spreadsheet_file = os.path.splitext( self.combobox_files.GetValue() ) + '.xlsx'
			print('Opening output file: ', spreadsheet_file)
			if platform.system()=='Linux':
				os.system('xdg-open ' + '"' + spreadsheet_file + '"&')
			elif platform.system()=='Windows':
				os.system('explorer ' + '"' + spreadsheet_file + '"&')
			elif platform.system()=='Darwin': # Mac-OS
				os.system('open -n ' + '"' + spreadsheet_file + '"&')
			else:
				print('Not recognized OS.')
		
		event.Skip()

	#----------------------------------------------------------------------
	def restore_properties(self):
		''' Restore the current proprieties of the graphical elements '''
		
		# Set the aplication windows title and configurations
		self.SetTitle('KiCost v.' + __version__)
		
		# Recovery the last configurations used (found the folder of the file by the OS).
		if platform.system()=='Linux':
			self.configFile =  str(os.path.expanduser('~')) + '/kicost.config'
		elif platform.system()=='Windows':
			self.configFile = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData) + '\\kicost.config'
		elif platform.system()=='Darwin': # Mac-OS
			self.configFile = '??'
		else:
			print('Not recognized OS.')
		try:
			print(self.configFile)
			h_configFile = open(self.configFile,'r')
			configs = h_configFile.read()
			h_configFile.close()
		except:
			print('Configuration file not founded.')
		
		# Files in the history.
		if not self.m_comboBox_files.IsListEmpty(): # If have some history, set to the last used file.
			self.m_comboBox_files.IsListEmpty(0)
		
		# Current distrubutors module recognized.
		self.distributors_list = [*sorted(list(distributors.keys()))]
		self.m_checkList_dist.Clear()
		self.m_checkList_dist.Append(self.distributors_list)
		for idx in range(len(self.distributors_list)):
			self.m_checkList_dist.Check(idx,True) # All start checked (after is modifed by the configuration file).
		
		# Current EDA tools module recoginized.
#		self.eda_list = [*sorted(list(eda_tools.keys()))]
#		self.m_radioBox_edatool.Clear(0)
		self.m_radioBox_edatool.SetString(0,"jk")
		
		# Credits, search by `AUTHOR.rst` file.
		try:
			credits_file = open( os.path.dirname(os.path.abspath(__file__)) \
				 + '/../kicost-' + __version__ + '.dist-info/AUTHOR.rst')
			credits = credits_file.read()
			credits_file.close()
		except:
			credits = '''
			=======
			Credits
			=======\n
			Development Lead
			----------------
			* XESS Corporation <info@xess.com>\n
			Contributors
			------------
			* Oliver Martin: https://github.com/oliviermartin
			* Timo Alho: https://github.com/timoalho
			* Steven Johnson: https://github.com/stevenj
			* Diorcet Yann: https://github.com/diorcety
			* Giacinto Luigi Cerone https://github.com/glcerone
			* Hildo Guillardi Júnior https://github.com/hildogjr
			* Adam Heinrich https://github.com/adamheinrich
			'''
			credits = re.sub('[\t*, +]','',credits)
		self.m_staticText_credits.SetLabel( 
			'KiCost version ' + __version__ + '\n\n'
			+ credits + '\nGraphical interface by ' + __author__ )

	#----------------------------------------------------------------------
	def save_properties(self):
		''' Save the current proprieties of the graphical elements '''
		try:
			h_configFile = open(self.configFile,'w')
			h_configFile.write('teste')
			h_configFile.close()
		except:
			print('Configurations not salved.')





#######################################################################

def kicost_gui():
	app = wx.App(redirect=False)
	frame = MyForm(None)
	frame.Show()
	app.MainLoop()
