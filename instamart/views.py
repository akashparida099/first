from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Haldiram(request):
    return HttpResponse('''<h1>Haldiram Snacks</h1>
<h2>Haldiram Aloo Bhujia</h2>
<h2>Haldiram Punjabi Tadka</h2>
<h2>Haldiram Lite Mixture</h2>
<h2>Haldiram Moong Dal</h2>''')

def Bikaji(request):
    return HttpResponse('''<h1>Bikaji Mixture</h1>
<h2>Bikaji Bhelpuri Mix</h2>
<h2>Bikaji Coated Peanuts</h2>
<h2>Balaji Ratlami Sev</h2>
<h2>Balaji Chana Dal</h2>''')

def Namkeen(request):
    return HttpResponse('''<h1>Namkeen Snacks</h1>
<h2>Too Yumm Multigrain Mixture</h2>
<h2>Open Secret Baked Bhujia</h2>
<h2>Noice Aloo Ke Lacche</h2>
<h2>Let’s Try Kerala Garlic Mix</h2>
<h2>Let’s Try Crunchy Party Mix</h2>
<h2>Crax Roasted Chana Peanuts Mix</h2>''')