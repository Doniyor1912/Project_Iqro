from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from about.models import *


@register(CompanyInfo)
class CompanyInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'mission_statement', )



@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('name', 'role', )
