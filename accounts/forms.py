from django.contrib.auth.forms import UserCreationForm
# TODO: このフォームの存在意義がない可能性出てくるため、不要な場合は削除する


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')
