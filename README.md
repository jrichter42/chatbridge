# chatbridge
Bridge for connecting chat groups across platforms

## Supported Platforms
* Discord
* Signal

## Setup
### Docker
```console
git clone https://github.com/jrichter42/chatbridge.git
cd chatbridge
docker compose up -d
docker compose build
```
### Other
You will need to host:
- signal-cli REST API (like https://github.com/bbernhard/signal-cli-rest-api)
- Python (3.8)
- chatbridge

## Todo
- [x] Project init
- [x] Discord Hello world
- [ ] Signal Hello world
- [ ] Docker Hello world
- [ ] Signal auth setup
- [ ] Receive & Send Messages
- [ ] Relay Messages
- [ ] Group & Single Contact support
- [ ] Bot Resume (catch up?)
- [ ] (Links?, Emojis?)
- [ ] Images
- [ ] Correct replies
- [ ] Sticker?
- [ ] Reactions?
- [ ] Attachments
- [ ] Additional Platforms? (Telegram, ~~WhatsApp~~)