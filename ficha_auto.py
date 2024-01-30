#Importação do sync_playwright da biblioteca playwright
from playwright.sync_api import sync_playwright

#Importando a biblioteca time para visualizar a página melhor
import time

#Criando o navegador
with (sync_playwright() as p):
    navegador = p.chromium.launch(headless=False)

    #Criando uma nova página
    pagina = navegador.new_page()

    #Apontando para qual site o código deve ir
    pagina.goto("https://demo.automationtesting.in/Register.html")

    #Preenche o campo "First Name"
    pagina.fill('xpath=//*[@id="basicBootstrapForm"]/div[1]/div[1]/input', 'Teste')
    time.sleep(2)
    pagina.screenshot(path="print_first_name.png", full_page=True)

    #Preenche o campo "Last Name"
    pagina.fill('xpath=//*[@id="basicBootstrapForm"]/div[1]/div[2]/input', 'Playwright')
    time.sleep(2)
    pagina.screenshot(path="print_last_name.png", full_page=True)

    #Preenche o campo "Adress"
    pagina.fill('xpath=//*[@id="basicBootstrapForm"]/div[2]/div/textarea', 'Rua Teste Playwright, 123')
    time.sleep(2)
    pagina.screenshot(path="print_adress.png", full_page=True)

    #Preenche o campo "Email adress"
    pagina.fill('xpath=//*[@id="eid"]/input', 'testeplaywright@gmail.com')
    time.sleep(2)
    pagina.screenshot(path="print_email.png", full_page=True)

    #Preence o campo "Phone"
    pagina.fill('xpath=//*[@id="basicBootstrapForm"]/div[4]/div/input', '1234567890')
    time.sleep(2)
    pagina.screenshot(path="print_phone.png", full_page=True)

    #Seleciona a opção "Male" no campo "Gender"
    pagina.locator('xpath=//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input').click()
    time.sleep(2)
    pagina.screenshot(path="print_gender.png", full_page=True)

    #Seleciona a opção "Movies" do campo "Hobbies"
    pagina.locator('xpath=//*[@id="checkbox2"]').click()
    time.sleep(2)
    pagina.screenshot(path="print_hobbies.png", full_page=True)

    #Seleciona a linguagem "Portuguese" no campo "Languages"
    pagina.locator('xpath=//*[@id="msdd"]').click()
    pagina.wait_for_load_state("load")
    pagina.locator('xpath=//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[29]/a').click()
    pagina.mouse.click(300,300)
    time.sleep(2)
    pagina.screenshot(path="print_languages.png", full_page=True)

    #Seleciona "Python" no campo "Skills"
    pagina.query_selector('xpath=//*[@id="Skills"]').select_option(label='Python')
    time.sleep(2)
    pagina.screenshot(path="print_skills.png", full_page=True)

    #Seleciona select country
    pagina.query_selector('xpath=//*[@id="countries"]').select_option(label='Select Country')
    time.sleep(2)
    pagina.screenshot(path="print_select_country.png", full_page=True)

    #Seleciona "Japão" no campo "Select Country"
    pagina.query_selector('xpath=//*[@id="country"]').select_option(label='Japan')
    time.sleep(2)
    pagina.screenshot(path="print_country.png", full_page=True)

    #Seleciona o ano 2000 no dropdown year
    pagina.query_selector('xpath=//*[@id="yearbox"]').select_option(label='2000')
    time.sleep(2)
    pagina.screenshot(path="print_year.png", full_page=True)

    #Seleciona o mês Janeiro no dropdown month
    pagina.query_selector('xpath=//*[@id="basicBootstrapForm"]/div[11]/div[2]/select').select_option(label='January')
    time.sleep(2)
    pagina.screenshot(path="print_month.png", full_page=True)

    #Seleciona o dia 1 no dropdown day
    pagina.query_selector('xpath=//*[@id="daybox"]').select_option(label='1')
    time.sleep(2)
    pagina.screenshot(path="print_day.png", full_page=True)

    #Preenche o campo password
    pagina.fill('xpath=//*[@id="firstpassword"]', 'Senha')
    time.sleep(2)
    pagina.screenshot(path="print_password.png", full_page=True)

    #Confirma a senha
    pagina.fill('xpath=//*[@id="secondpassword"]', 'Senha')
    time.sleep(2)
    pagina.screenshot(path="print_password2.png", full_page=True)

    #Insere uma foto
    pagina.locator('xpath=//*[@id="imagesrc"]').set_input_files('thornicon.png')
    time.sleep(2)
    pagina.screenshot(path="print_images.png", full_page=True)

    #Clica no botão submit
    pagina.locator('xpath=//*[@id="submitbtn"]').click()
    pagina.screenshot(path="print_submit.png", full_page=True)

    #Sinalizando qual página o código deve direcionar
    pagina.goto("https://demo.automationtesting.in/FileUpload.html")

    #Faz os uploads das screenshots
    pagina.locator('id=input-4').set_input_files(['print_first_name.png', 'print_last_name.png',
    'print_adress.png', 'print_email.png', 'print_phone.png', 'print_gender.png', 'print_hobbies.png',
    'print_languages', 'print_skills.png', 'print_select_country.png', 'print_country.png', 'print_year.png',
    'print_month.png', 'print_day.png', 'print_password.png', 'print_password2.png', 'print_images.png', 'print_submit.png'])
    time.sleep(2)

    #Clica no botão para fazer upload
    pagina.locator('xpath=/html/body/section/div[1]/div/div/div[1]/button[3]/span').click()
    time.sleep(10)

    time.sleep(5)
