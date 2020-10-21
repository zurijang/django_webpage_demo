import os
from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    def clean_file(self):
        file = self.cleaend_data.get('file', None)
        if file:
            extension = os.path.splitext(file.name)[-1].lower()
            if extension not in ('.mp4', '.avi'):
                raise forms.ValidationError['비디오 파일을 업로드해주세요.']
        return file

        
    class Meta:
        model = Video
        fields = [
            'title',
            'description',
            'file',
            'photo',
        ]