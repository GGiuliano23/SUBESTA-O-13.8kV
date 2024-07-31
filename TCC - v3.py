import customtkinter
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time
import math

modoescuro = False
cordefundo = "white"
cordebotao = ""
customtkinter.set_appearance_mode("light")  # Modos: sistema (default), light, dark
customtkinter.set_default_color_theme("blue")  # Temas: blue (default), dark-blue, green

app = customtkinter.CTk()  # Cria janela CTK
app.title("Dimensionamento de Subestacao")
app.geometry("1920x1080")
#app.iconbitmap("icone.ico")
app.state('zoomed')


frame = customtkinter.CTkScrollableFrame(app, orientation="vertical", width=1920, height=1080, fg_color=cordefundo)
frame.pack(fill="both", expand=True)

# Dados da Instalacao
dadosdainstalacaolabel = customtkinter.CTkLabel(frame, text="Dados de instalação", font=customtkinter.CTkFont(family="Arial", size=40, weight="bold"))
dadosdainstalacaolabel.pack(side="top", pady=10)

# Botao escuro/claro
def toggle_mode():
    global modoescuro
    global cordefundo
    if modoescuro == False:
        customtkinter.set_appearance_mode("dark")
        cordefundo = "#1f1f1f"
        modoescuro = True
        cordebotao = "#708090"
    else:
        customtkinter.set_appearance_mode("light")
        cordefundo = "white"
        modoescuro = False
        cordebotao = "#3e92c4"

    # Background Color
    frame.configure(fg_color=cordefundo)

    # Update cores de Widgets
    dadosdainstalacaolabel.configure(fg_color=cordefundo)
    modoescuro_button.configure(fg_color=cordebotao)

# Modo escuro
modoescuro_button = customtkinter.CTkButton(frame, text="Modo Escuro", command=toggle_mode)
modoescuro_button.pack(side="top", anchor='e', pady=20)

botaodeconsulta = customtkinter.CTkImage(light_image=Image.open("duvidas.png"), dark_image=Image.open("duvidaswhite.png"))

def retorna_tabela(frame, tab):
    table = tab
    return customtkinter.CTkButton(
        frame,
        hover=True,
        image=botaodeconsulta,
        text='',
        bg_color="transparent",
        fg_color="transparent",
        hover_color="gray",
        width=30,
        height=30,
        command=lambda: abrir_janela_com_imagem(table)
    )

def abrir_janela_com_imagem(tabela):
    qualatabela = tabela
    imagem = Image.open(qualatabela)
    imagem.show()

def cria_label(frame, text, font_family="Arial", font_size=20, font_weight="bold"):
    return customtkinter.CTkLabel(
        frame,
        text=text,
        font=customtkinter.CTkFont(family=font_family, size=font_size, weight=font_weight)
    )

def cria_entry(frame, width=300, font_family="Arial", font_size=20):
    return customtkinter.CTkEntry(
        frame,
        width=width,
        font=customtkinter.CTkFont(family=font_family, size=font_size)
    )

# Frame linha um #================================================================================================================================================================================
line1_frame = customtkinter.CTkFrame(frame)
line1_frame.pack(fill="x", pady=5, padx=0)
tensaoprimarialabel = cria_label(line1_frame, "Tensão Primaria")
tensaoprimariaentry = cria_entry(line1_frame)
tensaosecundarialabel = cria_label(line1_frame, "Tensão Secundaria")
tensaosecundariaentry = cria_entry(line1_frame)
kV = cria_label(line1_frame, "kV")
V = cria_label(line1_frame, "V")

tensaoprimarialabel.pack(side="left", padx=10)
tensaoprimariaentry.pack(side="left", padx=10)
kV.pack(side="left", padx=10)
tensaosecundarialabel.pack(side="left", padx=10)
tensaosecundariaentry.pack(side="left", padx=10)
V.pack(side="left", padx=10)

# Frame linha dois #================================================================================================================================================================================
line2_frame = customtkinter.CTkFrame(frame)
line2_frame.pack(fill="x", pady=5, padx=0)


cargainstaladalabel = cria_label(line2_frame, "Carga instalada")
cargainstaladakva = cria_entry(line2_frame, width=200)
cargainstaladakw = cria_entry(line2_frame, width=200)
kw = cria_label(line2_frame, "kW")
kva = cria_label(line2_frame, "kVA")

cargainstaladalabel.pack(side="left", padx=10)
cargainstaladakva.pack(side="left", padx=(21.5, 10))
kva.pack(side="left", padx=10)
cargainstaladakw.pack(side="left", padx=10)
kw.pack(side="left", padx=10)


# Frame linha tres #================================================================================================================================================================================
line3_frame = customtkinter.CTkFrame(frame)
line3_frame.pack(fill="x", pady=5, padx=0)

demandalabel = cria_label(line3_frame, "Demanda")
demandakva = cria_entry(line3_frame, width=200)
demandakw = cria_entry(line3_frame, width=200)
kw = cria_label(line3_frame, "kW")
kva = cria_label(line3_frame, "kVA")

demandalabel.pack(side="left", padx=10)
demandakva.pack(side="left", padx=(85, 10))
kva.pack(side="left", padx=10)
demandakw.pack(side="left", padx=10)
kw.pack(side="left", padx=10)

# Frame linha quatro #================================================================================================================================================================================
line4_frame = customtkinter.CTkFrame(frame)
line4_frame.pack(fill="x", pady=5, padx=0)

fatordepotencialabel = cria_label(line4_frame, "Fator de potência")
fatordepotenciaentry = cria_entry(line4_frame, width=200)
fatordepotenciamediolabel = cria_label(line4_frame, "Fator de potência Médio")
fatordepotenciamedioentry = cria_entry(line4_frame, width=200)

fatordepotencialabel.pack(side="left", padx=10)#,anchor="w")
fatordepotenciaentry.pack(side="left", padx=10)

fatordepotenciamediolabel.pack(side="left", padx=10)
fatordepotenciamedioentry.pack(side="left", padx=10)

# Frame linha zeroum #================================================================================================================================================================================
line01_frame = customtkinter.CTkFrame(frame)
line01_frame.pack(fill="x", pady=5, padx=0)

dimtraf = retorna_tabela(line01_frame, "dimensionatrafo.png")

opcoestransformador = ['10', '15', '30', '45', '75', '150', '225', '300', '500', '637.5', '750', '1000','1300']

dimensionamentodotransformadorlabel = cria_label(line01_frame, "Dimensionamento do Transformador", font_size=25)
transformadorescolhidolabel = cria_label(line01_frame, "Transformador Escolhido")
correntemediatensaodemandadalabel = cria_label(line01_frame, "Corrente Média de Tensão Demandada")
correntenominaldotrafolabel = cria_label(line01_frame, "Corrente Nominal do Trafo")
Idemlabelzeroum = cria_label(line01_frame, "Idem")
Ienelabelzeroum = cria_label(line01_frame, "In")
Adezesete = cria_label(line01_frame, "A")
Adezoito = cria_label(line01_frame, "A")
kvazeroum = cria_label(line01_frame, "KVA")

transformadorescolhidoentry = customtkinter.CTkComboBox(
    master=line01_frame,
    width=200,
    font=customtkinter.CTkFont("Arial", 20),
    values=opcoestransformador
)

correntemedia = cria_entry(line01_frame, width=200)
correntenominaldotrafo = cria_entry(line01_frame, width=200)

dimensionamentodotransformadorlabel.grid(row = 0, column = 2, pady = (10, 10))
dimtraf.grid(row = 0, column = 4, pady = (10, 10), padx = (0,0))

transformadorescolhidolabel.grid(row = 1, column=2, padx=(30,0), pady = 5)
transformadorescolhidoentry.grid(row = 2, column=2, padx=(30,0), pady = 5)

correntemediatensaodemandadalabel.grid(row = 3, column = 2, padx=(30,0), pady = 5)
Idemlabelzeroum.grid(row = 4, column = 1, padx=(400,0), pady = 5)
correntemedia.grid(row = 4, column = 2, padx=(30,0), pady = 5)
Adezesete.grid(row = 4, column = 2, padx=(280,0), pady = 5)

correntenominaldotrafolabel.grid(row = 5, column = 2, padx=(30,0), pady = 5)
Ienelabelzeroum.grid(row = 6, column = 1, padx=(400,0), pady = 5)
correntenominaldotrafo.grid(row = 6, column = 2, padx=(30,0), pady = 5)
Adezoito.grid(row = 6, column = 2, padx=(280,0), pady = 5) 

# Frame linha zerodois #================================================================================================================================================================================
line02_frame = customtkinter.CTkFrame(frame)
line02_frame.pack(fill="x", pady=5, padx=0)

dimdisj = retorna_tabela(line02_frame, "dimensionamentodisj.png")

dimensionamentododisjuntor = cria_label(line02_frame, "Dimensionamento do Disjuntor", font_size=25)
correntenominalzerodoislabel = cria_label(line02_frame, "Corrente Nominal")
correntenominalzerodoisentry = cria_entry(line02_frame, width=200)
correntenominaldotrafolabelzerodoislabel = cria_label(line02_frame, "Corrente Nominal do Disjuntor")
correntenominaldodisjuntorzerodoisentry = cria_entry(line02_frame, width=200)

correntemaximadeinterrupcaodecclabel = cria_label(line02_frame, "Corrente Máxima de Interrupção de Curto-Circuito")
correntemaximadeinterrupcaodeccentry = cria_entry(line02_frame, width=200)

ienetres = cria_label(line02_frame, "In")
idisj = cria_label(line02_frame, "Idisj")
imi = cria_label(line02_frame, "Imi")
adezenove = cria_label(line02_frame, "A")
avinte = cria_label(line02_frame, "A")
avinteum = cria_label(line02_frame, "A")

dimensionamentododisjuntor.grid(row = 0, column = 2, pady = (10, 10))
dimdisj.grid(row = 0, column = 2, pady = (10, 10), padx = (410, 0))
correntenominalzerodoislabel.grid(row = 1, column = 2, pady = 5)
ienetres.grid(row = 2, column = 1, padx=(400,0), pady = 5)
correntenominalzerodoisentry.grid(row = 2, column = 2, pady = 5)
adezenove.grid(row = 2, column = 2, padx=(250,0), pady = 5)

correntenominaldotrafolabelzerodoislabel.grid(row = 3, column = 2, pady = 5)
idisj.grid(row = 4, column = 1, padx=(400,0), pady = 5)
correntenominaldodisjuntorzerodoisentry.grid(row = 4, column = 2, pady = 5)
avinte.grid(row = 4, column = 2, padx=(250,0), pady = 5)

correntemaximadeinterrupcaodecclabel.grid(row = 5, column = 2, pady = 5)
imi.grid(row = 6, column = 1, padx=(400,0), pady = 5)
correntemaximadeinterrupcaodeccentry.grid(row = 6, column = 2, pady = 5)
avinteum.grid(row = 6, column = 2, padx=(250,0), pady = 5)

# Frame linha zerotres #================================================================================================================================================================================
line03_frame = customtkinter.CTkFrame(frame)
line03_frame.pack(fill="x", pady=5, padx=0)

tabelachaveseccionadora = retorna_tabela(line03_frame, "chaveseccionadora.png")
tabela12 = retorna_tabela(line03_frame, "tabela12.png")

dimensionamentodachaveseccionadoratripolareelofusivel = cria_label(line03_frame, "Dimensionamento da Chave Seccionadora Tripolar e Elo Fusível", font_size=25)
chaveseccionadoratripolarlabel = cria_label(line03_frame, "Chave Seccionadora Tripolar")
elofusivellabel = cria_label(line03_frame, "Elo Fusível")
chaveseccionadoratripolarentry = cria_entry(line03_frame, width=200)
capacidadedoelolabel = cria_label(line03_frame, "Capacidade do Elo")
capacidadedoeloentry = cria_entry(line03_frame, width=200)
avinteedois = cria_label(line03_frame, "A")
kvazerodois = cria_label(line03_frame, "KVA")

opcoeselofusivel = ['5','10','15','25','30','37.5','45','75','112.5','150','200','225','250',
                    '300','350','400','450','500','550','600','650','700','750','800']

elofusivelentry = customtkinter.CTkComboBox(
    master=line03_frame,
    width=200,
    font=customtkinter.CTkFont("Arial", 20),
    values=opcoeselofusivel
)

dimensionamentodachaveseccionadoratripolareelofusivel.grid(row = 1, column = 1, padx=(300,0), pady = 10)
chaveseccionadoratripolarlabel.grid(row = 2, column = 1, padx=(300,0), pady = 5)
tabelachaveseccionadora.grid(row = 2, column = 1, padx=(630,0), pady = 5)
chaveseccionadoratripolarentry.grid(row = 3, column = 1, padx=(300,0), pady = 5)
avinteedois.grid(row = 3, column = 1, padx = (550, 0), pady = 5)
elofusivellabel.grid(row = 4, column = 1, padx=(300,0), pady = 5)
tabela12.grid(row = 4, column = 1, padx=(450,0), pady = 5)
elofusivelentry.grid(row = 5, column = 1, padx=(300,0), pady = 5)
kvazerodois.grid(row = 5, column = 1, padx = (550,0), pady = 5)
capacidadedoelolabel.grid(row = 6, column = 1, padx=(300,0), pady = 5)
capacidadedoeloentry.grid(row = 7, column = 1, padx=(300,0), pady = 5)

# Frame linha zeroquatro #================================================================================================================================================================================
line04_frame = customtkinter.CTkFrame(frame)
line04_frame.pack(fill="x", pady=5, padx=0)

dimfushh = retorna_tabela(line04_frame, "dimensionafusivelhh.png")

dimensionamentodefusivelhhclasse15kvlabel = cria_label(line04_frame, "Dimensionamento de Fusível HH Classe 15Kv", font_size=25)
fusivelhhlabel = cria_label(line04_frame, "Fusível HH")
kvazerotres = cria_label(line04_frame, "KVA")
fusivelminimoemaximolabel = cria_label(line04_frame, "Fusível Minimo e Máximo")
fusivelminimoemaximoentry = cria_entry(line04_frame, width=200)

opcoesfusivelhh = ['30','45','75','112.5','150','225','300', '500', '750','1000','1250', '1500']

fusivelhhentry = customtkinter.CTkComboBox(
    master=line04_frame,
    width=200,
    font=customtkinter.CTkFont("Arial", 20),
    values=opcoesfusivelhh
)


dimensionamentodefusivelhhclasse15kvlabel.grid(row = 1, column = 1, pady = 10, padx=(415,0))
dimfushh.grid(row = 1, column = 3, pady = 10, padx=(0,0))

fusivelhhlabel.grid(row = 2, column = 1, pady = 5, padx=(415,0))
fusivelhhentry.grid(row = 3, column = 1, pady = 5, padx=(415,0))
kvazerotres.grid(row = 3, column = 1, padx = (415+250,0), pady = 5)
fusivelminimoemaximolabel.grid(row = 4, column = 1, pady = 5, padx=(415,0))
fusivelminimoemaximoentry.grid(row = 5, column = 1, pady = 5, padx=(415,0))

# Frame linha zerocinco #================================================================================================================================================================================
line05_frame = customtkinter.CTkFrame(frame)
line05_frame.pack(fill="x", pady=5, padx=0)

tabelaraio = retorna_tabela(line05_frame, "tabela16.png")

dimensionamentodepararaios = cria_label(line05_frame, "Dimensionamento de Para-Raios 13,8KV", font_size=25)
tensaonominalraiolabel = cria_label(line05_frame, "Tensão Nominal")
tensaonominalraioentry = cria_entry(line05_frame, width=200)
correntenominalraiolabel = cria_label(line05_frame, "Corrente Nominal")
correntenominalraioentry = cria_entry(line05_frame, width=200)
kvazeocinco = cria_label(line05_frame, "KVA")
kvzerocinco = cria_label(line05_frame, "KV")

dimensionamentodepararaios.pack(side="top", pady = 10)
tabelaraio.pack(side = RIGHT, padx = (0, 200))
tensaonominalraiolabel.pack(side="left", padx = (230,10))
tensaonominalraioentry.pack(side="left", padx = 10)
kvazeocinco.pack(side = "left", padx = 10)
correntenominalraiolabel.pack(side="left", padx = (50,10))
correntenominalraioentry.pack(side="left", padx = 10, pady=10)
kvzerocinco.pack(side="left", padx = 10)

# Frame linha zeroseis #================================================================================================================================================================================
line06_frame = customtkinter.CTkFrame(frame)
line06_frame.pack(fill="x", pady=5, padx=0)

tab4 = retorna_tabela(line06_frame, "tabela4.png")

dimensionamentobarramentodecobremt = cria_label(line06_frame, "Dimensionamento Barramento de Cobre MT", font_size=25)
potenciatrafolabel = cria_label(line06_frame, "Potência Trafo")
barraoutuboocolabel = cria_label(line06_frame, "Barra ou Tubo Oco")
vergalhaolabel = cria_label(line06_frame, "Vergalhão")
mm = cria_label(line06_frame, "mm²")
pol = cria_label(line06_frame, "Pol")

opcoespotenciatrafo = ['P ≤ 500', '500 < P ≤ 1500', '1500 < P ≤ 2000', '2000 < P ≤ 2500', '2500 < P ≤ 5000']

potenciatrafo = customtkinter.CTkComboBox(
    master=line06_frame,
    width=200,
    font=customtkinter.CTkFont("Arial", 20),
    values=opcoespotenciatrafo
)

barraoutubooco = cria_entry(line06_frame, width=200)
vergalhaomm = cria_entry(line06_frame, width=200)
vergalhaopol = cria_entry(line06_frame, width=200)

kvzeroseis = cria_label(line06_frame, "KV")
kazeroseis = cria_label(line06_frame, "KA")

dimensionamentobarramentodecobremt.grid(row = 1, column = 2, padx = (100,0))
tab4.grid(row = 1, column = 2, padx = (650,0))

potenciatrafolabel.grid(row = 2, column = 1, padx = (50,0))
potenciatrafo.grid(row = 3, column = 1, padx = (50,0))
kvzeroseis.grid(row = 3, column = 1, padx = (300,0))

barraoutuboocolabel.grid(row = 2, column = 2)
barraoutubooco.grid(row = 3, column = 2)
kazeroseis.grid(row = 3, column = 2, padx = (250,0))

vergalhaolabel.grid(row = 2, column = 3)
vergalhaomm.grid(row = 3, column = 3)
mm.grid(row = 3, column = 3, padx = (250,0))
vergalhaopol.grid(row = 4, column = 3, pady = 5)
pol.grid(row = 4, column = 3, padx = (250,0))

# Frame linha zerosete #================================================================================================================================================================================
line07_frame = customtkinter.CTkFrame(frame)
line07_frame.pack(fill="x", pady=5, padx=0)

dimensionamentodoscondutores = cria_label(line07_frame, "Dimensionamento dos Condutores", font_size=25)

potenciadocircuitolabel = cria_label(line07_frame, "Potência do Circuito")
fatordesobrecargalabel = cria_label(line07_frame, "Fator de Sobrecarga")
correntemaximadecurtocircuitolabel = cria_label(line07_frame, "Corrente máxima de CC")
distancialabel = cria_label(line07_frame, "Distância")
fatordepotenciazerosetelabel = cria_label(line07_frame, "Fator de Potência")
tempodeoperacaolabel = cria_label(line07_frame, "Tempo de Operação")
correntenominalzerosetelabel = cria_label(line07_frame, "Corrente Nominal")
correntecomsobrecargalabel = cria_label(line07_frame, "Corrente com Sobrecarga")

potenciadocircuito = cria_entry(line07_frame, width=200)
fatordesobrecarga = cria_entry(line07_frame, width=200)
correntemaximadecurtocircuito = cria_entry(line07_frame, width=200)
distancia = cria_entry(line07_frame, width=200)
fatordepotenciazerosete = cria_entry(line07_frame, width=200)
tempodeoperacao = cria_entry(line07_frame, width=200)
correntenominalzerosete = cria_entry(line07_frame, width=200)
correntecomsobrecarga = cria_entry(line07_frame, width=200)

vazeroseteum = cria_label(line07_frame, "VA")
vazerosetedois = cria_label(line07_frame, "VA")
eme = cria_label(line07_frame, "m")
esse = cria_label(line07_frame, "s")

ienequatro = cria_label(line07_frame, "In")
isc = cria_label(line07_frame, "Isc")
avinteetres = cria_label(line07_frame, "A")
avinteequatro = cria_label(line07_frame, "A")

dimensionamentodoscondutores.grid(row = 1, column = 2, pady = 10)

potenciadocircuitolabel.grid(row = 2, column = 1, padx = (200,0), pady = 5)
potenciadocircuito.grid(row = 3, column = 1, padx = (200,0), pady = 5)
vazeroseteum.grid(row = 3, column = 1, padx = (200+250,0), pady = 5)

distancialabel.grid(row = 4, column = 1, padx = (200,0), pady = 5)
distancia.grid(row = 5, column = 1, padx = (200,0), pady = 5)
eme.grid(row = 5, column = 1, padx = (200+250,0), pady = 5)

fatordesobrecargalabel.grid(row = 2, column = 2, pady = 5)
fatordesobrecarga.grid(row = 3, column = 2, pady = 5)
fatordepotenciazerosetelabel.grid(row = 4, column = 2, pady = 5)
fatordepotenciazerosete.grid(row = 5, column = 2, pady = 5)

correntemaximadecurtocircuitolabel.grid(row = 2, column = 3, pady = 5)
correntemaximadecurtocircuito.grid(row = 3, column = 3, pady = 5)
vazerosetedois.grid(row = 3, column = 3, padx = (250,0), pady = 5)
tempodeoperacaolabel.grid(row = 4, column = 3, pady = 5)
tempodeoperacao.grid(row = 5, column = 3, pady = 5)
esse.grid(row = 5, column = 3, padx = (250,0), pady = 5)

correntenominalzerosetelabel.grid(row = 6, column = 1, padx = (200,0), pady = 5)
correntenominalzerosete.grid(row = 7, column = 1, padx = (200,0), pady = 5)
ienequatro.grid(row = 7, column = 1, padx = (200,250), pady = 5)
avinteetres.grid(row = 7, column = 1, padx = (450,0), pady = 5)
correntecomsobrecargalabel.grid(row = 6, column = 2, pady = 5)
correntecomsobrecarga.grid(row = 7, column = 2, pady = 5)
isc.grid(row = 7, column = 2, pady = 5, padx = (0, 250))
avinteequatro.grid(row = 7, column = 2, pady = 5, padx = (250,0))


# Frame linha zerooito #================================================================================================================================================================================
line08_frame = customtkinter.CTkFrame(frame)
line08_frame.pack(fill="x", pady=5, padx=0)

caracteriticasconstrutiva = cria_label(line08_frame, "Características Construtiva", font_size=25)

condutorlabel = cria_label(line08_frame, "Condutor")
opcoescondutor = ['Aluminio', 'Cobre']

condutor = customtkinter.CTkComboBox(
    master=line08_frame,
    width=200,
    font=customtkinter.CTkFont("Arial", 20),
    values=opcoescondutor
)


isolacaolabel = cria_label(line08_frame, "Isolacao")

opcoesisolacao = ['PVC','EPR 90','EPR 150','XLPE','HEPR',]

isolacao = customtkinter.CTkComboBox(
    master=line08_frame,
    width=200,
    font=customtkinter.CTkFont("Arial", 20),
    values=opcoesisolacao
)

mododeinstalacaolabel = cria_label(line08_frame, "Modo de Instalação")

opcoesmododeinstalacao = ['A1', 'A2','B1', 'B2', 'C', 'D', 'E', 'F1', 'F2', 'G1', 'G2', 'H', 'I']

mododeinstalacao = customtkinter.CTkComboBox(
    master=line08_frame,
    width=200,
    font=customtkinter.CTkFont("Arial", 20),
    values=opcoesmododeinstalacao
)

caracteriticasconstrutiva.grid(row = 1, column=2)

condutorlabel.grid(row = 2, column=1, padx = (325,0))
condutor.grid(row = 3, column = 1, padx = (325,0))

isolacaolabel.grid(row = 2, column = 2)
isolacao.grid(row = 3, column = 2)

mododeinstalacaolabel.grid(row = 2, column = 3)
mododeinstalacao.grid(row = 3, column = 3)

# Frame linha zero nove #================================================================================================================================================================================
line09_frame = customtkinter.CTkFrame(frame)
line09_frame.pack(fill="x", pady=5, padx=0)

tab3031 = retorna_tabela(line09_frame, "faltaatabela.jpg")
tab32 = retorna_tabela(line09_frame, "faltaatabela.jpg")
tab343738 = retorna_tabela(line09_frame, "faltaatabela.jpg")

fatoresdecorrecaodecorrentelabel = cria_label(line09_frame, "Fator de Correção de Corrente", font_size=25)

fatordecorrecaoportemperaturalabel = cria_label(line09_frame, "Fator de Correção por Temperatura (FCT)")
fatordecorrecaoportemperatura = cria_entry(line09_frame, width=200)

fatordecorrecaoporresistividadelabel = cria_label(line09_frame,"Fator de Correção por Resistividade (FCR)")
fatordecorrecaoporresistividade = cria_entry(line09_frame, width=200)

fatordecorrecaoporagrupamentolabel = cria_label(line09_frame, "Fator de Correção por Agrupamento (FCA)")
fatordecorrecaoporagrupamento = cria_entry(line09_frame, width=200)

fatoresdecorrecaodecorrentelabel.grid(row = 0, column = 1, pady = 10, padx = (480,0))
tab3031.grid(row = 1, column = 2)
fatordecorrecaoportemperaturalabel.grid(row = 1, column = 1, pady = 10, padx = (480,0))
fatordecorrecaoportemperatura.grid(row = 2, column = 1, pady = 10, padx = (480,0))
fatordecorrecaoporresistividadelabel.grid(row = 3, column = 1, pady = 10, padx = (480,0))
tab32.grid(row = 3, column = 2)
fatordecorrecaoporresistividade.grid(row = 4, column = 1, pady = 10, padx = (480,0))
fatordecorrecaoporagrupamentolabel.grid(row = 5, column = 1, pady = 10, padx = (480,0))
tab343738.grid(row = 5, column = 2)
fatordecorrecaoporagrupamento.grid(row = 6, column = 1, pady = 10, padx = (480,0))

# Frame dez #================================================================================================================================================================================
line10_frame = customtkinter.CTkFrame(frame)
line10_frame.pack(fill="x", pady=5, padx=0)

tab2829 = retorna_tabela(line10_frame, "faltaatabela.jpg")

validacaodoscondutoreslabel = cria_label(line10_frame, "Validação Dos Condutores", font_size=25)

metodo01label = cria_label(line10_frame, "Método 01 - Capacidade de Condução de Corrente",font_size=25)

secaodocondutorlabel = cria_label(line10_frame, "Seção Do Condutor")
opcoessecaodocondutor = ['2.5','4','6','10','16','25','50','70','95','120','150',
                         '185','240','300','400','500','630','800','1000']

secaodocondutorentry = customtkinter.CTkComboBox(
    master=line10_frame,
    width=200,
    font=customtkinter.CTkFont("Arial", 20),
    values=opcoessecaodocondutor
)

emeemedois = cria_label(line10_frame, "mm²")

capacidadedecorrentelabel = cria_label(line10_frame, "Capacidade de Corrente")
capacidadedecorrente = cria_entry(line10_frame, width=200)
avinteecinco = cria_label(line10_frame, "A")

capacidadedecorrentecorrigidalabel = cria_label(line10_frame, "Capacidade de Corrente Corrigida")
capacidadedecorrentecorrigida = cria_entry(line10_frame, width=200)
avinteeseis = cria_label(line10_frame, "A")

correntemaximadocircuitolabel = cria_label(line10_frame, "Corrente Máxima do Circuito")
correntemaximadocircuito = cria_entry(line10_frame, width=200)
avinteesete = cria_label(line10_frame, "A")

validacaodoscondutoreslabel.grid(row = 1, column = 2)
metodo01label.grid(row = 2, column = 2, pady  = 20)

secaodocondutorlabel.grid(row = 3, column = 1, padx = (40, 0))
secaodocondutorentry.grid(row = 4, column = 1, padx = (40, 0))
emeemedois.grid(row = 4, column = 1, padx = (350, 0))

capacidadedecorrentelabel.grid(row = 3, column = 2)
tab2829.grid(row = 3, column = 2, padx = (270,0))

capacidadedecorrente.grid(row = 4, column = 2)
avinteecinco.grid(row = 4, column = 2, padx = (220,0))

capacidadedecorrentecorrigidalabel.grid(row = 3, column = 3)
capacidadedecorrentecorrigida.grid(row = 4, column = 3)
avinteeseis.grid(row = 4, column = 3, padx = (220,0))

correntemaximadocircuitolabel.grid(row = 5, column = 2, pady = (10))
correntemaximadocircuito.grid(row = 6, column = 2)
avinteesete.grid(row = 6, column = 2, padx = (220,0))


metodo02label = cria_label(line10_frame, "Método 02 - Curto Circuito",font_size=25)

correntemaximadecurtocircuitolabeldois = cria_label(line10_frame, "Corrente Máxima de Curto-Circuito")
correntemaximadecurtocircuitodois = cria_entry(line10_frame, width=200)
tempolimiteatuacaolabel = cria_label(line10_frame, "Tempo Limite da Atuação da Proteção")
tempolimiteatuacao = cria_entry(line10_frame, width=200)
tempodeoperacaodaprotecaolabel = cria_label(line10_frame, "Tempo de Operação da Proteção (A)")
tempodeoperacaodaprotecao = cria_entry(line10_frame, width=200)

avinteeoito = cria_label(line10_frame, "A")
essetempo = cria_label(line10_frame, "s")
essetempodois = cria_label(line10_frame, "s")

metodo02label.grid(row = 7, column = 2, pady = 20)
correntemaximadecurtocircuitolabeldois.grid(row = 8, column = 2)
correntemaximadecurtocircuitodois.grid(row = 9, column = 2, pady = 5)

tempodeoperacaodaprotecaolabel.grid(row = 10, column = 2)
tempodeoperacaodaprotecao.grid(row = 11, column = 2, pady = 5)

tempolimiteatuacaolabel.grid(row = 12, column = 2)
tempolimiteatuacao.grid(row = 13, column = 2, pady = 5)

metodo03label = cria_label(line10_frame, "Método 03 - Queda de Tensão",font_size=25)

quantasfaseslabel = cria_label(line10_frame, "Quantas Fases o Circuito Possui?")

opcoesdefases = ['Monofásico', 'Bifásico', 'Trifásico']

quantasfases = customtkinter.CTkComboBox(
    master=line10_frame,
    width=200,
    font=customtkinter.CTkFont("Arial", 20),
    values=opcoesdefases
)

correnteabsorvidapelacargalabel = cria_label(line10_frame, "Corrente Absorvida Pela carga")
correnteabsorvidapelacarga = cria_entry(line10_frame, width=200)
fatordepotencialabeldois = cria_label(line10_frame, "Fator de Potência")
fatordepotenciadois = cria_entry(line10_frame, width=200)
xllabel = cria_label(line10_frame, "XL - Reatância Indutiva da LT")
xl = cria_entry(line10_frame, width=200)
resistenciadosalimentadoreslabel = cria_label(line10_frame,"Resistência dos Alimentadores em Corrente Alternada")
resistenciadosalimentadores = cria_entry(line10_frame, width=200)
distanciadaalimentacaolabel = cria_label(line10_frame, "Distância da Alimentação á Carga")
distanciadaalimentacao = cria_entry(line10_frame, width=200)

avinteenove = cria_label(line10_frame, "A")
atrinta = cria_label(line10_frame, "A")

ohmkm = cria_label(line10_frame, "OHM/KM")
ohmkmdois = cria_label(line10_frame, "OHM/KM")
km = cria_label(line10_frame, "KM")

quedadetensaolabel = cria_label(line10_frame, "Queda de Tensão")
quedadetensao = cria_entry(line10_frame, width=200)
porcentagem = cria_label(line10_frame, "%")

metodo03label.grid(row = 14, column = 2, pady = 20)

quantasfaseslabel.grid(row = 15, column = 1, padx = (40, 0))
quantasfases.grid(row = 16, column = 1, padx = (40, 0))

xllabel.grid(row = 17, column = 1, padx = (40, 0), pady = 10)
xl.grid(row = 18, column = 1, padx = (40, 0))
ohmkmdois.grid(row = 18, column = 1, padx = (40+260, 0))

correnteabsorvidapelacargalabel.grid(row = 15, column = 2, pady = 10)
correnteabsorvidapelacarga.grid(row = 16, column = 2)
avinteenove.grid(row = 16, column = 2, padx = (250,0))

resistenciadosalimentadoreslabel.grid(row = 17, column = 2, pady = 10)
resistenciadosalimentadores.grid(row = 18, column = 2)
ohmkm.grid(row = 18, column = 2, padx = (250,0))

fatordepotencialabeldois.grid(row = 15, column = 3, pady = 10)
fatordepotenciadois.grid(row = 16, column = 3)
atrinta.grid(row = 16, column = 3, padx = (250,0))

distanciadaalimentacaolabel.grid(row = 17, column = 3, pady = 10)
distanciadaalimentacao.grid(row = 18, column = 3)
km.grid(row = 18, column = 3, padx = (250,0))

quedadetensaolabel.grid(row = 19, column = 2, pady = 15)
quedadetensao.grid(row = 20, column = 2)
porcentagem.grid(row = 20, column = 2, padx = (250,0))



# Dados da Proteçãp #================================================================================================================================================================================
dadosdeprotecaolabel = customtkinter.CTkLabel(frame, text="Dados de Proteção", font=customtkinter.CTkFont(family="Arial", size=40, weight="bold"))
dadosdeprotecaolabel.pack(side="top", pady=(40,10))

# Frame linha  #================================================================================================================================================================================
line11_frame = customtkinter.CTkFrame(frame)
line11_frame.pack(fill="x", pady=5, padx=0)

niveisdecc = cria_label(line11_frame,"Níveis de Curto Circuito")

icctrifasicolabel = cria_label(line11_frame, "ICC Trifásico (ICC3F)")
icctrifasico = cria_entry(line11_frame, width=200)

iccbifasicolabel = cria_label(line11_frame, "ICC Bifásico (ICC2F)")
iccbifasico = cria_entry(line11_frame, width=200)

iccterralabel = cria_label(line11_frame, "ICC FASE-TERRA (ICCFT)")
iccterra = cria_entry(line11_frame, width=200)

iccterra40label = cria_label(line11_frame, "ICC FASE-TERRA 40Ω(ICCFT40)")
iccterra40 = cria_entry(line11_frame, width=200)

iccterra100label = cria_label(line11_frame, "ICC FASE-TERRA 100Ω(ICCFT100)")
iccterra100 = cria_entry(line11_frame, width=200)

atrintaeum = cria_label(line11_frame, "A")
atrintaedois = cria_label(line11_frame, "A")
atrintaetres = cria_label(line11_frame, "A")
atrintaequatro = cria_label(line11_frame, "A")
atrintaecinco = cria_label(line11_frame, "A")

niveisdecc.grid(row = 1, column = 2)

icctrifasicolabel.grid(row = 2, column = 1, padx = (330,0))
iccbifasicolabel.grid(row = 3, column = 1, padx = (330,0))
iccterralabel.grid(row = 4, column = 1, padx = (330,0))                 
iccterra40label.grid(row = 5, column = 1, padx = (330,0))
iccterra100label.grid(row = 6, column = 1, padx = (330,0))

icctrifasico.grid(row = 2, column = 2, pady = 10)
iccbifasico.grid(row = 3, column = 2, pady = 10)
iccterra.grid(row = 4, column = 2, pady = 10)                  
iccterra40.grid(row = 5, column = 2, pady = 10)
iccterra100.grid(row = 6, column = 2, pady = 10)


atrintaeum.grid(row = 2, column = 2, padx=(250,0))
atrintaedois.grid(row = 3, column = 2, padx=(250,0))
atrintaetres.grid(row = 4, column = 2, padx=(250,0))
atrintaequatro.grid(row = 5, column = 2, padx=(250,0))
atrintaecinco.grid (row = 6, column = 2, padx=(250,0))



# Frame linha sete #================================================================================================================================================================================
line7_frame = customtkinter.CTkFrame(frame)
line7_frame.pack(fill="x", pady=5, padx=0)

dadosadicionais = cria_label(line7_frame, "Dados Adicionais")

distenciaentrereleesetcslabel = cria_label(line7_frame, "Distância Entre Relé e TC's")
distenciaentrereleesetcs = cria_entry(line7_frame, width=200)

resistenciaunitariadocabolabel = cria_label(line7_frame, "Resistência Unitária do Cabo")
resistenciaunitariadocabo = cria_entry(line7_frame, width=200)

consumodorelelabel = cria_label(line7_frame, "Consumo do Relé")
consumodorele = cria_entry(line7_frame, width=200)

correntenominallabel = cria_label(line7_frame, "Corrente Nominal")
correntenominal = cria_entry(line7_frame, width=200)

zburdendotclabel = cria_label(line7_frame, "Z Burden do TC")
zburdendotc = cria_entry(line7_frame, width=200)

zporcentolabel = cria_label(line7_frame, "Impedância do Transformador %")
zporcento = cria_entry(line7_frame, width=200)
porcento = cria_label(line7_frame, "%")

zporcentolabel.grid(row = 1, column=0, padx=(400,15))
zporcento.grid(row = 1, column=1)
porcento.grid(row = 1, column=1, padx=(230,0))

dadosadicionais.grid(row = 0, column = 1)
distenciaentrereleesetcslabel.grid(row = 2, column = 0, pady = 15, padx=(400,15))
distenciaentrereleesetcs.grid(row = 2, column = 1)
resistenciaunitariadocabolabel.grid(row = 3, column = 0, pady = 15, padx=(400,15))
resistenciaunitariadocabo.grid(row = 3, column = 1)
consumodorelelabel.grid(row = 4, column = 0, pady = 15, padx=(400,15))
consumodorele.grid(row = 4, column = 1)
correntenominallabel.grid(row = 5, column = 0, pady = 15, padx=(400,15))
correntenominal.grid(row = 5, column = 1)
zburdendotclabel.grid(row = 6, column = 0, pady = 15, padx=(400,15))
zburdendotc.grid(row = 6, column = 1)


# Frame linha cinco #================================================================================================================================================================================
line5_frame = customtkinter.CTkFrame(frame)
line5_frame.pack(fill="x", pady=5, padx=0)

impedanciaequivalentelabel = cria_label(line5_frame, "Impedância Eq. Da concessionária")

ZCClabel = cria_label(line5_frame, "ZCC")
ZCCentry = cria_entry(line5_frame, width=200)

OHMSlabelum = cria_label(line5_frame, "OHMS")
OHMSlabeldois = cria_label(line5_frame, "OHMS")
OHMSlabeltres = cria_label(line5_frame, "OHMS")
OHMSlabelquatro = cria_label(line5_frame, "OHMS")

impedanciaequivalentelabel.grid(row=1, column=1, columnspan=1, pady = (10, 15))
ZCClabel.grid(row=2, column=0, padx=(200,0))
ZCCentry.grid(row=2, column=1)

OHMSlabelum.grid(row=2,  column=1, padx = (270, 0))

impedanciadotransformadorlabel = cria_label(line5_frame, "Impedância do Transformador")

Ztrafo1label = cria_label(line5_frame, "Ztrafo1")
Ztrafo1entry = cria_entry(line5_frame, width=200)

Ztrafo2label = cria_label(line5_frame, "Ztrafo2")
Ztrafo2entry = cria_entry(line5_frame, width=200)

Ztrafo3label = cria_label(line5_frame, "Ztrafo3")
Ztrafo3entry = cria_entry(line5_frame, width=200)

impedanciadotransformadorlabel.grid(row= 3, column=1, columnspan=1, pady = 15)

Ztrafo1label.grid(row=4, column=0, padx=(200,0), pady=(5))
Ztrafo1entry.grid(row=4, column=1)
OHMSlabeldois.grid(row=4, column=1, padx = (270, 0))

Ztrafo2label.grid(row=5, column=0, padx=(200,0), pady=(5))
Ztrafo2entry.grid(row=5, column=1)
OHMSlabeltres.grid(row=5, column=1, padx = (270, 0))

Ztrafo3label.grid(row=6, column=0, padx=(200,0), pady=(5))
Ztrafo3entry.grid(row=6, column=1)
OHMSlabelquatro.grid(row=6, column=1, padx = (270, 0))

ccnosecundariodostransformadores = cria_label(line5_frame, "CC no Secundário dos Transformadores")
Accum = cria_label(line5_frame, "A")
Accdois = cria_label(line5_frame, "A")
Acctres = cria_label(line5_frame, "A")

Ztrafo1labelcc = cria_label(line5_frame, "Ztrafo1")
Ztrafo1entrycc = cria_entry(line5_frame, width=200)

Ztrafo2labelcc = cria_label(line5_frame, "Ztrafo2")
Ztrafo2entrycc = cria_entry(line5_frame, width=200)

Ztrafo3labelcc = cria_label(line5_frame, "Ztrafo3")
Ztrafo3entrycc = cria_entry(line5_frame, width=200)

ccnosecundariodostransformadores.grid(row= 7, column=1, columnspan=1, pady = 15)

Ztrafo1labelcc.grid(row=8, column=0, padx=(200,0), pady=(5))
Ztrafo1entrycc.grid(row=8, column=1)
Accum.grid(row=8,  column=1, padx = (230, 0))

Ztrafo2labelcc.grid(row=9, column=0, padx=(200,0), pady=(5))
Ztrafo2entrycc.grid(row=9, column=1)
Accdois.grid(row=9,  column=1, padx = (230, 0))

Ztrafo3labelcc.grid(row=10, column=0, padx=(200,0), pady=(5))
Ztrafo3entrycc.grid(row=10, column=1)
Acctres.grid(row=10,  column=1, padx = (230, 0))


Aum = cria_label(line5_frame, "A")
Adois = cria_label(line5_frame, "A")
Atres = cria_label(line5_frame, "A")
Aquatro = cria_label(line5_frame, "A")

correntenominalmaximatri = cria_label(line5_frame, "Corrente Nominal MAX Trifásica")
correntedemandadatri = cria_label(line5_frame, "Corrente Demandada")
correntedesbalanco = cria_label(line5_frame, "Corrente de Desbalanço")
correntemagnetizacao = cria_label(line5_frame, "Corrente de Magnetização")

Ienelabel = cria_label(line5_frame, "In")
Iene = cria_entry(line5_frame, width=200)

Idemlabel = cria_label(line5_frame, "Idem")
Idem = cria_entry(line5_frame, width=200)

Ideslabel = cria_label(line5_frame, "Ides")
Ides = cria_entry(line5_frame, width=200)

Imaglabel = cria_label(line5_frame, "Imag")
Imag = cria_entry(line5_frame, width=200)

correntenominalmaximatri.grid(row=1, column=5, columnspan=1, pady = (10, 15), padx = (0, 0))
Ienelabel.grid(row=2, column=4, padx = (50,0))
Iene.grid(row=2, column=5)
Aum.grid(row=2, column=5, padx = (230, 0))

correntedemandadatri.grid(row=3, column=5, columnspan=1, pady = (10, 15), padx = (0, 0))

Idemlabel.grid(row=4, column=4, padx = (50,0))
Idem.grid(row=4, column=5)
Adois.grid(row=4, column=5, padx = (230, 0))

correntedesbalanco.grid(row=5, column=5, columnspan=1, pady = (10, 15), padx = (0, 0))

Ideslabel.grid(row=6, column=4, padx = (50,0))
Ides.grid(row=6, column=5)
Atres.grid(row=6, column=5, padx = (230, 0))

correntemagnetizacao.grid(row=7, column=5, columnspan=1, pady = (10, 15), padx = (0, 0))

Imaglabel.grid(row=8, column=4, padx = (50,0))
Imag.grid(row=8, column=5)
Aquatro.grid(row=8, column=5, padx = (230, 0))


pontoansi = cria_label(line5_frame, "Ponto Ansi")

Ianstrafo1label = cria_label(line5_frame, "Ianstrafo1")
Ianstrafo1 = cria_entry(line5_frame, width=200)

Ianstrafo2label = cria_label(line5_frame, "Ianstrafo2")
Ianstrafo2 = cria_entry(line5_frame, width=200)

Ianstrafo3label = cria_label(line5_frame, "Ianstrafo3")
Ianstrafo3 = cria_entry(line5_frame, width=200)

Acinco = cria_label(line5_frame, "A")
Aseis = cria_label(line5_frame, "A")
Asete = cria_label(line5_frame, "A")
Aoito = cria_label(line5_frame, "A")

pontoansi.grid(row=9, column=5, columnspan=1, pady = (10, 15), padx = (0, 0))

Ianstrafo1label.grid(row=10, column=4, padx = (50,0))
Ianstrafo1.grid(row=10, column=5)
Acinco.grid(row=10, column=5, padx = (230, 0))

Ianstrafo2label.grid(row=11, column=4, padx = (50,0), pady = (10,0))
Ianstrafo2.grid(row=11, column=5)
Aseis.grid(row=11, column=5, padx = (230, 0))

Ianstrafo3label.grid(row=12, column=4, padx = (50,0), pady = (10,0))
Ianstrafo3.grid(row=12, column=5)
Asete.grid(row=12, column=5, padx = (230, 0))


# Frame linha oito #================================================================================================================================================================================
line8_frame = customtkinter.CTkFrame(frame)
line8_frame.pack(fill="x", pady=5, padx=0)

impedanciadotclabel = cria_label(line8_frame, "Impedância do TC")
impedanciadocabolabel = cria_label(line8_frame, "Impedância do Cabo")
impedanciadorelelabel = cria_label(line8_frame, "Impedância do Relé")
tensaosecundariadotclabel = cria_label(line8_frame, "Tensão Secundária do TC")
ztclabel = cria_label(line8_frame, "Ztc")
zcabolabel = cria_label(line8_frame, "Zcabo")
zrelelabel = cria_label(line8_frame, "ZRelé")
vslabel = cria_label(line8_frame, "VS")
vlabel = cria_label(line8_frame, "V")
OHMSlabelcinco = cria_label(line8_frame, "OHMS")
OHMSlabelseis = cria_label(line8_frame, "OHMS")
OHMSlabelsete = cria_label(line8_frame, "OHMS")

ztc = cria_entry(line8_frame, width=200)
zcabo = cria_entry(line8_frame, width=200)
zrele = cria_entry(line8_frame, width=200)
vs = cria_entry(line8_frame, width=200)

impedanciadotclabel.grid(row = 1, column = 1)
impedanciadorelelabel.grid(row = 5, column = 1)
ztclabel.grid(row = 2, column = 0, padx = (300,10), pady = 10)
ztc.grid(row = 2, column = 1)
OHMSlabelcinco.grid(row = 2, column = 2, padx = 10)
impedanciadocabolabel.grid(row = 3, column = 1)
zcabolabel.grid(row = 4, column = 0, padx = (300,10), pady = 10)
zcabo.grid(row = 4, column = 1)
OHMSlabelseis.grid(row = 4, column = 2, padx = 10)
zrelelabel.grid(row = 6, column = 0, padx = (300,10), pady = 10)
zrele.grid(row = 6, column = 1)
OHMSlabelsete.grid(row = 6, column = 2, padx = 10)
tensaosecundariadotclabel.grid(row = 3, column = 4)
vslabel.grid(row = 4, column = 3, padx = (100,10))
vs.grid(row = 4, column = 4)
vlabel.grid(row = 4, column = 5)

# Frame linha seis #================================================================================================================================================================================
line6_frame = customtkinter.CTkFrame(frame)
line6_frame.pack(fill="x", pady=5, padx=0)

Anove = cria_label(line6_frame, "A")
Adez = cria_label(line6_frame, "A")
Aonze = cria_label(line6_frame, "A")
Adoze = cria_label(line6_frame, "A")

especificacoesdotc = cria_label(line6_frame, "Especificações do TC")

calculodotclabel = cria_label(line6_frame, "Calculo do TC")
ienedois = cria_label(line6_frame, "In ")
calculodotc = cria_entry(line6_frame, width=200)

tclabel = cria_label(line6_frame, "TC")

tcprimariolabel = cria_label(line6_frame, "Primário")
tcprimario = cria_entry(line6_frame, width=200)
tcsecundariolabel = cria_label(line6_frame, "Secundário")
tcsecundario = cria_entry(line6_frame, width=200)

rtclabel = cria_label(line6_frame, "RTC")
rtc = cria_entry(line6_frame, width=200)

especificacoesdotc.grid(row = 0, column=3, columnspan=1, pady = 15)

calculodotclabel.grid(row = 2, column=1)
ienedois.grid(row = 3, column=0, padx = (313,0))
calculodotc.grid(row = 3, column=1, padx = (10,0))
Anove.grid(row = 3, column=2, padx = (10))

tcprimariolabel.grid(row = 4, column=1)
tcsecundariolabel.grid(row = 4, column=3)
tclabel.grid(row = 5, column=0, padx = (313, 0))
tcprimario.grid(row = 5, column=1)
Adez.grid(row = 5, column=2, padx = (10))
tcsecundario.grid(row = 5, column=3)
Aonze.grid(row = 5, column=4, padx = (10))

rtclabel.grid(row = 5, column=6, padx = 15)
rtc.grid(row = 5, column = 7)
Adoze.grid(row = 5, column = 8, padx = 15, pady=10)

# Frame linha nove #================================================================================================================================================================================
line9_frame = customtkinter.CTkFrame(frame)
line9_frame.pack(fill="x", pady=5, padx=0)

sensordefase = cria_label(line9_frame, "Sensor de Fase")
temporizadofaselabel = cria_label(line9_frame, "Temporizado")
instantaneofaselabel = cria_label(line9_frame, "Instantâneo")
temporizadofase = cria_entry(line9_frame, width=200)
instantaneofase = cria_entry(line9_frame, width=200)

sensordeneutro = cria_label(line9_frame, "Sensor de Neutro")
temporizadoneutrolabel = cria_label(line9_frame, "Temporizado")
instantaneoneutrolabel = cria_label(line9_frame, "Instantâneo")
temporizadoneutro = cria_entry(line9_frame, width=200)
instantaneoneutro = cria_entry(line9_frame, width=200)


sensordefase.grid(row = 0, column = 2)

temporizadofaselabel.grid(row = 1, column = 1, padx = (500, 30), pady = 5)
instantaneofaselabel.grid(row = 2, column = 1, padx = (500, 30), pady = 5)
temporizadoneutrolabel.grid(row = 4, column = 1, padx = (500, 30), pady = 5)
instantaneoneutrolabel.grid(row = 5, column = 1, padx = (500, 30), pady = 5)

temporizadofase.grid(row = 1, column = 2)
instantaneofase.grid(row = 2, column = 2)

sensordeneutro.grid(row = 3, column = 2)

temporizadoneutro.grid(row = 4, column = 2)
instantaneoneutro.grid(row = 5, column = 2)

# Frame linha dez #================================================================================================================================================================================
line10_frame = customtkinter.CTkFrame(frame)
line10_frame.pack(fill="x", pady=5, padx=0)

Atreze = cria_label(line10_frame, "A")
Aquatorze = cria_label(line10_frame, "A")
Aquinze = cria_label(line10_frame, "A")
Adezesseis = cria_label(line10_frame, "A")

mi = cria_label(line10_frame, "MI")
midois = cria_label(line10_frame, "MI")

definicoesdosreleseajusteslabel = cria_label(line10_frame, "Definições dos Relés e Ajustes")
reledesobrecorrentefaselabel = cria_label(line10_frame, "Relé de Sobrecorrente - Fase")
funcaolabel = cria_label(line10_frame, "Função")
fabricantelabel = cria_label(line10_frame, "Fabricante")
tipolabel = cria_label(line10_frame, "Tipo")
rtcdoislabel = cria_label(line10_frame, "RTC")
ajtemporizadolabel = cria_label(line10_frame, "Aj. Temporizado")
curvalabel = cria_label(line10_frame, "Curva")
ajinstantaneolabel = cria_label(line10_frame, "Aj. Instantâneo")
reledesobrecorrenteneutrolabel = cria_label(line10_frame, "Relé de Sobrecorrente - Neutro")
funcaodoislabel = cria_label(line10_frame, "Função")
fabricantedoislabel = cria_label(line10_frame, "Fabricante")
tipodoislabel = cria_label(line10_frame, "Tipo")
rtctreslabel = cria_label(line10_frame, "RTC")
ajtemporizadodoislabel = cria_label(line10_frame, "Aj. Temporizado")
curvadoislabel = cria_label(line10_frame, "Curva")
ajinstantaneodoislabel = cria_label(line10_frame, "Aj. Instantâneo")

funcao = cria_entry(line10_frame, width=200)
fabricante = cria_entry(line10_frame, width=200)
tipo = cria_entry(line10_frame, width=200)
rtcdois = cria_entry(line10_frame, width=200)
ajtemporizado = cria_entry(line10_frame, width=200)
curva = cria_entry(line10_frame, width=200)
ajinstantaneo = cria_entry(line10_frame, width=200)

funcaodois = cria_entry(line10_frame, width=200)
fabricantedois = cria_entry(line10_frame, width=200)
tipodois = cria_entry(line10_frame, width=200)
rtctres = cria_entry(line10_frame, width=200)
ajtemporizadodois = cria_entry(line10_frame, width=200)
curvadois = cria_entry(line10_frame, width=200)
ajinstantaneodois = cria_entry(line10_frame, width=200)


definicoesdosreleseajusteslabel.grid(row=1, column=1, sticky="w")
reledesobrecorrentefaselabel.grid(row=2, column=0, padx=(400, 0), sticky="w")
funcaolabel.grid(row=3, column=0, padx=(400, 0), pady=10, sticky="w")
funcao.grid(row=3, column=1)
fabricantelabel.grid(row=4, column=0, padx=(400, 0), pady=10, sticky="w")
fabricante.grid(row=4, column=1)
tipolabel.grid(row=5, column=0, padx=(400, 0), pady=10, sticky="w")
tipo.grid(row=5, column=1)
rtcdoislabel.grid(row=6, column=0, padx=(400, 0), pady=10, sticky="w")
rtcdois.grid(row=6, column=1)
ajtemporizadolabel.grid(row=7, column=0, padx=(400, 0), pady=10, sticky="w")
ajtemporizado.grid(row=7, column=1)
curvalabel.grid(row=8, column=0, padx=(400, 0), pady=10, sticky="w")
curva.grid(row=8, column=1)
ajinstantaneolabel.grid(row=9, column=0, padx=(400, 0), pady=10, sticky="w")
ajinstantaneo.grid(row=9, column=1)

reledesobrecorrenteneutrolabel.grid(row=10, column=0, padx=(400, 0), pady=(10, 0), sticky="w")
funcaodoislabel.grid(row=11, column=0, padx=(400, 0), pady=10, sticky="w")
funcaodois.grid(row=11, column=1)
fabricantedoislabel.grid(row=12, column=0, padx=(400, 0), pady=10, sticky="w")
fabricantedois.grid(row=12, column=1)
tipodoislabel.grid(row=13, column=0, padx=(400, 0), pady=10, sticky="w")
tipodois.grid(row=13, column=1)
rtctreslabel.grid(row=14, column=0, padx=(400, 0), pady=10, sticky="w")
rtctres.grid(row=14, column=1)
ajtemporizadodoislabel.grid(row=15, column=0, padx=(400, 0), pady=10, sticky="w")
ajtemporizadodois.grid(row=15, column=1)
curvadoislabel.grid(row=16, column=0, padx=(400, 0), pady=10, sticky="w")
curvadois.grid(row=16, column=1)
ajinstantaneodoislabel.grid(row=17, column=0, padx=(400, 0), pady=10, sticky="w")
ajinstantaneodois.grid(row=17, column=1)

Atreze.grid(row = 7, column=1, padx = (230, 0))
Aquatorze.grid(row = 9, column=1, padx = (230, 0))
Aquinze.grid(row = 17, column=1, padx = (230, 0))
Adezesseis.grid(row = 15, column=1, padx = (230, 0))
mi.grid(row = 8, column=1, padx = (230, 0))
midois.grid(row = 16, column=1, padx = (230, 0))



#Calculos ===================================================================================================================================================================================================
# Função para calcular a demanda e inserir no campo de demanda
def calcula():
    try:
        print("Iniciando cálculos...")
        
        # Corrente Tensão Demandada
        demandacavea = float(demandakva.get())
        tensaoprimariavalor = float(tensaoprimariaentry.get())
        fatordepotencia = float(fatordepotenciaentry.get())

        print(f"demandacavea: {demandacavea}, tensaoprimariavalor: {tensaoprimariavalor}, fatordepotencia: {fatordepotencia}")

        correntemediavalor = 0
        if fatordepotencia != 0:
            correntemediavalor = demandacavea / (math.sqrt(3) * tensaoprimariavalor)

        print(f"correntemediavalor: {correntemediavalor}")

        correntemedia.delete(0, customtkinter.END)
        correntemedia.insert(0, f"{correntemediavalor:.2f}")

        # Corrente Nominal do Trafo
        potenciadotrafovalor = float(transformadorescolhidoentry.get())
        correntenominaldotrafovalor = potenciadotrafovalor / (math.sqrt(3) * tensaoprimariavalor)

        print(f"potenciadotrafovalor: {potenciadotrafovalor}, correntenominaldotrafovalor: {correntenominaldotrafovalor}")

        correntenominaldotrafo.delete(0, customtkinter.END)
        correntenominaldotrafo.insert(0, f"{correntenominaldotrafovalor:.2f}")

        # Corrente nominal do Disjutor
        correntenominalzerodoisentry.delete(0, customtkinter.END)
        correntenominalzerodoisentry.insert(0, f"{correntenominaldotrafovalor:.2f}")
        correntenominalvalor = float(correntenominalzerodoisentry.get())
        idisjvalor = correntenominalvalor * 1.25

        print(f"correntenominalvalor: {correntenominalvalor}, idisjvalor: {idisjvalor}")

        correntenominaldodisjuntorzerodoisentry.delete(0, customtkinter.END)
        correntenominaldodisjuntorzerodoisentry.insert(0, f"{idisjvalor:.2f}")


        iccdisjvalor = float(icctrifasico.get())
        iccdisjform = iccdisjvalor * 1.25

        print(f"iccdisjvalor: {iccdisjvalor}, iccdisjform: {iccdisjform}")

        

        correntemaximadeinterrupcaodeccentry.delete(0, customtkinter.END)
        correntemaximadeinterrupcaodeccentry.insert(0, f"{iccdisjform:.2f}")



        # Chave Seccionadora Tripolar
        chaveseccionadoratripolarentry.delete(0, customtkinter.END)
        chaveseccionadoratripolarentry.insert(0, str("400"))

        # Escolha dos Elos fusíveis
        valordoelo = float(elofusivelentry.get())
        print(f"valordoelo: {valordoelo}")

        capacidadeelo = ""
        if valordoelo == 5:
            capacidadeelo = "0.5H"
        elif valordoelo == 10:
            capacidadeelo = "1H"
        elif valordoelo == 15:
            capacidadeelo = "1H"
        elif valordoelo == 25:
            capacidadeelo = "2H"
        elif valordoelo == 30:
            capacidadeelo = "2H"
        elif valordoelo == 37.5:
            capacidadeelo = "3H"
        elif valordoelo == 45:
            capacidadeelo = "3H"
        elif valordoelo == 75:
            capacidadeelo = "5H"
        elif valordoelo == 112.5:
            capacidadeelo = "6K"
        elif valordoelo == 150:
            capacidadeelo = "8K"
        elif valordoelo == 200:
            capacidadeelo = "10K"
        elif valordoelo == 225:
            capacidadeelo = "10K"
        elif valordoelo == 250:
            capacidadeelo = "12K"
        elif valordoelo == 300:
            capacidadeelo = "15K"
        elif valordoelo == 350:
            capacidadeelo = "15K"
        elif valordoelo == 400:
            capacidadeelo = "20K"
        elif valordoelo == 450:
            capacidadeelo = "20K"
        elif valordoelo == 500:
            capacidadeelo = "25K"
        elif valordoelo == 550:
            capacidadeelo = "25K"
        elif valordoelo == 600:
            capacidadeelo = "30K"
        elif valordoelo == 650:
            capacidadeelo = "30K"
        elif valordoelo == 700:
            capacidadeelo = "40K"
        elif valordoelo == 750:
            capacidadeelo = "40K"
        elif valordoelo == 800:
            capacidadeelo = "40K"
        else:
            capacidadeelo = "Valor inválido"

        print(f"capacidadeelo: {capacidadeelo}")

        capacidadedoeloentry.delete(0, customtkinter.END)
        capacidadedoeloentry.insert(0, capacidadeelo)

        # Escolha do Fusivel HH
        valordofusivelhh = float(fusivelhhentry.get())
        print(f"valordofusivelhh: {valordofusivelhh}")

        fusivelmaxmin = ""
        if valordofusivelhh == 30:
            fusivelmaxmin = "4"
        elif valordofusivelhh == 45:
            fusivelmaxmin = "4"
        elif valordofusivelhh == 75:
            fusivelmaxmin = "6 - 10"
        elif valordofusivelhh == 112.5:
            fusivelmaxmin = "8 - 16"
        elif valordofusivelhh == 150:
            fusivelmaxmin = "16 - 25"
        elif valordofusivelhh == 225:
            fusivelmaxmin = "2 - 32"
        elif valordofusivelhh == 300:
            fusivelmaxmin = "25 - 40"
        elif valordofusivelhh == 500:
            fusivelmaxmin = "40 - 63"
        elif valordofusivelhh == 750:
            fusivelmaxmin = "50 - 75"
        elif valordofusivelhh == 1000:
            fusivelmaxmin = "63 - 75"
        elif valordofusivelhh == 1250:
            fusivelmaxmin = "75 - 125"
        elif valordofusivelhh == 1500:
            fusivelmaxmin = "100 - 125"

        print(f"fusivelmaxmin: {fusivelmaxmin}")

        fusivelminimoemaximoentry.delete(0, customtkinter.END)
        fusivelminimoemaximoentry.insert(0, fusivelmaxmin)

        # Dimensionamento de Para Raios
        tensaonominalraioentry.delete(0, customtkinter.END)
        tensaonominalraioentry.insert(0, str(12))

        correntenominalraioentry.delete(0, customtkinter.END)
        correntenominalraioentry.insert(0, str(10))

        # Dimensionamento do Barramento de Cobre MT
        potenciadotrafovalor = (potenciatrafo.get())
        print(f"potenciadotrafovalor (barramento): {potenciadotrafovalor}")

        valorbarratubooco = 0
        valorvergalhao = 0
        valorvergalhaopol = ""

        if potenciadotrafovalor == 'P ≤ 500':
            valorbarratubooco = 20 
            valorvergalhao = 6.5
            valorvergalhaopol = '1/4"'
        elif potenciadotrafovalor == '500 < P ≤ 1500':
            valorbarratubooco = 30
            valorvergalhao = 8
            valorvergalhaopol = '5/16"'
        elif potenciadotrafovalor == '1500 < P ≤ 2000':
            valorbarratubooco = 40
            valorvergalhao = 8
            valorvergalhaopol = '3/8"'
        elif potenciadotrafovalor == '2000 < P ≤ 2500':
            valorbarratubooco = 60
            valorvergalhao = 9.5
            valorvergalhaopol = '5/8"'
        elif potenciadotrafovalor == '2500 < P ≤ 5000':
            valorbarratubooco = 100
            valorvergalhao = 15
            valorvergalhaopol = '5/8"'

        print(f"valorbarratubooco: {valorbarratubooco}, valorvergalhao: {valorvergalhao}, valorvergalhaopol: {valorvergalhaopol}")

        barraoutubooco.delete(0, customtkinter.END)
        barraoutubooco.insert(0, valorbarratubooco)
        
        vergalhaomm.delete(0, customtkinter.END)
        vergalhaomm.insert(0, valorvergalhao) 
        
        vergalhaopol.delete(0, customtkinter.END)
        vergalhaopol.insert(0, str(valorvergalhaopol))


        potenciadotrafovalor = float(cargainstaladakva.get())

        # Dimensionamento dos Condutores
        correntenominalzerosete.delete(0, customtkinter.END)
        correntenominalzerosete.insert(0, f"{correntenominaldotrafovalor:.2f}")
        
        valorcorrentenominal = float(correntenominalzerosete.get())
        valorfatorsobrecarga = float(fatordesobrecarga.get())

        print(f"valorcorrentenominal: {valorcorrentenominal}, valorfatorsobrecarga: {valorfatorsobrecarga}")

        valorcorrentecomsobrecarga = valorcorrentenominal * valorfatorsobrecarga

        print(f"valorcorrentecomsobrecarga: {valorcorrentecomsobrecarga}")
        
        correntecomsobrecarga.delete(0, customtkinter.END)
        correntecomsobrecarga.insert(0, f"{valorcorrentecomsobrecarga:.2f}")

        # Validação dos condutores
        # Metodo 01
        correntemaximadocircuito.delete(0, customtkinter.END)
        correntemaximadocircuito.insert(0, f"{valorcorrentecomsobrecarga:.2f}")


        valorfatordecorrecaoportemperatura = float(fatordecorrecaoportemperatura.get())
        valorfatordecorrecaoporresistividade = float(fatordecorrecaoporresistividade.get())
        valorfatordecorrecaoporagrupamento = float(fatordecorrecaoporagrupamento.get())
        capacidadedecorrentecorrigidavalor = float(capacidadedecorrentecorrigida.get())

        print(f"valorfatordecorrecaoportemperatura: {valorfatordecorrecaoportemperatura}, valorfatordecorrecaoporresistividade: {valorfatordecorrecaoporresistividade}")
        print(f"valorfatordecorrecaoporagrupamento: {valorfatordecorrecaoporagrupamento}")
        print(f"capacidadedecorrentecorrigidavalor: {capacidadedecorrentecorrigidavalor}")
       
        
        capacidadedecorrentecorrigidaresult = capacidadedecorrentecorrigidavalor * valorfatordecorrecaoporresistividade * valorfatordecorrecaoporagrupamento * valorfatordecorrecaoportemperatura
        

        capacidadedecorrentecorrigida.delete(0, customtkinter.END) 
        capacidadedecorrentecorrigida.insert(0, f"{capacidadedecorrentecorrigidaresult:.5f}")

        # Método 02
        icc3fvalor = float(icctrifasico.get())
        condutorvalor = condutor.get()
        if condutorvalor == 'Cobre':
            beta = 115.679
            alfa = 234
        else:
            beta = 48.686
            alfa = 228

        t1 = 90
        t2 = 250

        # Ajustando a fórmula de k
        k = beta * math.log((t2 + alfa) / (t1 + alfa))

        secaodocondutorvalor = float(secaodocondutorentry.get())

        # Assumindo que icc3fvalor está definido corretamente
        t = (k * secaodocondutorvalor / icc3fvalor)**2

        tempolimiteatuacao.delete(0, customtkinter.END)
        tempolimiteatuacao.insert(0, f"{t:.2f}")

        #Metodo 03

        i = correntenominaldotrafovalor
        l = float(distanciadaalimentacao.get())
        r1 = float(resistenciadosalimentadores.get())
        xlvalor = float(xl.get())
        fatordepotenciavalor = float(fatordepotenciaentry.get())
        cos = fatordepotenciavalor
        sen = (1 - (fatordepotenciavalor**2))
        fasesvalor = (quantasfases.get())
        
        if fasesvalor == 'Monofásico':
            quedadetensaovalor = (2*i*l / 1) * (r1 * cos + xlvalor * sen)
        elif fasesvalor == 'Bifásico':
            quedadetensaovalor = (2*i*l / 1) * (r1 * cos + xlvalor * sen)
        else:
            quedadetensaovalor = (math.sqrt(3)*i*l / 3) * (r1 * cos + xlvalor * sen)
        
        qt = (quedadetensaovalor/tensaoprimariavalor)*100

        quedadetensao.delete(0, customtkinter.END)
        quedadetensao.insert(0, f"{quedadetensaovalor:.2f}")

        # Calculos parte II
        # Impedanca do sistema da concessionaria
        icctrifasicovalor = float(icctrifasico.get())
        zccvalor = tensaoprimariavalor*1000 / (math.sqrt(3) * icctrifasicovalor)
        
        print(f"icctrifasicovalor: {icctrifasicovalor}, zccvalor: {zccvalor}")

        ZCCentry.delete(0, customtkinter.END)
        ZCCentry.insert(0, f"{zccvalor:.2}")

        # Corrente maxima tri
        potenciadotrafovalorzero = float(transformadorescolhidoentry.get())
        Ienevalor = potenciadotrafovalorzero / (math.sqrt(3) * tensaoprimariavalor)

        print(f"Ienevalor: {Ienevalor}") #{potenciadotrafovalor}

        Iene.delete(0, customtkinter.END)
        Iene.insert(0, f"{Ienevalor:.4}")
        
        # Corrente demandada Trifasica
        demandaKWAT = float(demandakw.get())
        correntedemandadatrifasicavalor = demandaKWAT / ((math.sqrt(3) * tensaoprimariavalor)  * fatordepotencia)

        print(f"correntedemandadatrifasicavalor: {correntedemandadatrifasicavalor}")

        Idem.delete(0, customtkinter.END)
        Idem.insert(0, f"{correntedemandadatrifasicavalor:.3}")
    
        # Corrente de desbalanco
        idesvalor = correntedemandadatrifasicavalor * 0.20

        print(f"idesvalor: {idesvalor}")

        Ides.delete(0, customtkinter.END)
        Ides.insert(0, f"{idesvalor:.3}")

        # Corrente de desmagnetizacao
        icc3fvalor = float(icctrifasico.get())
        imagvalor = 1 / ((1 / icc3fvalor) + (1.732 * tensaoprimariavalor) / (float(potenciadotrafovalor) * 10))
        
        imagarredon = float(imagvalor)

        print(f"icc3fvalor: {icc3fvalor}, imagarredon: {imagarredon}")

        Imag.delete(0, customtkinter.END)
        Imag.insert(0, f"{imagarredon:.5}")

        # Impedancia dos trafos
        zporcentovalor = float(zporcento.get())
        zt1 = ((float(1000*tensaoprimariavalor) ** 2) * float(zporcentovalor/100)) / float(potenciadotrafovalorzero)
        zt1float = float(zt1)

        print(f"zporcentovalor: {zporcentovalor}, zt1float: {zt1float:.3}")

        Ztrafo1entry.delete(0, customtkinter.END)
        Ztrafo1entry.insert(0, f"{zt1float:.3}")

        # Curto circuito no secundario dos transformadores
        icctrafo = potenciadotrafovalor / ((math.sqrt(3)) * (zccvalor + zt1float))

        print(f"icctrafo: {icctrafo}")

        Ztrafo1entrycc.delete(0, customtkinter.END)
        Ztrafo1entrycc.insert(0, f"{icctrafo:.2}")

        # Ponto ansi
        pontoansivalor1 = 58 / zporcentovalor * correntenominaldotrafovalor
        pontoansivalor1float = float(pontoansivalor1)

        print(f"pontoansivalor1float: {pontoansivalor1float}")

        Ianstrafo1.delete(0, customtkinter.END)
        Ianstrafo1.insert(0, f"{pontoansivalor1float:.5}")

        # Calculo do tc
        intc = icc3fvalor / 20
        intcfloat = float(intc)

        print(f"intcfloat: {intcfloat }")

        calculodotc.delete(0, customtkinter.END)
        calculodotc.insert(0, f"{intcfloat :.5}")

        # Calculo do RTC
        tcprimariovalor = float(tcprimario.get())
        tcsecundariovalor = float(tcsecundario.get())

        valordortc = tcprimariovalor / tcsecundariovalor
        valordotcfloat = float(valordortc)

        print(f"tcprimariovalor: {tcprimariovalor}, tcsecundariovalor: {tcsecundariovalor}, valordotcfloat: {valordotcfloat}")

        rtc.delete(0, customtkinter.END)
        rtc.insert(0, f"{valordortc:.5}")
        
        # Impedancia do tc
        zburdenvalor = float(zburdendotc.get())
        impedanciadotcvalor = 0.2 * zburdenvalor

        print(f"zburdenvalor: {zburdenvalor}, impedanciadotcvalor: {impedanciadotcvalor}")

        ztc.delete(0, customtkinter.END)
        ztc.insert(0, f"{impedanciadotcvalor:.2}")

        # Impedancia de cabo
        resistenciaunitariadocabovalor = float(resistenciaunitariadocabo.get())
        distenciaentrereleesetcsvalor = float(distenciaentrereleesetcs.get())

        zcabovalor = (resistenciaunitariadocabovalor*distenciaentrereleesetcsvalor) / 1000
        zcabovalorfloat = (zcabovalor)

        print(f"distenciaentrereleesetcsvalor: {distenciaentrereleesetcsvalor}, resistenciaunitariadocabovalor: {resistenciaunitariadocabovalor}")

        zcabo.delete(0, customtkinter.END)
        zcabo.insert(0, f"{zcabovalorfloat:.5}")

        # Impedancia do rele
        consumodorelevalor = float(consumodorele.get())

        impedanciadorelevalor = consumodorelevalor / (5 ** 2)
        impedanciadorelevalorfloat = float(impedanciadorelevalor)


        print(f"impedanciadorelevalorfloat: {impedanciadorelevalorfloat}")

        zrele.delete(0, customtkinter.END)
        zrele.insert(0, f"{impedanciadorelevalorfloat:.5}")

        # Tensão secundaria do ??
        veesse = icc3fvalor / valordortc * (impedanciadotcvalor + 2 * zcabovalor + impedanciadorelevalor)

        print(f"veesse: {veesse}")

        vs.delete(0, customtkinter.END)
        vs.insert(0, f"{veesse:.5}")

        # Sensor de fase
        temporizadovalorfase = (correntedemandadatrifasicavalor * 1.2) / valordortc

        print(f"temporizadovalorfase: {temporizadovalorfase}")

        temporizadofase.delete(0, customtkinter.END)
        temporizadofase.insert(0, f"{temporizadovalorfase:.2}")

        instantaneovalorfase = (1.1 * imagvalor) / valordortc

        print(f"instantaneovalorfase: {instantaneovalorfase}")

        instantaneofase.delete(0, customtkinter.END)
        instantaneofase.insert(0, f"{instantaneovalorfase:.2}")

        # Sensor de neutro
        temporizadovalorneutro = (idesvalor * 1.2) / valordortc

        print(f"temporizadovalorneutro: {temporizadovalorneutro}")

        temporizadoneutro.delete(0, customtkinter.END)
        temporizadoneutro.insert(0, f"{temporizadovalorneutro:.2}")

        iccft100 = float(iccterra100.get())
        
        instantaneovalorneutro = iccft100 / valordortc

        print(f"iccft100: {iccft100}, instantaneovalorneutro: {instantaneovalorneutro}")

        instantaneoneutro.delete(0, customtkinter.END)
        instantaneoneutro.insert(0, f"{instantaneovalorneutro:.2}")

        ajtemporizado.delete(0, customtkinter.END)
        ajinstantaneo.insert(0, instantaneovalorfase)

        ajinstantaneodois.delete(0, customtkinter.END)
        ajtemporizadodois.insert(0, f"{temporizadovalorneutro:.2}")

    except ValueError as e:
        print(f"Erro: {e}")

    app.after(1000, calcula)

# Iniciar a função de cálculo de demanda a cada 1 segundo
app.after(1000, calcula)
# Inicie o loop principal do tkinter
app.mainloop()
