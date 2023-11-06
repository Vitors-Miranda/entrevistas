# Instale a biblioteca customtkinter para o estilo mais moderno
# pip install customtkinter
# pip install packaging

# Instale o  mysql-connector-python para banco de dados
# pip install mysql-connector-python

# instale o CTkMessagebox para notificaoes
# pip install CTkMessagebox

#App init
import customtkinter as ctk
from centerScreen import center_screen
from db import insert
from CTkMessagebox import CTkMessagebox

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

window_width = 1080
window_height = 720

app = ctk.CTk()  
app.resizable("false", "false")
app.geometry(f"{window_width }x{window_height}")

# centralizando a janela
center_screen(app, window_width, window_height)

#Salvar Info
def saveForm():
    if verification() == 1:
        insert(input_nome.get(), input_telefone.get(), input_email.get(), input_bio.get(), input_entrevista.get(), input_pratico.get(), input_teorico.get(), input_softSkills.get())
        clearForm()
        CTkMessagebox(title="Sucesso", message="Dados inseridos com sucessso.", icon="check")

    elif verification() == 2:
        CTkMessagebox(title="Erro", message="As notas da entrevista devem ser numéricas.", icon="cancel")

    else:
        CTkMessagebox(title="Erro", message="Preencha os dados do entrevistado.", icon="cancel")

#ClearForm
def clearForm():

    for campo in campos:
        campo.delete(0, 255)

# Verificação 
def verification():
    preenchido = 0
    cont = 0

    # Verificando se todos campos estão preenchidos
    for campo in campos:
        if campo.get() != "" :
            preenchido += 1
        cont += 1

    # Verificando se as notas são numéricas de fato
        if cont >= 5:
            try:
                float(campo.get())
            except:
                return 2

    if preenchido == 8:
        return 1

# MENU
frame_menu = ctk.CTkFrame(app)
frame_menu.grid(row=0, column=0, padx=20, pady=(20, 0))

txt_menu = ctk.CTkLabel(frame_menu, text= "Menu", font=("Helvetica", 15))
txt_menu.grid(row = 0, column = 0, pady = 15, padx = 10)

btn_cadastro = ctk.CTkButton(frame_menu, text="Cadastro")
btn_cadastro.grid(row = 2, column = 0, pady = 15, padx = 10)

btn_listagem = ctk.CTkButton(frame_menu, text="Listagem")
btn_listagem.grid(row = 3, column = 0, pady = 15, padx = 10)    

txt_autor = ctk.CTkLabel(frame_menu, text= "Vitor Miranda", font=("Helvetica", 15))
txt_autor.grid(row = 4, column = 0, pady=(450, 20), padx = 10)

# FORMULÁRIO DO ENTREVISTADO
frame_form = ctk.CTkFrame(app)
frame_form.grid(row=0, column=1, padx=10, pady=(10, 0))

txt_title1 = ctk.CTkLabel(frame_form, text= "Dados do entrevistado", font=("Helvetica", 15))
txt_title1.grid(row = 0, column = 1, pady = 15, padx = 0)

input_nome = ctk.CTkEntry(frame_form, placeholder_text="Nome", width=300)
input_nome.grid(row = 1, column = 1, pady = 15, padx = 20)

input_telefone = ctk.CTkEntry(frame_form, placeholder_text="Telefone", width=300)
input_telefone.grid(row = 2, column = 1, pady = 15, padx = 20)

input_email = ctk.CTkEntry(frame_form, placeholder_text="Email", width=300)
input_email.grid(row = 3, column = 1, pady = 15, padx = 20)

input_bio = ctk.CTkEntry(frame_form, placeholder_text="Minibio", width=300)
input_bio.grid(row = 4, column = 1, pady = 15, padx = 20)

# NOTAS DO ENTREVISTADO
txt_title2 = ctk.CTkLabel(frame_form, text= "Dados da entrevista", font=("Helvetica", 15))
txt_title2.grid(row = 0, column = 3, pady = 15, padx = 10)

input_entrevista = ctk.CTkEntry(frame_form, placeholder_text="Entrevista",  width=300)
input_entrevista.grid(row = 1, column = 3, pady = 15, padx = 20)

input_pratico = ctk.CTkEntry(frame_form, placeholder_text="Prático", width=300)
input_pratico.grid(row = 2, column = 3, pady = 15, padx = 20)

input_teorico = ctk.CTkEntry(frame_form, placeholder_text="Teórico", width=300)
input_teorico.grid(row = 3, column = 3, pady = 15, padx = 20)

input_softSkills = ctk.CTkEntry(frame_form, placeholder_text="Soft Skills", width=300)
input_softSkills.grid(row = 4, column = 3, pady = 15, padx = 20)

# campos
campos = (
    input_nome, 
    input_telefone,
    input_email,
    input_bio,
    input_entrevista,
    input_pratico,
    input_teorico,
    input_softSkills,
)

# SALVAR OS DADOS
btn_salvar = ctk.CTkButton(frame_form, text="Salvar", command=saveForm)
btn_salvar.grid(row = 5, column = 2, pady=(300, 20), padx = 10)


app.mainloop()