# chatbridge by jrichter

import logging

import bridge

logger = logging.getLogger('chatbridge')

"""
class SignalMessage(Message):
    def __init__(self, id, sender, target, content, attachment, reactions):
        super().__init__(id, sender, target, content, attachment, reactions)
"""

class SignalBot:
    def __init__(self, signalRestApiURL):
        self.apiUrl = signalRestApiURL

    def run(self):
        pass

    def sendRequest(self):
        pass#"curl -X POST -H "Content-Type: application/json" --data '{"use_voice": true}' 'http://127.0.0.1:8080/v1/register/<number>'"


    """
Register a number (with voice verification)
curl -X POST -H "Content-Type: application/json" --data '{"use_voice": true}' 'http://127.0.0.1:8080/v1/register/<number>'

Verify the number using the code received via SMS/voice
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8080/v1/register/<number>/verify/<verification code>'

Send a message to multiple recipients
curl -X POST -H "Content-Type: application/json" -d '{"message": "<message>", "number": "<number>", "recipients": ["<recipient1>", "<recipient2>"]}' 'http://127.0.0.1:8080/v2/send'

Send a message (+ base64 encoded attachment) to multiple recipients
curl -X POST -H "Content-Type: application/json" -d '{"message": "<message>", "base64_attachments": ["<base64 encoded attachment>"], "number": "<number>", "recipients": ["<recipient1>", "<recipient2>"]}' 'http://127.0.0.1:8080/v2/send'

Send a message to a group
The group id can be obtained via the "List groups" REST call.

curl -X POST -H "Content-Type: application/json" -d '{"message": "<message>", "number": "<number>", "recipients": ["<group id>"]}' 'http://127.0.0.1:8080/v2/send'
e.g: curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello World!", "number": "+431212131491291", "recipients": ["group.ckRzaEd4VmRzNnJaASAEsasa", "+4912812812121"]}' 'http://127.0.0.1:8080/v2/send'

Receive messages

Fetch all new messages in the inbox of the specified number.

curl -X GET -H "Content-Type: application/json" 'http://127.0.0.1:8080/v1/receive/<number>'



Link a device

curl -X GET -H "Content-Type: application/json" 'http://127.0.0.1:8080/v1/qrcodelink?device_name=<device name>'
e.g: curl -X GET -H "Content-Type: application/json" 'http://127.0.0.1:8080/v1/qrcodelink?device_name=HomeAssistant'

This provides a QR-Code image. In case of an error a JSON object will be returned.
Due to security reason of Signal, the provided QR-Code will change with each request.


The following REST API endpoints are deprecated and no longer maintained!
/v1/send
    """