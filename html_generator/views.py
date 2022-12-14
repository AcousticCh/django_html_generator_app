from django.shortcuts import render
from .forms import MarkdownForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown

def markdown_form_view(request):
    if str(request.method).upper() == "POST":
        form = MarkdownForm(request.POST)
        context = { "form": form }
    
        if form.is_valid():
            form.save()
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            page = f"# {title}\n{body}"

            html = markdown.markdown(page)
            print(html)
            return HttpResponseRedirect(reverse("html_generator:html_gen"))


    else:
        form = MarkdownForm()
        context = { "form": form }
        return render(request, "index.html", context)