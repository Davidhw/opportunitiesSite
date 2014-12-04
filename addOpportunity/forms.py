from addOpportunity import models
from django.forms import ModelForm
from django.forms import CharField
from django.forms import Textarea
class PostModelForm(ModelForm):
    class Meta:
        model = models.Posting
        exclude = ['date']
        description = CharField(widget=Textarea(attrs={'size': '4000','rows':5}))
        
def post_form_upload(request):
    if request.method == 'GET':
        form = PostModelForm()
    else:
        '''
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = PostModelForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['content']
            created_at = form.cleaned_data['created_at']
            post = m.Post.objects.create(content=content, created_at=created_at)
            return render(request, 'addOpportunity/post_form_upload.html', {
            '''
#            return HttpResponseRedirect(reverse('add/viewAdded'))
#            return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))
 
#    return render(request, 'addOpportunity/post_form_upload.html', {
    return render(request, 'addOpportunity/viewAdded', {
        'form': form,
    })
