from allauth.account.forms import (
    SignupForm,
    LoginForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
    ChangePasswordForm,
    AddEmailForm,
    SetPasswordForm, 
)


#allauthのsignupフォーム上書き
class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

#allauthのログインフォーム上書き
class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #form-control
        self.fields['login'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['remember'].widget.attrs['class'] = 'checkbox'
        #placeholder
        self.fields['login'].widget.attrs['placeholder'] = ''
        self.fields['password'].widget.attrs['placeholder'] = ''
        self.fields['remember'].widget.attrs['placeholder'] = ''
        #label
        self.fields['login'].label = 'メールアドレス' #email入力用のfieldだが、allauthのfields名は'login'
        self.fields['password'].label = 'パスワード'
        self.fields['remember'].label = 'ログイン状態を維持する'

#allauthのパスワードリセットのメールフォーム上書き
class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

#allauthのnewパスワードフォーム上書き
class CustomResetPasswordKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

#allauthのパスワード変更フォーム上書き
class CustomChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

#allauthのメール設定フォーム上書き
class CustomAddEmailForm(AddEmailForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

#allauthのパスワード設定フォーム
class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'