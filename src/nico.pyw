from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from main_window import Ui_MainWindow
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from requests import get
import json
from datetime import datetime, timedelta
from time import time
from jk import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        ui = Ui_MainWindow()
        ui.setupUi(self)

        self.ip = "nasneのIPアドレス"

        self.graph = ui.graphicsView
        self.graph.hideAxis("left")
        self.graph.hideAxis("bottom")

        self.played = False
        self.id_ = ""
        self.title = ui.title

        self.t = time()
        self.timing = 0.0
        self.timer = ui.timer
        self.seek = ui.seekbar
        self.seek.sliderMoved.connect(self.seeked)
        self.seek.sliderReleased.connect(self.seekend)
        self.seeking = False

        self.speed_ui = ui.speed
        self.speed = 1.0

        self.from_date = ui.fr
        self.to_date = ui.tO
        self.from_date.setDateTime(datetime.today())

        ui.spup.clicked.connect(self.speed_up)
        ui.spdn.clicked.connect(self.speed_down)

        self.comments = []
        self.viewed_comments = []
        self.pos = 0

        self.ch = 9
        self.duration = 1

        ui.action1.triggered.connect(self.set_ch(1))
        ui.action2.triggered.connect(self.set_ch(2))
        ui.action4.triggered.connect(self.set_ch(4))
        ui.action5.triggered.connect(self.set_ch(5))
        ui.action6.triggered.connect(self.set_ch(6))
        ui.action7.triggered.connect(self.set_ch(7))
        ui.action8.triggered.connect(self.set_ch(8))
        ui.action9.triggered.connect(self.set_ch(9))

        self.graph.setXRange(0, 1)
        self.graph.setYRange(0.0, 0.9)

        self.nasne()

    def sto(self, st, duration):
        return datetime.fromisoformat(st), datetime.fromisoformat(st) + timedelta(
            seconds=duration
        )

    def nasne(self):
        try:
            player_info = json.loads(
                get(f"http://{self.ip}:64210/status/dtcpipClientListGet").content
            )
            id_ = player_info["client"][0]["content"]["id"]
            if self.id_ != id_:
                self.id_ = id_
                data = json.loads(
                    get(
                        f"http://{self.ip}:64220/recorded/titleListGet?searchCriteria=0&filter=0&startingIndex=0&requestedCount=0&sortCriteria=0&withDescriptionLong=0&withUserData=0&id={id_}"
                    ).content
                )
                self.title.setText(data["item"][0]["title"])
                s, t = self.sto(
                    data["item"][0]["startDateTime"], data["item"][0]["duration"]
                )
                for k, v in jk_chs.items():
                    if data["item"][0]["serviceId"] in v:
                        self.ch = int(k[2:])
                self.from_date.setDateTime(s)
                self.to_date.setDateTime(t)
                self.timing = 0.0
                length = len(self.viewed_comments) - 1
                for i in range(length + 1):
                    self.graph.removeItem(self.viewed_comments.pop(length - i).item)
                self.pos = 0
                self.get_comments()
                self.played = True
            else:
                return False
        except:
            self.title.setText("")
            return False

    def set_ch(self, ch):
        def f(*args):
            self.ch = ch

        return f

    def get_comments(self):
        self.comments = self.get_jikkyo(self.ch, self.from_date, self.to_date)
        self.duration = (
            self.to_date.dateTime().toPyDateTime()
            - self.from_date.dateTime().toPyDateTime()
        ).total_seconds()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.speed_up()
        elif e.key() == Qt.Key_Down:
            self.speed_down()
        elif e.key() == Qt.Key_Space:
            self.played = not self.played
            self.t = time()
        elif e.key() == Qt.Key_Return:
            self.get_comments()
        elif e.key() == Qt.Key_Right:
            self.timing += 10
            self.timer.setText(f"{int(self.timing//60):02}:{int(self.timing%60):02}")
        elif e.key() == Qt.Key_Left:
            self.timing -= 10
            self.timer.setText(f"{int(self.timing//60):02}:{int(self.timing%60):02}")
        elif e.key() == Qt.Key_R:
            self.graph.setXRange(0, 1)
            self.graph.setYRange(0.0, 0.9)

    def timestamp(self, time):
        return int(datetime.timestamp(time.dateTime().toPyDateTime()))

    def get_jikkyo(self, ch, st, en):
        resp = get(
            f"https://jikkyo.tsukumijima.net/api/kakolog/jk{ch}?starttime={self.timestamp(st)}&endtime={self.timestamp(en)}&format=json"
        )
        jikkyo = [
            [
                (
                    datetime.fromtimestamp(
                        float(f"{i['chat']['date']}.{i['chat']['date_usec']}")
                    )
                    - st.dateTime().toPyDateTime()
                ).total_seconds(),
                i["chat"]["content"],
                i["chat"].get("mail") if i["chat"].get("mail") else "",
            ]
            for i in json.loads(resp.content)["packet"]
        ]
        return jikkyo

    def speed_up(self, *args):
        self.speed = min(2.0, self.speed + 0.1)
        self.speed_ui.setText(f"x {self.speed:.1f}")

    def speed_down(self, *args):
        self.speed = max(1.0, self.speed - 0.1)
        self.speed_ui.setText(f"x {self.speed:.1f}")

    def seeked(self, *args):
        delta = (
            self.to_date.dateTime().toPyDateTime()
            - self.from_date.dateTime().toPyDateTime()
        ).total_seconds()
        d = delta * (self.seek.sliderPosition() / 10000)
        self.timer.setText(f"{int(d//60):02}:{int(d%60):02}")
        self.seeking = True

    def seekend(self, *args):
        self.timing = 60 * int(self.timer.text()[:-3]) + int(self.timer.text()[-2:])
        length = len(self.viewed_comments) - 1
        for i in range(length + 1):
            self.graph.removeItem(self.viewed_comments.pop(length - i).item)
        self.pos = 0
        for comment in self.comments:
            if comment[0] > self.timing:
                break
            self.pos += 1
        self.seeking = False

    def update(self):
        if self.from_date.dateTime() > self.to_date.dateTime():
            self.to_date.setDateTime(self.from_date.dateTime())

        if self.played:
            self.timing -= self.speed * (self.t - time())
            self.t = time()
            if not self.seeking:
                self.timer.setText(
                    f"{int(self.timing//60):02}:{int(self.timing%60):02}"
                )
                self.seek.setSliderPosition(int(1e4 * self.timing / self.duration))
            for comment in self.comments[self.pos :]:
                if comment[0] > self.timing:
                    break
                self.pos += 1
                self.viewed_comments.append(
                    Comment(
                        comment[1],
                        self.graph,
                        **{a: i for i in comment[2].split() if (a := MAIL.get(i))},
                    )
                )

            length = len(self.viewed_comments) - 1
            for i, v_comment in enumerate(self.viewed_comments[::-1]):
                if v_comment.update():
                    self.graph.removeItem(self.viewed_comments.pop(length - i).item)
        else:
            self.t = time()


class Comment:
    def __init__(
        self, content, parent, font="defont", color="white", size="medium", place="naka"
    ):
        self.content = content
        self.font = FONTS[font]
        self.color = COLORS[color]
        self.size = SIZES[size]
        self.place = place
        self.x = 1.2
        if self.place == "naka":
            self.y = 0.9 * np.random.rand()
        elif self.place == "ue":
            self.y = 0.9
        elif self.place == "shita":
            self.y = 0
        self.speed = np.random.uniform(0.005, 0.008) + len(
            self.content
        ) * np.random.uniform(0.0002, 0.0004)
        self.item = pg.TextItem(
            anchor=(0.5, 0.5),
            html=f"<span style=\"color: {self.color}; font-size: {self.size}pt; font-family: '{self.font}';\">{self.content}</span>",
        )
        self.item.setPos(self.x, self.y)
        parent.addItem(self.item)

    def update(self):
        self.x -= self.speed
        if self.place == "naka":
            self.item.setPos(self.x, self.y)
        else:
            self.item.setPos(0.5, self.y)
        return self.x < -2


if __name__ == "__main__":

    # GUI
    app = QtWidgets.QApplication([])
    w = MainWindow()
    timer = QtCore.QTimer()
    timer.timeout.connect(w.update)
    timer.start(30)
    timer2 = QtCore.QTimer()
    timer2.timeout.connect(w.nasne)
    timer2.start(5000)
    w.show()
    QtGui.QApplication.instance().exec_()