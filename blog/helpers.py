from django.core.files.storage import FileSystemStorage
from time import gmtime, strftime
from django.core.files.storage import FileSystemStorage

import magic
class Helpers():  
    def editPost(post, request):
        post.title = request.POST['title']
        post.description = request.POST['description']
        if request.FILES:
            post.img_path = Helpers.loadFile(request.FILES['file'])
        post.date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        post.owner_id = request.user.pk
        post.save()
    def loadFile(file):
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        img_path = 'img/' + filename
        return img_path

