extends Spatial
class_name ProfilePersonification

var _body_material := SpatialMaterial.new()
var _face_material: Material

func _ready() -> void:
	$Face.set_surface_material(0, self._body_material)
	$HeadBack.set_surface_material(0, self._body_material)
	$Torso.set_surface_material(0, self._body_material)

func load_from_profile(profile: Profile) -> void:
	update_body_color(profile.body_color)

func update_body_color(color: Color) -> void:
	self._body_material.albedo_color = color
