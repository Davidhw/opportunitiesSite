from django.db import models
from datetime import datetime
from django.forms import ModelForm

class Posting(models.Model):
    def __unicode__(self):
        return self.name + " at "+ self.organization
    # choices pattern from https://docs.djangoproject.com/en/dev/ref/models/fields/
    VOLUNTEER = "V"
    INTERNSHIP = "I"
    JOB = "J"
    TYPE_CHOICES = ( 
        (JOB,'Job'),
        (INTERNSHIP,'Internship'),
        (VOLUNTEER,'Volunteering Opportunity'),
        )
    
    UNPAID = "u"
    STIPEND = "s"
    HOURLY = "h"
    YEARLY = "y"
    PAYMENT_TYPE_CHOICES = ( 
        (UNPAID,"unpaid"),
        (STIPEND,"stipend"),
        (HOURLY,'hourly'),
        (YEARLY,'yearly'),
        )

    position_Type = models.CharField(max_length=1, choices = TYPE_CHOICES, default = JOB)
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
#    isPaid = models.BooleanField()
    salary = models.PositiveIntegerField(default = 0)
    payment_Type = models.CharField(max_length=1, choices = PAYMENT_TYPE_CHOICES, default = UNPAID)

    email = models.CharField(max_length=100)
    key_Words = models.CharField(max_length=100)
    phone = models.CharField(max_length= 12)
    date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(max_length=500)
    hiring_Criteria = models.TextField(max_length=500)
    visible = models.BooleanField(default = False)

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

