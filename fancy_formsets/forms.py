from django.forms.models import BaseInlineFormSet
from fancy_formsets.helper import InlineFormHelper, InlineFormsetHelper
from django.template.loader import get_template
from django.template.context import Context
from django.utils.html import escape


class FancyBaseInlineFormSet(BaseInlineFormSet):
    helper = None
    empty_form = None

    def __init__(self, *args, **kwargs):
        if not self.helper:
            self.helper = InlineFormsetHelper()
        self.verbose_name = self.model._meta.verbose_name
        self.verbose_name_plural = self.model._meta.verbose_name_plural
        self.model_name = str(self.model._meta).split(".")[-1]
        super(FancyBaseInlineFormSet, self).__init__(*args, **kwargs)
        # Support get_form_kwargs in Django 1.9.
        if hasattr(self, 'get_form_kwargs') and callable(self.get_form_kwargs):
            form_kwargs = self.get_form_kwargs(None)
            self.empty_form = self._construct_form(9999999999999, **form_kwargs)
        else:
            self.empty_form = self._construct_form(9999999999999)
        for form in self.forms:
            if form in self.extra_forms:
                form.is_extra = True
            else:
                form.is_extra = False

    template = get_template("fancy_formsets_bootstrap/form.html")

    def render_empty_form(self):
        self.empty_form.helper = InlineFormHelper()
        return escape(self.template.render(Context({"form": self.empty_form})))
