#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Aug  5 11:53:02 2014
##################################################

from gnuradio import audio
from gnuradio import blks2
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.trans_width = trans_width = 20e3
		self.samp_rate = samp_rate = 1152e3
		self.quad_rate = quad_rate = 192e3
		self.freq = freq = 91.9e6
		self.cutoff_freq = cutoff_freq = 100e3

		##################################################
		# Blocks
		##################################################
		self._trans_width_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.trans_width,
			callback=self.set_trans_width,
			label="Transition Width",
			converter=forms.float_converter(),
		)
		self.Add(self._trans_width_text_box)
		self._quad_rate_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.quad_rate,
			callback=self.set_quad_rate,
			label="Quadrature Rate",
			converter=forms.float_converter(),
		)
		self.Add(self._quad_rate_text_box)
		self._freq_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.freq,
			callback=self.set_freq,
			label="Frequency",
			converter=forms.float_converter(),
		)
		self.Add(self._freq_text_box)
		self._cutoff_freq_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.cutoff_freq,
			callback=self.set_cutoff_freq,
			label="Cutoff Frequency",
			converter=forms.float_converter(),
		)
		self.Add(self._cutoff_freq_text_box)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot - Source",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0.win)
		self.rtlsdr_source_c_0 = osmosdr.source_c( args="nchan=" + str(1) + " " + "" )
		self.rtlsdr_source_c_0.set_sample_rate(samp_rate)
		self.rtlsdr_source_c_0.set_center_freq(freq, 0)
		self.rtlsdr_source_c_0.set_freq_corr(0, 0)
		self.rtlsdr_source_c_0.set_dc_offset_mode(0, 0)
		self.rtlsdr_source_c_0.set_iq_balance_mode(0, 0)
		self.rtlsdr_source_c_0.set_gain_mode(0, 0)
		self.rtlsdr_source_c_0.set_gain(10, 0)
		self.rtlsdr_source_c_0.set_if_gain(20, 0)
		self.rtlsdr_source_c_0.set_bb_gain(20, 0)
		self.rtlsdr_source_c_0.set_antenna("", 0)
		self.rtlsdr_source_c_0.set_bandwidth(0, 0)
		  
		self.low_pass_filter_0 = gr.fir_filter_ccf(6, firdes.low_pass(
			2, samp_rate, cutoff_freq, trans_width, firdes.WIN_HAMMING, 6.76))
		self.blks2_wfm_rcv_0 = blks2.wfm_rcv(
			quad_rate=quad_rate,
			audio_decimation=4,
		)
		self.audio_sink_0 = audio.sink(48000, "", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.low_pass_filter_0, 0), (self.blks2_wfm_rcv_0, 0))
		self.connect((self.blks2_wfm_rcv_0, 0), (self.audio_sink_0, 0))
		self.connect((self.rtlsdr_source_c_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.rtlsdr_source_c_0, 0), (self.low_pass_filter_0, 0))


	def get_trans_width(self):
		return self.trans_width

	def set_trans_width(self, trans_width):
		self.trans_width = trans_width
		self._trans_width_text_box.set_value(self.trans_width)
		self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.cutoff_freq, self.trans_width, firdes.WIN_HAMMING, 6.76))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
		self.rtlsdr_source_c_0.set_sample_rate(self.samp_rate)
		self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.cutoff_freq, self.trans_width, firdes.WIN_HAMMING, 6.76))

	def get_quad_rate(self):
		return self.quad_rate

	def set_quad_rate(self, quad_rate):
		self.quad_rate = quad_rate
		self._quad_rate_text_box.set_value(self.quad_rate)

	def get_freq(self):
		return self.freq

	def set_freq(self, freq):
		self.freq = freq
		self._freq_text_box.set_value(self.freq)
		self.rtlsdr_source_c_0.set_center_freq(self.freq, 0)

	def get_cutoff_freq(self):
		return self.cutoff_freq

	def set_cutoff_freq(self, cutoff_freq):
		self.cutoff_freq = cutoff_freq
		self._cutoff_freq_text_box.set_value(self.cutoff_freq)
		self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.cutoff_freq, self.trans_width, firdes.WIN_HAMMING, 6.76))

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

