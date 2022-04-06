from django.shortcuts import render
import pdfplumber
# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        pdf = request.FILES.get("pdf")
        p = pdfplumber.open(pdf)
        st = ""
        for num, i in enumerate(p.pages, 1):
            st += "="*30 + "\n"
            st += f"{num} PAGE INFO\n"
            st += "="*30 + "\n"
            st += i.extract_text() + "\n\n"
        context.update({
            "st" : st
        })
            
    return render(request, "pdfread/index.html", context)