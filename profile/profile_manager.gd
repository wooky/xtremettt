extends Node

const PROFILES_FILE := "user://profiles.dat"

var _file: File
var _profiles := {}

func _ready() -> void:
	self._file = File.new()
	var err := self._file.open(PROFILES_FILE, File.READ_WRITE)
	if err == OK:
		self._profiles = self._file.get_var(true)

func has_profiles() -> bool:
	return self._profiles.size() != 0
