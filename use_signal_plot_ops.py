import signal_plot_ops as ops

signal = ops.load_signal_from_txt("ekg_signal.txt")
print(ops.signal_avg(signal))
ops.plot_signal(signal)
