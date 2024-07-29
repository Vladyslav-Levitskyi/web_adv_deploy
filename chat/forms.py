from django import forms
from .models import ChatMessage

class ChatForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['text']



#class MessageForm(forms.Form):
#    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your message...'}), label="", max_length=1000)