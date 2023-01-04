resolve_url

return redirect('{}#comment_{}'.format(resolve_url('pybo:detail',
                                                   question_id=commnet.question.id), comment.id))