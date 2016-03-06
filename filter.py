#!/usr/bin/env python

from pandocfilters import toJSONFilter, Div, RawBlock

derivation_open = """
<div class="derivation" onclick="showHide(this);">
<div>
Derivation
</div>
<div class="derivation latex" style="display:none;">
"""
derivation_close = """
</div>
</div>
"""
proof_open = """
<div class="derivation" onclick="showHide(this);">
<div>
Proof
</div>
<div class="proof latex" style="display:none;">
"""
proof_close = """
</div>
</div>
"""

# make derivation blocks collapsible
def derivation(key, value, format, meta):
    if key == 'Div':
        [[ident, classes, kvs], contents] = value
        if 'derivation' in classes:
            return [RawBlock('html',derivation_open)] + \
                    contents + \
                    [RawBlock('html',derivation_close)]
        if 'proof' in classes:
            return [RawBlock('html',proof_open)] + \
                    contents + \
                    [RawBlock('html',proof_close)]

if __name__ == "__main__":
  toJSONFilter(derivation)
