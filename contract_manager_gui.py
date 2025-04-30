import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                            QWidget, QToolButton)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QTimer
import subprocess
import threading
import os

class ContractManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("合同管理系统")
        self.setGeometry(100, 100, 1200, 800)
        
        # 启动Flask服务器
        self.flask_process = None
        self.start_flask_server()
        
        # 创建Web视图
        self.browser = QWebEngineView()
        # 延迟3秒加载URL，等待服务器启动
        self.load_timer = QTimer()
        self.load_timer.setSingleShot(True)
        self.load_timer.timeout.connect(lambda: self.browser.setUrl(QUrl("http://127.0.0.1:5000")))
        self.load_timer.start(3000)  # 3秒后加载
        
        # 创建悬浮返回按钮
        self.back_btn = QToolButton(self)
        self.back_btn.setText("←")
        self.back_btn.setStyleSheet("""
            QToolButton {
                background: rgba(240, 240, 240, 0.9);
                border: 1px solid #ccc;
                border-radius: 15px;
                padding: 5px;
                min-width: 30px;
                min-height: 30px;
                font-size: 16px;
            }
            QToolButton:hover {
                background: rgba(224, 224, 224, 0.9);
            }
        """)
        self.back_btn.move(10, 10)
        self.back_btn.clicked.connect(self.browser.back)
        self.back_btn.raise_()  # 确保按钮在最上层
        
        # 设置主布局
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.browser)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def start_flask_server(self):
        """启动Flask服务器"""
        def run_flask():
            os.chdir("d:/DaBaiCai/pythonproject/contract_manager")
            self.flask_process = subprocess.Popen(["python", "run.py"])
        
        flask_thread = threading.Thread(target=run_flask)
        flask_thread.daemon = True
        flask_thread.start()
    
    def closeEvent(self, event):
        """关闭窗口时停止Flask服务器"""
        if self.flask_process:
            self.flask_process.terminate()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContractManagerApp()
    window.show()
    sys.exit(app.exec_())
