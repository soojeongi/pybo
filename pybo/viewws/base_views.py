from django.db.models import Q, Count

kw= request.GET.get('kw','')
so = request.GET.get('so', 'recent')

#정렬
if so == 'recommend':
    question_list = Question.objects.annotate(
        num_voter=Count('voter')).order_by('-num_voter', '-create_date')
if so == 'popular':
    question_list = Question.objects.annotate(
        num_answer=Count('answer')).order_by('-num_answer', '-create_date')
else:  #recent
    question_list = Question.objects.order_by('-create_Date')

if kw:
    question_list = question_list.filter(
        Q(subject__icontains=kw) |
        Q(content__icontains=kw) |
        Q(author__username__icontains=kw) |
        Q(answer__author__username__icontains=kw)
    ).distinct()