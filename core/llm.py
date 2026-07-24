from langchain_groq import ChatGroq

def get_llm(temperature: float = 0.0):
    '''
        Cliente de GPT-OSS 20B en Groq.
        
        La API key se lee automaticamente de la variable de entorno GROQ_API_KEY, asi que la clave nunca
        aparece escrita en el código.
    '''
    
    return ChatGroq(model="openai/gpt-oss-20b", temperature=temperature)
    