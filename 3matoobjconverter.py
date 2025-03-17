import json
import os

# change the file type of the 3ma file to json and load it as json

def start():
    global skript_dir
    skript_dir = os.path.dirname(os.path.abspath(__file__))
    print(" Folder path:", skript_dir)
    find_files()
    choice = input("Press Enter to convert again. 0 to exit")
    if choice == '0':
        pass
    else:
        start()

def find_files():
    global dreima_files, script_dir
    files = os.listdir(skript_dir)
    dreima_files = [f for f in files if f.endswith(".3ma")]

def convert():
    for i in range (0, (len(dreima_files) - 1)):
        thisfile = os.path.join(script_dir, dreima_files[i])

        file_3ma = open(thisfile)
        fjile_3ma = json.loads(file_3ma.read())

        base_name, _ = os.path.splitext(thisfile)
        obj_file = os.path.join(script_dir, f"{base_name}.obj")
        obj_file = open(obj_file, "wt")

        vertex_index = 0
        prev_vertex_index = vertex_index

        forward = 0
        meshes = fjile_3ma["meshes"]
        mesh_num = len(meshes)

        for msh in range(mesh_num):

            obj_file.write("\ng \n")
            preciseFactor = meshes[msh]["preciseFactor"]
            prev_vertex_index = vertex_index
            for vtx in range(0, len(meshes[msh]["_positions"]), 3):
                _pos_0 = meshes[msh]["_positions"][vtx] / preciseFactor
                _pos_1 = meshes[msh]["_positions"][vtx + 1] / preciseFactor
                _pos_2 = (meshes[msh]["_positions"][vtx + 2] * -1) / preciseFactor
                vtx_string = "v " + str(_pos_0) + " " + str(_pos_1) + " " + str(_pos_2) + "\n"
                obj_file.write(vtx_string)
                vertex_index = vertex_index + 1

            if msh > 0:
                forward = 1

            UnivertsList = meshes[msh]["facesUnivertsList"]
            obj_file.write("\ng name" + str(msh) + " \n")
            for fcx in UnivertsList:
                obj_file.write("f")
                for fcx_ndx in fcx["u"]:
                    obj_file.write(" " + str(fcx_ndx + 1 + (forward * prev_vertex_index)))
                obj_file.write("\n")
        file_3ma.close()
        obj_file.close()
    print(f"Coverted {i+1} Files successfully!")

if __name__ == '__main__':
    start()
