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

from PySide6.QtCore import QByteArray, QSettings
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow

from about_dialog import AboutDialog

import icons_rc


class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowIcon(QIcon(":/icons/apps/16/dwstudio.svg"))

        self._createActions()
        self._createMenuBar()
        self._createStatusBar()
        self._createToolBars()

        self._loadSettings()


    def closeEvent(self, event):

        if True:
            # Store application properties
            self._saveSettings()

            event.accept()
        else:
            event.ignore()


    def _loadSettings(self):

        settings = QSettings()

        # Application properties: Geometry
        geometry = settings.value("Application/Geometry", QByteArray())
        if not geometry.isEmpty():
            self.restoreGeometry(geometry)
        else:
            # Center window
            availableGeometry = self.screen().availableGeometry()
            self.resize(availableGeometry.width() * 2/3, availableGeometry.height() * 2/3)
            self.move((availableGeometry.width() - self.width()) / 2, (availableGeometry.height() - self.height()) / 2)

        # Application properties: State
        state = settings.value("Application/State", QByteArray())
        if not state.isEmpty():
            self.restoreState(state)
        else:
            # Show toolbars
            self._toolbarApplication.setVisible(True)


    def _saveSettings(self):

        settings = QSettings()

        # Application properties: Geometry
        geometry = self.saveGeometry()
        settings.setValue("Application/Geometry", geometry)

        # Application properties: State
        state = self.saveState()
        settings.setValue("Application/State", state)


    def _createActions(self):

        #
        # Actions: Application

        self._actionAbout = QAction(self.tr("About {0}").format(QApplication.applicationName()), self)
        self._actionAbout.setObjectName("actionAbout")
        self._actionAbout.setIcon(QIcon(":/icons/apps/16/dwstudio.svg"))
        self._actionAbout.setIconText(self.tr("About"))
        self._actionAbout.setToolTip(self.tr("Brief description of the application"))
        self._actionAbout.triggered.connect(self._onActionAboutTriggered)

        self._actionQuit = QAction(self.tr("Quit"), self)
        self._actionQuit.setObjectName("actionQuit")
        self._actionQuit.setIcon(QIcon.fromTheme("application-exit", QIcon(":/icons/actions/16/application-exit.svg")))
        self._actionQuit.setShortcut(QKeySequence.Quit)
        self._actionQuit.setToolTip(self.tr("Quit the application"))
        self._actionQuit.triggered.connect(self.close)


    def _createMenuBar(self):

        # Menu: Application
        menuApplication = self.menuBar().addMenu(self.tr("Application"))
        menuApplication.setObjectName("menuApplication")
        menuApplication.addAction(self._actionAbout)
        menuApplication.addSeparator()
        menuApplication.addAction(self._actionQuit)

        # Menu: View
        menuView = self.menuBar().addMenu(self.tr("View"))
        menuView.setObjectName("menuView")


    def _createStatusBar(self):

        statusbar = self.statusBar()
        statusbar.showMessage(self.tr("Ready"), 3000)


    def _createToolBars(self):

        # Toolbar: Application
        self._toolbarApplication = self.addToolBar(self.tr("Application"))
        self._toolbarApplication.setObjectName("toolbarApplication")
        self._toolbarApplication.addAction(self._actionAbout)
        self._toolbarApplication.addSeparator()
        self._toolbarApplication.addAction(self._actionQuit)


    def _onActionAboutTriggered(self):

        dialog = AboutDialog(self)
        dialog.open()
