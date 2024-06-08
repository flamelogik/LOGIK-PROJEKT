from PySide6.QtWidgets import QGridLayout

def add_widgets(gridbox):
    # Add labels
    from gridbox_labels import add_labels
    add_labels(gridbox)

    # Add line edits
    from gridbox_line_edits import add_line_edits
    add_line_edits(gridbox)

    # Add sliders
    from gridbox_sliders import add_sliders
    add_sliders(gridbox)
