extends WindowDialog

signal texture_changed(texture)

onready var texture: ImageTexture = $VBoxContainer/ScrollContainer/TextureRect.texture
onready var _face_selection: FaceSelection = $VBoxContainer/ScrollContainer/TextureRect/FaceSelection

func load_from_profile(profile: Profile) -> void:
	if profile.face_texture:
		var image := profile.face_texture.duplicate()
		self.texture.set_data(image)
		self._face_selection.load_from_image(image)
	else:
		clear_texture()

func clear_texture() -> void:
	self.texture.set_data(null)
	self._face_selection.hide()

func _on_FromFile_pressed() -> void:
	$FileDialog.popup_centered()

func _on_Done_pressed() -> void:
	self.hide()

func _on_FileDialog_file_selected(path: String) -> void:
	var err := self.texture.load(path)
	if err == OK:
		self._face_selection.load_from_image(self.texture.get_data())
		emit_signal("texture_changed", self.texture)
	else:
		$FileLoadingError.popup_centered()
