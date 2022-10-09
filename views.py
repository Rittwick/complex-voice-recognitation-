from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Example, PhrasalVerb 
import json, random

def add_verb(request):
    if request.method == 'POST':
        verb = request.POST.get('verb')
        verb = str(verb).strip()
        meaning = request.POST.get('meaning')
        meaning = str(meaning).strip()
        if(len(verb)>0 and len(meaning)>0):
            example_string = request.POST.get('example_string')
            examples = example_string.split('\n')
            verb_obj = PhrasalVerb.objects.get_or_create(verb=verb)[0]
            verb_obj.meaning = meaning 
            verb_obj.save() 
            for example in examples:
                Example.objects.create(verb=verb_obj, sentence=example)
            
            return JsonResponse({"verb":json.dumps(verb_obj)})
        else:
            return JsonResponse({"message": "Phrasal Verb and Meaning Must be provided"}, status=406)
    else:
        return HttpResponseNotAllowed() 

    # reading writing listening and speaking

def quiz(request):
    pks = [verb.pk for verb in PhrasalVerb.objects.all()]
    question_pk = random.choice(pks)
    question = PhrasalVerb.objects.get(pk=question_pk)
    return render(request, 'phrasalverb/quiz.html', {'question': question})

def toggle_bookmark(request, pk):
    if request.method == 'POST':
        verb = get_object_or_404(PhrasalVerb, pk=pk)
        verb.is_bookmarked = not verb.is_bookmarked 
        verb.save() 
        return JsonResponse({"status": str(verb.is_bookmarked)})
    return HttpResponseNotAllowed() 



