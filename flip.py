import bpy
import math

obj = bpy.context.active_object
v = obj.data.vertices[0]
co_final = obj.matrix_world @ v.co

coords = [(obj.matrix_world @ v.co) for v in obj.data.vertices]

projection_sphere_radius = 3

for i in range(0,len(bpy.context.active_object.data.vertices)):
	x = bpy.context.active_object.data.vertices[i].co[0]
	y = bpy.context.active_object.data.vertices[i].co[1]
	z = bpy.context.active_object.data.vertices[i].co[2]
	
	r = math.sqrt(x*x+y*y+z*z)
	theta = math.atan2(y, x)
	phi = math.asin(z/r)
	r1 = projection_sphere_radius-r
	x1 = r1*math.cos(theta)*math.cos(phi)
	y1 = r1*math.sin(theta)*math.cos(phi)
	z1 = r1*math.sin(phi)
	bpy.context.active_object.data.vertices[i].co[0] = x1
	bpy.context.active_object.data.vertices[i].co[1] = y1
	bpy.context.active_object.data.vertices[i].co[2] = z1
	
# print(bpy.context.active_object.data.vertices[i].co[0] + bpy.context.active_object.data.vertices[i].co[1]+ bpy.context.active_object.data.vertices[i].co[2])

# commands for executin script in Blender
# filename = 'flip.py
# exec(compile(open(filename).read(), filename, 'exec'))