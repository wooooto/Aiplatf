from django.shortcuts import render

# Create your views here.
import os
import requests
from django.shortcuts import render
from django.http import JsonResponse


def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')

        if user_input:
            openai_api_key = os.environ.get('OPENAI_API_KEY')  # OpenAI API 키

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {openai_api_key}',
            }

            data = {
                'prompt': user_input,
                'max_tokens': 50,
            }

            response = requests.post(
                'https://api.openai.com/v1/engines/davinci-codex/completions',
                json=data,
                headers=headers
            )

            if response.status_code == 200:
                chat_response = response.json()['choices'][0]['text']
                return JsonResponse({'response': chat_response})
            else:
                return JsonResponse({'response': 'Error communicating with the chatbot.'})

    return render(request, 'chatbot.html')
