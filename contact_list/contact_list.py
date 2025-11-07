"""The module defines the ContactList class."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Slot


class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts."""

    def __init__(self):
        """Initializes a new instance of the ContactList class."""

        super().__init__()
        self.__initialize_widgets()

        # Connect Buttons to Event Handlers
        self.add_button.clicked.connect(self.__on_add_contact)
        self.remove_button.clicked.connect(self.__on_remove_contact)

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.
        
        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot()
    def __on_add_contact(self) -> None:
        """Adds a new contact when the Add Contact button is clicked."""

        name = self.contact_name_input.text().strip()
        phone = self.phone_input.text().strip()

        if name and phone:
            row = self.contact_table.rowCount()
            self.contact_table.insertRow(row)

            self.contact_table.setItem(row, 0, QTableWidgetItem(name))
            self.contact_table.setItem(row, 1, QTableWidgetItem(phone))

            self.status_label.setText(f"Added contact: {name}")
        else:
            self.status_label.setText("Please enter a contact name and phone number.")

    @Slot()
    def __on_remove_contact(self) -> None:
        """Removes the selected contact when the Remove Contact button is clicked."""

        row = self.contact_table.currentRow()

        if row >= 0:
            reply = QMessageBox.question(
                self,
                "Remove Contact",
                "Are you sure you want to remove this contact?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )

            if reply == QMessageBox.Yes:
                self.contact_table.removeRow(row)
                self.status_label.setText("Contact removed.")
            else:
                self.status_label.setText("Removal canceled.")
        else:
            self.status_label.setText("Please select a row to remove.")




