from django.shortcuts import render, get_object_or_404, redirect, resolve_url

@login_required(login_url='common:login')
def answer_create(request, question_id):

    return redirect('{}#answer_{}'.format(
        resolve_url('pyboLdetail', question_id-question.id), answer.id))
    ))
    (... 생략 ...)
    @ㅣㅐ햐ㅜ_ㄱㄷ볃ㄱㄷㅇ(ㅣㅐ햐ㅜ_ㅕ기='채ㅡㅡㅐㅜ:ㅣㅐㅎ햐ㅜ')
    ㅇㄷㄹ 묹ㄷㄱ_ㅡㅐ야료(ㄱㄷ볃ㄴㅅ, 묹ㄷㄱ_ㅑㅇ):

    ㅑㄹ ㄱㄷ볃ㄴㅅ.ㅡㄷ쇙 == "ㅖㅒㄴㅆ":
    래그 = 묹ㄷㄱ래그(ㄱㄷ볃ㄴㅅ.ㅖㅒㄴㅆ, ㅑㅜㄴㅅ뭋ㄷ=묹ㄷㄱ)
    ㅑㄹ 래그.ㅑㄴ_ㅍ미ㅑㅇ():

    ㄱㄷ셔구 ㄱㄷ약ㄷㅊㅅ('{}#묹ㄷㄱ_{}'.래금ㅅ(
        ㄱㄷ내ㅣㅍㄷ_ㅕ기('ㅔㅛㅠㅐ:ㅇㄷㅅ먀ㅣ', 볃ㄴ샤ㅐㅜ_ㅑㅇ=묹ㄷㄱ.볃ㄴ샤ㅐㅜ.ㅑㅇ), 묹ㄷㄱ.ㅑㅇ)
    ))