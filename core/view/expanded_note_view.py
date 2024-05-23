from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame, QCheckBox, QRadioButton
from PySide6.QtCore import Qt

class ExpandedNoteView(QWidget):
    def __init__(self, note, main_controller):
        super().__init__()
        self.note = note
        self.main_controller = main_controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Заголовок заметки
        title = QLabel(self.note['title'])
        layout.addWidget(title)

        # Визуальная разделительная линия
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("background-color: black; min-height: 2px; max-height: 2px;")
        layout.addWidget(line)

        # Тело заметки
        body = QLabel(self.note['body'])
        body.setWordWrap(True)
        layout.addWidget(body)

        # Добавляем чекбоксы для списка задач
        if self.note['type'] == 'task':
            for item in self.note['items']:
                checkbox = QCheckBox(item)
                layout.addWidget(checkbox)
        elif self.note['type'] == 'list':
            for item in self.note['items']:
                radiobutton = QRadioButton(item)
                layout.addWidget(radiobutton)

        # Кнопки "Изменить" и "Удалить"
        buttons_layout = QHBoxLayout()
        edit_button = QPushButton("Изменить")
        edit_button.clicked.connect(self.edit_note)
        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(self.delete_note)
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def edit_note(self):
        self.main_controller.edit_note_editor(self.note)

    def delete_note(self):
        self.main_controller.delete_note_editor(self.note)