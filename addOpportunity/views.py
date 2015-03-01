from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from addOpportunity.models import Posting
from django.template import RequestContext
from django.forms.models import model_to_dict
from addOpportunity.forms import PostModelForm, PostFilter


def post_list(request):
    f = PostFilter(request.GET,queryset = Posting.objects.filter(visible=True).order_by('-date'))
    return render_to_response('addOpportunity/index.html', {'filter': f})

'''
class IndexView(generic.ListView):
    template_name = 'addOpportunity/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return published posts in reverse chronological order."""
        return Posting.objects.order_by('-date')
'''

class DetailView(generic.DetailView):
    model = Posting
    template_name = 'addOpportunity/detail.html'
    #p = PostModelForm(data=model_to_dict(Posting.objects.get(pk=self.pk)))
#    detail = DetailView.as_view()

class ResultsView(generic.DetailView):
    model = Posting
    template_name = 'addOpportunity/results.html'
    def detail(request, post_id):
        p = get_object_or_404(Posting, pk=post_id)
        return render_to_response('addOpportunity/detail.html', {'post': p},
                               context_instance=RequestContext(request))

def add(request, id):
    return HttpResponse("You've added opportunity %s." % id)
'''
def add(request):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
'''

#http://pydanny.com/the-easy-form-views-pattern-controversy.html 
def add(request):
    if request.method == 'GET':
        form = PostModelForm()
    else:
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/viewAdded')

    return render(request, 'addOpportunity/post_form_upload.html', {
        'form': form,
        })
