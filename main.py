from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modeloa
myChatBot.createModel()

#Giovana Ellero (RA: 22.220.003-2)
#Vagner Batazoli (RA: 22.217.022-7)


print("Bem vindo ao Chatbot sobre PIPE FAPESP !!!")

print("Olá seja bem-vindo você fala com o Bot PIPE.")
pergunta = input("Como posso te ajudar?")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")


while (intencao[0]['intent']!="despedida"):
    pergunta = input("Mais alguma duvida sobre o PIPE ?")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo.")
