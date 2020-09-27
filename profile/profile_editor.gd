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
	($Container/ProfileMugshot as ProfileMugshot).personification.load_from_profile(profile)
	$Container.visible = true

func _on_BodyColor_color_changed(color: Color) -> void:
	($Container/ProfileMugshot as ProfileMugshot).personification.update_body_color(color)
