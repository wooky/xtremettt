extends Control

func _on_Splash_splash_finished() -> void:
	var title: Node = load("res://scene/title.tscn").instance()
	self.add_child(title)
	$Splash.play_borf()
