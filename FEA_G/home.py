# -*- coding: utf-8 -*-


import wx
import wx.xrc
import io
import os
import requests
import gatherer as API, config as cf
import Fae_Datenbank as DB
from PIL import Image

path = os.path.dirname(os.path.realpath(__file__))
LANG = cf.read()[1]
LANGF = cf.load_lang()
NSFW = cf.read()[2]


class frame_main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"F E A", pos = wx.DefaultPosition, size = wx.Size( 1440,1024 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.parent = parent
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		self.SetIcon(wx.Icon(f"{path}\\assets\\logo.ico"))

		boxsizer_main = wx.BoxSizer( wx.VERTICAL )

		boxsizer_header = wx.BoxSizer( wx.HORIZONTAL )


		boxsizer_header.Add( ( 15, 0), 0, wx.EXPAND, 5 )

		self.bitmap_logo = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( f"{path}\\assets\\logo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		boxsizer_header.Add( self.bitmap_logo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.staticText_projectname = wx.StaticText( self, wx.ID_ANY, u"FEA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_projectname.Wrap( -1 )

		self.staticText_projectname.SetFont( wx.Font( 44, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.staticText_projectname.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		boxsizer_header.Add( self.staticText_projectname, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_header.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.searchCtrl_moviesearch = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_SIMPLE )
		self.searchCtrl_moviesearch.SetDescriptiveText(u""+LANGF["search"][LANG])
		self.searchCtrl_moviesearch.ShowSearchButton( True )
		self.searchCtrl_moviesearch.ShowCancelButton( False )
		self.searchCtrl_moviesearch.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.searchCtrl_moviesearch.SetForegroundColour( wx.Colour( 114, 114, 114 ) )
		self.searchCtrl_moviesearch.SetBackgroundColour( wx.Colour( 28, 29, 31 ) )

		boxsizer_header.Add( self.searchCtrl_moviesearch, 2, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_header.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.button_suprise = wx.ToggleButton( self, wx.ID_ANY, u""+LANGF["surprise_me"][LANG], wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
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

		self.button_home.SetBitmap( wx.Bitmap( f"{path}\\assets\\home.png", wx.BITMAP_TYPE_ANY ) )
		self.button_home.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.button_home.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_sideElements.Add( self.button_home, 0, wx.ALL, 5 )


		boxsizer_sideElements.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.button_watchlist = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.button_watchlist.SetBitmap( wx.Bitmap( f"{path}\\assets\\list.png", wx.BITMAP_TYPE_ANY ) )
		self.button_watchlist.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_sideElements.Add( self.button_watchlist, 0, wx.ALL, 5 )


		boxsizer_sideElements.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.button_like = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.button_like.SetBitmap( wx.Bitmap( f"{path}\\assets\\like.png", wx.BITMAP_TYPE_ANY ) )
		self.button_like.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_sideElements.Add( self.button_like, 0, wx.ALL, 5 )


		boxsizer_sideElements.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.button_settings = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.button_settings.SetBitmap( wx.Bitmap( f"{path}\\assets\\settings.png", wx.BITMAP_TYPE_ANY ) )
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

		boxsizer_moviesTop.Add( boxsizer_movie1, 1, wx.EXPAND, 5 )


		boxsizer_moviesTop.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_scrolledWindow1.SetSizer( boxsizer_moviesTop )
		self.m_scrolledWindow1.Layout()
		boxsizer_moviesTop.Fit( self.m_scrolledWindow1 )
		boxsizer_topRow.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )


		boxsizer_movies.Add( boxsizer_topRow, 1, wx.EXPAND, 5 )


		boxsizer_body.Add( boxsizer_movies, 1, wx.EXPAND, 5 )


		boxsizer_main.Add( boxsizer_body, 1, wx.EXPAND, 5 )

		self.on_home(None)
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
		self.Bind(wx.EVT_CLOSE, self.OnClose)
	def __del__( self ):
		pass

	def OnClose(self, event):
		exit()


	def on_search( self, event ):
		self.m_scrolledWindow1.DestroyChildren()
		trends = API.search_by_name(str(self.searchCtrl_moviesearch.GetValue()), enable_all=True)
		sizers_movie = []

		for movie in trends:
			self.m_bpButton5 = wx.BitmapButton(self.m_scrolledWindow1, wx.ID_ANY, cnvrt_bmp(trends[movie][1]), wx.DefaultPosition,
											   wx.Size(-1, -1), wx.BU_AUTODRAW | 0)
			sizers_movie += [wx.BoxSizer(wx.VERTICAL)]
			self.m_bpButton5.myname = movie
			sizers_movie[-1].Add(self.m_bpButton5, 0, wx.ALIGN_CENTER | wx.ALL, 5)
			self.staticText_movie1 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u""+short_name(trends[movie][0]), wx.DefaultPosition,
												   wx.DefaultSize, 0)
			self.staticText_movie1.Wrap(-1)
			self.staticText_movie1.SetFont(
				wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous"))
			self.staticText_movie1.SetForegroundColour(wx.Colour(255, 255, 255))
			sizers_movie[-1].Add(self.staticText_movie1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
			self.m_bpButton5.Bind(wx.EVT_BUTTON, self.on_movie)
		sizer_sizer = []
		boxsizer_moviesTop = wx.BoxSizer(wx.VERTICAL)
		for sizer in sizers_movie:
			sizer_sizer += [sizer]
			if len(sizer_sizer) == 4:
				temp_sizer = wx.BoxSizer(wx.HORIZONTAL)
				for sizer2 in sizer_sizer:
					temp_sizer.Add(sizer2, 1, wx.EXPAND, 5)
					temp_sizer.Add((0, 0), 1, wx.EXPAND, 5)
				sizer_sizer = []
				boxsizer_moviesTop.Add(temp_sizer)
		if sizer_sizer:
			temp_sizer = wx.BoxSizer(wx.HORIZONTAL)
			for sizer2 in sizer_sizer:
				temp_sizer.Add(sizer2, 1, wx.EXPAND, 5)
				temp_sizer.Add((0, 0), 1, wx.EXPAND, 5)
			boxsizer_moviesTop.Add(temp_sizer)
		boxsizer_moviesTop.Add((0, 0), 1, wx.EXPAND, 5)
		self.m_scrolledWindow1.SetSizer(boxsizer_moviesTop)
		self.m_scrolledWindow1.Layout()
		self.Layout()

	def on_suprise( self, event ):
		self.m_scrolledWindow1.DestroyChildren()
		movie_m = API.compare_genres(DB.get_all_movie_ids())
		trends = [API.search_by_id(movie_m, enable_all=True)]
		sizers_movie = []

		for movie in trends:
			self.m_bpButton5 = wx.BitmapButton(self.m_scrolledWindow1, wx.ID_ANY, cnvrt_bmp(movie[1]), wx.DefaultPosition,
											   wx.Size(210, 265), wx.BU_AUTODRAW | 0)
			sizers_movie += [wx.BoxSizer(wx.VERTICAL)]
			self.m_bpButton5.myname = movie_m
			sizers_movie[-1].Add(self.m_bpButton5, 0, wx.ALIGN_CENTER | wx.ALL, 5)
			self.staticText_movie1 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u""+short_name(movie[0]), wx.DefaultPosition,
												   wx.DefaultSize, 0)
			self.staticText_movie1.Wrap(-1)
			self.staticText_movie1.SetFont(
				wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous"))
			self.staticText_movie1.SetForegroundColour(wx.Colour(255, 255, 255))
			sizers_movie[-1].Add(self.staticText_movie1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
			self.m_bpButton5.Bind(wx.EVT_BUTTON, self.on_movie)
		sizer_sizer = []
		boxsizer_moviesTop = wx.BoxSizer(wx.HORIZONTAL)
		for sizer in sizers_movie:
			boxsizer_moviesTop.Add(sizer, 1, wx.EXPAND, 5)
		boxsizer_moviesTop.Add((0, 0), 1, wx.EXPAND, 5)
		self.m_scrolledWindow1.SetSizer(boxsizer_moviesTop)
		self.m_scrolledWindow1.Layout()
		self.Layout()

	def on_home( self, event ):
		self.m_scrolledWindow1.DestroyChildren()
		trends = API.get_trending(enable_all=True, limit=2)
		sizers_movie = []

		for movie in trends:
			self.m_bpButton5 = wx.BitmapButton(self.m_scrolledWindow1, wx.ID_ANY, cnvrt_bmp(trends[movie][1]), wx.DefaultPosition,
											   wx.Size(210, 265), wx.BU_AUTODRAW | 0)
			sizers_movie += [wx.BoxSizer(wx.VERTICAL)]
			self.m_bpButton5.myname = movie
			sizers_movie[-1].Add(self.m_bpButton5, 0, wx.ALIGN_CENTER | wx.ALL, 5)
			self.staticText_movie1 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u""+short_name(trends[movie][0]), wx.DefaultPosition,
												   wx.DefaultSize, 0)
			self.staticText_movie1.Wrap(-1)
			self.staticText_movie1.SetFont(
				wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous"))
			self.staticText_movie1.SetForegroundColour(wx.Colour(255, 255, 255))
			sizers_movie[-1].Add(self.staticText_movie1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
			self.m_bpButton5.Bind(wx.EVT_BUTTON, self.on_movie)
		sizer_sizer = []
		boxsizer_moviesTop = wx.BoxSizer(wx.VERTICAL)
		for sizer in sizers_movie:
			sizer_sizer += [sizer]
			if len(sizer_sizer) == 4:
				temp_sizer = wx.BoxSizer(wx.HORIZONTAL)
				for sizer2 in sizer_sizer:
					temp_sizer.Add(sizer2, 1, wx.EXPAND, 5)
					temp_sizer.Add((0, 0), 1, wx.EXPAND, 5)
				sizer_sizer = []
				boxsizer_moviesTop.Add(temp_sizer)
		if sizer_sizer:
			temp_sizer = wx.BoxSizer(wx.HORIZONTAL)
			for sizer2 in sizer_sizer:
				temp_sizer.Add(sizer2, 1, wx.EXPAND, 5)
				temp_sizer.Add((0, 0), 1, wx.EXPAND, 5)
			boxsizer_moviesTop.Add(temp_sizer, 1, wx.EXPAND, 5)
		boxsizer_moviesTop.Add((0, 0), 1, wx.EXPAND, 5)
		self.m_scrolledWindow1.SetSizer(boxsizer_moviesTop)
		self.m_scrolledWindow1.Layout()
		self.Layout()

	def on_watchlist( self, event):
		self.m_scrolledWindow1.DestroyChildren()
		movies = []
		movie_ids = []
		for movie in DB.get_all_movie_ids():
			movie_ids += [movie]
			movies += [API.search_by_id(movie, enable_all=True)]

		sizers_movie = []
		if movies:
			for i, movie in enumerate(movies):
				try:
					self.bmp_button = wx.BitmapButton(self.m_scrolledWindow1, wx.ID_ANY, cnvrt_bmp(movie[1]), wx.DefaultPosition,
													   wx.Size(210, 265), wx.BU_AUTODRAW | 0)
					self.bmp_button.myname = movie_ids[i]
					sizers_movie += [wx.BoxSizer(wx.VERTICAL)]
					sizers_movie[-1].Add(self.bmp_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)
					self.staticText_movie1 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u""+short_name(movie[0]), wx.DefaultPosition,
														   wx.DefaultSize, 0)
					self.staticText_movie1.Wrap(-1)
					self.staticText_movie1.SetFont(
						wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous"))
					self.staticText_movie1.SetForegroundColour(wx.Colour(255, 255, 255))
					sizers_movie[-1].Add(self.staticText_movie1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
					self.bmp_button.Bind(wx.EVT_BUTTON, self.on_movie)
				except:
					pass
			sizer_sizer = []
			boxsizer_moviesTop = wx.BoxSizer(wx.VERTICAL)
			for sizer in sizers_movie:
				sizer_sizer += [sizer]
				if len(sizer_sizer) == 4:
					temp_sizer = wx.BoxSizer(wx.HORIZONTAL)
					for sizer2 in sizer_sizer:
						temp_sizer.Add(sizer2, 1, wx.EXPAND, 5)
						temp_sizer.Add((0, 0), 1, wx.EXPAND, 5)
					sizer_sizer = []
					boxsizer_moviesTop.Add(temp_sizer)
			if sizer_sizer:
				temp_sizer = wx.BoxSizer(wx.HORIZONTAL)
				for sizer2 in sizer_sizer:
					temp_sizer.Add(sizer2, 1, wx.EXPAND, 5)
					temp_sizer.Add((0, 0), 1, wx.EXPAND, 5)
				boxsizer_moviesTop.Add(temp_sizer)
			boxsizer_moviesTop.Add((0, 0), 1, wx.EXPAND, 5)
		else:
			boxsizer_moviesTop = wx.BoxSizer(wx.VERTICAL)
			temp_sizer = wx.BoxSizer(wx.HORIZONTAL)
			self.staticText_movie1 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u""+LANGF["empty"][LANG],
												   wx.DefaultPosition,
												   wx.DefaultSize, 0)
			self.staticText_movie1.Wrap(-1)
			self.staticText_movie1.SetFont(
				wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous"))
			self.staticText_movie1.SetForegroundColour(wx.Colour(255, 255, 255))
			temp_sizer.Add(self.staticText_movie1, 1, wx.ALIGN_CENTER, 5)
			boxsizer_moviesTop.Add(temp_sizer)
			boxsizer_moviesTop.Add((0, 0), 1, wx.EXPAND, 5)

		self.m_scrolledWindow1.SetSizer(boxsizer_moviesTop)
		self.m_scrolledWindow1.Layout()
		self.Layout()

	def on_like( self, event ):
		event.Skip()

	def on_settings( self, event ):
		self.m_scrolledWindow1.DestroyChildren()

		boxsizer_settings = wx.BoxSizer(wx.VERTICAL)

		boxsizer_lang_text = wx.BoxSizer(wx.HORIZONTAL)



		self.st_lang = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u""+LANGF["choose_language"][LANG], wx.DefaultPosition, wx.DefaultSize, 0)
		self.st_lang.Wrap(-1)

		self.st_lang.SetFont(
			wx.Font(36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
		self.st_lang.SetForegroundColour(wx.Colour(255, 255, 255))
		self.st_lang.SetBackgroundColour(wx.Colour(24, 24, 24))

		boxsizer_lang_text.Add(self.st_lang, 0, wx.ALL, 5)

		boxsizer_settings.Add(boxsizer_lang_text, 0, wx.ALIGN_CENTER, 5)

		boxsizer_lang_box = wx.BoxSizer(wx.HORIZONTAL)



		ch_langChoices = [u"Deutsch", u"English"]
		self.ch_lang = wx.Choice(self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_langChoices, 0)

		self.ch_lang.SetSelection(1 if LANG == "en-US" else 0)
		self.ch_lang.SetFont(
			wx.Font(36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
		self.ch_lang.SetBackgroundColour(wx.Colour(24, 24, 24))

		boxsizer_lang_box.Add(self.ch_lang, 0, wx.ALL | wx.TOP, 5)

		boxsizer_settings.Add(boxsizer_lang_box, 1, wx.ALIGN_CENTER, 5)




		boxsizer_nsfw = wx.BoxSizer(wx.VERTICAL)

		boxsizer_nsfw_text = wx.BoxSizer(wx.HORIZONTAL)

		self.st_nsfw = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u""+LANGF["nsfw"][LANG], wx.DefaultPosition, wx.DefaultSize, 0)
		self.st_nsfw.Wrap(-1)

		self.st_nsfw.SetFont(
			wx.Font(36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
		self.st_nsfw.SetForegroundColour(wx.Colour(255, 255, 255))
		self.st_nsfw.SetBackgroundColour(wx.Colour(24, 24, 24))

		boxsizer_nsfw_text.Add(self.st_nsfw, 0, wx.ALL, 5)

		boxsizer_settings.Add(boxsizer_nsfw_text, 0, wx.ALIGN_CENTER, 5)

		ch_nsfw_c = [u""+LANGF["disabled"][LANG], u""+LANGF["enabled"][LANG]]
		self.ch_nsfw = wx.Choice(self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_nsfw_c, 0)
		self.ch_nsfw.SetSelection(1 if NSFW == "true" else 0)
		self.ch_nsfw.SetFont(wx.Font(36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))
		self.ch_nsfw.SetBackgroundColour(wx.Colour(24, 24, 24))

		boxsizer_nsfw.Add(self.ch_nsfw, 0, wx.ALL, 5)

		boxsizer_settings.Add(boxsizer_nsfw, 0, wx.ALIGN_CENTER, 5)

		self.ch_nsfw.Bind(wx.EVT_CHOICE, self.on_nsfw)

		self.ch_lang.Bind(wx.EVT_CHOICE, self.on_lang)

		self.m_scrolledWindow1.SetSizer(boxsizer_settings)
		self.m_scrolledWindow1.Layout()
		self.Layout()

	def on_lang(self, event):
		global LANG
		sel = int(self.ch_lang.GetCurrentSelection()) # 0 = DE| 1 = EN
		if sel == 1:
			sel = "en-US"
		else:
			sel = "de-DE"
		print(sel)
		cf.change(language=sel)
		API.setup()
		LANG = sel
		self.Hide()
		self.child = self.__init__(self)


	def on_nsfw(self, event):
		global NSFW
		print("here")
		sel = "false" if int(self.ch_nsfw.GetCurrentSelection()) == 0 else "true" # 0 = OFF | 1 = ON
		print(sel)
		print(cf.change(nsfw=sel))
		API.setup()
		NSFW = sel


	def on_movie( self, event):
		movie_id = event.GetEventObject().myname
		movie = API.search_by_id(movie_id, enable_all=True)
		description = movie[4]

		self.m_scrolledWindow1.DestroyChildren()

		boxsizer_movies = wx.BoxSizer( wx.VERTICAL )


		boxsizer_movies.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		box_sizer_mall = wx.BoxSizer( wx.VERTICAL )

		boxsizer_movie = wx.BoxSizer( wx.HORIZONTAL )

		boxsizer_left = wx.BoxSizer( wx.VERTICAL )

		self.img = wx.StaticBitmap( self.m_scrolledWindow1, wx.ID_ANY, cnvrt_bmp(movie[1]), wx.DefaultPosition, wx.Size( 210,265 ), 0 )
		boxsizer_left.Add( self.img, 0, wx.ALL, 5 )

		self.name = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Name: "+str(movie[0]), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name.Wrap( -1 )

		self.name.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.name.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.name.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_left.Add(self.name, 0, wx.ALL, 5)

		self.year = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u""+LANGF["release"][LANG]+": "+str(movie[2]), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.year.Wrap( -1 )

		self.year.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.year.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.year.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_left.Add( self.year, 0, wx.ALL, 5 )

		self.rating = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u""+LANGF["rating"][LANG]+": "+str(movie[3])+u"★", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rating.Wrap( -1 )

		self.rating.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.rating.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.rating.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_left.Add( self.rating, 0, wx.ALL, 5 )


		boxsizer_movie.Add( boxsizer_left, 1, 0, 5 )

		bSizer10 = wx.BoxSizer(wx.VERTICAL)

		self.description = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, u""+description, wx.DefaultPosition,
									   wx.Size( 800,250 ), wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH)
		self.description.SetForegroundColour(wx.Colour(255, 255, 255))
		self.description.SetBackgroundColour(wx.Colour(24, 24, 24))

		bSizer10.Add(self.description, 0, wx.ALL, 5)


		boxsizer_movie.Add( bSizer10, 10, wx.EXPAND, 5 )


		box_sizer_mall.Add( boxsizer_movie, 1, wx.EXPAND, 5 )

		watchlist = wx.BoxSizer( wx.VERTICAL )

		entry_box_status = wx.BoxSizer( wx.HORIZONTAL )


		data = []
		try:
			a = 0
			if a := DB.get_movie_data_by_id(movie_id):
				data = a
		except:
			data = [0, 0, 0, ""]


		self.st_status = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u""+LANGF["status"][LANG]+": ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_status.Wrap( -1 )

		self.st_status.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.st_status.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		entry_box_status.Add( self.st_status, 0, wx.ALL, 5 )

		ch_statusChoices = [ u"Planned", u"Watching", u"Done"]
		self.ch_status = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_statusChoices, 0 )
		self.ch_status.SetSelection(data[2])
		entry_box_status.Add( self.ch_status, 0, wx.ALL, 5 )


		watchlist.Add( entry_box_status, 0, 0, 0 )

		entry_box_rating = wx.BoxSizer( wx.HORIZONTAL )

		self.st_rating = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u""+LANGF["rating"][LANG]+": ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_rating.Wrap( -1 )

		self.st_rating.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.st_rating.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		entry_box_rating.Add( self.st_rating, 0, wx.ALL, 5 )

		self.m_spinCtrlDouble1 = wx.SpinCtrlDouble( self.m_scrolledWindow1, wx.ID_ANY, str(data[1]), wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0.000000, 1 )
		self.m_spinCtrlDouble1.SetDigits(0)
		entry_box_rating.Add( self.m_spinCtrlDouble1, 0, wx.ALL, 5 )


		watchlist.Add( entry_box_rating, 0, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.st_comment = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u""+LANGF["comment"][LANG]+": ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_comment.Wrap( -1 )

		self.st_comment.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.st_comment.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer15.Add( self.st_comment, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, data[3], wx.DefaultPosition, wx.Size( 400,200 ), wx.TE_MULTILINE )
		bSizer15.Add( self.m_textCtrl1, 0, wx.ALL, 5 )


		watchlist.Add( bSizer15, 0, wx.EXPAND, 5 )

		buttons = wx.BoxSizer( wx.HORIZONTAL )

		self.delete = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u""+LANGF["delete"][LANG], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.delete.Bind(wx.EVT_BUTTON, self.on_delete)
		buttons.Add( self.delete, 0, wx.ALIGN_CENTER, 5 )

		self.delete.myname = movie_id

		self.save = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u""+LANGF["save"][LANG], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.save.Bind(wx.EVT_BUTTON, self.on_save)
		buttons.Add( self.save, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		self.save.myname = movie_id


		watchlist.Add( buttons, 0, wx.EXPAND, 5 )


		box_sizer_mall.Add( watchlist, 5, wx.EXPAND, 0 )


		self.m_scrolledWindow1.SetSizer( box_sizer_mall )
		self.m_scrolledWindow1.Layout()
		box_sizer_mall.Fit( self.m_scrolledWindow1 )

	def on_delete(self, event):
		movie_id = event.GetEventObject().myname
		DB.delete_entry(movie_id)

	def on_save(self, event):
		movie_id = event.GetEventObject().myname
		status = int(self.ch_status.GetCurrentSelection())
		rating = float(self.m_spinCtrlDouble1.GetValue())
		comment_len = int(self.m_textCtrl1.GetNumberOfLines())
		comment_strings = [self.m_textCtrl1.GetLineText(x) for x in range(comment_len)]
		comment = "\n".join(comment_strings)
		DB.insert_data(movie_id, rating, status, comment)


def cnvrt_bmp(link):
	try:
		bmp = requests.get(link)
		img = Image.open(io.BytesIO(bmp.content))
		img.save("temp.bmp")
		bmp = wx.Bitmap("temp.bmp")
	except:
		bmp = wx.Bitmap(f"{path}\\assets\\missing.bmp")
	finally:
		bmp.Rescale(bmp, (210, 265))
		bmp = wx.Bitmap(bmp)
		return bmp


def short_name(name):
	if len(name) > 20:
		name = name[:20]+"..."
	return name

