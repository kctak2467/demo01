from .models import kiki
from django import forms

class SearchForm(forms.Form):

    kiki_id = forms.CharField(
        initial='',
        label='機器ID',
        required = False, # 必須ではない
    )

    kiki_name = forms.CharField(
        initial='',
        label='機器名称',
        required=False,  # 必須ではない
    )