const qrcode = require('qrcode');

const {
  default: makeWASocket,
  useMultiFileAuthState
} = require('@whiskeysockets/baileys');

const pino = require('pino');

async function connectToWhatsApp() {
  const {
    state,
    saveCreds
  } = await useMultiFileAuthState('baileys_auth_info');
  const socket = makeWASocket({
    logger: pino({
      level: 'silent'
    }),
    auth: state
  });

  socket.ev.on('connection.update', (update) => {
    const {
        connection,
        lastDisconnect,
        qr
    } = update;

    if (qr) {
        // Usa a biblioteca 'qrcode' para gerar uma representação em texto do código QR
        qrcode.toString(qr, {
        type: 'terminal',
        small: true
        }, (err, url) => {
        if (err) return console.log('Erro ao gerar o QR code:', err);
        console.log(url);
        });
    }

    if (connection === 'close') {
        // ... (lógica de reconexão)
    } else if (connection === 'open') {
        console.log('Conexão aberta!');

        // --- Adicione este código para testar o envio de mensagem ---
        const recipient = '5571999552509@s.whatsapp.net'; // Substitua pelo seu próprio número de WhatsApp com o formato correto
        const messageText = 'Olá! O programa está funcionando e enviou esta mensagem.';

        socket.sendMessage(recipient, {
            text: messageText
        }).then(() => {
            console.log(`Mensagem enviada para ${recipient}`);
        }).catch((err) => {
            console.error('Erro ao enviar a mensagem:', err);
        });
    }
    });


  socket.ev.on('creds.update', saveCreds);

  return socket;
}

connectToWhatsApp();
