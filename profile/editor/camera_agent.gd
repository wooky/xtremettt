extends Button

func _on_CameraAgent_pressed() -> void:
	JavaScript.eval("openCameraWindow()")
