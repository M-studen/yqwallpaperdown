import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,QComboBox, QHBoxLayout, \
    QFileDialog, QSpinBox
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from spider import Spider
# spider = spider()

class MyCustomWidget1(QWidget):
    def __init__(self, widget):
        self.widget = widget
        super().__init__()
        # 创建标签和输入框
        self.label1 = QLabel('链接：')
        self.lineEdit1 = QLineEdit()

        self.label2 = QLabel('保存位置')
        self.lineEdit2 = QLineEdit()

        # 创建文件夹浏览按钮
        self.folderButton = QPushButton('浏览')
        self.pushButton = QPushButton("开始下载")
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.folderButton.clicked.connect(lambda: self.openFolderDialog(self.lineEdit2))

        # 创建第一个水平布局并添加组件
        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.label1)
        self.layout1.addWidget(self.lineEdit1)

        # 创建第二个水平布局并添加组件
        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(self.label2)
        self.layout2.addWidget(self.lineEdit2)
        self.layout2.addWidget(self.folderButton)
        self.layout3 = QHBoxLayout()
        self.layout3.addWidget(self.pushButton)
        # 创建垂直布局并添加两个水平布局
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.layout1)
        self.mainLayout.addLayout(self.layout2)
        self.mainLayout.addLayout(self.layout3)

        # 将主布局设置为窗口的布局
        self.setLayout(self.mainLayout)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.s=Spider.spider(url=self.lineEdit1.text(),path=self.lineEdit2.text() + '/',func=0)
        self.s.start()
        self.s.finished.connect(self.updateText)
        self.pushButton.setEnabled(False)
        self.lineEdit1.setText('')
        self.lineEdit2.setText('')

    def openFolderDialog(self, lineEdit):
        # 打开文件夹对话框
        self.folderDialog = QFileDialog()
        self.folderPath = self.folderDialog.getExistingDirectory(self, '选择文件夹')
        # 更新第二个输入框的文本
        lineEdit.setText(self.folderPath)
    def updateText(self,result):
        self.widget.textBrowser.setText(result)
        self.pushButton.setEnabled(True)

class MyCustomWidget2(QWidget):
    def __init__(self, widget):
        self.num = 0
        super().__init__()
        # 创建标签和输入框
        self.widget = widget
        self.label1 = QLabel('关键词')
        self.lineEdit1 = QLineEdit()

        self.label2 = QLabel('页数')
        self.spinBox = QSpinBox()
        self.spinBox.setValue(1)

        self.label3 = QLabel('保存位置')
        self.lineEdit2 = QLineEdit()
        self.folderButton = QPushButton('浏览')
        self.folderButton.clicked.connect(lambda: self.openFolderDialog(self.lineEdit2))
        self.pushButton1 = QPushButton("开始下载")
        self.pushButton1.clicked.connect(self.on_pushButton1_clicked)
        # 创建第一个水平布局并添加组件
        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.label1)
        self.layout1.addWidget(self.lineEdit1)

        # 创建第二个水平布局并添加组件
        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(self.label2)
        self.layout2.addWidget(self.spinBox)

        # 创建第三个水平布局并添加组件
        self.layout3 = QHBoxLayout()
        self.layout3.addWidget(self.label3)
        self.layout3.addWidget(self.lineEdit2)
        self.layout3.addWidget(self.folderButton)
        self.layout4 = QHBoxLayout()
        self.layout4.addWidget(self.pushButton1)
        # 创建垂直布局并添加三个水平布局
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.layout1)
        self.mainLayout.addLayout(self.layout2)
        self.mainLayout.addLayout(self.layout3)
        self.mainLayout.addLayout(self.layout4)
        # 将主布局设置为窗口的布局
        self.setLayout(self.mainLayout)

    @pyqtSlot()
    def on_pushButton1_clicked(self):
        self.s=Spider.spider(keyword=str(self.lineEdit1.text()),path=self.lineEdit2.text() + '/',page=self.spinBox.value(),func=1,callback=self.update_textBrowser,widget=MyCustomWidget2(MyWidget))
        # self.widget.textBrowser.setText('开始下载......\n'
        #                                 '下载内容过多时可能会造成未响应，请等待即可')
        # text=spider.DownloadSearchVideo(keyword=str(self.lineEdit1.text()), path=self.lineEdit2.text() + '/',page=self.spinBox.value())
        self.s.start()
        self.s.finished.connect(self.updatebutton)
        self.pushButton1.setEnabled(False)
        self.lineEdit1.setText('')
        self.lineEdit2.setText('')
        self.spinBox.setValue(1)

    def update_textBrowser(self, text):
            self.widget.textBrowser.append(str(text+'\n'))
            # self.pushButton.setEnabled(True)

    def openFolderDialog(self, lineEdit):
        # 打开文件夹对话框
        self.folderDialog = QFileDialog()
        self.folderPath = self.folderDialog.getExistingDirectory(self, '选择文件夹')
        # 更新第三个输入框的文本
        lineEdit.setText(self.folderPath)
    def updatebutton(self,t):
        self.pushButton1.setEnabled(True)



class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        #捐款弹窗
        # 创建下拉框和自定义组件
        self.comboBox = QComboBox()
        self.customWidget1 = MyCustomWidget1(widget=self)
        self.customWidget2 = MyCustomWidget2(widget=self)
        self.textBrowser = QtWidgets.QTextBrowser()
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 331, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.setWindowTitle('元气Downloader')
        self.setWindowIcon(QIcon('assets/Logo.png'))

        # 设置下拉框选项和默认文本
        self.comboBox.addItems(['输入链接', '输入搜索关键词'])
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "hr { height: 1px; border-width: 0; }\n"
                                            "li.unchecked::marker { content: \"\\2610\"; }\n"
                                            "li.checked::marker { content: \"\\2612\"; }\n"
                                            "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">批量下载元气桌面壁纸</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">目前提供两种模式：</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.输入壁纸地址</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.输入关键字进行搜索</p></body></html>"))

        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.textBrowser)
        layout.addWidget(self.comboBox)

        # 创建占位符Widget，并设置为垂直布局
        self.placeholderWidget = QWidget()
        placeholderLayout = QVBoxLayout()
        self.placeholderWidget.setLayout(placeholderLayout)
        layout.addWidget(self.placeholderWidget)

        self.setLayout(layout)

        # 连接下拉框的currentIndexChanged信号到槽函数
        self.comboBox.currentIndexChanged.connect(self.updateUI)

        # 默认显示第一个自定义组件
        self.currentWidget = None  # 当前显示的自定义组件
        self.updateUI(0)

    def updateUI(self, index):
        # 隐藏当前显示的自定义组件，如果不为空
        if self.currentWidget:
            self.currentWidget.hide()

        # 根据选项索引，获取新的自定义组件
        if index == 0:
            self.currentWidget = self.customWidget1
        elif index == 1:
            self.currentWidget = self.customWidget2

        # 显示新的自定义组件
        self.currentWidget.show()
        layout = self.placeholderWidget.layout()
        layout.addWidget(self.currentWidget)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    with open('assets/light_orange.qss', 'r') as file:
        app.setStyleSheet(file.read())
    window = MyWidget()
    window.show()
    app.exec()
