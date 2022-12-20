import random


class SongsQuiz:
    songs = ["Jingle Bells", "Last Christmas", "Never Gonna Give You Up", "Shape of You",
             "We Wish You a Merry Christmas"]
    usedSongs = []
    i = 5
    pluses = 0
    result = ""
    quizes = 0
    testpluses = 0
    file = 0
    song = "Jingle Bells"
    TP = []
    TNTSS = []
    answer = "Jingle Bells"
    TRQ = []
    TRR = 0

    def chooseSong(self):
        self.song = random.choice(self.songs)
        self.songs.remove(self.song)

    def askQuestion(self):
        self.file = open(self.song + ".txt", "r")
        while True:
            line = self.file.readline()
            if not line:
                break
            print(line.strip())
        print()
        print("Введите название песни")

    def testPlus(self):
        if self.answer.lower() == self.song.lower() and self.pluses == (self.testpluses + 1):
            self.testpluses = self.testpluses + 1
            self.TP.append(1)
        elif self.answer.lower() != self.song.lower() and self.pluses == self.testpluses:
            self.TP.append(1)
        else:
            self.TP.append(0)

    def testNotTheSameSong(self):
        if self.song in self.usedSongs or self.song == "":
            self.TNTSS.append(0)
        else:
            self.TNTSS.append(1)
            self.usedSongs.append(self.song)

    def testRightQuestion(self):
        temp = open(self.song + ".txt", "r")
        if str(temp) == str(self.file):
            self.TRQ.append(1)
        else:
            self.TRQ.append(0)

    def testRightResult(self):
        if self.result == f"Вы угадали {self.pluses} из {self.i} песен.":
            self.TRR = 1

    def testsCheck(self):
        if 0 in self.TP:
            print("testPlus: unsuccess")
        else:
            print("testPlus: success")
        if 0 in self.TNTSS:
            print("testNotTheSameSong: unsuccess")
        else:
            print("testNotTheSameSong: success")
        if 0 in self.TRQ:
            print("testRightQuestion: unsuccess")
        else:
            print("testRightQuestion: success")
        if self.TRR == 1:
            print("testRightResult: success")
        else:
            print("testRightResult: unsuccess")

    def main(self):
        while self.quizes != 5:
            self.chooseSong(obj)
            self.testNotTheSameSong(obj)
            self.askQuestion(obj)
            self.testRightQuestion(obj)
            self.testPlus(obj)
            self.quizes = self.quizes + 1
        self.testRightResult(obj)
        self.testsCheck(obj)


obj = SongsQuiz
obj.main(obj)