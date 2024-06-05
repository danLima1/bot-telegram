from datetime import datetime, timedelta
import telebot
import time
from config import api_key, chat_id

# Chave de API do seu bot Telegram
# Caminho da imagem
image = '/home/jeane/Downloads/fortune.jpeg'
image_sort = '/home/jeane/Downloads/pix.jpeg'
image_iphone = '/home/jeane/Downloads/sorteio.jpg'

# Link do seu site, se aplicável
LINK_SITE = 'https://go.aff.donald.bet/spnpc6hv/'

# Inicialização do bot
bot = telebot.TeleBot(api_key)

# Função para enviar a mensagem do sorteio
def enviar_mensagem_sorteio():
    mensagem_sort = '''
SORTEIO RELÂMPAGO PARA OS 3 PRIMEIROS DEPÓSITOS! 🎉

🚀 Serão 3 Pix de R$250 cada!

Para participar é fácil:
1. Passo: Cadastro na plataforma
➡ CLICA NESSE LINK:
👉🏼

2. Passo:
➡ Clique na aba Depósito dentro da Plataforma
➡ Coloque o Valor Mínimo de R$50,00

👉🏼 Envie sua chave PIX no privado com o print do comprovante.
    '''

    bot.send_photo(chat_id=chat_id, photo=open(image_sort, 'rb'), caption=mensagem_sort, parse_mode='Markdown')

# Função para enviar a mensagem do sorteio de iPhone
def enviar_mensagem_sorteio_iphone():
    mensagem_iphone = f'''
VOCÊ QUER GANHAR UM IPHONE DE GRAÇA?

Veja a regra

➡ Você vai se CADASTRAR nessa plataforma de graça e vai
fazer o DEPÓSITO de qualquer valor acima de R$32,00.

➡ Vai ME MANDAR NO PRIVADO o print do COMPROVANTE.

E eu vou escolher aleatoriamente a pessoa que vai levar o
iPhone 😍

👉🏻 Link para se CADASTRAR na plataforma e fazer o depósito:
[CADASTRE-SE AQUI]({LINK_SITE})

👉🏻 Para mandar o COMPROVANTE é nesse número no privado

É SOMENTE ISSO PARA PARTICIPAR
    '''
    bot.send_photo(chat_id=chat_id, photo=open(image_iphone, 'rb'), caption=mensagem_iphone, parse_mode='Markdown')

# Função para enviar a mensagem de brecha identificada
def enviar_mensagem_brecha():
    agora = datetime.now()
    horario_base = agora.replace(minute=5, second=0, microsecond=0)
    horarios = [horario_base + timedelta(minutes=4 * i) for i in range(10)]
    horarios_formatados = "\n".join([f"✅🕘{horario.strftime('%H:%M')}" for horario in horarios])

    mensagem = f'''
✅ BRECHA IDENTIFICADA ✅

⏰ ATENÇÃO SESSÃO DAS {agora.strftime('%H:%M')}! HORÁRIO DE BRASÍLIA!

Funciona em quais jogos?
🐯TIGRE 🐂TOURO 🐇COELHO 🐲DRAGÃO

{horarios_formatados}

🎁 [CADASTRE-SE AQUI]({LINK_SITE}) 🎁

Horários enviados com base nos Históricos da Plataforma 📈
➖➖➖➖➖➖➖➖➖➖➖

🚨 PRÓXIMA SESSÃO EM 1 HORA ⏰

💸 Banca Recomendada R$25,00 💸
    '''

    bot.send_photo(chat_id=chat_id, photo=open(image, 'rb'), caption=mensagem, parse_mode='Markdown')

# Flags para garantir que as mensagens de sorteio e brecha sejam enviadas nos horários corretos
sorteio_enviado_14 = False
sorteio_enviado_18 = False
sorteio_iphone_enviado_9 = False
sorteio_iphone_enviado_18 = False
brecha_enviada_hora = {}

# Loop principal
while True:
    # Obter o horário atual
    now = datetime.now()
    hora = now.strftime('%H:%M:%S')
    print(hora)

    # Verificar se é 9:00h
    if now.hour == 9 and now.minute == 1 and not sorteio_iphone_enviado_9:
        # Enviar a mensagem do sorteio de iPhone
        enviar_mensagem_sorteio_iphone()
        sorteio_iphone_enviado_9 = True

    # Verificar se é 14:10h
    if now.hour == 12 and now.minute == 1 and not sorteio_enviado_14:
        # Enviar a mensagem do sorteio
        enviar_mensagem_sorteio()
        sorteio_enviado_14 = True

    # Verificar se é 18:00h
    if now.hour == 18 and now.minute == 1 and not sorteio_iphone_enviado_18:
        # Enviar a mensagem do sorteio de iPhone
        enviar_mensagem_sorteio_iphone()
        sorteio_iphone_enviado_18 = True

    # Verificar se é 18:10h
    if now.hour == 21 and now.minute == 1 and not sorteio_enviado_18:
        # Enviar a mensagem do sorteio
        enviar_mensagem_sorteio()
        sorteio_enviado_18 = True

    # Resetar as flags às 00:00h
    if now.hour == 0 and now.minute == 0:
        sorteio_enviado_14 = False
        sorteio_enviado_18 = False
        sorteio_iphone_enviado_9 = False
        sorteio_iphone_enviado_18 = False
        brecha_enviada_hora = {}

    # Verificar se é o início de uma nova hora para enviar a mensagem de brecha
    if now.minute == 0 and now.second == 0 and now.hour not in brecha_enviada_hora:
        enviar_mensagem_brecha()
        brecha_enviada_hora[now.hour] = True

    # Aguardar 1 segundo antes de verificar novamente
    time.sleep(1)
