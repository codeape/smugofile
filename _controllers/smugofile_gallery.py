# Author: Oscar Norlander <oscar-no(at)codeape(dot)org>

import os
import sys
import json
from blogofile.cache import bf

config = {
         "name"            : "Smugofile gallery",
         "description"     : "This is a gallery script using SmugMug links",
         "author"          : "Oscar (codeape) Norlander",
         "url"             : "http://www.codeape.org/download/index.html",
         "priority"        : 50.0,
         "smugofile_file"  : os.path.join("_smugofile","smugofile.json")}

root_path = "photos"
debug = False

def read_file(a_file):
        """
        Reads a json file and returns a python representation of it.
        """
        smug_data = []
        # Read file
        try:
                json_file = open(a_file)
        except IOError as e:
                print("{0} failed!".format(config["name"]))
                print("File {0}. {1}".format(a_file, e.strerror))
                exit(-1)
        json_str = json_file.read().rstrip()
        if json_str == "" :
                return smug_data
        json_file.close()
        # Decode from json to python built-ins
        try:
                smug_data = json.loads(json_str)
        except ValueError as e:
                print("{0} failed!".format(config["name"]))
                print("File {0}. {1}".format(a_file, str(e)))
                exit(-1)
        return smug_data

def write_index_and_images(a_data):
        """
        Writes an album index and pages for each picture in the album using the
        mako templates:
        - smugofile_index.mako : The index of an photo album
        - smugofile_image.mako : The page that show the image, photo or picture
                                 or what you call it =)
        """
        for gallery in a_data :
                gallery_path = os.path.join(root_path, str(gallery["album_id"]))
                bf.writer.materialize_template("smugofile_index.mako",
                                               (gallery_path, "index.html"),
                                               {"gallery_path" : gallery_path,
                                                "gallery" : gallery})
                for photo in gallery["images"]:
                        bf.writer.materialize_template("smugofile_image.mako",
                                                       (gallery_path, "{0}.html".format(photo["image_id"])),
                                                       {"gallery_path" : gallery_path, 
                                                        "photo" : photo})

def write_main(a_data):
        """
        Writes a index of albums using the template:
        - smugofile_main.mako : The index of photo albums
        """
        bf.writer.materialize_template("smugofile_main.mako",
                                       (root_path, "index.html"),
                                       {"root_path" : root_path, 
                                        "galleries" : a_data})

def run():
        """
        Read the documentation about controllers on http://www.blogofile.com/.
        """
        data = read_file(config["smugofile_file"])
        if (len(data) > 0) and (debug == False):
                write_main(data)
                write_index_and_images(data)
        elif debug == True:
                print(data)
                print("")
                print("Debug mode. No data written!")

def debug_help():
        """
        Prints a help text in debug mode.
        """
        prog_str = os.path.basename(sys.argv[0])
        print("usage: {0} [-h] [smug_path]".format(prog_str))
        print("")
        print("arguments:")
        print("  -h         Help ... this text.")
        print("  smug_path  The path to the smugofile.json file.")
        print("             Default: {0}".format(config["smugofile_file"]))
        print("")

def debug_smug():
        """
        This is the debug mode function. If you need to do some debugging 
        without using blogofile.
        """
        config["smugofile_file"] = os.path.join("..", config["smugofile_file"])
        if len(sys.argv) not in [1, 2] :
                debug_help()
                exit(-1)
        elif len(sys.argv) == 2 and sys.argv[1] == "-h":
                debug_help()
                exit(0)
        elif len(sys.argv) == 2:
                config["smugofile_file"] = sys.argv[1]
        print("Debug using path {0}".format(config["smugofile_file"]))
        debug = True
        run()

if __name__ == "__main__":
        debug_smug()

#eof
