extends Spatial
class_name ProfilePersonification

var _body_material := SpatialMaterial.new()
var _face_material: SpatialMaterial

func _ready() -> void:
	$Face.set_surface_material(0, self._body_material)
	$HeadBack.set_surface_material(0, self._body_material)
	$Torso.set_surface_material(0, self._body_material)

func load_from_profile(profile: Profile) -> void:
	update_body_color(profile.body_color)

func update_body_color(color: Color) -> void:
	self._body_material.albedo_color = color

func update_face_texture(texture: Texture) -> void:
	if self._face_material == null:
		self._face_material = SpatialMaterial.new()
		$Face.set_surface_material(0, self._face_material)
	self._face_material.albedo_texture = texture

func clear_face_texture() -> void:
	$Face.set_surface_material(0, self._body_material)
	self._face_material = null
