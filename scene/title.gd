extends Control

signal transition(where)

func detrans() -> void:
	$AnimationPlayer.play("detrans")
	self.visible = true

func _on_SinglePlayer_pressed() -> void:
	_prepare_to_transition("")

func _on_Multiplayer_pressed() -> void:
	_prepare_to_transition("")

func _prepare_to_transition(where: String) -> void:
	if ProfileManager.has_profiles():
		emit_signal("transition", where)
	else:
		$NoProfilesDialog.popup_centered()

func _on_Profiles_pressed() -> void:
	emit_signal("transition", "ProfileEditor")
