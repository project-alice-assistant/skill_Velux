from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class Velux(AliceSkill):
	"""
	Author: Psychokiller1888
	Description: Control your velux equipment with your voice! this requires a velux remote hack
	"""

	@IntentHandler('MyIntentName')
	def dummyIntent(self, session: DialogSession, **_kwargs):
		pass
