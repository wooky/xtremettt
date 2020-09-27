extends WindowDialog

signal image_changed(image)

onready var _texture: ImageTexture = $VBoxContainer/ScrollContainer/TextureRect.texture
onready var _face_selection: FaceSelection = $VBoxContainer/ScrollContainer/TextureRect/FaceSelection

func load_from_profile(profile: Profile) -> void:
	if profile.face_texture:
		var image := profile.face_texture.duplicate()
		self._texture.set_data(image)
		self._face_selection.load_from_image(image)
	else:
		clear_texture()

func get_image() -> Image:
	if self._texture.get_data() == null: return null
	return self._texture.get_data().get_rect(self._face_selection.get_rect())

func clear_texture() -> void:
	self._texture.set_data(null)
	self._face_selection.hide()

func _on_FromFile_pressed() -> void:
	$FileDialog.popup_centered()

func _on_Done_pressed() -> void:
	self.hide()

func _on_FileDialog_file_selected(path: String) -> void:
	var err := self._texture.load(path)
	if err == OK:
		self._face_selection.load_from_image(self._texture.get_data())
		emit_signal("image_changed", get_image())
	else:
		$FileLoadingError.popup_centered()

func _on_FaceSelection_selection_changed() -> void:
	emit_signal("image_changed", get_image())
