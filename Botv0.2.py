import telebot
from telebot import types
import requests
import json
from datetime import datetime
from pytz import timezone 
from time import sleep  


class bot_blaze():
    ## CLASSE CONSTRUTORA ##
    def __init__(self,api,canal):
        self.results_counter()
        self.Stickers()
        self.layout2()
        self.variaveis()
        self.standards()
        print('''
INICIANDO BOT...
        ''')
        sleep(3)
        print('''
CONFIGURANDO BOT DO TELEGRAM...
        ''')
        self.api = api
        self.canal = canal
        self.bot = telebot.TeleBot(self.api)
        self.cad = types.InlineKeyboardButton(text='CADASTRE-SE🎁', url='blaze.com/r/PZYGj8')
        self.jogue = types.InlineKeyboardButton(text='APOSTE-AQUI💰', url='https://blaze.com/pt/games/double')
        self.keyboard1 = types.InlineKeyboardMarkup()
        self.keyboard2 = types.InlineKeyboardMarkup()
        self.keyboard1.add(self.cad)
        self.keyboard2.add(self.jogue)
        message_id = self.bot.send_message(self.canal, text='''
🧿 ATENTOS BOT CONFIGURADO
📡 INICIANDO ANALISES...''', reply_markup=self.keyboard1).message_id
        self.message_id = message_id
        print('''
MENSSAGEM DE CONFIGURAÇÃO ENVIADA COM SUCESSO!
        ''')
        sleep(3)
        print('''
MAIS ALGUNS AJUSTES...
CARREGANDO...
        ''')
        while True:
            try:
                self.sondar_resultado()
                self.status()
                self.minuto_atual()
            except:
                continue
                ## START BOT ##
            if self.momento == 'complete':
                self.lista_append()
                self.giro += 1
                self.ult_cor()
                self.ult_numero()
                print(f'BLAZE GIROU: {self.ult_cor()}/{self.ult_numero()}')
                self.cont_results_geral(self.ult_numero(), self.ult_cor())
                display = self.filter_display(self.minuto)
                if display:
                    if self.control_estatistica == 0:
                        self.control_estatistica += 1
                        self.ver_prompt()
                        self.sinal_porc_cores()
                    else:
                        self.control_estatistica = 0
                sleep(4.7)
                print('ANALYZING...')
                self.control_count(self.giro)
                self.filter_num(self.ult_numero())
            else:
                continue


## VARIAVEIS DOS STICKERS ##
    def Stickers(self):
        self.win_sem_gale = 'CAACAgEAAxkBAAEIc0FkK2xRcIPIkJOucJQNBYO6esTgkAACqQIAAlD_YEUTThBkC36q1i8E'
        self.win_no_gale = 'CAACAgEAAxkBAAPxZCy9tjkrxVp9GZXNEG6HoqYDa-sAAnADAAIN3mhFd6jeH-5QpYgvBA'
        self.Entrada_confirmada = 'CAACAgEAAx0CbiAYVAACDFJkGxVqJpY6MSg9udscVKG5zQrunwACCgADLnPHPuJiimLffwABui8E'
        self.perdeu = 'CAACAgEAAxkBAAEIcz9kK2vmdzZ3g5qJ8I3RaniGOprNiAACywMAAp-qWUWoGfMdyjLygS8E'
        self.em_analise = 'CAACAgEAAx0CbiAYVAACDFZkGxf2E5FkVGY2xzYr-JlPP2ckVwACDgADLnPHPvbAY0yXy1w9LwQ'
        self.atentos = 'CAACAgEAAxkBAAEIc0NkK2x7yuB1yZwYoNGWCj2uR5Uw6AACoQMAAiBUYEWuPV4yCZV9Wy8E'   


## METODOS DE LAYOUT ##            
    def layout(self):
        texto = 'BOT BLAZE DEV ALENCAR'
        tam = len(texto)
        print('=' * (tam + 2))
        print('')
        print(texto)
        print('')
        print('=' * (tam + 2))  


    def layout2(self):
        RED   = "\033[1;31m"  
        BLUE  = "\033[1;34m"
        CYAN  = "\033[1;36m"
        GREEN = "\033[0;32m"
        RESET = "\033[0;0m"
        BOLD    = "\033[;1m"
        REVERSE = """\033[;7m"""


        print("""
        ######################################################################################
        #                                                                                    #
        ######################################################################################
        #   #####      ####     ######     #####     #           ##      ######    ######    #
        #   #    #    #    #      #        #    #    #          #  #         #     #         #
        #   #####     #    #      #        #####     #         #####       #       ####      #
        #   #    #    #    #      #        #    #    #        #    #     #         #         #
        #   #####      ####       #        #####     #####   #     #     ######    ######    #
        #                                                                                    # 
        #       #    #    #    #    ##   ##    ######    #####      ####       #####         #
        #       ##   #    #    #    # # # #    #         #    #    #    #     #              #
        #       # #  #    #    #    #  #  #    #####     #####     #    #     ######         #
        #       #  # #    #    #    #  #  #    #         #  #      #    #          #         #
        #       #   ##     ####     #  #  #    ######    #   #      ####      #####          #
        #                                                                                    #
        ######################################################################################
                    

                                    VAMOS PARA AS ANALISES...
    """)


## VARIAVEIS ##
    def variaveis(self):
        self.lista_padroes = []
        self.taxa = 0
        self.alert = 0
        self.gale1 = 0
        self.gale2 = 0
        self.gale3 = 0
        self.giro = 0
        self.message_id = 0
        self.cont = 0
        self.cont_red = 0
        self.cont_black = 0
        self.cont_white = 0
        self.cont_num1 = 0
        self.cont_num2 = 0
        self.cont_num3 = 0
        self.cont_num4 = 0
        self.cont_num5 = 0
        self.cont_num6 = 0
        self.cont_num7 = 0
        self.cont_num8 = 0
        self.cont_num9 = 0
        self.cont_num10 = 0
        self.cont_num11 = 0
        self.cont_num12 = 0
        self.cont_num13 = 0
        self.cont_num14 = 0
        self.num1_back_white = 0
        self.num2_back_white = 0
        self.num3_back_white = 0
        self.num4_back_white = 0
        self.num5_back_white = 0
        self.num6_back_white = 0
        self.num7_back_white = 0
        self.num8_back_white = 0
        self.num9_back_white = 0
        self.num10_back_white = 0
        self.num11_back_white = 0
        self.num12_back_white = 0
        self.num13_back_white = 0
        self.num14_back_white = 0
        self.control_estatistica = 0
        self.total_rounds = 0


    def standards(self):
        self.p1 = ['🔴', '⚫', '⚪', '⚫', '🔴']
        self.p2 = ['🔴', '🔴', '🔴', '🔴', '🔴']
        self.p3 = ['⚫', '⚫', '⚫', '⚫', '⚫']
        self.p4 = ['🔴', '⚫', '🔴', '⚫', '🔴']
        self.p5 = ['⚫', '🔴', '⚫', '🔴', '⚫']
        self.p6 = ['🔴', '🔴', '⚫', '⚫', '🔴']
        self.p7 = ['⚫', '⚫', '🔴', '🔴', '⚫']


## MÉTODOS DE REQUISIÇÃO PARA API ##
    def sondar_resultado(self):
        self.roulette_current = 'https://blaze.com/api/roulette_games/current'
        response = requests.get(self.roulette_current)
        self.resposta = json.loads(response.content)


    def ult_numero(self):
        self.res_num = self.resposta['roll']
        return self.res_num
    

    def ult_cor(self):
        res_cor = self.resposta['color']
        if res_cor == 1:
            return '🔴'
        if res_cor == 2:
            return '⚫'
        if res_cor == 0:
            return '⚪'   
    

    def status(self):
        self.momento = self.resposta['status']


    def minuto_atual(self):
        fuso_horario = timezone('America/Fortaleza')
        atual = datetime.now(tz=fuso_horario)
        hora_minuto = atual.strftime('%M')
        self.minuto = int(hora_minuto)

    
    def hora_atual(self):
        fuso_horario = timezone('America/Fortaleza')
        atual = datetime.now(tz=fuso_horario)
        hora = atual.strftime('%H')
        self.hora = int(hora)
    

    def hora_string(self):
        fuso_horario = timezone('America/Fortaleza')
        atual = datetime.now(tz=fuso_horario)
        hora = atual.strftime('%H:%M:%S')
        return hora

       
    def minuto_sinal(self, num1, num2):
        numero_da_jogada = (num1 + num2) - 2
        if numero_da_jogada < 0:
            numero_da_jogada = 2
        if numero_da_jogada >= 0 and numero_da_jogada <= 2:
            numero_da_jogada == 2
        return numero_da_jogada


## FUNÇÕES PARA MANDAR OS SINAIS PARA O CANAL DO TELEGRAM ##
    def sinal_preto(self):
        message_id = self.bot.send_message(self.canal, text=f'''
ATENÇÃO📣📣
==============
💰JOGAR ⚫
APOS {self.ult_cor()} {self.ult_numero()} 
COBRIR COM ⚪
MAXIMO 3 GALE
============== 
        ''', reply_markup=self.keyboard2).message_id
        self.message_id = message_id
    

    def sinal_vermelho(self):
        message_id = self.bot.send_message(self.canal, text=f'''
ATENÇÃO📣📣
==============
💰JOGAR 🔴
APOS {self.ult_cor()} {self.ult_numero()}
COBRIR COM ⚪
MAXIMO 3 GALE
==============        
        ''', reply_markup=self.keyboard2).message_id
        self.message_id = message_id


    def sinal_cancelado(self):
        message_id = self.bot.send_message(self.canal, text='''
💢SINAL CANCELADO💢
PROBABILIDADE BAIXA
        ''', reply_markup=self.keyboard1).message_id
        self.message_id = message_id


    def sinal_gale1(self):
        message_id = self.bot.send_message(self.canal, text='''
===============
VAMOS AO GALE 1
"DOBRAR APOSTA"
===============
        ''').message_id
        self.message_id = message_id


    def sinal_gale2(self):
        message_id = self.bot.send_message(self.canal, text='''
===============
VAMOS AO GALE 2
"DOBRAR APOSTA"
===============
        ''').message_id
        self.message_id = message_id
    

    def sinal_gale3(self):
        message_id = self.bot.send_message(self.canal, text='''
===============
VAMOS AO GALE 3
"DOBRAR APOSTA"
===============
        ''').message_id
        self.message_id = message_id


    def win_direct(self):
        message_id = self.bot.send_sticker(self.canal, self.win_sem_gale).message_id
        self.message_id = message_id


    def win_gale(self):
        message_id = self.bot.send_sticker(self.canal, self.win_no_gale).message_id
        self.message_id = message_id
    

    def derrora(self):
        self.bot.send_sticker(self.canal, self.perdeu)


    def atencao(self):
        message_id = self.bot.send_sticker(self.canal, self.atentos, reply_markup=self.keyboard1).message_id
        self.message_id = message_id


    def sinal_result(self):
        message_id = self.bot.send_message(self.canal, text=f'''
➖➖➖➖➖➖➖➖➖➖➖
✳ RESULTADOS DAS ENTRADAS ✳
▪ TOTAL DE ENTRADAS = {self.total_rounds}
▪ TOTAL DE WINS = {self.total_wins}
▪ WINS CONSECUTIVOS = {self.consecutive_wins}
▪ WIN DE PRIMEIRA = {self.win_0}
▪ WIN GALE 1 = {self.win_gale_one}
▪ WIN GALE 2 = {self.win_gale_two}
▪ WIN GALE 3 = {self.win_gale_three}
▪ WIN NO BRANCO = {self.win_white}
▪ TOTAL DE LOSS = {self.Loss}
➖➖➖➖➖➖➖➖➖➖➖
▪ ACERTIVIDADE = {self.hit_hat()}%
▪ ACERTIVIDADE DE 1° =  {self.first_time_hit_hat()}%
➖➖➖➖➖➖➖➖➖➖➖
        ''', reply_markup=self.keyboard1).message_id
        self.message_id = message_id


    def delete_message(self):
        self.bot.delete_message(self.canal, self.message_id)


    def sinal_prompt(self):
        print(f'''
RESULTADOS DAS ENTRADAS
=========================
TOTAL DE ENTRADAS = {self.total_rounds}
TOTAL DE WINS = {self.total_wins}
WINS CONSECUTIVOS = {self.consecutive_wins}
WINS DE PRIMEIRA = {self.win_0}
WINS GALE 1 = {self.win_gale_one}
WINS GALE 2 = {self.win_gale_two}
WINS NO BRANCO = {self.win_white}
TOTAL DE LOSS = {self.Loss}
=========================
=========================
ACERTOS TOTAIS = {self.hit_hat()}%
ACERTOS DE PRIMEIRA = {self.first_time_hit_hat()}%
=========================
        ''')


    def sinal_estatisticas(self):
        print(f'''
# TOTAL DE RODADAS = {self.giro}
=================================================
# COR VERMELHA SAIU: {self.cont_red} VEZES
# COR PRETA SAIU: {self.cont_black} VEZES
# COR BRANCA SAIU: {self.cont_white} VEZES
=================================================
# PORCENTAGEM DE BRANCO ==> {self.hat_porcent(self.cont_white, self.giro)} %
# PORCENTAGEM DE VERMELHO ==> {self.hat_porcent(self.cont_red, self.giro)} %
# PORCENTAGEM DE PRETO ==> {self.hat_porcent(self.cont_black, self.giro)} %
=================================================
        ''')


    def ver_prompt(self):
        print(f'''
TOTAL DE RODADAS = {self.giro}
VERMELHO = {self.cont_red}
PRETO = {self.cont_black}
BRANCO = {self.cont_white}
% BRANCO = {self.hat_porcent(self.cont_white, self.giro)} %
% PRETO = {self.hat_porcent(self.cont_black, self.giro)} %
% VERMELHO = {self.hat_porcent(self.cont_red, self.giro)} %
        ''')


    def sinal_porc_cores(self):
        self.bot.send_message(self.canal, text=f'''
👨‍💻📈💹
RESULTADOS DA ULTIMA HORA
HORA: {self.hora_string()}
TOTAL DE RODADAS = {self.giro}
VERMELHO = {self.cont_red}
PRETO = {self.cont_black}
BRANCO = {self.cont_white}
% BRANCO = {self.hat_porcent(self.cont_white, self.giro)} %
% PRETO = {self.hat_porcent(self.cont_black, self.giro)} %
% VERMELHO = {self.hat_porcent(self.cont_red, self.giro)} %        
        ''')


    def sinal_numeros_antes(self):
        pass


## MÉTODOS DE ANALISE ##
    def cont_results_geral(self, num, cor):
        if cor == '⚪':
            ult_result = True
        else:
            ult_result = False
        if num == 0:
            self.cont_white += 1
            return
        if num == 1:
            self.cont_red += 1
            self.cont_num1 += 1
            if ult_result:
                self.num1_back_white += 1
        if num == 2:
            self.cont_red += 1
            self.cont_num2 += 1
            if ult_result:
                self.num2_back_white += 1
        if num == 3:
            self.cont_red += 1
            self.cont_num3 += 1
            if ult_result:
                self.num3_back_white += 1
        if num == 4:
            self.cont_red += 1
            self.cont_num4 += 1
            if ult_result:
                self.num4_back_white += 1
        if num == 5:
            self.cont_red += 1
            self.cont_num5 += 1
            if ult_result:
                self.num5_back_white += 1
        if num == 6:
            self.cont_red += 1
            self.cont_num6 += 1
            if ult_result:
                self.num6_back_white += 1
        if num == 7:
            self.cont_red += 1
            self.cont_num7 += 1
            if ult_result:
                self.num7_back_white += 1
        if num == 8:
            self.cont_black += 1
            self.cont_num8 += 1
            if ult_result:
                self.num8_back_white += 1
        if num == 9:
            self.cont_black += 1
            self.cont_num9 += 1
            if ult_result:
                self.num9_back_white += 1
        if num == 10:
            self.cont_black += 1
            self.cont_num10 += 1
            if ult_result:
                self.num10_back_white += 1
        if num == 11:
            self.cont_black += 1
            self.cont_num11 += 1
            if ult_result:
                self.num11_back_white += 1
        if num == 12:
            self.cont_black += 1
            self.cont_num12 += 1
            if ult_result:
                self.num12_back_white += 1
        if num == 13:
            self.cont_black += 1
            self.cont_num13 += 1
            if ult_result:
                self.num13_back_white += 1
        if num == 14:
            self.cont_black += 1
            self.cont_num14 += 1
            if ult_result:
                self.num14_back_white += 1
        return


    def num_estrategy(self, numero):
        while True:
            try:
                try:
                    self.sondar_resultado()
                    self.status()
                    self.minuto_atual()
                except:
                    break
                if self.momento == 'complete':
                    self.lista_append()
                    self.cont += 1
                    self.giro += 1
                    self.cont_results_geral(self.ult_numero(), self.ult_cor())
                    display = self.filter_display(self.minuto)
                    if display:
                        if self.control_estatistica == 0:
                            self.control_estatistica += 1
                            self.ver_prompt()
                            self.sinal_porc_cores()
                        else:
                            self.control_estatistica = 0
                    sleep(4.7)
                    if self.cont == self.alert:
                        self.delete_message()
                        self.atencao()
                    if self.cont == self.sinal:
                        VerSe = self.filter_sinal(numero)
                        if VerSe:
                            VerPadrao = self.filter_standard(numero)
                            if VerPadrao:
                                self.total_rounds += 1
                                self.delete_message()
                                self.filter_sinal_cor(numero)
                            else:
                                self.delete_message()
                                self.sinal_cancelado()
                                break
                        else:
                            self.delete_message()
                            self.sinal_cancelado()
                            break
                    if self.cont == self.control:
                        correcao = self.correct(numero)
                        if correcao:
                            print(f'''BLAZE GIROU ==> {self.ult_numero()} WIN!''')
                            self.filter_control(0)
                            self.win_direct()
                            self.reset()
                            break
                        else:
                            print(f'''BLAZE GIROU ==> {self.ult_numero()} GALE 1''')
                            self.sinal_gale1()
                            continue
                    if self.cont == self.gale1:
                        correcao = self.correct(numero)
                        if correcao:
                            print(f'''BLAZE GIROU ==> {self.ult_numero()} WIN GALE 1!''')
                            self.filter_control(1)
                            self.delete_message()
                            self.win_gale()
                            self.reset()
                            break
                        else:
                            print(f'''BLAZE GIROU {self.ult_numero()} GALE 2''')
                            self.delete_message()
                            self.sinal_gale2()
                            continue
                    if self.cont == self.gale2:
                        correcao = self.correct(numero)
                        if correcao:
                            print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 2!''')
                            self.filter_control(2)
                            self.delete_message()
                            self.win_gale()
                            self.reset()
                            break
                        else:
                            print(f'''BLAZE GIROU {self.ult_numero()} GALE 3!''')
                            self.delete_message()
                            self.sinal_gale3()
                            continue
                    if self.cont == self.gale3:
                        correcao = self.correct(numero)
                        if correcao:
                            print(f'''BLAZE GIROU {self.ult_numero()} WIN GALE 3!''')
                            self.filter_control(3)
                            self.delete_message()
                            self.win_gale()
                            self.reset()
                            break
                        else:
                            print(f'''BLAZE GIROU {self.ult_numero()} LOSS!''')
                            self.Loss += 1
                            self.consecutive_wins = 0
                            self.delete_message()
                            self.derrora()
                            self.reset()
                            break
                else:
                    continue
            except TimeoutError:
                break
        self.taxa = self.hit_hat()
        self.first_time_hit_hat()
        self.sinal_prompt()
        self.sinal_result()
        self.sinal_estatisticas()
        return


    def filter_num(self, num):
        if num == 3 or num == 4 or num == 5 or num == 6 or num == 7:
            self.cont = 0
            self.alert = num - 1
            self.sinal = num
            self.control = num + 1
            self.gale1 = num + 2
            self.gale2 = num + 3
            self.gale3 = num + 4
            self.num_estrategy(num)
            print("DOESN'T HAVE A STANDARD...")
        elif num == 8 or num == 9 or num == 10:
            self.cont = 0
            self.alert = num - 1
            self.sinal = num
            self.control = num + 1
            self.gale1 = num + 2
            self.gale2 = num + 3
            self.gale3 = num + 4
            self.num_estrategy(num)
        else:
            print("DOESN'T HAVE A STANDARD...")
            return


    def filter_sinal(self, num):
        if num >= 3 and num <= 7:
            if self.hat_porcent(self.cont_black, self.giro) <= 45 or self.hat_porcent(self.cont_red, self.giro) >= 48:
                return True
            else:
                return False
        elif num > 7 and num <= 10:
            if self.hat_porcent(self.cont_red, self.giro) <= 45 or self.hat_porcent(self.cont_black, self.giro) >= 48:
                return True
            else:
                return False


    def filter_standard(self, numero):
        if numero >= 3 and numero <= 7:
            if self.p2 == self.lista_padroes or self.p4 == self.lista_padroes or self.p6 == self.lista_padroes or self.p7 == self.lista_padroes:
                self.lista_padroes.clear()
                return False
            else:
                self.lista_padroes.clear()
                return True
        if numero >= 8 and numero <= 10:
            if self.p3 == self.lista_padroes or self.p5 == self.lista_padroes:
                self.lista_padroes.clear()
                return False
            else:
                self.lista_padroes.clear()
                return True


    def filter_sinal_cor(self, numero):
        if numero >= 3 and numero <= 7:
            self.sinal_preto()
            return
        if numero >= 8 and numero <= 10:
            self.sinal_vermelho()
            return


    def reset(self):
        self.control = 0
        self.alert = 0
        self.gale1 = 0
        self.gale2 = 0
        self.gale3 = 0
        self.message_id = 0
        self.cont = 0


    def correct(self, num):
        if num == 3 or num == 4 or num == 5 or num == 6 or num == 7:
            verfy = 'preto'
        if num == 8 or num == 9 or num == 10:
            verfy = 'vermelho'
        if verfy == 'preto':
            if self.ult_cor() == '⚫' or self.ult_cor() == '⚪':
                self.total_wins += 1
                return True
            else:
                return False
        if verfy == 'vermelho':
            if self.ult_cor() == '🔴' or self.ult_cor() == '⚪':
                self.total_wins += 1
                return True
            else:
                return False


    def filter_control(self, gale):
        self.consecutive_wins += 1
        if gale == 0:
            self.win_0 += 1
            if self.ult_cor() == '⚪':
                self.win_white += 1
            return
        elif gale == 1:
            self.win_gale_one += 1
            if self.ult_cor() == '⚪':
                self.win_white += 1
            return
        elif gale == 2:
            self.win_gale_two += 1
            if self.ult_cor() == '⚪':
                self.win_white += 1
            return
        else:
            self.win_gale_three += 1
            if self.ult_cor() == '⚪':
                self.win_white += 1
            return


    def lista_append(self):
        if len(self.lista_padroes) == 5:
            del self.lista_padroes[0]
            self.lista_padroes.append(self.ult_cor())
        else:
            self.lista_padroes.append(self.ult_cor())
        return


## CONTADORES DE RESULTADOS ##
    def hat_porcent(self, contador, giros):
        porc = (contador * 100) // giros
        return porc


    def hit_hat(self):
        if self.total_rounds >= 1:
            self.porcent = (self.total_wins * 100) // self.total_rounds
            return self.porcent
        else:
            self.porcent = 0
            return self.porcent


    def first_time_hit_hat(self):
        if self.total_rounds > 0:
            self.taxa = (self.win_0 * 100) // self.total_rounds
            return self.taxa
        else:
            self.taxa = 0
            return self.taxa


    def results_counter(self):
        self.consecutive_wins = 0
        self.total_rounds = 0
        self.Loss = 0
        self.win_0 = 0
        self.win_gale_one = 0
        self.win_gale_two = 0
        self.win_gale_three = 0
        self.max_count = 0
        self.win_white = 0
        self.total_wins = 0

    
    def control_count(self, count):
        if count == 2000:
            self.reset_count()
        return


    def reset_count(self):
        self.giro = 0
        self.cont_red = 0
        self.cont_black = 0
        self.cont_white = 0
        return

        
    def filter_display(self, minute):
        if minute == 0 or minute == 10 or minute == 20 or minute == 30 or minute == 40 or minute == 50:
            return True
        else:
            return False



token = input('DIGITE SEU TOKEN DO BOT: ')
chat_id = input('DIGITE SEU CHAT_ID: ')

bot_blaze(token, chat_id)