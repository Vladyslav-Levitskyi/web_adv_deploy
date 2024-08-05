# from django import forms
# from .models import ChatMessage

# class ChatForm(forms.ModelForm):
#    class Meta:
#        model = ChatMessage
#        fields = ['text']

#    def clean_text(self):
#        text = self.cleaned_data.get("text")
#        if not text:
#            raise forms.ValidationError("This field cannot be empty.")
#        return text

#class MessageForm(forms.Form):
#    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your message...'}), label="", max_length=1000)