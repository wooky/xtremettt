extends Control

signal transition(where)

func detrans() -> void:
	$AnimationPlayer.play("detrans")
	self.visible = true

func _prepare_to_transition(where: String) -> void:
	print(where)
	if ProfileManager.has_profiles():
		emit_signal("transition", where)
	else:
		$NoProfilesDialog.popup_centered()
