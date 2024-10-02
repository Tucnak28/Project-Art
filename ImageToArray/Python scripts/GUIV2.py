import sys
import numpy as np
import PIL
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal, QObject
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmapCache, QGuiApplication, QPixmap
from PIL import Image
from scripts.ImageToArray import Img2Arr
from scripts.ArrayToImage import Arr2Img

class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)
        
class Worker(QObject):
    finished = pyqtSignal(object)

    def __init__(self, image_path, index):
        super().__init__()
        self.image_path = image_path
        self.index = index

    def run(self):
        color_converter = Img2Arr(self.image_path, self.index)
        result = color_converter.ColorsJSON()
        self.finished.emit(result)

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 800)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()

        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)

        self.setLayout(mainLayout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()

            if file_path.endswith('.json'):
                self.JSON = file_path
                width = 32#int(input("Enter width: ")) # ask for user input for width
                height = 32#int(input("Enter height: ")) # ask for user input for height
                self.image = self.toImage(width, height, self.JSON)
                self.set_image(self.image)
                event.accept()
            else:
                self.image1 = Image.open(file_path)
                if self.image1.width % 32 == 0 and self.image1.height % 32 == 0:            
                    img_width, img_height = self.image1.size
                    parts = []
                    index = 1
                    for i in range(0, img_height, 32):
                        for j in range(0, img_width, 32):
                            # Crop image piece
                            box = (j, i, j+32, i+32)
                            part = self.image1.crop(box)
                            # Append to parts list
                            
                            JSONImage = self.toArray(part, index)
                            print(index)
                            parts.append(self.toImage(32, 32, JSONImage))
                            index += 1
                    # Combine parts into original size image
                    new_image = Image.new('RGBA', (self.image1.width, self.image1.height))
                    for i, part in enumerate(parts):
                        print(part)
                        x = (i % (self.image1.width // 32)) * 32
                        y = (i // (self.image1.width // 32)) * 32
                        new_image.paste(part, (x, y))
                    new_image.save("MinecraftImage.png")
                    self.set_image(new_image)
                    print("Done")
                    event.accept()
                    return

                JSONImage = self.toArray(self.image1)
        
                self.image2 = self.toImage(self.image1.width, self.image1.height, JSONImage)
                self.set_image(self.image2)

                event.accept()
        else:
            event.ignore()

    def set_image(self, image):
        QPixmapCache.setCacheLimit(int(max(QPixmapCache.cacheLimit(), QGuiApplication.primaryScreen().logicalDotsPerInch() * 100)))
        img_qt = ImageQt(image)
        pixmap = QPixmap.fromImage(img_qt)
        scale = 200 % pixmap.width()
        pixmap = pixmap.scaled(pixmap.width()*scale, pixmap.height()*scale)
        self.photoViewer.setPixmap(pixmap)


    def ToArray_thread(self, image_path, index):
        color_converter = Img2Arr(image_path, index)  # pass image_path argument
        self.JSON = color_converter.ColorsJSON()
    
    def ToImage_thread(self, JSON, width, height):
        image_creator = Arr2Img(JSON, width, height)
        self.image = image_creator.ImageParse()

    # Then, instead of using threading directly in the main GUI thread:
    def toArray(self, image, index):
        self.worker = Worker(image, index)
        self.worker.finished.connect(self.onArrayFinished)
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def onArrayFinished(self, result):
        self.JSON = result
        self.thread.quit()
    
    def toImage(self, width, height, JSON):
        t2 = threading.Thread(target=self.ToImage_thread, args=(JSON, width, height))
        t2.start()
        t2.join()

        return self.image



app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())