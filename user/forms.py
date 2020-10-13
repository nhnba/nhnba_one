from django import forms

from user.models import User,Profile

#ModelForm是form的一种方法，可以djang方便直接获取model中的值的一种方法
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['nickname','gender','birthday','location']

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'

	def clean_max_distance(self):
		clean_data = super().clean()
		if clean_data['max_distance'] < clean_data['min_distance']:
			raise forms.ValidationError('最大距离必须大于最小距离')
		else:
			return clean_data['max_distance']

	def clean_max_dating_age(self):
		clean_data = super().clean()
		if clean_data['max_dating_age'] < clean_data['min_dating_age']:
			raise forms.ValidationError('最大年龄必须大于最小年龄')
		else:
			return clean_data['max_dating_age']