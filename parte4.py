from gtts import  gTTS

# Cria um objeto gTTS com a resposta gerada pelo ChatGPT e a língua que será sintetizada em voz (variável "language").
gtts_object = gTTS(text=chatgpt_response, lang=language, slow=False)

# Salva o áudio da resposta no arquivo especificado (pasta padrão do Google Colab)
response_audio = "/content/response_audio.wav"
gtts_object.save(response_audio)

# Reproduz o áudio da resposta salvo no arquivo
display(Audio(response_audio, autoplay=True))
