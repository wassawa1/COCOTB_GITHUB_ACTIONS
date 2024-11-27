# Makefile
TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(PWD)/dff.v
MODULE = tests.test_dff

include $(shell cocotb-config --makefiles)/Makefile.sim