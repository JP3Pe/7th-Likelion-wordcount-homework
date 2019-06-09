'''
I import this module to render webpage
'''
from django.shortcuts import render

# Create your views here.

def home(request):
    '''
    return request and home.html
    '''
    return render(request, './home.html')

def about(request):
    '''
    return request to about.html
    '''
    return render(request, './about.html')

def count(request):
    '''
    get request(fulltext) from home.html as full_text
    return request and {fulltext: full_text} at ./count.html
    '''
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            #increasement
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, './count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})
