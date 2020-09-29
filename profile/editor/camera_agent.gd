extends Button

signal captured(data)

func _ready() -> void:
	if not OS.has_feature("JavaScript"):
		self.disabled = true
		self.hint_tooltip = "Camera capture only available in web browser"

func _on_CameraAgent_pressed() -> void:
	$PollingDialog.popup_centered()
	JavaScript.eval("openCameraWindow()")
	$PollingTimer.start()

func _on_PollingDialog_popup_hide() -> void:
	JavaScript.eval("cancelCameraCapture()")

func _on_PollingTimer_timeout() -> void:
	if JavaScript.eval("isCameraCaptured()"):
		$PollingTimer.stop()
		var data = JavaScript.eval("captureData")
		if data != null: emit_signal("captured", data)
		$PollingDialog.hide()

func _process(_delta: float) -> void:
	if $PollingDialog.visible:
		$PollingDialog/Hourglass.rect_rotation += rand_range(5, 90)
