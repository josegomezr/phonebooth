import types
from django.forms.widgets import Input, Select
from django.forms.utils import ErrorDict as BaseErrorDict, ErrorList as BaseErrorList
from django.utils.html import format_html, html_safe, format_html_join


def _get_feedback_class(self, form, key='controls'):
    if self.errors or '__all__' in form.errors:
        return form.css_classes['feedback_status'][key]['invalid']

    if form.is_bound:
        return form.css_classes['feedback_status'][key]['valid']

    return ''

class BootstrapifyMixin:
    css_classes = {
        'controls': {
            'select': 'form-control',
            'input': 'form-control',
        },
        'feedback_status': {
            'controls': {
                'valid': 'is-valid',
                'invalid': 'is-invalid',
            },
        },
        'errors': {
            'list': 'alert alert-danger',
            'field_feedback': 'invalid-feedback',
        }
    }

    def full_clean(self):
        """
        Clean all of self.data and populate self._errors and self.cleaned_data.
        """
        self._errors = MyOwnErrorDict()

        if not self.is_bound:  # Stop further processing.
            return
        self.cleaned_data = {}
        # If the form is permitted to be empty, and none of the form data has
        # changed from the initial data, short circuit any validation.
        if self.empty_permitted and not self.has_changed():
            return

        self._clean_fields()
        self._clean_form()
        self._post_clean()


    def _bootstrapify_form(self):
        for bf in self:
            self._bootstrapify_boundfield(bf)

    def _bootstrapify_boundfield(self, bf):
        def wrap(bf):
            oldfn = bf.as_widget

            def inner(self):
                if isinstance(self.field.widget, Input):
                    key = 'input'
                elif isinstance(self.field.widget, Select):
                    key = 'select'
                else:
                    raise NotImplementedError(f"Not implemented yet: {self.field.widget.__class__}")

                klasses = self.field.widget.attrs.get('class', '').split(' ')
                target_css_class = self.form.css_classes['controls'][key]

                if target_css_class not in klasses:
                    klasses = [target_css_class] + klasses

                klasses += [_get_feedback_class(self, self.form)]
                self.field.widget.attrs['class'] = ' '.join(klasses)

                return oldfn()
            return inner

        bf.as_widget  = types.MethodType(wrap(bf), bf)
        return


    def __init__(self, *args, **kwargs):
        kwargs['error_class'] = MyOwnErrorList
        super().__init__(*args, **kwargs)

        self._bootstrapify_form()


@html_safe
class MyOwnErrorList(BaseErrorList):
    def __str__(self):
        return self.as_bootstrap()

    def as_bootstrap(self):
        return format_html(
            '<ul class="{}">{}</ul>',
            self.error_class,
            format_html_join('', '<li>{}</li>', ((e,) for e in self))
        )


@html_safe
class MyOwnErrorDict(BaseErrorDict):
    def __str__(self):
        return self.as_bootstrap()

    def as_bootstrap(self):
        res = ''
        for k, v in sorted(self.items(), key=lambda x: x[0]):
            if k == '__all__':
                res += format_html('<strong>{}</strong>', v)
            else:
                res += format_html('<li><strong>{}</strong>: {}</li>', k.capitalize(), v)

        return format_html(
            f'<div class="alert alert-danger" role="alert"><ul class="errorlist">{res}</ul></div>'
        )





