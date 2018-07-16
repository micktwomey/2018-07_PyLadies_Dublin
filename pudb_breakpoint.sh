#!/bin/bash

export PYTHONBREAKPOINT=pudb.set_trace
exec python example_breakpoint.py
