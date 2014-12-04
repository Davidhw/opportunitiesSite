from django.db import models
from datetime import datetime
from django.forms import ModelForm

class Posting(models.Model):
    # choices pattern from https://docs.djangoproject.com/en/dev/ref/models/fields/
    VOLUNTEER = "V"
    INTERNSHIP = "I"
    JOB = "J"
    TYPE_CHOICES = ( 
        (JOB,'Job'),
        (INTERNSHIP,'Internship'),
        (VOLUNTEER,'Volunteering Opportunity'),
        )
    positionType = models.CharField(max_length=1, choices = TYPE_CHOICES, default = JOB)
    title = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    keyWords = models.CharField(max_length=100)
    phone = models.CharField(max_length= 12)
    date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(max_length=500)
    hiringCriteria = models.TextField(max_length=500)


def post_form_upload(request):
    print "in post form upload!"
    if request.method == 'GET':
        form = PostModelForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = PostModelForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['content']
            created_at = form.cleaned_data['created_at']
            post = m.Post.objects.create(content=content, created_at=created_at)
            return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))
 
#    return render(request, 'addOpportunity/post_form_upload.html', {
    return render(request, 'addOpportunity/add', {
        'form': form,
        })

