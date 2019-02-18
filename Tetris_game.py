"""
俄罗斯方块
"""

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtGui import QPen, QPainter
import sys

"""
1.  PyQt5 中用以制作小游戏的组件：


2.  整体思路介绍：
    四个class：
    =========
        Tetris(QMainWindow):
        -------
            创建游戏.
        
        Board(QFrame):
        ------
            游戏主要逻辑.
            
            
        
        Tetrominoe:
        -----------
            所有砖块.
        
        Shape:
        ------
            所有砖块代码。
"""