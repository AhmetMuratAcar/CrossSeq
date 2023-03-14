from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QPalette, QColor, QBrush
from PyQt5.QtCore import Qt

class FastaSequences(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.setWindowTitle('FASTA Sequences')
        self.setFixedSize(500, 300)

        # Set the background color
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor('#ffffff'))
        self.setPalette(palette)

        # Create the font styles
        bold_font = QFont()
        bold_font.setPointSize(14)
        bold_font.setBold(True)

        regular_font = QFont()
        regular_font.setPointSize(12)

        # Create the labels
        header_label = QLabel('Enter FASTA Sequences', self)
        header_label.setGeometry(20, 20, 400, 30)
        header_label.setFont(bold_font)

        label1 = QLabel('Sequence 1:', self)
        label1.setGeometry(20, 80, 120, 30)
        label1.setFont(bold_font)

        label2 = QLabel('Sequence 2:', self)
        label2.setGeometry(20, 140, 120, 30)
        label2.setFont(bold_font)

        # Create the text input fields
        text_input_style = '''
            QLineEdit {{
                background-color: #f5f5f5;
                color: #333333;
                font-size: 12pt;
                border: 1px solid #d9d9d9;
                border-radius: 5px;
                padding: 5px;
            }}
        '''

        self.sequence1_input = QLineEdit(self)
        self.sequence1_input.setGeometry(150, 80, 300, 30)
        self.sequence1_input.setFont(regular_font)
        self.sequence1_input.setStyleSheet(text_input_style)

        self.sequence2_input = QLineEdit(self)
        self.sequence2_input.setGeometry(150, 140, 300, 30)
        self.sequence2_input.setFont(regular_font)
        self.sequence2_input.setStyleSheet(text_input_style)

        # Create the submit button
        button_style = '''
            QPushButton {{
                background-color: #007bff;
                color: #ffffff;
                font-size: 12pt;
                border-radius: 5px;
                padding: 10px 20px;
            }}
            QPushButton:hover {{
                background-color: #0056b3;
            }}
        '''

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setGeometry(190, 200, 120, 50)
        self.submit_button.setFont(bold_font)
        self.submit_button.setStyleSheet(button_style)
        self.submit_button.clicked.connect(self.submit_sequences)

    def submit_sequences(self):
        seq1 = self.sequence1_input.text()
        seq2 = self.sequence2_input.text()
        print("Sequence 1:", seq1)
        print("Sequence 2:", seq2)


if __name__ == '__main__':
    app = QApplication([])
    fasta_sequences = FastaSequences()
    fasta_sequences.show()
    app.exec_()
