import csv
import os

with open ('missio_groga.csv', 'w') as Y_file:
	Y_list_names = []
	types = ["liso", "punto", "tejido_sofa", "mimbre", "cuadros", "rayas", "estampado_floral1", "estampado_floral2"]

	# añade los archivos a Y_list_names
	for (dir_path, dir_names, file_names) in os.walk("files/A1/A1/"): 
		for files in file_names:
			if files.endswith(".tif"):
				Y_list_names.append(files)
	#   
	Y_writer = csv.writer(Y_file, delimiter=',')
	
	# TODO: si da tiempo  mejorar esto con un swich
	for name in Y_list_names:
		if name.startswith("c1r1"):
			Y_writer.writerow([name, types[0]])
		elif name.startswith("c1r3"):
			Y_writer.writerow([name, types[1]])
		elif name.startswith("c2r2"):
			Y_writer.writerow([name, types[2]])
		elif name.startswith("c2r3"):
			Y_writer.writerow([name, types[3]])
		elif name.startswith("c3r1"):
			Y_writer.writerow([name, types[4]])
		elif name.startswith("c3r3"):
			Y_writer.writerow([name, types[5]])
		elif name.startswith("c4r1"):
			Y_writer.writerow([name, types[6]])
		elif name.startswith("c4r3"):
			Y_writer.writerow([name, types[7]])
   	
