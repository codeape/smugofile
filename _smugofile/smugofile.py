#!/usr/bin/env python
# Author: Oscar Norlander <oscar-no(at)codeape(dot)org>

try:
        import xmlrpc.client as xmlrpclib
except ImportError:
        import xmlrpclib

import sys
import json
import os

app_version="0.0.1"
api_key="GyxzE1JizQ6ZYIWsL9CbThbUoQyslYgH"
api_url="http://api.smugmug.com/services/api/xmlrpc/1.3.0/"

arg_nick_name = ""
arg_debug = False
arg_file = "smugofile.json"

def help():
        """
        Prints a help message
        """
        prog_str = os.path.basename(sys.argv[0])
        print("usage: {0} [-h]".format(prog_str))
        print("       {0} [-d] nick_name".format(prog_str))
        print("")
        print("options:")
        print("  -h         Help ... this text.")
        print("  -d         Print all xml-rpc traffic")
        print("  -v         Version")
        print("  nick_name  The SmugMug nick name for a specific user")
        print("")

def msg(a_message):
        """
        Status messages that are specific to normal behavior uses this.
        """
        print(a_message)

def status_ok(a_message):
        """
        All ok messages uses this so we do not get the ok suffix message wrong.
        """
        print(a_message +" [ ok ]")

def status_fault(a_message, a_fault):
        """
        Handle errors from xml-rpc calls.
        """
        print(a_message +" [ fail ]")
        print("A fault occurred")
        print("Fault code: {0}".format(a_fault.faultCode))
        print("Fault string: {0}".format(a_fault.faultString))
        exit(-1)

def status_error(a_message, a_error):
        """
        Handle faults from xml-rpc calls.
        """
        print("A protocol error occurred")
        print("URL: {0}".format(a_error.url))
        print("HTTP/HTTPS headers: {0}".format(a_error.headers))
        print("Error code: {0}".format(a_error.errcode))
        print("Error message: {0}".format(a_error.errmsg))

class SmugofileTranspot(xmlrpclib.Transport):
        """
        We only have this class so we can follow SmugMugs best practice by 
        having a custom User-Agent string.
        """
        user_agent = "Smugofile/{0} (by www.codeape.org)".format(app_version)

# Check so that we have the right number of options (arguments)
if len(sys.argv) < 2 or len(sys.argv) > 3:
        help()
        print("ERROR: 1 or 2 arguments please.")
        exit(-1)

# Map options to functionality
for arg in sys.argv[1:]:
        if arg == "-h" :
                help()
                exit(0)
        elif arg == "-d":
                arg_debug = True
        elif arg == "-v":
                print("{0} {1}".format(os.path.basename(sys.argv[0]),
                                       app_version))
                exit(0)
        elif arg_nick_name == "":
                arg_nick_name = arg
        else:
                help()
                print("ERROR: Argument '{0}' make no sense.".format(arg))
                exit(-1)

# Create the xml-rpc client
trans = SmugofileTranspot()
proxy = xmlrpclib.ServerProxy(api_url, trans, verbose=arg_debug)

msg("Fetching album list");
try:
        galleries = proxy.smugmug.albums.get({"APIKey" : api_key, "NickName" : arg_nick_name})
        status_ok("Album list fetch")
except xmlrpclib.Fault as f :
        status_fault("Album list fetch", f)
        exit(-1)
except xmlrpclib.ProtocolError as e:
        status_error("Album list fetch", e)
        exit(-1)

print("Fetching images for albums")
album_list = []
for album in galleries["Albums"] :
        msg("Fetching " + album["Title"])
        # Create data structure for album that holds pictures
        album_dic = {
                "album_title" : album["Title"],
                "album_id" : album["id"],
                "images" : []
        }
        try:
                images = proxy.smugmug.images.get({"APIKey" : api_key,
                                                   "AlbumID" : album["id"],
                                                   "AlbumKey" : album["Key"],
                                                   "Heavy" : "true"})
                status_ok("Album fetch")
        except xmlrpclib.Fault as f :
                status_fault("Album fetch", f)
                exit(-1)
        except xmlrpclib.ProtocolError as e:
                status_error("Album fetch", e)
                exit(-1)
        for img in images["Album"]["Images"]:
                # Create data structure for pictures
                image_dic = {
                        "image_name" : img["FileName"],
                        "image_id" : img["id"],
                        "url_thumb" : img["ThumbURL"],
                        "url_tiny" : img["TinyURL"],
                        "url_small" : img["SmallURL"],
                        "url_medium" : img["MediumURL"],
                        "url_large" : img["LargeURL"],
                        "url_xlarge" : img["XLargeURL"],
                        "url_x2large" : img["X2LargeURL"],
                        "url_x3large" : img["X3LargeURL"],
                        "url_original" : img["OriginalURL"]
                }
                album_dic["images"].append(image_dic)
        album_list.append(album_dic);

# Save the albums and pictures to a json file
try:
        jsonfile = open(arg_file, "w")
except IOError as e:
        print(e.strerror)
        exit(-1)
jsonfile.write(json.dumps(album_list, indent=4));
jsonfile.close()

#eof
