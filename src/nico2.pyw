from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from main_window import Ui_MainWindow
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime, timedelta
from time import time
import re
from jk import *


class InputWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        self.setWindowTitle("アニメタイトルから検索")
        self.title_entry = QtWidgets.QLineEdit(self)
        self.ep_entry = QtWidgets.QLineEdit(self)
        self.title_entry.setPlaceholderText("Title")
        self.ep_entry.setPlaceholderText("Episode")
        self.title_entry.setAlignment(QtCore.Qt.AlignCenter)
        self.ep_entry.setAlignment(QtCore.Qt.AlignCenter)
        self.title_entry.setFixedWidth(400)
        self.ep_entry.setFixedWidth(100)
        self.button = QtWidgets.QPushButton(self, text="取得")
        self.layout.addWidget(self.title_entry, 0, 0)
        self.layout.addWidget(self.ep_entry, 0, 1)
        self.layout.addWidget(self.button, 1, 0, 1, 2)
        self.button.clicked.connect(self.set)
        self.chs = {
            "NHK総合": 1,
            "日本テレビ": 4,
            "テレビ朝日": 5,
            "TBS": 6,
            "テレビ東京": 7,
            "フジテレビ": 8,
            "TOKYO MX": 9,
        }
        self.tids = {}

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.button.click()

    def get_tid(self, title):
        url = f"https://cal.syoboi.jp/json?Req=TitleSearch&Search={title}&Limit=1"
        tid = (
            self.tids.get(title)
            or list(list(json.loads(get(url).content).values())[0].keys())[0]
        )
        self.tids[title] = tid
        return tid

    def set(self):
        title = self.title_entry.text()
        ep = self.ep_entry.text()
        tid = self.get_tid(title)
        url = f"https://cal.syoboi.jp/tid/{tid}/time?Filter2=All&Filter=ChUser"
        filt = "ChFilter=2%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29%2C30%2C31%2C32%2C33%2C34%2C35%2C36%2C37%2C38%2C39%2C40%2C41%2C42%2C43%2C44%2C45%2C46%2C47%2C48%2C49%2C50%2C51%2C52%2C53%2C54%2C55%2C56%2C57%2C58%2C59%2C60%2C61%2C62%2C63%2C64%2C65%2C66%2C67%2C68%2C69%2C70%2C71%2C72%2C73%2C74%2C75%2C76%2C77%2C78%2C79%2C80%2C81%2C82%2C83%2C84%2C85%2C86%2C87%2C88%2C89%2C90%2C91%2C92%2C93%2C94%2C95%2C96%2C97%2C98%2C99%2C100%2C101%2C102%2C103%2C104%2C105%2C106%2C107%2C108%2C109%2C110%2C111%2C112%2C113%2C114%2C115%2C116%2C117%2C118%2C119%2C120%2C121%2C122%2C123%2C124%2C125%2C126%2C127%2C128%2C129%2C130%2C131%2C132%2C133%2C134%2C135%2C136%2C137%2C138%2C139%2C140%2C141%2C142%2C143%2C144%2C145%2C146%2C147%2C148%2C149%2C150%2C151%2C152%2C153%2C154%2C155%2C156%2C157%2C158%2C159%2C160%2C161%2C162%2C163%2C164%2C165%2C166%2C167%2C168%2C169%2C170%2C171%2C172%2C173%2C174%2C175%2C176%2C177%2C178%2C179%2C180%2C181%2C182%2C183%2C184%2C185%2C186%2C187%2C188%2C189%2C190%2C191%2C192%2C193%2C194%2C195%2C196%2C197%2C198%2C199%2C200%2C201%2C202%2C203%2C204%2C205%2C206%2C207%2C208%2C209%2C210%2C211%2C212%2C213%2C214%2C215%2C216%2C217%2C218%2C219%2C220%2C221%2C222%2C223%2C224%2C225%2C226%2C227%2C228%2C229%2C230%2C231%2C232%2C233%2C234%2C235%2C236%2C237%2C238%2C239%2C240%2C241%2C242%2C243%2C244%2C245%2C246%2C247%2C248%2C249%2C250%2C251%2C252%2C253%2C254%2C255%2C256%2C257%2C258%2C259%2C260%2C261%2C262%2C263%2C264%2C265%2C266%2C267%2C268%2C269%2C270%2C271%2C272%2C273%2C274%2C275%2C276;"
        soup = BeautifulSoup(
            get(
                url,
                headers={
                    "cookie": filt,
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                },
            ).content,
            "lxml",
            from_encoding="utf-8",
        )
        df = pd.read_html(str(soup.find(id="ProgList")))[0]
        a = df[df["回数▲▼"] == int(ep)].iloc[0]
        ch = self.chs[a["チャンネル▲▼"]]
        y, m, d, H, M = map(
            int,
            re.findall(
                "(\d{4})-(\d{2})-(\d{2})\(.+?\)\xa0(\d{2}):(\d{2})", a["開始日時▲▼"]
            )[0],
        )
        st = datetime(y, m, d + H // 24, H % 24, M)
        ed = st + timedelta(minutes=int(a["分▲▼"]))
        self.parent.ch = ch
        self.parent.from_date.setDateTime(st)
        self.parent.to_date.setDateTime(ed)
        self.parent.comments = self.parent.get_jikkyo(
            ch, self.parent.from_date, self.parent.to_date
        )
        self.parent.duration = a["分▲▼"] * 60
        self.hide()


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
        self.subwin = None

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

    def get_comments2(self):
        self.subwin = self.subwin or InputWindow(self)
        self.subwin.show()

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
        elif e.modifiers() & Qt.ControlModifier:
            if e.key() == Qt.Key_F:
                self.get_comments2()
        elif e.key() == Qt.Key_Right:
            self.timing += 10
            self.timer.setText(f"{int(self.timing//60):02}:{int(self.timing%60):02}")
        elif e.key() == Qt.Key_Left:
            self.timing -= 10
            self.timer.setText(f"{int(self.timing//60):02}:{int(self.timing%60):02}")
        elif e.key() == Qt.Key_R:
            self.graph.setXRange(0, 1)
            self.graph.setYRange(0.0, 0.9)
        elif e.key() == Qt.Key_A:
            self.skip("A")
        elif e.key() == Qt.Key_B:
            self.skip("B")
        elif e.key() == Qt.Key_C:
            self.skip("C")
        elif e.key() == Qt.Key_T:
            self.skip("ｷﾀ", False)

    def skip(self, key, match=True):
        x, *_ = zip(*self.comments)
        if match:
            a, b = np.histogram(
                [i for i, j, k in self.comments if j == key],
                bins=60,
                range=(min(x), max(x)),
            )
        else:
            a, b = np.histogram(
                [i for i, j, k in self.comments if key in j],
                bins=60,
                range=(min(x), max(x)),
            )
        length = len(self.viewed_comments) - 1
        for i in range(length + 1):
            self.graph.removeItem(self.viewed_comments.pop(length - i).item)
        self.timing = b[a.argmax()]
        self.pos = 0
        for comment in self.comments:
            if comment[0] > self.timing:
                break
            self.pos += 1

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
