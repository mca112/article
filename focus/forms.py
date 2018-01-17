from django import forms

class LoginForm(forms.Form):
	uid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'uid','placeholder':'Username'}))
	pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'pwd','placeholder':'Password'}))

class RegisterForm(forms.Form):
	username = forms.CharField(label='username',max_length=100,widget=forms.TextInput(attrs={'id':'username','class':'form-control'}))
	password1 = forms.CharField(label='pwd1',widget=forms.PasswordInput(attrs={'id':'pwd1','class':'form-control'}))
	password2 = forms.CharField(label='pwd2',widget=forms.PasswordInput(attrs={'id':'pwd2','class':'form-control'}))
class SetInfoForm(forms.Form):
	username = forms.CharField()

class CommentForm(forms.Form):
	comment = forms.CharField(label='',widget=forms.Textarea(attrs={'cols':'60','rows':'6'}))

class SearchForm(forms.Form):
	keyword = forms.CharField(widget=forms.TextInput)
	#'onblur':'authentication()'
	#Username = forms.CharField(label='username',max_length=100,
		#widget=forms.TextInput(attrs={'id':'username','class':'form-control'}))

