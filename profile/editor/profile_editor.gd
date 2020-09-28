extends Control

signal back

func _ready() -> void:
	$ProfileList.unselect_all()
	$Container.visible = false

func _on_New_pressed() -> void:
	_load_container(Profile.default())

func _load_container(profile: Profile) -> void:
	$Container/ProfileId.text = profile.profile_id
	$Container/PlayerName.text = profile.player_name
	$Container/BodyColor.color = profile.body_color
	$Container/Taunts.text = profile.taunts.join("\n")
	$Container/ProfileMugshot.personification.load_from_profile(profile)
	$FaceTextureEditor.load_from_profile(profile)
	$Container.visible = true
