import openai
from pydantic import BaseModel

openai.organization = 'org-12FUMX09MeUBB9qHHmTRzXa1'
openai.api_key = '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'


class Document(BaseModel):
    prompt: str = ''

    def inference(prompt: str) -> list:
        print('[PROCESANDO]'.center(40, '-'))
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            context="Estas en un aula de clases",
            messages=[
                {"role": "system", "content": """Eres un Calculador Factorial, cada número ingresado
                te calcula el factorial, y si es un texto presentas syntax error""",
                 },
                {"role": "user", "content": prompt}
            ]
        )
        content: object = completion.choices[0].message.content
    #USO DE TOKENS
        total_tokens = completion.usage.total_tokens
        print("Se han utilizado los siguientes tokens: " + total_tokens)
        print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
        return [content, total_tokens]
