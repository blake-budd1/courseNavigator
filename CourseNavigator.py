import sys
import csv
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QStackedWidget, QFrame, QDateEdit, QScrollArea
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPalette, QColor, QPixmap


class LoginScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Title
        title = QLabel("Course Navigator")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #34495E;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Create a frame to serve as the background box for the login form
        login_frame = QFrame()
        login_frame.setStyleSheet("""
            QFrame {
                background-color: #F0F0F0;
                border: 2px solid #D0D0D0;
                border-radius: 20px;
                padding: 30px;
            }
        """)
        login_layout = QVBoxLayout()

        # Username Field
        self.username_field = QLineEdit()
        self.username_field.setPlaceholderText("User Name")
        self.username_field.setFixedWidth(260)
        self.username_field.setStyleSheet("padding: 10px; font-size: 14px; border-radius: 10px; border: 1px solid #CCC;")
        login_layout.addWidget(self.username_field, alignment=Qt.AlignCenter)

        # Password Field
        self.password_field = QLineEdit()
        self.password_field.setPlaceholderText("Password")
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.setFixedWidth(260)
        self.password_field.setStyleSheet("padding: 10px; font-size: 14px; border-radius: 10px; border: 1px solid #CCC;")
        login_layout.addWidget(self.password_field, alignment=Qt.AlignCenter)

        # Login Button
        login_button = QPushButton("Login")
        login_button.setFixedWidth(150)
        login_button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                border-radius: 15px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)
        login_button.clicked.connect(self.handle_login)
        login_layout.addWidget(login_button, alignment=Qt.AlignCenter)

        login_frame.setLayout(login_layout)
        layout.addWidget(login_frame, alignment=Qt.AlignCenter)
        layout.setAlignment(Qt.AlignCenter)

        # Set background to soft light blue
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(240, 248, 255))  # light pastel blue
        self.setPalette(palette)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_field.text()
        password = self.password_field.text()

        if username and password:
            self.parent.username = username
            self.parent.switch_to_filter_screen()
        else:
            self.warning = QLabel("Please enter both username and password.")
            self.warning.setStyleSheet("color: red;")
            self.layout().addWidget(self.warning, alignment=Qt.AlignCenter)


class FilterScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()

        # Left side filter panel
        filter_panel = QVBoxLayout()

        # Profile Image and Username in a horizontal layout
        profile_layout = QHBoxLayout()

        # Profile Image (Placeholder)
        profile_image = QLabel()
        pixmap = QPixmap(100, 100)  # Placeholder size 100x100
        pixmap.fill(QColor("#6290C3"))  # Grey placeholder
        profile_image.setPixmap(pixmap)
        
        profile_image.setStyleSheet("""
            QLabel {
                border-radius: 50px;  # Circular image
                border: 2px solid #2C3E50;
            }
        """)
        profile_image.setFixedSize(75, 75)
        profile_layout.addWidget(profile_image)

        # Username (Placed to the right of the profile image)
        self.username_label = QLabel(self.parent.username)
        self.username_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #2C3E50;")
        profile_layout.addWidget(self.username_label, alignment=Qt.AlignVCenter)

        filter_panel.addLayout(profile_layout)

        combo_box_style = """
            QComboBox {
                background-color: #ECF0F1;
                border: 1px solid #BDC3C7;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
                min-height: 30px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: #BDC3C7;
                border-left-style: solid;
            }
            QComboBox QAbstractItemView {
                background-color: white;
                border: 1px solid #BDC3C7;
                selection-background-color: #3498DB;
            }
        """

        # Filters
        self.course_dropdown = QComboBox()
        self.course_dropdown.addItems(["", "CEN4777", "CEN4721", "CEN4722", "CEN2876"])
        self.course_dropdown.setStyleSheet(combo_box_style)
        filter_panel.addWidget(QLabel("Select Course"), alignment=Qt.AlignLeft)
        filter_panel.addWidget(self.course_dropdown)

        self.content_type_dropdown = QComboBox()
        self.content_type_dropdown.addItems(["", "Assignment", "Announcements", "Quiz", "Exams", "File"])
        self.content_type_dropdown.setStyleSheet(combo_box_style)
        filter_panel.addWidget(QLabel("Content Type"), alignment=Qt.AlignLeft)
        filter_panel.addWidget(self.content_type_dropdown)

        self.module_dropdown = QComboBox()
        self.module_dropdown.addItems([""] + [str(i) for i in range(1, 13)])
        self.module_dropdown.setStyleSheet(combo_box_style)
        filter_panel.addWidget(QLabel("Module Tag"), alignment=Qt.AlignLeft)
        filter_panel.addWidget(self.module_dropdown)

        self.keyword_field = QLineEdit()
        self.keyword_field.setPlaceholderText("Enter Keyword")
        self.keyword_field.setStyleSheet("""
            QLineEdit {
                background-color: #ECF0F1;
                border: 1px solid #BDC3C7;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
            }
        """)
        filter_panel.addWidget(QLabel("Search Keyword"), alignment=Qt.AlignLeft)
        filter_panel.addWidget(self.keyword_field)

        # Start Date and End Date fields with no default value
        self.start_date = QDateEdit()
        self.start_date.setCalendarPopup(True)
        self.start_date.setSpecialValueText("Select Start Date")  # No date selected initially
        self.start_date.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))
        self.start_date.setDate(QDate(2020, 8, 1)) # Set the date to 8/1/2020 -> instead of 1/1/2000
        self.start_date.setStyleSheet(combo_box_style)
        filter_panel.addWidget(QLabel("Start Date"), alignment=Qt.AlignLeft)
        filter_panel.addWidget(self.start_date)

        self.end_date = QDateEdit()
        self.end_date.setCalendarPopup(True)
        self.end_date.setDate(QDate.currentDate())  # Set default end date to today
        self.end_date.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))
        self.end_date.setStyleSheet(combo_box_style)
        filter_panel.addWidget(QLabel("End Date"), alignment=Qt.AlignLeft)
        filter_panel.addWidget(self.end_date)

        search_button = QPushButton("                  Search                  ")
        search_button.setStyleSheet("""
            QPushButton {
                background-color: #2ECC71;
                color: white;
                border-radius: 15px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #27AE60;
            }
        """)
        search_button.clicked.connect(self.handle_search)  # Connect search button to handle_search

        clear_button = QPushButton("Clear Filters")
        clear_button.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C;
                color: white;
                border-radius: 15px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
        """)
        clear_button.clicked.connect(self.handle_clear)  # Connect clear button to handle_clear
        
        filter_panel.addWidget(clear_button, alignment=Qt.AlignCenter)
        
        # Add the search button after the clear filters button
        filter_panel.addWidget(search_button, alignment=Qt.AlignCenter)

        filter_panel_container = QFrame()
        filter_panel_container.setStyleSheet("background-color: white; padding: 10px;")
        filter_panel_container.setLayout(filter_panel)
        filter_panel_container.setFixedWidth(360)
        main_layout.addWidget(filter_panel_container)

        # Right side: Display announcements
        self.result_area = QScrollArea()
        self.result_area.setWidgetResizable(True)
        self.results_container = QWidget()

        # Set background to light blue for the results area
        self.results_container.setStyleSheet("background-color: #6290C3;")  # Light pastel blue background
        self.results_layout = QVBoxLayout()
        self.results_container.setLayout(self.results_layout)
        self.result_area.setWidget(self.results_container)

        main_layout.addWidget(self.result_area)

        self.setLayout(main_layout)

    def handle_search(self):
        selected_course = self.course_dropdown.currentText()
        selected_content_type = self.content_type_dropdown.currentText()
        selected_module_tag = self.module_dropdown.currentText()
        entered_keyword = self.keyword_field.text()

        selected_start_date = (
            self.start_date.date().toString("yyyy-MM-dd") if self.start_date.date().isValid() else None
        )
        selected_end_date = (
            self.end_date.date().toString("yyyy-MM-dd") if self.end_date.date().isValid() else None
        )

        # Clear previous results
        for i in reversed(range(self.results_layout.count())):
            widget = self.results_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Filter announcements from CSV
        with open('announcements.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (
                    (not selected_course or row['Course'] == selected_course) and
                    (not selected_content_type or row['Content Type'] == selected_content_type) and
                    (not selected_module_tag or row['Module Tag'] == selected_module_tag) and
                    (not entered_keyword or entered_keyword.lower() in row['Content'].lower()) and
                    (not selected_start_date or selected_start_date <= row['Date']) and
                    (not selected_end_date or row['Date'] <= selected_end_date)
                ):
                    # Display the filtered result
                    announcement_widget = QFrame()
                    announcement_widget.setStyleSheet("""
                        background-color: rgba(255,255,255,180);
                        border: 1px solid #BDC3C7;
                        border-radius: 10px;
                        padding: 10px;
                        margin-bottom: 10px;
                    """)

                    announcement_layout = QVBoxLayout()

                    # Add course to results
                    title = QLabel(f"{row['Title']}")
                    title.setStyleSheet("font-weight: bold; font-size: 16px; color: #2C3E50;")
                    course = QLabel(f"Course: {row['Course']}")
                    content_type = QLabel(f"Content Type: {row['Content Type']}")
                    date = QLabel(f"Date: {row['Date']}")
                    module_tag = QLabel(f"Module Tag: {row['Module Tag']}")
                    content = QLabel(f"Content: {row['Content']}")
                    content.setWordWrap(True)

                    announcement_layout.addWidget(title)
                    announcement_layout.addWidget(course)
                    announcement_layout.addWidget(content_type)
                    announcement_layout.addWidget(date)
                    announcement_layout.addWidget(module_tag)
                    announcement_layout.addWidget(content)

                    announcement_widget.setLayout(announcement_layout)
                    self.results_layout.addWidget(announcement_widget)

    def handle_clear(self):
        self.course_dropdown.setCurrentIndex(0)
        self.content_type_dropdown.setCurrentIndex(0)
        self.module_dropdown.setCurrentIndex(0)
        self.keyword_field.clear()
        self.start_date.setDate(QDate(2020, 8, 1)) # Set the date to 8/1/2020 -> instead of 1/1/2000
        self.end_date.setDate(QDate.currentDate())

        # Clear the results area
        for i in reversed(range(self.results_layout.count())):
            widget = self.results_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()


class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.username = None
        self.login_screen = LoginScreen(self)
        self.filter_screen = FilterScreen(self)
        self.addWidget(self.login_screen)
        self.addWidget(self.filter_screen)
        self.setCurrentWidget(self.login_screen)

    def switch_to_filter_screen(self):
        self.filter_screen.username_label.setText(self.username)  # Set username next to the profile picture
        self.setCurrentWidget(self.filter_screen)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Course Navigator')
    window.resize(1200, 800)
    window.show()
    sys.exit(app.exec_())
