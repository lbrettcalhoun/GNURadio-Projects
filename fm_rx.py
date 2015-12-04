#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Fm Rx
# Generated: Tue Aug  5 11:58:16 2014
##################################################

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.gr import firdes
from gnuradio.qtgui import qtgui
from optparse import OptionParser
import math
import osmosdr
import sip
import sys

class fm_rx(gr.top_block, Qt.QWidget):

	def __init__(self):
		gr.top_block.__init__(self, "Fm Rx")
		Qt.QWidget.__init__(self)
		self.setWindowTitle("Fm Rx")
		self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
		self.top_scroll_layout = Qt.QVBoxLayout()
		self.setLayout(self.top_scroll_layout)
		self.top_scroll = Qt.QScrollArea()
		self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
		self.top_scroll_layout.addWidget(self.top_scroll)
		self.top_scroll.setWidgetResizable(True)
		self.top_widget = Qt.QWidget()
		self.top_scroll.setWidget(self.top_widget)
		self.top_layout = Qt.QVBoxLayout(self.top_widget)
		self.top_grid_layout = Qt.QGridLayout()
		self.top_layout.addLayout(self.top_grid_layout)


		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 2e6
		self.in_rate = in_rate = samp_rate
		self.audio_rate = audio_rate = 44.1e3
		self.volume = volume = 0.2
		self.resamp_rate = resamp_rate = audio_rate/in_rate
		self.nfilts = nfilts = 32
		self.fm_deviation_hz = fm_deviation_hz = 75e3

		##################################################
		# Blocks
		##################################################
		self.rtlsdr_source_c_0 = osmosdr.source_c( args="nchan=" + str(1) + " " + "" )
		self.rtlsdr_source_c_0.set_sample_rate(samp_rate)
		self.rtlsdr_source_c_0.set_center_freq(91.9e6, 0)
		self.rtlsdr_source_c_0.set_freq_corr(0, 0)
		self.rtlsdr_source_c_0.set_dc_offset_mode(0, 0)
		self.rtlsdr_source_c_0.set_iq_balance_mode(0, 0)
		self.rtlsdr_source_c_0.set_gain_mode(0, 0)
		self.rtlsdr_source_c_0.set_gain(10, 0)
		self.rtlsdr_source_c_0.set_if_gain(20, 0)
		self.rtlsdr_source_c_0.set_bb_gain(20, 0)
		self.rtlsdr_source_c_0.set_antenna("", 0)
		self.rtlsdr_source_c_0.set_bandwidth(0, 0)
		  
		self.qtgui_sink_x_2 = qtgui.sink_f(
			1024, #fftsize
			firdes.WIN_BLACKMAN_hARRIS, #wintype
			0, #fc
			samp_rate, #bw
			"QT GUI Plot", #name
			True, #plotfreq
			True, #plotwaterfall
			True, #plottime
			True, #plotconst
		)
		self.qtgui_sink_x_2.set_update_time(1.0 / 10)
		self._qtgui_sink_x_2_win = sip.wrapinstance(self.qtgui_sink_x_2.pyqwidget(), Qt.QWidget)
		self.top_layout.addWidget(self._qtgui_sink_x_2_win)
		self.qtgui_sink_x_1 = qtgui.sink_f(
			1024, #fftsize
			firdes.WIN_BLACKMAN_hARRIS, #wintype
			0, #fc
			samp_rate, #bw
			"QT GUI Plot", #name
			True, #plotfreq
			True, #plotwaterfall
			True, #plottime
			True, #plotconst
		)
		self.qtgui_sink_x_1.set_update_time(1.0 / 10)
		self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.pyqwidget(), Qt.QWidget)
		self.top_layout.addWidget(self._qtgui_sink_x_1_win)
		self.qtgui_sink_x_0 = qtgui.sink_c(
			1024, #fftsize
			firdes.WIN_BLACKMAN_hARRIS, #wintype
			91.9e6, #fc
			samp_rate/2, #bw
			"QT GUI Plot", #name
			True, #plotfreq
			True, #plotwaterfall
			True, #plottime
			True, #plotconst
		)
		self.qtgui_sink_x_0.set_update_time(1.0 / 10)
		self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
		self.top_layout.addWidget(self._qtgui_sink_x_0_win)
		self.pfb_arb_resampler_xxx_0 = filter.pfb.arb_resampler_fff(
			  resamp_rate,
		          taps=(firdes.low_pass_2(volume*nfilts, nfilts*in_rate, 15e3, 1e3, 60, firdes.WIN_KAISER)),
			  flt_size=nfilts)
			
		self.audio_sink_0 = audio.sink(int(audio_rate), "pulse", True)
		self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(in_rate/(2*math.pi*fm_deviation_hz/8.0))

		##################################################
		# Connections
		##################################################
		self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.audio_sink_0, 0))
		self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.qtgui_sink_x_2, 0))
		self.connect((self.rtlsdr_source_c_0, 0), (self.qtgui_sink_x_0, 0))
		self.connect((self.rtlsdr_source_c_0, 0), (self.analog_quadrature_demod_cf_0, 0))
		self.connect((self.analog_quadrature_demod_cf_0, 0), (self.qtgui_sink_x_1, 0))
		self.connect((self.analog_quadrature_demod_cf_0, 0), (self.pfb_arb_resampler_xxx_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.set_in_rate(self.samp_rate)
		self.rtlsdr_source_c_0.set_sample_rate(self.samp_rate)
		self.qtgui_sink_x_0.set_frequency_range(91.9e6, self.samp_rate/2)
		self.qtgui_sink_x_2.set_frequency_range(0, self.samp_rate)
		self.qtgui_sink_x_1.set_frequency_range(0, self.samp_rate)

	def get_in_rate(self):
		return self.in_rate

	def set_in_rate(self, in_rate):
		self.in_rate = in_rate
		self.set_resamp_rate(self.audio_rate/self.in_rate)
		self.pfb_arb_resampler_xxx_0.set_taps((firdes.low_pass_2(self.volume*self.nfilts, self.nfilts*self.in_rate, 15e3, 1e3, 60, firdes.WIN_KAISER)))
		self.analog_quadrature_demod_cf_0.set_gain(self.in_rate/(2*math.pi*self.fm_deviation_hz/8.0))

	def get_audio_rate(self):
		return self.audio_rate

	def set_audio_rate(self, audio_rate):
		self.audio_rate = audio_rate
		self.set_resamp_rate(self.audio_rate/self.in_rate)

	def get_volume(self):
		return self.volume

	def set_volume(self, volume):
		self.volume = volume
		self.pfb_arb_resampler_xxx_0.set_taps((firdes.low_pass_2(self.volume*self.nfilts, self.nfilts*self.in_rate, 15e3, 1e3, 60, firdes.WIN_KAISER)))

	def get_resamp_rate(self):
		return self.resamp_rate

	def set_resamp_rate(self, resamp_rate):
		self.resamp_rate = resamp_rate
		self.pfb_arb_resampler_xxx_0.set_rate(self.resamp_rate)

	def get_nfilts(self):
		return self.nfilts

	def set_nfilts(self, nfilts):
		self.nfilts = nfilts
		self.pfb_arb_resampler_xxx_0.set_taps((firdes.low_pass_2(self.volume*self.nfilts, self.nfilts*self.in_rate, 15e3, 1e3, 60, firdes.WIN_KAISER)))

	def get_fm_deviation_hz(self):
		return self.fm_deviation_hz

	def set_fm_deviation_hz(self, fm_deviation_hz):
		self.fm_deviation_hz = fm_deviation_hz
		self.analog_quadrature_demod_cf_0.set_gain(self.in_rate/(2*math.pi*self.fm_deviation_hz/8.0))

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	qapp = Qt.QApplication(sys.argv)
	tb = fm_rx()
	tb.start()
	tb.show()
	qapp.exec_()
	tb.stop()

