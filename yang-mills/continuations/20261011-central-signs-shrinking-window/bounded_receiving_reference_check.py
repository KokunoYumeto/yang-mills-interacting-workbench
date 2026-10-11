import re

def rename_numbered_references(text):
    # Numbered references only; preserve the original operator product BM.
    return re.sub(r'\bBM(?=\d)', 'IB', text)
