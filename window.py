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

from PySide6.QtCore import QByteArray, QSettings, Qt
from PySide6.QtGui import QAction, QActionGroup, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu

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
            self._toolbarView.setVisible(False)

        # Application properties: Status Bar
        visible = settings.value("Application/StatusBar", True, type=bool)
        self._statusbar.setVisible(visible)
        self._actionStatusbar.setChecked(visible)


    def _saveSettings(self):

        settings = QSettings()

        # Application properties: Geometry
        geometry = self.saveGeometry()
        settings.setValue("Application/Geometry", geometry)

        # Application properties: State
        state = self.saveState()
        settings.setValue("Application/State", state)

        # Application properties: Status Bar
        visible = self._statusbar.isVisible()
        settings.setValue("Application/StatusBar", visible)


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

        #
        # Actions: View

        self._actionToolbarApplication = QAction(self.tr("Show Application Toolbar"), self)
        self._actionToolbarApplication.setObjectName("actionToolbarApplication")
        self._actionToolbarApplication.setCheckable(True)
        self._actionToolbarApplication.setToolTip(self.tr("Display the Application toolbar"))
        self._actionToolbarApplication.toggled.connect(lambda checked: self._toolbarApplication.setVisible(checked))

        self._actionToolbarView = QAction(self.tr("Show View Toolbar"), self)
        self._actionToolbarView.setObjectName("actionToolbarView")
        self._actionToolbarView.setCheckable(True)
        self._actionToolbarView.setToolTip(self.tr("Display the View toolbar"))
        self._actionToolbarView.toggled.connect(lambda checked: self._toolbarView.setVisible(checked))

        self._actionStatusbar = QAction(self.tr("Show Status Bar"), self)
        self._actionStatusbar.setObjectName("actionStatusbar")
        self._actionStatusbar.setCheckable(True)
        self._actionStatusbar.setToolTip(self.tr("Display the Status bar"))
        self._actionStatusbar.toggled.connect(lambda checked: self._statusbar.setVisible(checked))

        #
        # Action group: Tool Button Style

        actionToolButtonStyleIconOnly = QAction(self.tr("Icon Only"), self)
        actionToolButtonStyleIconOnly.setObjectName("actionToolButtonStyleIconOnly")
        actionToolButtonStyleIconOnly.setCheckable(True)
        actionToolButtonStyleIconOnly.setToolTip(self.tr("Only display the icon"))
        actionToolButtonStyleIconOnly.setData(Qt.ToolButtonIconOnly)

        actionToolButtonStyleTextOnly = QAction(self.tr("Text Only"), self)
        actionToolButtonStyleTextOnly.setObjectName("actionToolButtonStyleTextOnly")
        actionToolButtonStyleTextOnly.setCheckable(True)
        actionToolButtonStyleTextOnly.setToolTip(self.tr("Only display the text"))
        actionToolButtonStyleTextOnly.setData(Qt.ToolButtonTextOnly)

        actionToolButtonStyleTextBesideIcon = QAction(self.tr("Text Beside Icon"), self)
        actionToolButtonStyleTextBesideIcon.setObjectName("actionToolButtonStyleTextBesideIcon")
        actionToolButtonStyleTextBesideIcon.setCheckable(True)
        actionToolButtonStyleTextBesideIcon.setToolTip(self.tr("The text appears beside the icon"))
        actionToolButtonStyleTextBesideIcon.setData(Qt.ToolButtonTextBesideIcon)

        actionToolButtonStyleTextUnderIcon = QAction(self.tr("Text Under Icon"), self)
        actionToolButtonStyleTextUnderIcon.setObjectName("actionToolButtonStyleTextUnderIcon")
        actionToolButtonStyleTextUnderIcon.setCheckable(True)
        actionToolButtonStyleTextUnderIcon.setToolTip(self.tr("The text appears under the icon"))
        actionToolButtonStyleTextUnderIcon.setData(Qt.ToolButtonTextUnderIcon)

        self._actionsToolButtonStyle = QActionGroup(self)
        self._actionsToolButtonStyle.setObjectName("actionsToolButtonStyle")
        self._actionsToolButtonStyle.addAction(actionToolButtonStyleIconOnly)
        self._actionsToolButtonStyle.addAction(actionToolButtonStyleTextOnly)
        self._actionsToolButtonStyle.addAction(actionToolButtonStyleTextBesideIcon)
        self._actionsToolButtonStyle.addAction(actionToolButtonStyleTextUnderIcon)
        self._actionsToolButtonStyle.triggered.connect(self._onActionsToolButtonStyleTriggered)


    def _createMenuBar(self):

        # Menu: Application
        menuApplication = self.menuBar().addMenu(self.tr("Application"))
        menuApplication.setObjectName("menuApplication")
        menuApplication.addAction(self._actionAbout)
        menuApplication.addSeparator()
        menuApplication.addAction(self._actionQuit)

        #
        # Menu: View

        menuToolbars = QMenu(self.tr("Toolbars"), self)
        menuToolbars.setObjectName("menuToolbars")
        menuToolbars.addAction(self._actionToolbarApplication)
        menuToolbars.addAction(self._actionToolbarView)
        menuToolbars.addSection(self.tr("Tool Button Style"))
        menuToolbars.addActions(self._actionsToolButtonStyle.actions())

        menuView = self.menuBar().addMenu(self.tr("View"))
        menuView.setObjectName("menuView")
        menuView.addMenu(menuToolbars)
        menuView.addAction(self._actionStatusbar)


    def _createStatusBar(self):

        self._statusbar = self.statusBar()
        self._statusbar.showMessage(self.tr("Ready"), 3000)


    def _createToolBars(self):

        # Toolbar: Application
        self._toolbarApplication = self.addToolBar(self.tr("Application"))
        self._toolbarApplication.setObjectName("toolbarApplication")
        self._toolbarApplication.addAction(self._actionAbout)
        self._toolbarApplication.addSeparator()
        self._toolbarApplication.addAction(self._actionQuit)
        self._toolbarApplication.visibilityChanged.connect(lambda visible: self._actionToolbarApplication.setChecked(visible))

        # Toolbar: View
        self._toolbarView = self.addToolBar(self.tr("View"))
        self._toolbarView.setObjectName("toolbarView")
        self._toolbarView.visibilityChanged.connect(lambda visible: self._actionToolbarView.setChecked(visible))


    def _onActionAboutTriggered(self):

        dialog = AboutDialog(self)
        dialog.open()


    def _onActionsToolButtonStyleTriggered(self, actionToolButtonStyle):

        style = Qt.ToolButtonStyle(actionToolButtonStyle.data())

        self._toolbarApplication.setToolButtonStyle(style)
        self._toolbarView.setToolButtonStyle(style)
