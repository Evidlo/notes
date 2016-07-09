#!/usr/bin/env python
# Evan Widloski - 2016-03-06
# Custom Pandoc Filtering for Orgmode

from pandocfilters import toJSONFilter, Div, RawBlock, Link, Image

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
href_image = """
<a href="{0}"><img src="{0}"></a>
"""


def filter(key, value, format, meta):
    if key == 'Image':
        src = value[2][0]
        attr = ("",[],[])
        target = (src,"")
        return  Link(attr,[Image(("",[],[]),[],target)],target)

    # make derivation blocks collapsible
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
  toJSONFilter(filter)
