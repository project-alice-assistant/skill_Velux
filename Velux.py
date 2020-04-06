	from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class Velux(AliceSkill):
	"""
	Author: Psychokiller1888
	Description: Control your velux equipment with your voice! This requires a velux remote hack
	"""

	@IntentHandler('Velux_DoAction')
	def handleVelux(self, session: DialogSession, **_kwargs):
		room = session.slotValue(slotName='Room', defaultValue=session.siteId)
		action = session.slotValue(slotName='Action', defaultValue='open')
		device = session.slotValue(slotName='Device', defaultValue='windows')
		duration = session.slotValue(slotName='Duration', defaultValue=-1)
		percentage = session.slotValue(slotName='Percentage', defaultValue=100)

		self.publish(
			topic=f'projectalice/devices/{device}/{action}',
			payload = {
				'room'      : room,
				'duration'  : duration,
				'percentage': percentage
			}
		)
