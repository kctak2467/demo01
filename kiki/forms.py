from .models import Kiki
from django import forms
from django.core.validators import FileExtensionValidator
import os
VALID_EXTENSIONS = ['.csv']

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

class CSVUploadForm(forms.Form):

    file = forms.FileField(label='CSVファイル',
                           help_text='※拡張子csvのファイルをアップロードしてください。')
    # def clean_file(self):
    #     filenm = self.cleaned_data['file']
    #     extension = os.path.splitext(filenm.name)[1] # 拡張子を取得
    #     if not extension.lower() in VALID_EXTENSIONS:
    #         raise forms.ValidationError('csvファイルを選択してください！')

class ExcelUploadForm(forms.Form):

    file1 = forms.FileField(label='xlsxファイル')
    # file1 = forms.FileField(label='xlsxファイル',
    #                        help_text='※拡張子xlsxのファイルをアップロードしてください。',
    #                        validators=[FileExtensionValidator(allowed_extensions=['xlsx'])])

    # def clean_file(self):
    #     filenm = self.cleaned_data['file']
    #     extension = os.path.splitext(filenm.name)[1] # 拡張子を取得
    #     if not extension.lower() in VALID_EXTENSIONS:
    #         raise forms.ValidationError('csvファイルを選択してください！')
