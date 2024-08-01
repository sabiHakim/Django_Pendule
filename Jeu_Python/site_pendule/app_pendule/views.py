import os
import random

from django.shortcuts import render
from django.http import HttpResponse
from .models import Facile
from .models import Difficile
from django.conf import settings
def home(request):
    return render(request, 'app_pendule/home.html')
def process_form(request):
    essai_total = 5
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'essai' not in request.session:
        request.session['essai'] = essai_total

    count = request.session['count']
    essai = request.session['essai']
    if request.method == 'GET':
        niveau = request.GET.get('niveau')
        if niveau == 'Facile':
            chemin_fichier_facile = os.path.join(settings.BASE_DIR, 'app_pendule', 'static', 'faciles.txt')
            mots = Facile.process_file(chemin_fichier_facile, [])
            if 'mots' not in request.session:
                request.session['mots'] = mots
            motss =   request.session['mots']
            mot_a_deviner = random.choice(mots).strip()
            lettres_a_deviner = ['_' if lettre.isalpha() else ' ' for lettre in mot_a_deviner]
            lettres_a_deviner_str = ''.join(lettres_a_deviner)
            return render(request, 'app_pendule/facile.html', {
                'mot_a_deviner': lettres_a_deviner_str,
                'deviner': mot_a_deviner,
                'mot':motss,
                'essai':essai,
                'count':count
            })
    return render(request, 'app_pendule/facile.html')


def guess_letter(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'essai' not in request.session:
        request.session['essai'] = 3
    if 'mots' not in request.session:
        request.session['mots'] = []

    count = request.session['count']
    essai = request.session['essai']
    mots = request.session['mots']
    message_counter = ''
    nice =''
    if request.method == 'POST':
        letter = request.POST.get('letter').lower()
        deviner = request.POST.get('deviner')
        lettres_a_deviner = request.POST.get('lettres_a_deviner')

        if letter.isalpha() and len(letter) == 1:
            updated_lettres_a_deviner = list(lettres_a_deviner)
            if letter in deviner:
                for index, char in enumerate(deviner):
                    if char == letter:
                        updated_lettres_a_deviner[index] = letter
                if ''.join(updated_lettres_a_deviner) == deviner:
                    message_counter = 'Gagné!!!'
                    nice ='nice'
                    request.session.flush()
                else:
                    request.session['count'] = count
                    request.session['essai'] = essai
            else:
                count += 1
                essai -= 1
                if count == 5:
                    message_counter = 'Perdu!!!'
                    request.session.flush()
                else:
                    request.session['count'] = count
                    request.session['essai'] = essai

            updated_lettres_a_deviner_str = ''.join(updated_lettres_a_deviner)

            return render(request, 'app_pendule/facile.html', {
                'mot_a_deviner': updated_lettres_a_deviner_str,
                'deviner': deviner,
                'essai': essai,
                'count': count,
                'message_counter': message_counter,
                'mot': mots,
                'nice':nice
            })

    return redirect('home')
