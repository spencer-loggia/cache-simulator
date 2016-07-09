#!/usr/bin/env python3

import contextlib
import io
import nose.tools as nose
import cachesimulator.simulator as sim
from unittest.mock import patch


@patch('sys.argv', [
    sim.__file__, '--cache-size', '4', '--num-blocks-per-set', '1',
    '--num-words-per-block', '1', '--word-addrs', '0', '8', '0', '6', '8'])
def test_main():
    """main function should produce some output"""
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        sim.main()
    main_output = out.getvalue()
    nose.assert_regexp_matches(main_output, r'\bWordAddr\b')
    nose.assert_regexp_matches(main_output, r'\b0110\b')
    nose.assert_regexp_matches(main_output, r'\bCache')
    nose.assert_regexp_matches(main_output, r'\b01\b')
    nose.assert_regexp_matches(main_output, r'\b8\s*6\b')
