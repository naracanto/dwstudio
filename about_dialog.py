# This Python file uses the following encoding: utf-8
#
# Copyright 2022 naracanto, <https://naracanto.github.io>.
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
from PySide6.QtWidgets import QApplication, QDialog, QDialogButtonBox, QVBoxLayout

from colophon_pages import ColophonPageAbout
from dialog_header_box import DialogHeaderBox


class AboutDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setMinimumSize(480, 320)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle(self.tr("About {0}").format(QApplication.applicationName()))

        # Header box
        headerBox = DialogHeaderBox()

        # Content
        pageAbout = ColophonPageAbout()
        pageAbout.layout().setContentsMargins(0, 0, 0, 0)

        # Button box
        buttonBox = QDialogButtonBox(QDialogButtonBox.Close)
        buttonBox.rejected.connect(self.close)

        # Main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(headerBox)
        mainLayout.addWidget(pageAbout)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
