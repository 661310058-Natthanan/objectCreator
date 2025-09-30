try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui
import os
import importlib
from . import objectCreatorUtil as obutil
importlib.reload(obutil)

ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'icons'))

class ObjectcreatorDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.resize(300,300)
		self.setWindowTitle('☀︎Object Creator')

		self.main_layout = QtWidgets.QVBoxLayout()
		self.setLayout(self.main_layout)

		self.object_listWidget = QtWidgets.QListWidget()
		self.object_listWidget.setIconSize(QtCore.QSize(60,60))
		self.object_listWidget.setSpacing(5)
		self.object_listWidget.setViewMode(QtWidgets.QListView.IconMode)
		self.object_listWidget.setMovement(QtWidgets.QListView.Static)
		self.object_listWidget.setResizeMode(QtWidgets.QListView.Adjust)

		self.main_layout.addWidget(self.object_listWidget)

		self.name_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.name_layout)
		self.name_label = QtWidgets.QLabel('Name:')
		self.name_lineEdit = QtWidgets.QLineEdit()
		self.name_lineEdit.setStyleSheet(
			'''
				QLineEdit {
					border-radius: 5px;
					background-color: white;
					color: navy;
					font-size: 24px;
					font-family: Oswald;
				}
			'''
		)

		self.name_layout.addWidget(self.name_label)
		self.name_layout.addWidget(self.name_lineEdit)

		self.button_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.button_layout)
		self.create_button = QtWidgets.QPushButton('☂︎Create')
		self.create_button.setStyleSheet(
			'''
				QPushButton{
					background-color: #669933
				}
			'''
		)

		self.cancel_button = QtWidgets.QPushButton('☔︎Cancel')
		self.cancel_button.setStyleSheet(
			'''
				QPushButton{
					background-color: #993300
				}
			'''
		)

		self.button_layout.addStretch()
		self.button_layout.addWidget(self.create_button)
		self.button_layout.addWidget(self.cancel_button)
		self.create_button.clicked.connect(self.onClickCreateObject)
		self.cancel_button.clicked.connect(self.close)

		self.initIconWidget()

	def initIconWidget(self):
		objs = ['cube', 'cone', 'sphere', 'torus']
		for obj in objs:
			item = QtWidgets.QListWidgetItem(obj)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH, f'{obj}.png')))
			self.object_listWidget.addItem(item)

	def onClickCreateObject(self):
		item = self.object_listWidget.currentItem()
		if not item:
			QtWidgets.QMessageBox.warning(self,'No Selection', 'Please select a object type.')
			return

		obj_type = item.text()
		objName = self.name_lineEdit.text() or obj_type
		obutil.createObject(obj_type, objName)

def run():
	global ui
	try:
		ui.close()

	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = ObjectcreatorDialog(parent=ptr)
	ui.show()