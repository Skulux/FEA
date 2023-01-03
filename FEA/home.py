# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import io
import requests
import gatherer as API
import Fae_Datenbank as DB
from PIL import Image
###########################################################################
## Class frame_main
###########################################################################

class frame_main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"F E A", pos = wx.DefaultPosition, size = wx.Size( 1440,1024 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_main = wx.BoxSizer( wx.VERTICAL )

		boxsizer_header = wx.BoxSizer( wx.HORIZONTAL )


		boxsizer_header.Add( ( 15, 0), 0, wx.EXPAND, 5 )

		self.bitmap_logo = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"assets\\logo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		boxsizer_header.Add( self.bitmap_logo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.staticText_projectname = wx.StaticText( self, wx.ID_ANY, u"FEA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_projectname.Wrap( -1 )

		self.staticText_projectname.SetFont( wx.Font( 44, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.staticText_projectname.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		boxsizer_header.Add( self.staticText_projectname, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_header.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.searchCtrl_moviesearch = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_SIMPLE )
		self.searchCtrl_moviesearch.ShowSearchButton( True )
		self.searchCtrl_moviesearch.ShowCancelButton( False )
		self.searchCtrl_moviesearch.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.searchCtrl_moviesearch.SetForegroundColour( wx.Colour( 114, 114, 114 ) )
		self.searchCtrl_moviesearch.SetBackgroundColour( wx.Colour( 28, 29, 31 ) )

		boxsizer_header.Add( self.searchCtrl_moviesearch, 2, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_header.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.button_suprise = wx.ToggleButton( self, wx.ID_ANY, u"Überrasch mich!", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.button_suprise.SetValue( True )
		self.button_suprise.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.button_suprise.SetForegroundColour( wx.Colour( 114, 114, 114 ) )
		self.button_suprise.SetBackgroundColour( wx.Colour( 28, 29, 31 ) )

		boxsizer_header.Add( self.button_suprise, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_header.Add( ( 15, 0), 0, wx.EXPAND, 5 )


		boxsizer_main.Add( boxsizer_header, 0, wx.EXPAND, 5 )


		boxsizer_main.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		boxsizer_body = wx.BoxSizer( wx.HORIZONTAL )


		boxsizer_body.Add( ( 15, 0), 0, wx.EXPAND, 5 )

		boxsizer_sideElements = wx.BoxSizer( wx.VERTICAL )

		self.button_home = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.button_home.SetBitmap( wx.Bitmap( u"assets\\home.png", wx.BITMAP_TYPE_ANY ) )
		self.button_home.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.button_home.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_sideElements.Add( self.button_home, 0, wx.ALL, 5 )


		boxsizer_sideElements.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.button_watchlist = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.button_watchlist.SetBitmap( wx.Bitmap( u"assets\\list.png", wx.BITMAP_TYPE_ANY ) )
		self.button_watchlist.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_sideElements.Add( self.button_watchlist, 0, wx.ALL, 5 )


		boxsizer_sideElements.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.button_like = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.button_like.SetBitmap( wx.Bitmap( u"assets\\like.png", wx.BITMAP_TYPE_ANY ) )
		self.button_like.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_sideElements.Add( self.button_like, 0, wx.ALL, 5 )


		boxsizer_sideElements.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.button_settings = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.button_settings.SetBitmap( wx.Bitmap( u"assets\\settings.png", wx.BITMAP_TYPE_ANY ) )
		self.button_settings.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_sideElements.Add( self.button_settings, 0, wx.ALL, 5 )


		boxsizer_sideElements.Add( ( 0, 15), 0, wx.EXPAND, 5 )


		boxsizer_body.Add( boxsizer_sideElements, 0, wx.EXPAND, 5 )

		boxsizer_movies = wx.BoxSizer( wx.VERTICAL )

		boxsizer_topRow = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		boxsizer_moviesTop = wx.BoxSizer( wx.HORIZONTAL )


		boxsizer_moviesTop.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		boxsizer_movie1 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton5 = wx.BitmapButton( self.m_scrolledWindow1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 210,265 ), wx.BU_AUTODRAW|0 )
		boxsizer_movie1.Add( self.m_bpButton5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.staticText_movie1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_movie1.Wrap( -1 )

		self.staticText_movie1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.staticText_movie1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		boxsizer_movie1.Add( self.staticText_movie1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_moviesTop.Add( boxsizer_movie1, 1, wx.EXPAND, 5 )


		boxsizer_moviesTop.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_scrolledWindow1.SetSizer( boxsizer_moviesTop )
		self.m_scrolledWindow1.Layout()
		boxsizer_moviesTop.Fit( self.m_scrolledWindow1 )
		boxsizer_topRow.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )


		boxsizer_movies.Add( boxsizer_topRow, 1, wx.EXPAND, 5 )


		boxsizer_body.Add( boxsizer_movies, 1, wx.EXPAND, 5 )


		boxsizer_main.Add( boxsizer_body, 1, wx.EXPAND, 5 )


		self.SetSizer( boxsizer_main )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.searchCtrl_moviesearch.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.on_search )
		self.button_suprise.Bind( wx.EVT_TOGGLEBUTTON, self.on_suprise )
		self.button_home.Bind( wx.EVT_BUTTON, self.on_home )
		self.button_watchlist.Bind( wx.EVT_BUTTON, self.on_watchlist )
		self.button_like.Bind( wx.EVT_BUTTON, self.on_like )
		self.button_settings.Bind( wx.EVT_BUTTON, self.on_settings )
		self.m_bpButton5.Bind( wx.EVT_BUTTON, self.on_movie )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_search( self, event ):
		event.Skip()

	def on_suprise( self, event ):
		self.m_scrolledWindow1.DestroyChildren()
		trends = [API.search_by_id(API.compare_genres(DB.get_all_movie_ids()), enable_all=True)]
		sizers_movie = []

		for movie in trends:
			self.m_bpButton5 = wx.BitmapButton(self.m_scrolledWindow1, wx.ID_ANY, cnvrt_bmp(movie[1]), wx.DefaultPosition,
											   wx.Size(210, 315), wx.BU_AUTODRAW | 0)
			sizers_movie += [wx.BoxSizer(wx.VERTICAL)]
			sizers_movie[-1].Add(self.m_bpButton5, 0, wx.ALIGN_CENTER | wx.ALL, 5)
			self.staticText_movie1 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u""+movie[0], wx.DefaultPosition,
												   wx.DefaultSize, 0)
			self.staticText_movie1.Wrap(-1)
			self.staticText_movie1.SetFont(
				wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous"))
			self.staticText_movie1.SetForegroundColour(wx.Colour(255, 255, 255))
			sizers_movie[-1].Add(self.staticText_movie1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
		sizer_sizer = []
		boxsizer_moviesTop = wx.BoxSizer(wx.HORIZONTAL)
		for sizer in sizers_movie:
			boxsizer_moviesTop.Add(sizer, 1, wx.EXPAND, 5)
		boxsizer_moviesTop.Add((0, 0), 1, wx.EXPAND, 5)
		self.m_scrolledWindow1.SetSizer(boxsizer_moviesTop)
		self.m_scrolledWindow1.Layout()

	def on_home( self, event ):
		self.m_scrolledWindow1.DestroyChildren()
		trends = API.get_trending(enable_all=True, limit=2)
		sizers_movie = []

		for movie in trends:
			self.m_bpButton5 = wx.BitmapButton(self.m_scrolledWindow1, wx.ID_ANY, cnvrt_bmp(trends[movie][1]), wx.DefaultPosition,
											   wx.Size(210, 315), wx.BU_AUTODRAW | 0)
			sizers_movie += [wx.BoxSizer(wx.VERTICAL)]
			sizers_movie[-1].Add(self.m_bpButton5, 0, wx.ALIGN_CENTER | wx.ALL, 5)
			self.staticText_movie1 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u""+trends[movie][0], wx.DefaultPosition,
												   wx.DefaultSize, 0)
			self.staticText_movie1.Wrap(-1)
			self.staticText_movie1.SetFont(
				wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous"))
			self.staticText_movie1.SetForegroundColour(wx.Colour(255, 255, 255))
			sizers_movie[-1].Add(self.staticText_movie1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
		sizer_sizer = []
		boxsizer_moviesTop = wx.BoxSizer(wx.HORIZONTAL)
		for sizer in sizers_movie:
			boxsizer_moviesTop.Add(sizer, 1, wx.EXPAND, 5)
		boxsizer_moviesTop.Add((0, 0), 1, wx.EXPAND, 5)
		self.m_scrolledWindow1.SetSizer(boxsizer_moviesTop)
		self.m_scrolledWindow1.Layout()

	def on_watchlist( self, event ):
		self.m_scrolledWindow1.DestroyChildren()
		movies = []

		for movie in DB.get_all_movie_ids():
			movies += [API.search_by_id(movie, enable_all=True)]

		sizers_movie = []

		for movie in movies:
			try:
				self.m_bpButton5 = wx.BitmapButton(self.m_scrolledWindow1, wx.ID_ANY, cnvrt_bmp(movie[1]), wx.DefaultPosition,
												   wx.Size(210, 315), wx.BU_AUTODRAW | 0)
				sizers_movie += [wx.BoxSizer(wx.VERTICAL)]
				sizers_movie[-1].Add(self.m_bpButton5, 0, wx.ALIGN_CENTER | wx.ALL, 5)
				self.staticText_movie1 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u""+movie[0], wx.DefaultPosition,
													   wx.DefaultSize, 0)
				self.staticText_movie1.Wrap(-1)
				self.staticText_movie1.SetFont(
					wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous"))
				self.staticText_movie1.SetForegroundColour(wx.Colour(255, 255, 255))
				sizers_movie[-1].Add(self.staticText_movie1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
			except:
				pass
		sizer_sizer = []
		boxsizer_moviesTop = wx.BoxSizer(wx.HORIZONTAL)
		for sizer in sizers_movie:
			boxsizer_moviesTop.Add(sizer, 1, wx.EXPAND, 5)
		boxsizer_moviesTop.Add((0, 0), 1, wx.EXPAND, 5)
		self.m_scrolledWindow1.SetSizer(boxsizer_moviesTop)
		self.m_scrolledWindow1.Layout()

	def on_like( self, event ):
		event.Skip()

	def on_settings( self, event ):
		event.Skip()

	def on_movie( self, event ):
		event.Skip()



def cnvrt_bmp(link):
	try:
		bmp = requests.get(link)
		img = Image.open(io.BytesIO(bmp.content))
		img = img.save("temp.bmp")
		bmp = wx.Bitmap("temp.bmp")
	except:
		bmp = wx.Bitmap("assets\\missing.bmp")
	finally:
		bmp.Rescale(bmp, (210, 265))
		bmp = wx.Bitmap(bmp)
		return bmp

