from pytube import YouTube
from PyQt5 import uic, QtWidgets

def dwld():
    link = downloader.lineEdit.text()
    yt = YouTube(link)
    ys = yt.streams.first()
    downloader.label_3.setText("Title: "+yt.title)
    downloader.label_4.setText("Views: "+str(yt.views))
    downloader.label_5.setText("Lenght: "+str(yt.length)+" seconds")
    downloader.label_6.setText("Rating: "+str(yt.rating))

    ys.download('/home/otavio/Desktop/')
    
    downloader.label.setText("Download Completed! Enter another YouTube Link:")
    downloader.label_7.setText("Downloaded video info:")
    downloader.lineEdit.setText("")

app = QtWidgets.QApplication([])
downloader = uic.loadUi("yt_downloader.ui")
downloader.pushButton.clicked.connect(dwld)

downloader.show()
app.exec()