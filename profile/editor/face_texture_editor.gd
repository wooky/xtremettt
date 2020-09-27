extends WindowDialog

signal texture_changed(texture)

func load_from_profile(profile: Profile) -> void:
	# TODO
	pass

func get_texture() -> Texture:
	return $VBoxContainer/TextureRect.texture

func clear_texture() -> void:
	# TODO
	pass

func _on_FromFile_pressed() -> void:
	$FileDialog.popup_centered()

func _on_Done_pressed() -> void:
	self.hide()

func _on_FileDialog_file_selected(path: String) -> void:
	var texture := $VBoxContainer/TextureRect.texture as ImageTexture
	var err := texture.load(path)
	if err == OK:
		emit_signal("texture_changed", texture)
	else:
		$FileLoadingError.popup_centered()
