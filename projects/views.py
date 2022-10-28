from django.shortcuts import render

# Create your views here.
projectList = [
    {
        "id": "1",
        "nombre": "valleapp",
        "descripcion": "Valle app PRO",
    },
    {
        "id": "2",
        "nombre": "direktu",
        "descripcion": "Direktu app PRO",
    },
    {
        "id": "3",
        "nombre": "Gestion Requerimientos",
        "descripcion": "Gestion Requerimientos PRO",
    }
]

def projects(request):
    msg = "All projects"
    number = 20
    context = {'msg': msg, 'number': number, 'projects': projectList}
    return render(request, "projects/projects.html", context)

def project(request, pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
    return render(request, "projects/single-project.html", projectObj)
