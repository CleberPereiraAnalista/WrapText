# Classe para inserir quebra de linhas em string dentro de espaços em branco

class WrapText:

    def __init__(self, text=None, length_wrap=50, break_type="\n"):
        self.length_wrap = length_wrap
        self.break_type = break_type
        self.text = text
        self.size_text = len(text)
        self.text_aux = ""

        if self.size_text > length_wrap:
            self.start()

    
    def get(self):
        return self.text

    
    def has_break_type(self):
        if self.text.find(self.break_type) > 0:
            return True
        else:
            return False

    def search_space(self):
        for i, char in reversed(list(enumerate(self.text_aux))):
            if char == " ":
                self.replace_char(i)
                break

    def start(self):

        if self.has_break_type():
            # Outras quebras
            breaked_text = self.text.split(self.break_type)

            # pega a última parte
            initial_text = f"{self.break_type}".join(breaked_text[:-1])
            last_text = self.text.split(self.break_type)[-1]

            # Verifica se precisa ser tratada
            if len(last_text) > self.length_wrap:
                self.text_aux = f"{initial_text}{self.break_type}{last_text[:self.length_wrap]}"
                self.search_space()
            else:
                return self.text
        else:
            # 1ª quebra
            self.text_aux = self.text[:self.length_wrap]
            self.search_space()
        

    def replace_char(self, pos):
        # Localiza a 1ª ocorrência do espaço em branco e substitui no texto principal
        text_listed = list(self.text)
        text_listed[pos] = self.break_type
        self.text = "".join(text_listed)

        # Reinicia processo
        self.start()
