extends Control

var _submenu_control: Control

func _on_Title_transition(where: String) -> void:
	if self._submenu_control: self._submenu_control.visible = false
	self._submenu_control = $Mover/Submenu.get_node(where)
	self._submenu_control.visible = true
	$AnimationPlayer.play("mover")

func _return() -> void:
	$AnimationPlayer.play_backwards("mover")
