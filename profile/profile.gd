extends Node
class_name Profile

var profile_id: String
var player_name: String
var body_color: Color
var face_texture: Image
var taunts: PoolStringArray

func _init(profile_id: String, player_name: String, body_color: Color, face_texture: Image,\
		taunts: PoolStringArray) -> void:
	self.profile_id = profile_id
	self.player_name = player_name
	self.body_color = body_color
	self.face_texture = face_texture
	self.taunts = taunts

static func default() -> Profile:
	var me := load("res://profile/profile.gd")
	return me.new("New Profile", "New Player", Color.brown, null, [])
