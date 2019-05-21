import pyttsx3

class RecogbyEn():
    def __init__(self,dict_en,mainform):
        self.dict_en = dict_en
        self.error_count = 0
        self.__audio_engine = pyttsx3.init()
        self.mainform = mainform
        self.mainform.playaudio_btn_en.clicked.connect(self.playaudio)
        self.mainform.remember_btn_en.clicked.connect(mainform.remember_en)
        self.mainform.forget_btn_en.clicked.connect(mainform.forget_en)
        self.mainform.tooeasy_btn_en.clicked.connect(mainform.tooeasy_en)

    def playaudio(self):
        self.__audio_engine.say(self.dict_en.nowword['word'])
        self.__audio_engine.runAndWait()

    def update(self):
        tips_html = ''
        print('update recog')
        print(tips_html)
        for i in range(0,self.error_count):
            print(i)
            tips_html += self.__html[i] + '\n'

        self.mainform.html_tb_en.setHtml(tips_html)

    def initform(self):
        self.error_count = 0
        self.__html = self.dict_en.nowword_tips_html
