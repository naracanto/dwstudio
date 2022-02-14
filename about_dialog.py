# This Python file uses the following encoding: utf-8
#
# Copyright 2022 naracanto, <https://naracanto.com>.
#
# This file is part of dwStudio, <https://github.com/naracanto/dwstudio>.
#
# dwStudio is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dwStudio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dwStudio.  If not, see <https://www.gnu.org/licenses/>.
#

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDialog, QDialogButtonBox, QFrame, QTextBrowser, QVBoxLayout


class AboutDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(480, 320)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle(self.tr("About {0}").format(QApplication.applicationName()))


        #
        # Content

        text = "<html><body>"
        text += self.tr("<p>{0} is an open source front-end tool for the Datawrapper API written in Python using the Python bindings for the Qt framework.</p>").format(QApplication.applicationName())
        text += self.tr("<p>Copyright &copy; 2022 <a href=\"{0}\" title=\"Visit organization's homepage\">{1}</a>.</p>").format(QApplication.organizationDomain(), QApplication.organizationName())
        text += self.tr("<p>This application is licensed under the terms of the <a href=\"https://www.gnu.org/licenses/gpl-3.0.en.html\" title=\"Visit license's homepage\">GNU General Public License, version 3</a>.</p>")
        text += "</body></html>"

        textBox = QTextBrowser()
        textBox.setFrameStyle(QFrame.NoFrame)
        textBox.setStyleSheet("background-color:transparent;")
        textBox.setOpenExternalLinks(True)
        textBox.setHtml(text)


        # Button box
        buttonBox = QDialogButtonBox(QDialogButtonBox.Close)
        buttonBox.rejected.connect(self.close)

        # Main layout
        layout = QVBoxLayout(self)
        layout.addWidget(textBox)
        layout.addWidget(buttonBox)
