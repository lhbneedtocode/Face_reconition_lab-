import sys
import cv2
import numpy as np
import face_recognition
import face_detect
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QPushButton
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal, Qt

match=[]

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    change_finish_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self._run_flag = True
    def foo(self):
        pass

    def run(self):
        # Capture from the default webcam
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        while self._run_flag:
            ret, frame = cap.read()
            ret, frame = cap.read()

            if ret:
                # Perform face recognition
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                face_locations = face_recognition.face_locations(rgb_frame)

                # Draw rectangles around faces
                if face_locations:
                    face_encodings = face_recognition.face_encodings(frame, known_face_locations=face_locations)
                    global match
                    match=face_detect.check(face_encodings)
                    for (top, right, bottom, left) in face_locations:
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

                self.change_pixmap_signal.emit(frame)
                self.change_finish_signal.emit(match)
        # Release the video capture object
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()


class FaceRecognitionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Face Recognition")
        self.setGeometry(100, 350, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.result_label = QLabel("", self)
        self.layout.addWidget(self.result_label)

        self.retu = QPushButton("OK",self)
        self.retu.setCheckable(True)
        self.retu.move(200, 480)
        #self.retu.clicked.connect(self.closeEvent)
        self.retu.clicked.connect(self.to_close)
        self.match = []

        # Create the video capture thread
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        #self.thread.change_finish_signal.connect(self.retuu)
        self.thread.start()

    def to_close(self):
        self.close()

    '''def retuu(self,match):
        print(match)'''

    def update_image(self, frame):
        # Convert the frame to QImage
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
        self.image_label.setPixmap(QPixmap.fromImage(p))

    def closeEvent(self, event):
        self.thread.stop()
        cv2.destroyAllWindows()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FaceRecognitionApp()
    window.show()
    sys.exit(app.exec_())
