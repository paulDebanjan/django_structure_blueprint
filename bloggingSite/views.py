from django.shortcuts import render,redirect

def decision(request):
    if not request.user.is_authenticated:
        return redirect("authentication:login")
    if request.user.is_user:
        return redirect("user:news_feed")
    elif request.user.is_administrator:
        return redirect("administration:home")
    else:
        pass
    return render(request,'decision.html')

def document_print(request):
    
    return render(request,'document.html')

# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.template import Context
# from weasyprint import HTML


# def render_pdf(request):
#     # Get the template
#     template = get_template('document.html')
#     context = {}  # Add your context data here

#     # Render the template with the provided context
#     html_content = template.render(context)

#     # Generate PDF
#     pdf_file = HTML(string=html_content).write_pdf()

#     # Return PDF as response
#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; filename="your_file.pdf"'  # Inline display for printing
#     return response