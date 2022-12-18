# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

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

		self.bitmap_logo = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"assets/logo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
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

		self.button_home.SetBitmap( wx.Bitmap( u"assets/home.png", wx.BITMAP_TYPE_ANY ) )
		self.button_home.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.button_home.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_sideElements.Add( self.button_home, 0, wx.ALL, 5 )


		boxsizer_sideElements.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.button_watchlist = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.button_watchlist.SetBitmap( wx.Bitmap( u"assets/list.png", wx.BITMAP_TYPE_ANY ) )
		self.button_watchlist.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_sideElements.Add( self.button_watchlist, 0, wx.ALL, 5 )


		boxsizer_sideElements.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.button_like = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.button_like.SetBitmap( wx.Bitmap( u"assets/like.png", wx.BITMAP_TYPE_ANY ) )
		self.button_like.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_sideElements.Add( self.button_like, 0, wx.ALL, 5 )


		boxsizer_sideElements.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.button_settings = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

		self.button_settings.SetBitmap( wx.Bitmap( u"assets/settings.png", wx.BITMAP_TYPE_ANY ) )
		self.button_settings.SetBackgroundColour( wx.Colour( 24, 24, 24 ) )

		boxsizer_sideElements.Add( self.button_settings, 0, wx.ALL, 5 )


		boxsizer_sideElements.Add( ( 0, 15), 0, wx.EXPAND, 5 )


		boxsizer_body.Add( boxsizer_sideElements, 0, wx.EXPAND, 5 )

		boxsizer_movies = wx.BoxSizer( wx.VERTICAL )

		boxsizer_topRow = wx.BoxSizer( wx.VERTICAL )

		boxsizer_moviesTop = wx.BoxSizer( wx.HORIZONTAL )


		boxsizer_moviesTop.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		boxsizer_movie1 = wx.BoxSizer( wx.VERTICAL )

		self.bitmap_movie1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 210,265 ), 0 )
		boxsizer_movie1.Add( self.bitmap_movie1, 0, wx.ALL, 5 )

		self.staticText_movie1 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_movie1.Wrap( -1 )

		self.staticText_movie1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.staticText_movie1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		boxsizer_movie1.Add( self.staticText_movie1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_moviesTop.Add( boxsizer_movie1, 1, wx.EXPAND, 5 )


		boxsizer_moviesTop.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		boxsizer_movie2 = wx.BoxSizer( wx.VERTICAL )

		self.bitmap_movie2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 210,265 ), 0 )
		boxsizer_movie2.Add( self.bitmap_movie2, 0, wx.ALL, 5 )

		self.staticText_movie11 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_movie11.Wrap( -1 )

		self.staticText_movie11.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.staticText_movie11.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		boxsizer_movie2.Add( self.staticText_movie11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_moviesTop.Add( boxsizer_movie2, 1, wx.EXPAND, 5 )


		boxsizer_moviesTop.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		boxsizer_movie3 = wx.BoxSizer( wx.VERTICAL )

		self.bitmap_movie3 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 210,265 ), 0 )
		boxsizer_movie3.Add( self.bitmap_movie3, 0, wx.ALL, 5 )

		self.staticText_movie2 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_movie2.Wrap( -1 )

		self.staticText_movie2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.staticText_movie2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		boxsizer_movie3.Add( self.staticText_movie2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_moviesTop.Add( boxsizer_movie3, 1, wx.EXPAND, 5 )


		boxsizer_moviesTop.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		boxsizer_movie1 = wx.BoxSizer( wx.VERTICAL )

		self.bitmap_movie4 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 210,265 ), 0 )
		boxsizer_movie1.Add( self.bitmap_movie4, 0, wx.ALL, 5 )

		self.staticText_movie3 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_movie3.Wrap( -1 )

		self.staticText_movie3.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.staticText_movie3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		boxsizer_movie1.Add( self.staticText_movie3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_moviesTop.Add( boxsizer_movie1, 1, wx.EXPAND, 5 )


		boxsizer_moviesTop.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		boxsizer_topRow.Add( boxsizer_moviesTop, 0, wx.EXPAND, 5 )


		boxsizer_movies.Add( boxsizer_topRow, 1, wx.EXPAND, 5 )

		boxsizer_bottomRow = wx.BoxSizer( wx.VERTICAL )

		boxsizer_moviesBottom = wx.BoxSizer( wx.HORIZONTAL )


		boxsizer_moviesBottom.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		boxsizer_movie5 = wx.BoxSizer( wx.VERTICAL )

		self.bitmap_movie5 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 210,265 ), 0 )
		boxsizer_movie5.Add( self.bitmap_movie5, 0, wx.ALL, 5 )

		self.staticText_movie5 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_movie5.Wrap( -1 )

		self.staticText_movie5.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.staticText_movie5.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		boxsizer_movie5.Add( self.staticText_movie5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_moviesBottom.Add( boxsizer_movie5, 1, wx.EXPAND, 5 )


		boxsizer_moviesBottom.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		boxsizer_movie6 = wx.BoxSizer( wx.VERTICAL )

		self.bitmap_movie6 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 210,265 ), 0 )
		boxsizer_movie6.Add( self.bitmap_movie6, 0, wx.ALL, 5 )

		self.staticText_movie6 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_movie6.Wrap( -1 )

		self.staticText_movie6.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.staticText_movie6.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		boxsizer_movie6.Add( self.staticText_movie6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_moviesBottom.Add( boxsizer_movie6, 1, wx.EXPAND, 5 )


		boxsizer_moviesBottom.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		boxsizer_movie7 = wx.BoxSizer( wx.VERTICAL )

		self.bitmap_movie7 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 210,265 ), 0 )
		boxsizer_movie7.Add( self.bitmap_movie7, 0, wx.ALL, 5 )

		self.staticText_movie7 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_movie7.Wrap( -1 )

		self.staticText_movie7.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.staticText_movie7.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		boxsizer_movie7.Add( self.staticText_movie7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_moviesBottom.Add( boxsizer_movie7, 1, wx.EXPAND, 5 )


		boxsizer_moviesBottom.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		boxsizer_movie8 = wx.BoxSizer( wx.VERTICAL )

		self.bitmap_movie8 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 210,265 ), 0 )
		boxsizer_movie8.Add( self.bitmap_movie8, 0, wx.ALL, 5 )

		self.staticText_movie8 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_movie8.Wrap( -1 )

		self.staticText_movie8.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Righteous" ) )
		self.staticText_movie8.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		boxsizer_movie8.Add( self.staticText_movie8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		boxsizer_moviesBottom.Add( boxsizer_movie8, 1, wx.EXPAND, 5 )


		boxsizer_moviesBottom.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		boxsizer_bottomRow.Add( boxsizer_moviesBottom, 1, wx.EXPAND, 5 )


		boxsizer_movies.Add( boxsizer_bottomRow, 1, wx.EXPAND, 5 )


		boxsizer_body.Add( boxsizer_movies, 1, wx.EXPAND, 5 )


		boxsizer_main.Add( boxsizer_body, 1, wx.EXPAND, 5 )


		self.SetSizer( boxsizer_main )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


