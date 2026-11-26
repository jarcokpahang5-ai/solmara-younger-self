#!/usr/bin/env python3
"""Print the one line to my younger self.

The text is kept in the sibling module entry_text; here it is
loaded dynamically and written out exactly as stored.
"""

import importlib

_text_module = importlib.import_module("entry_text")

print(_text_module.LINE)
