from twilio.rest import Client 
 
account_sid = 'idname' 
auth_token =  "token name"
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:sender number',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:receive number' 
                          ) 
 
print(message.sid)