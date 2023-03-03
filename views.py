import openai
from django.shortcuts import render
from django.http import JsonResponse

openai.api_key = "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"

def chat(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")

        response = openai.Completion.create(
            engine="davinci", prompt=user_input, max_tokens=1024, n=1, stop=None, temperature=0.5
        )

        chatbot_response = response.choices[0].text.strip()

        return JsonResponse({"user_input": user_input, "chatbot_response": chatbot_response})
    else:
        return render(request, "chat.html")
