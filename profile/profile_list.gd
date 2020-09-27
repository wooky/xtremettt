extends ItemList

signal profile_selected(profile)

func _ready() -> void:
	var profiles := ProfileManager.get_profiles()
	var i := 0
	for key in profiles.keys():
		self.add_item(key)
		self.set_item_metadata(i, profiles[key])
		i += 1

func _on_ProfileList_item_selected(index: int) -> void:
	emit_signal("profile_selected", self.get_item_metadata(index))

func add_profile(profile: Profile) -> void:
	self.add_item(profile.profile_id)
	var last_item_id = self.get_item_count() - 1
	self.set_item_metadata(last_item_id, profile)
	self.select(last_item_id)
