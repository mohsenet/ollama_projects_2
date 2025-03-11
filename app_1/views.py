# views.py
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.shortcuts import render

from app_1.tests import save_object


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


@csrf_exempt  # Disable CSRF for simplicity (use proper CSRF handling in production)
def send_prompt(request):
    if request.method == 'POST':
        try:
            # Get the prompt from the request body
            data = json.loads(request.body)
            prompt = data.get('prompt')

            if not prompt:
                return JsonResponse({"error": "Prompt is required"}, status=400)

            # Prepare the data for the Ollama API
            ollama_url = "http://localhost:11434/api/generate"
            ollama_data = {
                "model": "deepseek-r1:1.5b",
                "prompt": prompt,
                "stream": False,
                # "max_tokens": 100,
                "temperature": 0.2
            }

            # Send the prompt to the Ollama service
            response = requests.post(ollama_url, json=ollama_data)
            # test
            # save_object('obj_1.pkl', 'save', response)  # save
            # response = save_object('obj_1.pkl', 'load')  # load

            # Check if the request to Ollama was successful
            if response.status_code == 200:
                # Return the response from Ollama to the client
                response2 = response.json()
                response_text = response2['response']

                # markdown_text = f"**Response:**\n\n{response_text}"

                return JsonResponse(response_text, safe=False)
            else:
                # Return an error message
                return JsonResponse({"error": "Failed to get response from Ollama", "status_code": response.status_code}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data in request body"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)