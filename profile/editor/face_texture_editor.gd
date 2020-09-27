extends WindowDialog

signal texture_changed(texture)

onready var texture: ImageTexture = $VBoxContainer/ScrollContainer/TextureRect.texture

func load_from_profile(profile: Profile) -> void:
	self.texture.set_data(profile.face_texture.duplicate())

func clear_texture() -> void:
	self.texture.set_data(null)

func _on_FromFile_pressed() -> void:
	$FileDialog.popup_centered()

func _on_Done_pressed() -> void:
	self.hide()

func _on_FileDialog_file_selected(path: String) -> void:
	var err := self.texture.load(path)
	if err == OK:
		emit_signal("texture_changed", self.texture)
	else:
		$FileLoadingError.popup_centered()
