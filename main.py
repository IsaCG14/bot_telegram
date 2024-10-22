from config import * #Importar todas las configuraciones
import telebot #usado para realizar operaciones en telegram
import threading

bot = telebot.TeleBot(TELEGRAM_TOKEN)

producto = {}

@bot.message_handler(commands=['start'])
def inicio(mensaje):
    bot.reply_to(mensaje, f'Hola {mensaje.from_user.first_name}, mira michele el bot que cree con telegram xd')
    print(mensaje.chat.id)

#Funcion que se encarga de responder el comando /new
@bot.message_handler(commands=['new'])
def nuevo(mensaje):
    producto[mensaje.chat.id] = {}
    msg = bot.send_message(TELEGRAM_CHAT_ID, '¿Cual es el nombre del producto?')
    bot.register_next_step_handler(msg, nuevo_producto_precio)

def nuevo_producto_precio(mensaje):
    producto[mensaje.chat.id]["Nombre"] = mensaje.text
    msg = bot.send_message(TELEGRAM_CHAT_ID, '¿Cual es el precio del producto?')
    bot.register_next_step_handler(msg, nuevo_producto_stock)

def nuevo_producto_stock(mensaje):
    producto[mensaje.chat.id]["Precio"] = mensaje.text
    msg = bot.send_message(TELEGRAM_CHAT_ID, '¿Cual es el stock del producto?')
    bot.register_next_step_handler(msg, nuevo_fin)

def nuevo_fin(mensaje):
    producto[mensaje.chat.id]["Stock"] = mensaje.text
    bot.send_message(TELEGRAM_CHAT_ID, 'Producto creado')


def inicioBot():
    bot.infinity_polling()

if __name__ == '__main__':
    print("Iniciando bot...")
    bot.send_message(TELEGRAM_CHAT_ID, "BOT INICIADO")

    hilo_inicio = threading.Thread(name="bot", target=inicioBot) #Crear el hilo inicial
    hilo_inicio.start() #Iniciar el hilo

    print("Bot inició")