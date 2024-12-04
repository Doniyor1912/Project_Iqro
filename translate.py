from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from homepage.models import *


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', )


@register(Ideas)
class IdeasTranslationOptions(TranslationOptions):
    fields = ('name', 'role', 'content', )


@register(ProcessStep)
class ProcessStepTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', )