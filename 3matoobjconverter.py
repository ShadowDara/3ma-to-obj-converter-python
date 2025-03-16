import json
import os

skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))

def olfmain():

# change the file type of the 3ma file to json and load it as json
    filename_3ma = "C:\\filepath\\filename.json"

    file_3ma = open(filename_3ma)

    fjile_3ma = json.loads(file_3ma.read())

    fout = open("C:\\filepath\\filename.obj","wt")

    vertex_index = 0
    prev_vertex_index = vertex_index

    forward = 0

    meshes = fjile_3ma["meshes"]

    mesh_num = len(meshes)

    for msh in range(mesh_num):
    
        fout.write("\ng \n")
        preciseFactor = meshes[msh]["preciseFactor"]
        prev_vertex_index = vertex_index
        for vtx in range(0,len(meshes[msh]["_positions"]),3):
            _pos_0 = meshes[msh]["_positions"][vtx]/preciseFactor
            _pos_1 = meshes[msh]["_positions"][vtx+1]/preciseFactor
            _pos_2 = (meshes[msh]["_positions"][vtx+2]*-1)/preciseFactor
            vtx_string = "v "+str(_pos_0)+" "+str(_pos_1)+" "+str(_pos_2)+"\n"
            fout.write(vtx_string)
            vertex_index = vertex_index+1
        
        if msh>0:
            forward = 1
    
        UnivertsList = meshes[msh]["facesUnivertsList"]
        fout.write("\ng name"+str(msh)+" \n")
        for fcx in UnivertsList:
            fout.write("f")
            for fcx_ndx in fcx["u"]:
                fout.write(" "+str(fcx_ndx+1+(forward*prev_vertex_index)))
            fout.write("\n")

    file_3ma.close()
    fout.close()

if __name__ == '__main__':
    print(" Folder path:", skript_verzeichnis)
