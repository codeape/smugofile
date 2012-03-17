# Smugofile #

Smugofile is a collection of scripts to create galleries for Blogofile 
(http://www.blogofile.com/) from public SmugMug (http://www.smugmug.com/) 
galleries. These scripts are under  BSD 2-Clause License (see LICENSE file)

# Features #

* Smugofile galleries link images on SmugMug and no pictures will be 
  downloaded.
* Smugofile only fetches links for public galleries.
* smugofile.py works bot for python 2.6+ and 3.0+
* smugofile_gallery.py only works for 2.6+ but will be made to work for 3.0+ 
  when Blogofile officially supports python 3.

# Installation and Configuration #

1. Download Smugofile and unpack the tar file or clone the git repository in to 
   a new directory.
2. Go to the directory where you unpacked or cloned Smugofile
3. Copy the files of Smugofile to the corresponding directory in Blogofile:

    cp -Rv _* /path/to/blog/root
    _smugofile -> /path/to/blog/root/_smugofile
    _smugofile/smugofile.py -> /path/to/blog/root/_smugofile/smugofile.py
    _templates -> /path/to/blog/root/_templates
    ...

4. Add the following line to your Blogofile _config.py:

    controllers.smugofile_gallery.enabled = True

5. Copy or rename all the file ending with .mako.x to end with .mako in the 
   _templates folder of your Blogofile installation. You should also make 
   changes to the mako templates so they generate something more pretty than the
   templates that are packaged with Smugofile. See section templates
6. See the Operation section of this file. 
7. If you use git for your Blogofile installation you should add all new files
   (including smugofile.json) to your git repository.
8. Run blogofile build and check out your gallery in /photos/index.html 
   (for example http://localhost:8080/photos/index.html).

# Templates #

All the variables that can be accessed by the mako templates are documented in 
the .mako.x files (which are working mako templates, x is for example). Some 
hints may be in place though. The data accessible from smugofile_main.mako is 
an array of galleries and every gallery contains a array of images. The data 
accessible from smugofile_index.mako is an gallery with an array of images. 
Finally, the data accessible from smugofile_image.mako is an image. Simply put, 
the data accessible to smugofile_image.mako and smugofile_index.mako is also 
accessible to smugofile_main.mako.x and the data accessible from 
smugofile_image.mako is also accessible to smugofile_index.mako.


# Operation #

1. Enter the _smugofile directory of your Blogofile installation.
2. Good to know. You can always run: 

    smugofile -h

3. Then run:

    mugofile.py smugmug_nick_name

4. This will generate a file called smugofile.json which contains the data 
   fetched from SmugMug. By default the smugofile_gallery.py controller will 
   look in the _smugofile directory for smugofile.json but you can change this 
   by setting a path up in your Blogofile _config.py:

    controllers.smugofile_gallery.smugofile_file = "mypath/smugofile.json"

# Revison history #

* 0.0.1 (2012-03-16) - Created Smugofile.

