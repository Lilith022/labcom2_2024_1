#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
import numpy
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import Practica_1_epy_block_0 as epy_block_0  # embedded python block
import sip



class Practica_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
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

        self.settings = Qt.QSettings("GNU Radio", "Practica_1")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################

        self.epy_block_0 = epy_block_0.blk(example_param=1.0)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.analog_random_source_x_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 100, 1000))), True)
        self.Var = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.Var.set_update_time(0.10)
        self.Var.set_title('VAR')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.Var.set_min(i, -1)
            self.Var.set_max(i, 1)
            self.Var.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.Var.set_label(i, "Data {0}".format(i))
            else:
                self.Var.set_label(i, labels[i])
            self.Var.set_unit(i, units[i])
            self.Var.set_factor(i, factor[i])

        self.Var.enable_autoscale(False)
        self._Var_win = sip.wrapinstance(self.Var.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._Var_win)
        self.STD = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.STD.set_update_time(0.10)
        self.STD.set_title('STD')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.STD.set_min(i, -1)
            self.STD.set_max(i, 1)
            self.STD.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.STD.set_label(i, "Data {0}".format(i))
            else:
                self.STD.set_label(i, labels[i])
            self.STD.set_unit(i, units[i])
            self.STD.set_factor(i, factor[i])

        self.STD.enable_autoscale(False)
        self._STD_win = sip.wrapinstance(self.STD.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._STD_win)
        self.Promedio = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.Promedio.set_update_time(0.10)
        self.Promedio.set_title('Promedio')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.Promedio.set_min(i, -1)
            self.Promedio.set_max(i, 1)
            self.Promedio.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.Promedio.set_label(i, "Data {0}".format(i))
            else:
                self.Promedio.set_label(i, labels[i])
            self.Promedio.set_unit(i, units[i])
            self.Promedio.set_factor(i, factor[i])

        self.Promedio.enable_autoscale(False)
        self._Promedio_win = sip.wrapinstance(self.Promedio.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._Promedio_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.epy_block_0, 0))
        self.connect((self.epy_block_0, 0), (self.Promedio, 0))
        self.connect((self.epy_block_0, 1), (self.STD, 0))
        self.connect((self.epy_block_0, 2), (self.Var, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Practica_1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate




def main(top_block_cls=Practica_1, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
