from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import time

driver = webdriver.Chrome()
# Inicia pelo navegador

loginUser = "" # EMAIL
loginPass = "" # SENHA

# VAIRIACES INICIAIS
mainArtist = "" # NOME O ARTISTA
nameAlbum = "" # INSERIR AQUI O NOME DO ALBUM

ano_direitos_autorais_P = "2023" # ANO DIREITO AUTORAÇ
texto_copyright_direitos_autorais_P = "Notlew Sons 2023 Todos os direitos reservados." # DESCRICAO DIREITO AUTORAL

array_nomes_musicas = [ # NOMES DAS SUAS MUSICAS
    "Cosmic Dreamscape Serenade",
    "Neon Nebula Echoes",
    "Mind Bending Kaleidoscope",
    "Psychedelic Whirlwind Voyage",
    "Ethereal Psyche Odyssey",
    "Galactic Mirage Harmonies",
    "Trippy Time Warp Fantasia",
    "Psychedelic Enchanted Reverie",
    "Celestial Harmonic Fusion",
    "Lunar Lullaby Mirage"
]

name_compositor = "WELTON RODRIGUES" # NOME COMPOSITOR
name_productor = "NOTLEW" # NOME PRODUTOR

# TRATATIVA DE PATH DA IMAGEM
file_path_relative = '../src/img/3000.png'
file_path_absolute = str(Path(file_path_relative).resolve())


driver.get('https://api.imusics.com/') # ABRE LINK IMUSIC

#                       AUTENTICA
search_email_box = driver.find_element(By.NAME, "email")
search_email_box.send_keys(loginUser)
search_pass_box = driver.find_element(By.NAME, "password")
search_pass_box.send_keys(loginPass)
search_pass_box.send_keys(Keys.RETURN)
time.sleep(3)
print("Fim criar Autenticação")

#                       CLICAR CRIAR ALBUM
search_create_album = driver.find_element(
    By.XPATH, "//*[@id=\"btn-dash-distribuir-album\"]")
search_create_album.send_keys(Keys.RETURN)
time.sleep(3)
print("Fim criar album")

#                       PREENCHE DADOS PRINCIPAIS
# 1 - SELECIONA O ARTISTA
select_main_artist = driver.find_element(
    By.XPATH, "//*[@id=\"basic-info\"]/div/div[1]/div[1]/div[1]/span/span[1]/span/ul/li/input")
select_main_artist.send_keys(mainArtist)
select_main_artist.send_keys(Keys.RETURN)
time.sleep(0.5)
print("Fim selecao de artista")

# 3 - SELECIONA DATA DE LANCAMENTO
campo_original = driver.find_element(By.ID,"release_date")
valor_min = campo_original.get_attribute("min")
data_convertida = datetime.strptime(valor_min, "%Y-%m-%d").strftime("%d-%m-%Y")


time.sleep(0.5)
print(data_convertida)
campo_destino = driver.find_element(By.ID,"release_date")
campo_destino.send_keys(data_convertida)

# 4 - SELECAO DE CAPA "IMAGEM"
select_image_cover = driver.find_element(By.ID, "launching_cover_file")
image_path = file_path_absolute
select_image_cover.send_keys(image_path)
time.sleep(0.5)

# 5 - INSERE NOME DO ALBUM
insert_name_album = driver.find_element(By.ID, "album_title")
insert_name_album.send_keys(nameAlbum)
time.sleep(0.5)
print("Fim insere nome album")

# 8 - DIREITOS AUTORAIS
insert_ano_copyright_P = driver.find_element(By.ID, "p_line_year")
insert_ano_copyright_P.send_keys(ano_direitos_autorais_P)
time.sleep(0.5)
insert_text_copyright_P = driver.find_element(By.ID, "p_line_text")
insert_text_copyright_P.send_keys(texto_copyright_direitos_autorais_P)
time.sleep(0.5)
print("Fim DIREITOS AUTORAIS")

# 9 - DIREITOS AUTORAIS
insert_ano_copyright_C = driver.find_element(By.ID, "c_line_year")
insert_ano_copyright_C.send_keys(ano_direitos_autorais_P)
time.sleep(0.5)
insert_text_copyright_C = driver.find_element(By.ID, "c_line_text")
insert_text_copyright_C.send_keys(texto_copyright_direitos_autorais_P)
time.sleep(0.5)
print("Fim  DIREITOS AUTORAIS")
#                      FIM PREENCHE DADOS PRINCIPAIS

# CLICA NO BOTAO CONTINUE
click_button_continue = driver.find_element(
    By.ID, "progress_wizard_button_next")
click_button_continue.send_keys(Keys.RETURN)


#                       PREENCHE SOBRE AS MUSICAS
for name in array_nomes_musicas :
    # 1 - NOME DA MUSICA
    insert_name_music = driver.find_element(By.ID, "track_title")
    insert_name_music.send_keys(name)
    time.sleep(0.5)

    # 5 - MUSICA AUTORAL
    select_yes_authoral = driver.find_element(By.ID, "input-authoral")
    driver.execute_script("arguments[0].click();", select_yes_authoral)

    # 7 - MAIN GENRE
    insert_main_genre = driver.find_element(By.ID, "primary_genre")
    select = Select(insert_main_genre)
    select.select_by_value("788")
    time.sleep(0.5)

    # 9 - NOME DO COMPOSITOR
    insert_compositor = driver.find_element(By.XPATH, "//*[@id=\"progress-product-img\"]/div/div[2]/div[2]/div/div/span/span[1]/span/ul/li/input")
    insert_compositor.send_keys(name_compositor)
    insert_compositor.send_keys(Keys.RETURN)
    time.sleep(0.5)

    # 10 - NOME DO PRODUTOR
    insert_productor = driver.find_element(By.XPATH, "//*[@id=\"progress-product-img\"]/div/div[2]/div[4]/div/div/span/span[1]/span/ul/li/input")
    insert_productor.send_keys(name_productor)
    insert_productor.send_keys(Keys.RETURN)
    time.sleep(0.5)

    # 8 - LANGUAGE MUSIC
    insert_main_genre = driver.find_element(By.ID, "language")
    select = Select(insert_main_genre)
    select.select_by_value("216")
    time.sleep(0.5)

    # CLICA NO BOTAO ADICIONAR NOVA MUSICA
    click_button_add_track = driver.find_element(
    By.ID, "btn-add-new-track").click()

# DELETA A MUSICA 11
click_button_delete_last_item = driver.find_element(By.XPATH, "//*[@id=\"album_track_guide\"]/div[11]/div/div[3]/i")
driver.execute_script("arguments[0].click();", click_button_delete_last_item)
print("exlcui a faixa 11")

# CLICA NO BOTAO CONTINUE
click_button_continue = driver.find_element(By.ID, "progress_wizard_button_next")
driver.execute_script("arguments[0].click();", click_button_continue)
print("cliquei no botao pra ir pra proxima etapa")

for i, name in enumerate(array_nomes_musicas) :
    print("inicio for upload musicas", i, name)
    time.sleep(0.5)

    insert_music = driver.find_element(By.XPATH, f"//*[@id=\"upload-track-{i}\"]")
    file_path_music_relative = f'../src/music/{name}.wav'
    file_path_music_absolute = str(Path(file_path_music_relative).resolve())
    insert_music.send_keys(file_path_music_absolute)
print("FINALIZEI UPLOAD MUSICAS")

# CLICA NO BOTAO CONTINUE
click_button_continue = driver.find_element(By.ID, "progress_wizard_button_next")
driver.execute_script("arguments[0].click();", click_button_continue)
print("cliquei no botao pra ir pra proxima etapa")

# ESPERA ARQUIVOS SEREM CARREGADOS
wait = WebDriverWait(driver, 10)  # Defina o tempo máximo de espera que você achar apropriado
while True:
    try:
        # Espere até que a classe "busy" esteja presente na página
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "busy")))
    except TimeoutException:
        # Se a classe "busy" não estiver mais presente, saia do loop
        break

print("FIM CARREGAMENTO DE ARQUIVOS")

time.sleep(1)

# CLICA NO BOTAO PUBLICAR
click_button_continue = driver.find_element(By.ID, "btn-submit")
driver.execute_script("arguments[0].click();", click_button_continue)
print("cliquei no botao pra ir pra finalizar")