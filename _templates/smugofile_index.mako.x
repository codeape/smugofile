## Template for the index of an album

<%inherit file="site.mako" />

## An url back to the index of photo albums 
<a href="/photos/index.html">Main index</a>

## The title of the current photo album
<h1>${gallery["album_title"]}</h1>

## List all the pictures of the current photo album
% for photo in gallery["images"]:
        <a href="/${gallery_path}/${photo["image_id"]}.html">
        <img src="${photo["url_thumb"]}" alt="${photo["image_name"]}">
        </a>
        </br>
% endfor
