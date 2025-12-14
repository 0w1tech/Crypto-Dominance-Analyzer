import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QMessageBox,QWidget, QLabel, QComboBox, QProgressBar, QPushButton
from PyQt6.QtGui import QIcon, QPixmap, QGuiApplication, QCursor
from PyQt6.QtCore import Qt, QSize

app = QApplication(sys.argv)
radioBtn_style =(
    "QRadioButton::indicator:unchecked"
    "{"
    "border: 1px solid #e3e3e3;"
    "border-radius: 2px;"
    "}"
    "QRadioButton::indicator:checked"
    "{"
    "border: 1px solid ;"
    "border-radius: 2px;"
    "background:#1768ff;"
    "}")
app.setStyleSheet(radioBtn_style)
app.setStyle('Fusion') # ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
window = QMainWindow(windowTitle='Trading Journal DB')
window.setWindowIcon(QIcon("Icons/accounting.png"))
window.setFixedSize(620,580)
window.frameGeometry().moveCenter(QGuiApplication.primaryScreen().availableGeometry().center())
container = QWidget(window)
window.setCentralWidget(container)
# Information 0    
info_frame = QFrame(container)
info_frame.resize(580,120)
info_frame.move(20,0)
info_frame.setStyleSheet('font:bold 9pt;')

def market_dir_detector():
    if USDTD.currentIndex() != -1 and BTCD.currentIndex() != -1 and BTCP.currentIndex() != -1:     
        if (USDTD.currentIndex() == 0 or USDTD.currentIndex() == 3 or USDTD.currentIndex() == 5) and (BTCD.currentIndex() == 0 or BTCD.currentIndex() == 3 or BTCD.currentIndex() == 5) and (BTCP.currentIndex() == 0 or BTCP.currentIndex() == 3 or BTCP.currentIndex() == 5):
            card_handler(name='btc',dir=0,strong=2,caption='Bullish',hide=False)
            card_handler(name='alts',dir=2,strong=0,caption='Range or Weak Bearish/Bullish',hide=False)
            complete_analyze.setHidden(False)
            complete_analyze.setText('LONG BTC') 
        elif (USDTD.currentIndex() == 0 or USDTD.currentIndex() == 3 or USDTD.currentIndex() == 5) and (BTCD.currentIndex() == 0 or BTCD.currentIndex() == 3 or BTCD.currentIndex() == 5) and (BTCP.currentIndex() == 1 or BTCP.currentIndex() == 4 or BTCP.currentIndex() == 6):
            card_handler(name='btc',dir=1,strong=1,caption='Range or Weak Bearish',hide=False)
            card_handler(name='alts',dir=1,strong=3,caption='Strong Bearish',hide=False)
            complete_analyze.setHidden(False)
            complete_analyze.setText('SHORT ALTS') 
        elif (USDTD.currentIndex() == 0 or USDTD.currentIndex() == 3 or USDTD.currentIndex() == 5) and (BTCD.currentIndex() == 1 or BTCD.currentIndex() == 4 or BTCD.currentIndex() == 6) and (BTCP.currentIndex() == 0 or BTCP.currentIndex() == 3 or BTCP.currentIndex() == 5):
            card_handler(name='btc',dir=0,strong=1,caption='Weak Bullish',hide=False)
            card_handler(name='alts',dir=2,strong=0,caption='Range or Weak Bullish',hide=False)
            complete_analyze.setHidden(False)
            complete_analyze.setText('RANGE') 
        elif (USDTD.currentIndex() == 0 or USDTD.currentIndex() == 3 or USDTD.currentIndex() == 5) and (BTCD.currentIndex() == 1 or BTCD.currentIndex() == 4 or BTCD.currentIndex() == 6) and (BTCP.currentIndex() == 1 or BTCP.currentIndex() == 4 or BTCP.currentIndex() == 6):
            card_handler(name='btc',dir=1,strong=3,caption='Strong Bearish',hide=False)
            card_handler(name='alts',dir=1,strong=2,caption='bearish weaker than BTC',hide=False)
            complete_analyze.setHidden(False)
            complete_analyze.setText('SHORT') 
        elif (USDTD.currentIndex() == 1 or USDTD.currentIndex() == 4 or USDTD.currentIndex() == 6) and (BTCD.currentIndex() == 0 or BTCD.currentIndex() == 3 or BTCD.currentIndex() == 5) and (BTCP.currentIndex() == 0 or BTCP.currentIndex() == 3 or BTCP.currentIndex() == 5):
            card_handler(name='btc',dir=0,strong=3,caption='Strong Bullish',hide=False)
            card_handler(name='alts',dir=0,strong=2,caption='Bullish Weaker Than BTC',hide=False)
            complete_analyze.setHidden(False)
            complete_analyze.setText('LONG') 
        elif (USDTD.currentIndex() == 1 or USDTD.currentIndex() == 4 or USDTD.currentIndex() == 6) and (BTCD.currentIndex() == 0 or BTCD.currentIndex() == 3 or BTCD.currentIndex() == 5) and (BTCP.currentIndex() == 1 or BTCP.currentIndex() == 4 or BTCP.currentIndex() == 6):
            card_handler(name='btc',dir=1,strong=1,caption='Weak Bearish',hide=False)
            card_handler(name='alts',dir=1,strong=2,caption='Bearish Stronger Than BTC',hide=False)
            complete_analyze.setHidden(False)
            complete_analyze.setText('SHORT ALTS') 
        elif (USDTD.currentIndex() == 1 or USDTD.currentIndex() == 4 or USDTD.currentIndex() == 6) and (BTCD.currentIndex() == 1 or BTCD.currentIndex() == 4 or BTCD.currentIndex() == 6) and (BTCP.currentIndex() == 0 or BTCP.currentIndex() == 3 or BTCP.currentIndex() == 5):
            card_handler(name='btc',dir=0,strong=1,caption='Weak Bullish or Range',hide=False)
            card_handler(name='alts',dir=0,strong=3,caption='Strong Bullish',hide=False)
            complete_analyze.setHidden(False)
            complete_analyze.setText('LONG ALTS (ALT Seasion)') 
        elif (USDTD.currentIndex() == 1 or USDTD.currentIndex() == 4 or USDTD.currentIndex() == 6) and (BTCD.currentIndex() == 1 or BTCD.currentIndex() == 4 or BTCD.currentIndex() == 6) and (BTCP.currentIndex() == 1 or BTCP.currentIndex() == 4 or BTCP.currentIndex() == 6):
            card_handler(name='btc',dir=1,strong=2,caption='Bearish',hide=False)
            card_handler(name='alts',dir=1,strong=1,caption='Bearish Weaker Than BTC',hide=False)
            complete_analyze.setHidden(False)
            complete_analyze.setText('SHORT')
        else:
            card_handler(name='btc',dir=0,strong=0,caption='',hide=True)
            card_handler(name='alts',dir=0,strong=0,caption='',hide=True)
            complete_analyze.setHidden(False)
            complete_analyze.setText('Undefind Conditions!')                     
    else:
        datetime_warning = QMessageBox.warning(window,"WARNING!", "Entre All Inputs")            
        
label_USDTD = QLabel(info_frame,text="USDT.D")
label_USDTD.resize(50,30)
label_USDTD.move(10,20)            
USDTD = QComboBox(info_frame)
USDTD_cursor = QCursor()
USDTD_cursor.setShape(Qt.CursorShape.PointingHandCursor)
USDTD.setCursor(USDTD_cursor)
USDTD.setPlaceholderText("choose...")
USDTD.setCurrentIndex(-1)
USDTD.addItems(["Bull Trend","Bear Trend","Range","Reversal to Bull","Reversal to Bear","Range / Bull","Range / Bear"])
USDTD.setItemIcon(0,QIcon("Icons/arrow-up.png"))
USDTD.setItemIcon(1,QIcon("Icons/arrow-down.png"))
USDTD.setItemIcon(2,QIcon("Icons/range.png"))
USDTD.setItemIcon(3,QIcon("Icons/u-turn-to-up.png"))
USDTD.setItemIcon(4,QIcon("Icons/u-turn-to-down.png"))
USDTD.setItemIcon(5,QIcon("Icons/range-bull.png"))
USDTD.setItemIcon(6,QIcon("Icons/range-bear.png"))
USDTD.resize(120,30)
USDTD.move(60,20)

label_BTCD = QLabel(info_frame,text="BTC.D")
label_BTCD.resize(50,30)
label_BTCD.move(205,20)            
BTCD = QComboBox(info_frame)
BTCD_cursor = QCursor()
BTCD_cursor.setShape(Qt.CursorShape.PointingHandCursor)
BTCD.setCursor(BTCD_cursor)
BTCD.setPlaceholderText("choose...")
BTCD.setCurrentIndex(-1)
BTCD.addItems(["Bull Trend","Bear Trend","Range","Reversal to Bull","Reversal to Bear","Range / Bull","Range / Bear"])
BTCD.setItemIcon(0,QIcon("Icons/arrow-up.png"))
BTCD.setItemIcon(1,QIcon("Icons/arrow-down.png"))
BTCD.setItemIcon(2,QIcon("Icons/range.png"))
BTCD.setItemIcon(3,QIcon("Icons/u-turn-to-up.png"))
BTCD.setItemIcon(4,QIcon("Icons/u-turn-to-down.png"))
BTCD.setItemIcon(5,QIcon("Icons/range-bull.png"))
BTCD.setItemIcon(6,QIcon("Icons/range-bear.png"))
BTCD.resize(120,30)
BTCD.move(255,20)

label_BTCP = QLabel(info_frame,text="BTC.P")
label_BTCP.resize(50,30)
label_BTCP.move(400,20)            
BTCP = QComboBox(info_frame)
BTCP_cursor = QCursor()
BTCP_cursor.setShape(Qt.CursorShape.PointingHandCursor)
BTCP.setCursor(BTCP_cursor)
BTCP.setPlaceholderText("choose...")
BTCP.setCurrentIndex(-1)
BTCP.addItems(["Bull Trend","Bear Trend","Range","Reversal to Bull","Reversal to Bear","Range / Bull","Range / Bear"])
BTCP.setItemIcon(0,QIcon("Icons/arrow-up.png"))
BTCP.setItemIcon(1,QIcon("Icons/arrow-down.png"))
BTCP.setItemIcon(2,QIcon("Icons/range.png"))
BTCP.setItemIcon(3,QIcon("Icons/u-turn-to-up.png"))
BTCP.setItemIcon(4,QIcon("Icons/u-turn-to-down.png"))
BTCP.setItemIcon(5,QIcon("Icons/range-bull.png"))
BTCP.setItemIcon(6,QIcon("Icons/range-bear.png"))
BTCP.resize(120,30)
BTCP.move(450,20)

def clear():
    USDTD.setCurrentIndex(-1)
    BTCD.setCurrentIndex(-1)
    BTCP.setCurrentIndex(-1)
    btc_frame.setHidden(True)
    alts_frame.setHidden(True)
    complete_analyze.setHidden(True)

clear_btn = QPushButton(info_frame,text='CLEAR')
clear_btn.resize(100,50)
clear_btn.move(0,70)
clear_btn.setIcon(QIcon('Icons/erase.png'))
clear_btn.setIconSize(QSize(35,35))
clear_btn.clicked.connect(clear)

analyze_btn = QPushButton(info_frame,text='ANALYZE')
analyze_btn.resize(470,50)
analyze_btn.move(110,70)
analyze_btn.setIcon(QIcon('Icons/analyze.png'))
analyze_btn.setIconSize(QSize(35,35))
analyze_btn.clicked.connect(market_dir_detector)

result = QFrame(window)
result.setStyleSheet("background:#333;border-radius:3px")
result.resize(580,420)
result.move(20,140)

btc_frame = QFrame(result)
btc_frame.resize(260,210)
btc_frame.move(20,20)
btc_frame.setStyleSheet('border:1px solid #009643;')
btc_frame.setHidden(True)

btc_strong = QProgressBar(btc_frame,alignment=Qt.AlignmentFlag.AlignCenter)
btc_strong.resize(235,20)
btc_strong.move(12,15)
btc_strong.setRange(0,3)
btc_strong.setStyleSheet(f'border:1px solid gray;')

btc_label = QLabel(btc_frame,text="BTC",alignment=Qt.AlignmentFlag.AlignCenter)
btc_label.resize(100,30)
btc_label.move(60,65)
btc_label.setStyleSheet('border:none;font: bold 24pt')
btc_icon = QLabel(btc_frame,alignment=Qt.AlignmentFlag.AlignCenter)
btc_icon.setPixmap(QPixmap(f"Icons/arrow-up.png"))
btc_icon.setScaledContents(True)
btc_icon.resize(40,40)
btc_icon.move(150,60)
btc_icon.setStyleSheet('border:none;font: bold 16pt')

btc_analyze = QLabel(btc_frame,alignment=Qt.AlignmentFlag.AlignCenter)
btc_analyze.resize(235,60)
btc_analyze.move(12,135)
btc_analyze.setStyleSheet('border:none;font: bold 10pt;background:#555;')

alts_frame = QFrame(result)
alts_frame.resize(260,210)
alts_frame.move(300,20)
alts_frame.setStyleSheet('border:4px solid #009643;')
alts_frame.setHidden(True)

alts_strong = QProgressBar(alts_frame,alignment=Qt.AlignmentFlag.AlignCenter)
alts_strong.resize(235,20)
alts_strong.move(12,15)
alts_strong.setRange(0,3)
alts_strong.setStyleSheet(f'border:1px solid gray;')

alts_label = QLabel(alts_frame,text="ALTS",alignment=Qt.AlignmentFlag.AlignCenter)
alts_label.resize(100,30)
alts_label.move(60,65)
alts_label.setStyleSheet('border:none;font: bold 24pt')

alts_icon = QLabel(alts_frame,alignment=Qt.AlignmentFlag.AlignCenter)
alts_icon.setPixmap(QPixmap(f"Icons/arrow-up.png"))
alts_icon.setScaledContents(True)
alts_icon.resize(40,40)
alts_icon.move(150,60)
alts_icon.setStyleSheet('border:none;font: bold 16pt')

alts_analyze = QLabel(alts_frame,alignment=Qt.AlignmentFlag.AlignCenter)
alts_analyze.resize(235,60)
alts_analyze.move(12,135)
alts_analyze.setStyleSheet('border:none;font: bold 10pt;background:#555;')

def card_handler(name,dir,strong,caption,hide):
    '''
    name: str( btc , eth , alts )\n
    dir: int( 0 , 1 , 2) > 0 = bullish  1 = bearish  2 = range\n 
    strong: int( 1 , 2 , 3 ) > 1 = weak  2 = medium  3 = powerful\n
    caption: str( text )\n
    hide: bool
    '''
    
    if name == "btc":
        if dir == 0:
            btc_icon.setPixmap(QPixmap(f"Icons/arrow-up.png"))
            btc_frame.setStyleSheet(f'border:{strong+1 if strong == 3 or strong == 0 else strong}px solid #009643;')
            btc_strong.setStyleSheet(
            "QProgressBar::chunk "
            "{"
            "background-color: #009643;"
            "}")
            
        elif dir == 1:
            btc_icon.setPixmap(QPixmap(f"Icons/arrow-down.png")) 
            btc_frame.setStyleSheet(f'border:{strong+1 if strong == 3 or strong == 0 else strong}px solid red;')
            btc_strong.setStyleSheet(
            "QProgressBar::chunk "
            "{"
            "background-color: red;"
            "}")
            
        elif dir == 2:
            btc_icon.setPixmap(QPixmap(f"Icons/equal.png"))
            btc_frame.setStyleSheet(f'border:{strong+1 if strong == 3 or strong == 0 else strong}px solid gray;')
            btc_strong.setStyleSheet(
            "QProgressBar::chunk "
            "{"
            "background-color: yellow;"
            "}")    
                
        btc_strong.setValue(strong)
        btc_analyze.setText(caption)
        btc_frame.setHidden(hide)

    elif name == "alts": 
        if dir == 0:
            alts_icon.setPixmap(QPixmap(f"Icons/arrow-up.png"))
            alts_frame.setStyleSheet(f'border:{strong+1 if strong == 3 or strong == 0 else strong}px solid green;')
            alts_strong.setStyleSheet(
            "QProgressBar::chunk "
            "{"
            "background-color: green;"
            "border:none;"
            "}")
            
        elif dir == 1:
            alts_icon.setPixmap(QPixmap(f"Icons/arrow-down.png")) 
            alts_frame.setStyleSheet(f'border:{strong+1 if strong == 3 or strong == 0 else strong}px solid red;')
            alts_strong.setStyleSheet(
            "QProgressBar::chunk "
            "{"
            "background-color: red;"
            "border:none;"
            "}")
            
        elif dir == 2:
            alts_icon.setPixmap(QPixmap(f"Icons/equal.png"))
            alts_frame.setStyleSheet(f'border:{strong+1 if strong == 3 or strong == 0 else strong}px solid gray;')
            alts_strong.setStyleSheet(
            "QProgressBar::chunk "
            "{"
            "background-color: yellow;"
            "border:none;"
            "}")    
                
        alts_strong.setValue(strong)
        alts_analyze.setText(caption)
        alts_frame.setHidden(hide) 
    else:
        print("input name error!")    
          
complete_analyze = QLabel(result,alignment=Qt.AlignmentFlag.AlignCenter)
complete_analyze.resize(540,150)
complete_analyze.move(20,250)
complete_analyze.setHidden(True)
complete_analyze.setStyleSheet("background:#555;border-radius:3px;font:bold 32pt")

window.show()
sys.exit(app.exec())