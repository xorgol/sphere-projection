# sphere-projection
Take the active mesh in a Blender scene, and turn it inside out by projecting it onto a sphere of arbirary radius.

We take a model of a car [from Sketchfab](https://sketchfab.com/3d-models/hyundai-ioniq-5-lowpoly-675e78311e8440d88714bd212cb7a8fb), we flip the normals so it's visible from the inside.
![equirectangular-ioniq5](https://user-images.githubusercontent.com/9532220/205151543-522e2b42-7863-49a8-b39d-3fe776495bca.png)

This is what we see in 3D space
<img width="823" alt="flipped-normals" src="https://user-images.githubusercontent.com/9532220/205152116-d43b5f65-f8c0-435d-9d8f-262e5cbe375a.PNG">
And this is after the transformation
<img width="814" alt="transformed" src="https://user-images.githubusercontent.com/9532220/205152118-b5095586-8f4c-4500-a306-ceca6e5ac253.PNG">
By doing a panoramic rendering we obtain an image like this
![flipped_equirectangular_3m](https://user-images.githubusercontent.com/9532220/205152297-e1fd0a24-0cdb-4d1b-8446-12d49a3846b9.png)

Which can be applied to a sphere geometry in three.js, [like this](https://adrianofarina.it/flipped), and orbited.
The projection depends on the radius of the sphere.

This will be used for noise mapping applications.
