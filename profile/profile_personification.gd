extends Spatial
class_name ProfilePersonification

var _body_material := SpatialMaterial.new()
var _face_material: SpatialMaterial

onready var _face: MeshInstance = $Face/Sphere

func _ready() -> void:
	self._face.set_surface_material(0, self._body_material)
	$HeadBack.set_surface_material(0, self._body_material)
	$Torso.set_surface_material(0, self._body_material)

func load_from_profile(profile: Profile) -> void:
	update_body_color(profile.body_color)

func update_body_color(color: Color) -> void:
	self._body_material.albedo_color = color

func update_face_image(image: Image) -> void:
	if self._face_material == null:
		self._face_material = SpatialMaterial.new()
		self._face_material.albedo_texture = ImageTexture.new()
		self._face.set_surface_material(0, self._face_material)
	(self._face_material.albedo_texture as ImageTexture).create_from_image(image)

func clear_face_texture() -> void:
	self._face.set_surface_material(0, self._body_material)
	self._face_material = null
