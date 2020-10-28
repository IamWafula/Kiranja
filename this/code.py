import africastalking

username = "Kiranja"
api_key = "bdee8c92d02f69eead16821598fc13d6e4139ed39a51d6cf1febb0dc6870e0ba"

africastalking.initialize(username, api_key)

sms = africastalking.SMS

message = " Welcome to E-FIRM, we will keep you informed on the latest methods of farming "
message2 = "Growing strawberries with cassava will lead to added yield."
message3 = "There is market potential for strawberries in Nairobi going at 100 shillings per kilo."
    
sms.send(message, ["+13472336099"])
sms.send(message2, ["+13472336099"])
sms.send(message3, ["+13472336099"])