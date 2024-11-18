import sys
import csv
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QStackedWidget, QFrame, QDateEdit, QScrollArea, QTabWidget, QCheckBox, QTabBar
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
        main_layout = QVBoxLayout()

        # Top panel for search filters
        filter_layout = QHBoxLayout()

        self.course_dropdown = QComboBox()
        self.course_dropdown.addItems(["", "CEN4721", "CEN4722", "CEN4777", "CEN2876"])
        self.course_dropdown.setStyleSheet("padding: 8px; font-size: 14px;")

        self.keyword_field = QLineEdit()
        self.keyword_field.setPlaceholderText("Search Keyword")
        self.keyword_field.setStyleSheet("padding: 8px; font-size: 14px;")

        self.content_type_dropdown = QComboBox()
        self.content_type_dropdown.addItems(["", "Assignments", "Announcements", "Exams", "Quizzes"])
        self.content_type_dropdown.setStyleSheet("padding: 8px; font-size: 14px;")

        self.module_dropdown = QComboBox()
        self.module_dropdown.addItems([""] + [str(i) for i in range(1, 13)])
        self.module_dropdown.setStyleSheet("padding: 8px; font-size: 14px;")

        self.start_date = QDateEdit()
        self.start_date.setCalendarPopup(True)
        self.start_date.setDate(QDate.currentDate())
        self.start_date.setStyleSheet("padding: 8px; font-size: 14px;")

        self.end_date = QDateEdit()
        self.end_date.setCalendarPopup(True)
        self.end_date.setDate(QDate.currentDate())
        self.end_date.setStyleSheet("padding: 8px; font-size: 14px;")

        search_button = QPushButton("Search")
        search_button.setFixedWidth(120)
        search_button.setStyleSheet("background-color: #2ECC71; color: white; font-size: 14px;")
        search_button.clicked.connect(self.handle_search)

        clear_button = QPushButton("Clear Filters")
        clear_button.setFixedWidth(120)
        clear_button.setStyleSheet("background-color: #E74C3C; color: white; font-size: 14px;")
        clear_button.clicked.connect(self.handle_clear)

        filter_layout.addWidget(search_button)
        filter_layout.addWidget(self.course_dropdown)
        filter_layout.addWidget(self.keyword_field)
        filter_layout.addWidget(self.content_type_dropdown)
        filter_layout.addWidget(self.module_dropdown)
        filter_layout.addWidget(self.start_date)
        filter_layout.addWidget(self.end_date)
        filter_layout.addWidget(clear_button)

        main_layout.addLayout(filter_layout)

        # Tabs for different searches
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.tab_widget.setStyleSheet("""
            QTabBar::tab {
                padding: 10px;
                background: #BDC3C7;
                border-radius: 5px;
            }
            QTabBar::tab:selected {
                background: #3498DB;
                color: white;
            }
        """)

        main_layout.addWidget(self.tab_widget)
        self.setLayout(main_layout)

    def handle_search(self):
        # Create a new tab for the search results
        course = self.course_dropdown.currentText()
        keyword = self.keyword_field.text()
        content_type = self.content_type_dropdown.currentText()
        module_tag = self.module_dropdown.currentText()

        new_tab = QWidget()
        tab_layout = QVBoxLayout()

        result_area = QScrollArea()
        result_area.setWidgetResizable(True)
        results_container = QWidget()

        # Set background for the results container to match the design
        results_container.setStyleSheet("background-color: #F0F8FF; padding: 10px;")
        results_layout = QVBoxLayout()
        results_container.setLayout(results_layout)
        result_area.setWidget(results_container)

        # Populate results based on the search filters (read from CSV)
        announcements = self.read_csv_data(course, content_type, module_tag, keyword)

        for announcement in announcements:
            results_layout.addWidget(self.create_announcement_card(
                announcement['Title'],
                announcement['Content Type'],
                announcement['Date'],
                announcement['Content']
            ))

        tab_layout.addWidget(result_area)
        new_tab.setLayout(tab_layout)

        # Add the new tab with search parameters
        self.tab_widget.addTab(new_tab, f"{course} ({keyword})")
        self.tab_widget.setCurrentWidget(new_tab)

    def read_csv_data(self, course, content_type, module_tag, keyword):
        # This function reads the CSV file and filters the data
        announcements = []
        with open('announcements.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (not course or row['Course'] == course) and \
                   (not content_type or content_type == "Any" or row['Content Type'] == content_type) and \
                   (not module_tag or row['Module Tag'] == module_tag) and \
                   (not keyword or keyword.lower() in row['Content'].lower()):
                    announcements.append(row)
        return announcements

    def handle_clear(self):
        self.course_dropdown.setCurrentIndex(0)
        self.keyword_field.clear()
        self.content_type_dropdown.setCurrentIndex(0)
        self.module_dropdown.setCurrentIndex(0)
        self.start_date.setDate(QDate.currentDate())
        self.end_date.setDate(QDate.currentDate())

    def create_announcement_card(self, title, content_type, due_date, description):
        announcement_widget = QFrame()
        announcement_widget.setStyleSheet("""
            background-color: white;
            border: 1px solid #BDC3C7;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        """)
        announcement_layout = QVBoxLayout()

        title_label = QLabel(title)
        title_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #2C3E50;")
        announcement_layout.addWidget(title_label)

        content_type_label = QLabel(f"Content Type: {content_type}")
        announcement_layout.addWidget(content_type_label)

        due_date_label = QLabel(f"Due: {due_date}")
        announcement_layout.addWidget(due_date_label)

        description_label = QLabel(description)
        description_label.setWordWrap(True)
        announcement_layout.addWidget(description_label)

        announcement_widget.setLayout(announcement_layout)
        return announcement_widget

    def close_tab(self, index):
        self.tab_widget.removeTab(index)


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
        self.setCurrentWidget(self.filter_screen)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Course Navigator')
    window.resize(1200, 800)
    window.show()
    sys.exit(app.exec_())
