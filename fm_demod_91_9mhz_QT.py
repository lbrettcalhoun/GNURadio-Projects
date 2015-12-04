#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: FM Demodulation - 91.9 MHz
# Generated: Tue Aug  5 11:43:17 2014
##################################################

from PyQt4 import Qt
from gnuradio import audio
from gnuradio import blks2
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.qtgui import qtgui
from optparse import OptionParser
import osmosdr
import sip
import sys

class fm_demod_91_9mhz_QT(gr.top_block, Qt.QWidget):

	def __init__(self):
		gr.top_block.__init__(self, "FM Demodulation - 91.9 MHz")
		Qt.QWidget.__init__(self)
		self.setWindowTitle("FM Demodulation - 91.9 MHz")
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
		self.samp_rate = samp_rate = 1152e3

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
		  
		self.qtgui_sink_x_1 = qtgui.sink_f(
			1024, #fftsize
			firdes.WIN_BLACKMAN_hARRIS, #wintype
			0, #fc
			samp_rate/24, #bw
			"QT GUI Plot - Demodulated Signal", #name
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
			samp_rate, #bw
			"QT GUI Plot - Source", #name
			True, #plotfreq
			True, #plotwaterfall
			True, #plottime
			True, #plotconst
		)
		self.qtgui_sink_x_0.set_update_time(1.0 / 10)
		self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
		self.top_layout.addWidget(self._qtgui_sink_x_0_win)
		self.blks2_wfm_rcv_0 = blks2.wfm_rcv(
			quad_rate=samp_rate,
			audio_decimation=24,
		)
		self.audio_sink_0 = audio.sink(48000, "", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.rtlsdr_source_c_0, 0), (self.blks2_wfm_rcv_0, 0))
		self.connect((self.blks2_wfm_rcv_0, 0), (self.audio_sink_0, 0))
		self.connect((self.rtlsdr_source_c_0, 0), (self.qtgui_sink_x_0, 0))
		self.connect((self.blks2_wfm_rcv_0, 0), (self.qtgui_sink_x_1, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.rtlsdr_source_c_0.set_sample_rate(self.samp_rate)
		self.qtgui_sink_x_0.set_frequency_range(91.9e6, self.samp_rate)
		self.qtgui_sink_x_1.set_frequency_range(0, self.samp_rate/24)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	qapp = Qt.QApplication(sys.argv)
	tb = fm_demod_91_9mhz_QT()
	tb.start()
	tb.show()
	qapp.exec_()
	tb.stop()

