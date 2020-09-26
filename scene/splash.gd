extends Spatial

signal splash_finished

func play_borf() -> void:
	$AnimationPlayer.play("borf")

func _on_AnimationPlayer_animation_finished(anim_name: String) -> void:
	if anim_name == "swoosh":
		emit_signal("splash_finished")
