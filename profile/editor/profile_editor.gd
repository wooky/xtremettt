extends Control

signal back

func _ready() -> void:
	$ProfileList.unselect_all()
	$Container.visible = false

func _on_Back_pressed() -> void:
	emit_signal("back")

func _on_New_pressed() -> void:
	load_container(Profile.default())

func load_container(profile: Profile) -> void:
	$Container/ProfileId.text = profile.profile_id
	$Container/PlayerName.text = profile.player_name
	$Container/BodyColor.color = profile.body_color
	$Container/Taunts.text = profile.taunts.join("\n")
	$Container/ProfileMugshot.personification.load_from_profile(profile)
	$FaceTextureEditor.load_from_profile(profile)
	$Container.visible = true

func _on_BodyColor_color_changed(color: Color) -> void:
	$Container/ProfileMugshot.personification.update_body_color(color)

func _on_EditFaceTexture_pressed() -> void:
	$FaceTextureEditor.popup()

func _on_ClearFaceTexture_pressed() -> void:
	$FaceTextureEditor.clear_texture()
	$Container/ProfileMugshot.personification.clear_face_texture()

func _on_FaceTextureEditor_image_changed(image: Image) -> void:
	$Container/ProfileMugshot.personification.update_face_image(image)
