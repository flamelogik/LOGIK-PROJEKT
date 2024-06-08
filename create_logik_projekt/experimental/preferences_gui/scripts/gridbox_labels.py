from PySide6.QtWidgets import QLabel, QGridLayout

def add_labels(gridbox):
    labels = [
        'Render Node Type', 'Write File Node Setup', 'Media Path', 'Pattern',
        'File Type', 'Frame Index', 'Padding', 'Compression', 'Settings', 'Version Name'
    ]

    for i, label_text in enumerate(labels):
        label = QLabel(label_text)
        gridbox.addWidget(label, i // 2, i % 2)
